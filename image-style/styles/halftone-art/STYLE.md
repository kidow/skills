# Halftone Art

A photo turned into a bold retro halftone print, with tones made only from visible dots that grow and shrink on a regular grid, in two or three flat ink colors on paper.

## Prompt

```text
Convert the attached photo into a bold, graphic halftone print, like a retro pop-art screen print.

Dots: make every tone only from round halftone dots on a perfectly regular grid rotated about 45 degrees. Dots grow larger in dark areas until they merge into solid ink, and shrink to tiny specks in light areas, leaving bare paper in the brightest highlights. Use a coarse screen with clearly visible dots, about 60 to 90 dots across the width of the image, so the dot pattern itself is the main visual texture.

Ink: print with only two or three flat ink colors. Use one dark key ink for the halftone dots, such as deep navy, black, or dark purple, over one or two bright, flat background or accent colors chosen from the photo's main colors and pushed bolder, such as hot pink, yellow, cyan, orange, or acid green. No gradients, blending, or extra colors.

Contrast: posterize the photo into strong, high-contrast light and dark areas before screening, so faces and forms read clearly as bold graphic shapes.

Subject: keep the photo's subject, setting, composition, poses, and expressions recognizable. Simplify small details where the dots can't hold them. Don't add objects that aren't in the photo.

Surface: printed ink on slightly warm paper, with tiny misregistration between ink colors, a little dot gain, and faint paper grain. No photographic detail, smooth tones, or digital glow.

Show only the print filling the frame, with no frame, wall, border, or mockup.

Don't include any text, speech balloons, logos, or watermarks.

Keep the same aspect ratio as the attached image.
```

## Observed in references

These traits come from viewing Google image results for "halftone art" from the user's link. The images weren't stored. Add the ones you want to the image prompt.

- **Pop art:** many results are portraits with dark dots over neon pink, green, yellow, or blue backgrounds, often with comic-style outlines.
- **Monochrome:** black-and-white dot portraits with very fine screens look like old newspaper photos.
- **Line screens:** some use wavy or concentric lines that thicken in dark areas instead of dots, which this style doesn't follow.
- **Comics:** comic panels use flat Ben-Day dot fills with speech balloons, which this style leaves out.
- **Context:** many results show posters, mockups, or software tutorials with titles, which this style leaves out.
- **Overlap:** `georges-seurat` uses hand-painted dots in many mixed hues, and `ascii-art` uses text characters, while this style uses a mechanical dot grid in two or three flat inks.

## Sources

- [Wikipedia: Halftone](https://en.wikipedia.org/wiki/Halftone)

## Examples

- [bicycle-repair.webp](examples/bicycle-repair.webp): conversion of a generated photo of two people repairing a bicycle on a street, made with `gpt-image` from the prompt above. It has no text or frame, keeps the 3:2 ratio and the source's people, poses, smiles, bicycle, and street, and prints everything in coarse navy and hot-pink halftone dots with yellow accents on warm cream paper, with slight misregistration. With only three inks, the man's green sweater and the blue jeans became navy dots, so the photo's clothing colors aren't kept.
