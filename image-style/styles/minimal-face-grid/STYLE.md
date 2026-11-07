# Minimal Face Grid

People in a photo redrawn as naive black-and-white line portraits, each in its own hand-drawn square frame, evenly arranged on white.

## Prompt

```text
Convert the people in the attached photo into a black-and-white, minimal, hand-drawn portrait grid. Draw one portrait for each person in the photo, and don't add people who aren't in it. Arrange the portraits in even rows and columns on a white background. If the photo has one person, draw one large portrait.

Key structure: each portrait is a simple front-facing head with no neck, shoulders, or clothing, enclosed in its own square frame. Each head floats at the center of its frame, with clear white space on all sides, taking up about 60-65% of the frame. Frames are thick, slightly wobbly marker lines.

Style:
- Pure black and white, with no colors, shadows, or gradients
- Hand-drawn feel with slightly irregular lines, in a naive, quirky editorial illustration style
- A simple, distinct face shape for each person
- Minimal, thin facial features: dot eyes, small circle eyes, short line eyebrows, one thin curved line for the nose, straight line mouth, small smile, small sad mouth, sleepy eyes, surprised O-shaped mouth, or a blank expression
- Hair filled with solid black as one simple shape, without individual strands. Show the hairstyle through its outline: wavy bangs, curls, center-parted curtains, flat short hair, side-swept bangs, swirling curls, or scalloped bangs
- Add round glasses, square glasses, a mustache, freckles, closed eyes, or X-shaped eyes only when they match the person in the photo

Keep each person's recognizable traits from the photo: hairstyle, face shape, accessories, and expression. Choose the closest happy, sad, confused, sleepy, surprised, or blank expression.

Overall, it looks like a hand-drawn character encyclopedia: geometric, restrained, and naive but not loose. Flat and high contrast, with no color, background decoration, or realistic detail. Don't include the photo's background, objects, or any text.

Keep the same aspect ratio as the attached image.
```

## Observed in references

The user's original reference image isn't stored. It showed these traits in more detail than the prompt states. Add the ones you want to the image prompt.

- **Face shapes:** shapes vary widely, such as a circle, triangle, rounded square, or long oval.
- **Nose:** many noses are a single curved or L-shaped line.

## Examples

- [two-people.webp](examples/two-people.webp): conversion of a generated photo of two people repairing a bicycle, made with `gpt-image` using the solid hair, front-facing head, and frame rules now in the prompt, given as overrides at the time. Without those rules, an earlier attempt had detailed line hair, three-quarter faces, and shoulders. This result has no text or color, keeps the 3:2 ratio, draws one frame per person, and keeps the curls, bun, and hoop earrings. It closely matches the reference, but the two faces share the same shape and expression, the man's stubble is gone, and the heads are larger than the requested 60-65%.
