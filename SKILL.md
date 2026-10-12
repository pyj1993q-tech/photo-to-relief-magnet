---
name: photo-to-relief-magnet
description: Turn reference photos into generation-ready concepts and prompts for painted bas-relief fridge magnets. Use for pets, bouquets, flowers, landmarks, landscapes, keepsakes, series consistency, die-cut versus framed construction, or PNG transparency checks. Do not use for CAD, STL, depth maps, or production-ready 3D geometry.
metadata:
  short-description: Photo-to-relief magnet concept design and QA
---

# Photo to Relief Magnet

Create a clear, attractive bas-relief fridge-magnet concept from one or more reference photos. Preserve the source's important identity and memory cues while simplifying it into a coherent physical object.

This skill produces concept artwork and generation prompts. Do not describe an image as a manufactured sample, print-ready cut file, relief height map, CAD model, or STL unless that separate work has actually been completed and verified.

## Start From the Request

Inspect every supplied image before proposing a design. Identify:

- what must remain recognizable;
- what may be simplified or removed;
- whether exact text must be preserved;
- whether the user wants a display render, a genuinely transparent PNG, or another deliverable;
- whether multiple images are independent designs or ingredients for one composition.

Treat multiple photos as separate magnets by default. Combine them only when the user explicitly asks for a composite design.

If a missing choice would materially change the result, ask one concise question. Otherwise make a conservative choice and state it.

## Choose the Physical Structure

Select a structure that makes the subject readable and the silhouette plausible:

- **Clean isolated subject:** irregular die-cut silhouette with a narrow connected border.
- **Subject with fragile protrusions or a weak outline:** compact plaque or medallion, optionally using a restrained break-the-frame effect.
- **Landscape, architecture, garden, or complete scene:** rounded rectangle, portrait plaque, or landscape plaque with a slim raised rim.
- **Dense all-over pattern:** simple framed geometry so the internal relief can carry the detail.
- **Series:** keep rim color, material, relief language, lighting, presentation margin, and shadow consistent while allowing the physical format to suit each image.

Avoid thin isolated branches, unsupported appendages, accidental holes, floating pieces, and details too fine to read as relief. These are concept-level manufacturability cues, not engineering validation.

Read [references/design-guide.md](references/design-guide.md) when structure selection, series consistency, or relief hierarchy needs more detail.

## Build a Complete Generation Prompt

Write a complete prompt rather than a loose style phrase. Cover the reference role, preservation list, removal list, object structure, relief hierarchy, material, palette, presentation, constraints, and avoid list.

Keep these distinctions explicit:

- the **magnet body** is the physical object;
- the **presentation canvas** and contact shadow are only for display;
- a checkerboard pattern rendered as pixels is not transparency;
- painted resin relief is dimensional but is not photorealistic raw photography or a flat sticker.

Use [references/prompt-blueprint.md](references/prompt-blueprint.md) for the prompt schema and adaptable examples.

## Generate and Revise

Use an available image-generation capability with the user's photo as reference. Preserve recognizable proportions, pose, palette, composition, and exact requested details unless the redesign requires a clearly explained simplification.

For revisions, incorporate the requested change into a fresh, complete prompt and regenerate. Keep every previously accepted element that the user did not ask to change. Use the prior result only as a consistency reference unless the user explicitly asks for direct image editing or localized inpainting.

Do not silently introduce motifs from unrelated photos, swap identities, invent branding, or replace copyrighted characters with original ones without telling the user.

For exact wording, copy the source text verbatim and verify every character, punctuation mark, and line break after generation. If the image model cannot render it reliably, leave a clean text area and use an editable typography or compositing workflow instead of repeatedly sampling near-miss text.

## Review the Result

Check the actual image, not only the prompt. Use [references/qc-checklist.md](references/qc-checklist.md) for the full delivery review. At minimum, confirm:

1. The subject remains recognizable and required text is exact.
2. The magnet is one connected object with a clear physical edge and readable relief hierarchy.
3. Removed clutter has not returned, and no unintended text, branding, subjects, or fake transparency appeared.
4. Claims about transparency, manufacturability, and production readiness match verified facts.

If a transparent PNG is required, run:

```bash
python scripts/check_png_alpha.py path/to/output.png
```

The checker has no third-party dependencies. Do not label the output transparent when it reports no alpha channel or a fully opaque alpha channel. If it reports an unsupported PNG variant, inspect that file with a capable image tool rather than guessing.

## Deliver

Provide the generated artwork together with:

- the final complete prompt;
- the chosen physical structure and the reason for it;
- a short list of preserved and removed elements;
- the verified transparency status;
- an explicit note that the result is a concept render unless production files and a physical sample were separately made.
