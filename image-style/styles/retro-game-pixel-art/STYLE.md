# Retro Game Pixel Art

A photo fully reinterpreted as a 16-bit console game sprite or background, with blocky pixels, dithering, and a limited palette, with no border or text.

## Prompt

```text
Convert the attached photo into an image in the style below.

[Work order - important]
Step 1: Fully reinterpret the forms like a 90s retro game (16-bit console) sprite or background, not a realistic photo. Remove all realistic photographic texture (light reflections, fine surface grain, gradient shading), and simplify into large color blocks and clear outlines.
Step 2: Downsample the simplified forms angularly onto a real pixel grid. Use only block-unit pixels with distinct stair-stepping, with no smooth curves or anti-aliasing.
Always work in the order of "simplify forms, then pixelate". Original detail must not show through as if a pixel filter were simply laid over the photo.

[Overall composition]
- The pixel art fills the entire canvas.
- Keep pixel size consistent across the whole image (for example, based on a grid 64-96 pixels wide). Render at a unified resolution, with no areas where detail becomes partly denser or sparser.
- Express shading with dot-level dithering patterns instead of smooth gradients.

[Color]
- Use a limited retro game palette of 16-32 colors. Mostly slightly saturated primary colors with the feel of SNES/Mega Drive era game sprites (deep blue, coral red, lime green, yellow, and so on), plus near-black outlines.
- Noticeably limit the number of colors, expressing them in the abruptly stepped color levels typical of game palettes rather than natural, photo-like color transitions.

[Form simplification by subject]
- Food: don't draw each ingredient's realistic texture; simplify into chunks like an in-game item icon (for example, a soup dish as a bowl plus 2-3 color blocks of contents).
- Products: keep a brand logo or signature form recognizable, with flat pixel-block surfaces.
- People/animals: simplify to 2-3 head-tall SD proportions like an 8-16-bit game character sprite, with facial features expressed in only minimal pixel dots.
- Landscapes/buildings: compose sky, mountains, and buildings as overlapping pixel layers, like a retro game background tilemap.

[Border and text]
No border or frame. Don't add text, logos, keyword lists, or game UI elements such as health bars, coin counters, or star icons.

[Avoid]
- The photo's original forms, lighting, and detail showing through beneath the pixel grid
- Pixels with smooth gradients or remaining anti-aliasing
- So many colors that it looks close to a real photo
- Pixel sizes that vary by area, making the resolution inconsistent

[Ratio]
Same as the attached image.
```

## Observed in references

The user's original reference images aren't stored. They showed these traits, which the prompt doesn't state. Add the ones you want to the image prompt. The references also have a cream mount, titles, and game UI text, which this style removes by the user's choice.

- **Proportions:** people and subjects aren't always SD. One person has natural anime-like proportions with a detailed face.
- **Scenes:** settings are rich and full of small elements, such as a classroom with cherry blossoms outside, or a beach with a bridge and tiny figures.
- **Outlines:** subjects have near-black outlines, while distant scenery often has none.
- **Dithering:** checkerboard dithering shows most in clouds, skies, grass, and fur.
- **Color:** one main hue often dominates the image, such as lime green or deep blue.

## Examples

- [bicycle.webp](examples/bicycle.webp): conversion of a generated photo of a red bicycle against a wall, made with `gpt-image` from the prompt above. It has no border or text, keeps the source's 3:2 ratio, and shows clear stair-stepping, checkerboard dithering, and near-black outlines. Pixel size varies a little, and some pixel edges look slightly soft rather than perfectly crisp.
