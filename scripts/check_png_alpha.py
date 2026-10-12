#!/usr/bin/env python3
"""Inspect real pixel transparency in common PNG files without dependencies.

Exit codes: 0 means every inspected file has non-opaque pixels; 1 means an
invalid/unreadable file; 2 means at least one valid file is fully opaque; and
3 means a valid PNG uses a variant this deliberately small checker cannot
decode (non-8-bit or interlaced).
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
import zlib
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
CHANNELS = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}


def paeth(a: int, b: int, c: int) -> int:
    estimate = a + b - c
    distances = (abs(estimate - a), abs(estimate - b), abs(estimate - c))
    if distances[0] <= distances[1] and distances[0] <= distances[2]:
        return a
    return b if distances[1] <= distances[2] else c


def read_chunks(data: bytes):
    offset = len(PNG_SIGNATURE)
    saw_iend = False
    while offset < len(data):
        if offset + 12 > len(data):
            raise ValueError("truncated PNG chunk")
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        end = offset + 12 + length
        if end > len(data):
            raise ValueError("PNG chunk length exceeds file size")
        kind = data[offset + 4 : offset + 8]
        payload = data[offset + 8 : offset + 8 + length]
        expected_crc = struct.unpack(">I", data[offset + 8 + length : end])[0]
        actual_crc = zlib.crc32(kind + payload) & 0xFFFFFFFF
        if actual_crc != expected_crc:
            raise ValueError(f"CRC mismatch in {kind.decode('ascii', errors='replace')} chunk")
        yield kind, payload
        offset = end
        if kind == b"IEND":
            saw_iend = True
            break
    if not saw_iend:
        raise ValueError("missing IEND chunk")


def unfilter(raw: bytes, width: int, height: int, bytes_per_pixel: int) -> list[bytes]:
    stride = width * bytes_per_pixel
    expected = height * (stride + 1)
    if len(raw) != expected:
        raise ValueError(f"unexpected decompressed size: expected {expected}, got {len(raw)}")

    rows: list[bytes] = []
    position = 0
    prior = bytearray(stride)
    for _ in range(height):
        method = raw[position]
        position += 1
        source = raw[position : position + stride]
        position += stride
        row = bytearray(stride)
        for index, value in enumerate(source):
            left = row[index - bytes_per_pixel] if index >= bytes_per_pixel else 0
            up = prior[index]
            upper_left = prior[index - bytes_per_pixel] if index >= bytes_per_pixel else 0
            if method == 0:
                decoded = value
            elif method == 1:
                decoded = value + left
            elif method == 2:
                decoded = value + up
            elif method == 3:
                decoded = value + ((left + up) // 2)
            elif method == 4:
                decoded = value + paeth(left, up, upper_left)
            else:
                raise ValueError(f"unsupported PNG filter {method}")
            row[index] = decoded & 0xFF
        rows.append(bytes(row))
        prior = row
    return rows


def inspect_png(path: Path) -> tuple[dict[str, object], int]:
    data = path.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("not a PNG file")

    header = None
    idat = bytearray()
    transparency = None
    for kind, payload in read_chunks(data):
        if kind == b"IHDR":
            if len(payload) != 13 or header is not None:
                raise ValueError("invalid IHDR chunk")
            header = struct.unpack(">IIBBBBB", payload)
        elif kind == b"IDAT":
            idat.extend(payload)
        elif kind == b"tRNS":
            transparency = payload

    if header is None or not idat:
        raise ValueError("missing IHDR or IDAT chunk")

    width, height, bit_depth, color_type, compression, filtering, interlace = header
    base = {
        "path": str(path.resolve()),
        "size": [width, height],
        "bit_depth": bit_depth,
        "color_type": color_type,
    }
    if width < 1 or height < 1:
        raise ValueError("invalid image dimensions")
    if compression != 0 or filtering != 0:
        raise ValueError("invalid PNG compression or filtering method")
    if bit_depth != 8 or interlace != 0:
        return ({**base, "status": "unsupported-png-variant"}, 3)

    channels = CHANNELS.get(color_type)
    if channels is None:
        raise ValueError(f"unsupported color type {color_type}")
    if color_type in (0, 2) and transparency is None:
        return ({**base, "status": "no-alpha-channel", "alpha_range": [255, 255]}, 2)

    rows = unfilter(zlib.decompress(bytes(idat)), width, height, channels)
    if color_type == 6:
        alpha_values = [row[i] for row in rows for i in range(3, len(row), 4)]
    elif color_type == 4:
        alpha_values = [row[i] for row in rows for i in range(1, len(row), 2)]
    elif color_type == 3:
        table = list(transparency or b"")
        alpha_values = [table[index] if index < len(table) else 255 for row in rows for index in row]
    elif color_type == 0:
        if transparency is None or len(transparency) != 2:
            raise ValueError("invalid grayscale tRNS chunk")
        transparent_gray = struct.unpack(">H", transparency)[0] & 0xFF
        alpha_values = [0 if value == transparent_gray else 255 for row in rows for value in row]
    else:
        if transparency is None or len(transparency) != 6:
            raise ValueError("invalid truecolor tRNS chunk")
        transparent_rgb = tuple(value & 0xFF for value in struct.unpack(">HHH", transparency))
        alpha_values = [
            0 if tuple(row[i : i + 3]) == transparent_rgb else 255
            for row in rows
            for i in range(0, len(row), 3)
        ]

    total = width * height
    transparent = sum(value == 0 for value in alpha_values)
    opaque = sum(value == 255 for value in alpha_values)
    semitransparent = total - transparent - opaque
    alpha_min, alpha_max = min(alpha_values), max(alpha_values)
    report = {
        **base,
        "alpha_range": [alpha_min, alpha_max],
        "corner_alpha": [
            alpha_values[0],
            alpha_values[width - 1],
            alpha_values[-width],
            alpha_values[-1],
        ],
        "pixels": {
            "total": total,
            "transparent": transparent,
            "semitransparent": semitransparent,
            "opaque": opaque,
        },
    }
    if alpha_min < 255:
        return ({**report, "status": "real-transparency-present"}, 0)
    return ({**report, "status": "alpha-present-but-fully-opaque"}, 2)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check PNG alpha metadata and actual pixel transparency."
    )
    parser.add_argument("images", nargs="+", type=Path, help="PNG file(s) to inspect")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    reports: list[dict[str, object]] = []
    result_codes: list[int] = []
    errors: list[str] = []
    for path in args.images:
        try:
            report, code = inspect_png(path)
            reports.append(report)
            result_codes.append(code)
        except (OSError, ValueError, EOFError, IndexError, struct.error, zlib.error) as exc:
            errors.append(f"{path}: {exc}")

    if args.json:
        print(json.dumps({"reports": reports, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        for report in reports:
            print(f"{report['path']}: {report['status']}")
            print(
                f"  size={report['size'][0]}x{report['size'][1]} "
                f"bit_depth={report['bit_depth']} color_type={report['color_type']}"
            )
            if "alpha_range" in report:
                print(
                    f"  alpha_range={report['alpha_range']} "
                    f"corner_alpha={report.get('corner_alpha', 'not decoded')}"
                )
            if "pixels" in report:
                print(f"  pixels={report['pixels']}")
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        return 1
    if 3 in result_codes:
        return 3
    if 2 in result_codes:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
