# Glitch Art

A photo corrupted into digital glitch art, with RGB channel splits, shifted horizontal slices, pixel-sorted streaks, and blocky compression errors, while the subject stays recognizable.

## Prompt

```text
Convert the attached photo into an original piece of digital glitch art, as if the image file or video signal had been corrupted.

Channel split: separate the red, green, and blue channels so edges show offset red and cyan fringes, shifted a few pixels sideways, strongest around the subject's outlines.

Slices: cut the image into several thin and thick horizontal bands and shift some of them left or right, so parts of the subject and background are sliced out of line. Repeat or stretch a few bands.

Pixel sorting: in a few areas, smear the pixels into long, straight streaks of sorted color, mostly vertical, dripping down from bright areas or flowing sideways from edges.

Data errors: add rectangular blocks of compression artifacts, such as blocky macroblocks, repeated tiles, and areas of misplaced or wrong-colored pixels, plus a few thin bands of digital noise and scan lines.

Color: keep the photo's colors as the base, and push parts of them into saturated, unnatural neon shades, such as magenta, cyan, electric green, and violet, inside the glitched areas.

Balance: glitch about a third to half of the image, and keep the main subject's faces and key shapes mostly recognizable, so the photo is clearly visible through the corruption.

Subject: keep the photo's subject, setting, composition, poses, and expressions recognizable. Don't add objects that aren't in the photo.

Surface: crisp digital pixels with hard edges in the glitched areas. No painted, drawn, or printed look, and no screen, monitor, or device around the image.

Show only the glitched image filling the frame, with no border or interface.

Don't include any text, error messages, code, logos, or watermarks.

Keep the same aspect ratio as the attached image.
```

## Observed in references

These traits come from viewing Google image results for "glitch art" from the user's link and from the source below. The images weren't stored. Add the ones you want to the image prompt.

- **Portraits:** many results are faces or classic paintings with sliced bands, RGB fringes, and faces dissolved into colorful streaks.
- **Pixel sorting:** some works melt the lower half of a figure or landscape into long vertical color drips.
- **Abstract:** fully corrupted images become dense, colorful noise, stripes, and blocks with no visible subject, which this style avoids.
- **Hand-drawn:** some drawings imitate glitch with offset red and blue marker lines on paper, which this style doesn't follow.
- **Neon:** skulls and figures on black with neon RGB edges are common in posters.
- **Overlap:** `ascii-art` rebuilds a photo from characters, and `halftone-art` from printed dots, while this style corrupts the photo itself with digital errors.

## Sources

- [Wikipedia: Glitch art](https://en.wikipedia.org/wiki/Glitch_art)

## Examples

- [bicycle-repair.webp](examples/bicycle-repair.webp): conversion of a generated photo of two people repairing a bicycle on a street, made with `gpt-image` from the prompt above. It has no text or interface, keeps the 3:2 ratio and the source's people, poses, smiles, clothing, bicycle, and street, and adds red and cyan channel fringes, shifted horizontal slices, vertical pixel-sorted drips in the leaves, magenta and green compression blocks, and noise bands. Most of the corruption sits in the background and edges, while the people stay almost photographic, with only a few slices crossing them.
