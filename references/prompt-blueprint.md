# Prompt Blueprint

Use the smallest complete prompt that removes ambiguity. Adapt the fields below rather than copying irrelevant details.

## Schema

```text
Use case: reference-guided transformation
Asset type: collectible painted bas-relief fridge-magnet concept

Reference role:
[State which image controls identity, pose, composition, palette, or supporting details.]

Primary request:
[Describe the transformation and the intended emotional or cultural character.]

Preserve:
[List the few identity-bearing shapes, proportions, colors, text, and memory cues.]

Remove or simplify:
[List clutter, people, signage, background objects, and fine details that should not survive.]

Physical structure:
[Die-cut silhouette, medallion, rounded plaque, portrait plaque, landscape plaque, raised rim, connected base.]

Relief hierarchy:
[Name high-, middle-, and low-relief elements.]

Style and material:
Premium hand-painted resin bas-relief, tactile sculpted forms, satin-matte finish, refined souvenir craftsmanship; dimensional but not a full 3D figurine, cute only if appropriate and not automatically chibi.

Composition and framing:
[Subject scale, placement, full-body/full-scene requirement, edge visibility, stable silhouette, presentation margin.]

Lighting and palette:
[Source-led colors, soft studio light or scene-led light, restrained contrast.]

Presentation:
Show exactly one complete physical magnet centered on a clean neutral presentation canvas with a subtle contact shadow. The canvas and shadow are not part of the magnet.

Constraints:
[Exact text, one connected object, no identity drift, no unrelated motifs, no logos or watermark.]

Avoid:
Flat sticker look, photo pasted into a frame, freestanding figurine, fragile floating pieces, thick cartoon outlines, oversaturated colors, fake checkerboard transparency, extra text, duplicate subjects.
```

## Isolated Subject Example

```text
Use case: reference-guided transformation
Asset type: collectible painted bas-relief fridge-magnet concept

Reference role: Use the supplied pet photo as the sole identity, pose, and palette reference.
Primary request: Transform the pet into a refined resin bas-relief magnet that remains immediately recognizable.
Preserve: Exact body proportions, pose, expression, ear and tail shapes, coat colors, and the distinctive collar.
Remove or simplify: Remove the room, people, signs, floor clutter, and reflections. Simplify individual hairs into readable layered fur carving.
Physical structure: One connected die-cut silhouette with a narrow creamy-white support border; reinforce thin legs and tail connections without making them bulky.
Relief hierarchy: Face and front paws in high relief, torso and tail in middle relief, collar pattern in shallow crisp relief.
Style and material: Premium hand-painted resin, satin-matte finish, softly rounded sculpted edges, tactile fur detail, charming but not chibi.
Composition and framing: Full body visible, no cropping, clear physical edge, generous margin.
Lighting and palette: Soft neutral studio light; retain natural source colors with restrained warm highlights.
Presentation: Center exactly one complete magnet on a clean white canvas with a very soft neutral-gray contact shadow. The canvas is not part of the magnet.
Constraints: Preserve identity; no text, logo, watermark, extra props, or added scenery.
Avoid: Flat sticker, thick cartoon outline, generic pet face, floating pieces, neon colors, fake checkerboard transparency.
```

## Complete Scene Example

```text
Use case: reference-guided transformation
Asset type: collectible painted bas-relief fridge-magnet concept

Reference role: Use the supplied travel photo as the sole composition, landmark, and palette reference.
Primary request: Reinterpret the scene as a compact framed relief souvenir while preserving the landmark and the photograph's atmosphere.
Preserve: Landmark silhouette, horizon placement, main path or river direction, time-of-day light, and any user-specified inscription exactly.
Remove or simplify: Remove unrelated people, vehicles, advertisements, QR codes, and visual clutter. Consolidate distant detail into clean relief planes.
Physical structure: Landscape rounded-rectangle plaque with a slim raised rim and all four edges visible.
Relief hierarchy: Landmark in high relief, nearby trees and street elements in middle relief, sky and distance in low relief, inscription engraved or raised only as requested.
Style and material: Premium hand-painted resin bas-relief, layered architectural carving, satin-matte finish, polished cultural souvenir design.
Composition and framing: Retain the original visual path and landmark dominance; create one connected, stable object.
Lighting and palette: Preserve the source's natural light and key colors without neon saturation.
Presentation: Center exactly one complete magnet on a clean white canvas with a subtle contact shadow. The canvas is not part of the magnet.
Constraints: Exact spelling; no invented branding, watermark, duplicate landmark, or cropped physical edge.
Avoid: Flat printed photograph, generic replacement architecture, illegible text, excessive lens flare, fake checkerboard transparency.
```

## Revision Pattern

When the user requests a change, rewrite the full prompt. Include three explicit groups:

1. **Change now:** the requested adjustment and any necessary linked changes.
2. **Keep locked:** every accepted identity, structure, material, palette, and composition choice that must stay.
3. **Still avoid:** the existing failure modes plus any new failure revealed by the prior result.

Regenerate from the complete prompt. Do not accumulate edits on the previous bitmap unless the user explicitly asks for direct editing.

## Exact Text Addendum

Append this only when the source contains wording that must survive:

```text
Text (verbatim): "<copy the required text exactly>"
Reproduce every character, punctuation mark, and line break exactly. Do not
paraphrase, add, omit, or substitute text. If exact rendering is not possible,
leave a clean editable text area for a later typography/compositing pass.
```

Generated text still requires character-by-character human review.
