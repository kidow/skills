# ASCII Art

A photo rebuilt as image-to-ASCII art, a strict grid of monospaced keyboard characters on black, where character density makes the tones and character color follows the photo.

## Prompt

```text
Convert the attached photo into ASCII art: a picture made only of monospaced keyboard characters arranged in a strict text grid on a solid black background, like a computer terminal.

No photo underneath: this is not a photo with a text overlay. There is no photographic image at all. The picture exists only as colored characters on pure black, and pure black must show between every character and line.

Grid: every character sits in a perfectly regular grid of equal-width columns and equal-height rows, with no rotation, overlap, or scaling. Use about 100 to 130 columns across the width of the image, so each character is clearly readable as a keyboard symbol while the picture still reads from a distance.

Tone: map brightness to character density. Use dense characters such as @, #, %, &, 8, and B for the brightest areas, middle characters such as *, +, =, o, and x for midtones, light characters such as :, -, ., and ' for dark areas, and leave dark and shadowed areas as empty black space or sparse dots, so the picture has strong black gaps.

Edges: follow strong edges and contours with characters whose shapes match their direction where it helps, such as /, \, |, _, (, and ).

Color: color each character with the photo's color at that spot, slightly brightened and saturated, glowing softly against the black background, like colored terminal text. Each character has one flat, uniform color, with no texture, shading, or photographic detail inside it.

Subject: keep the photo's subject, setting, composition, and main colors recognizable. Don't add objects that aren't in the photo.

Characters must not form readable words, names, or numbers. Don't include any text outside the grid, logos, watermarks, window frames, or terminal interface.

Show only the character grid filling the whole frame, with no border or margin.

Keep the same aspect ratio as the attached image.
```

## Observed in references

These traits come from viewing Google image results for "ascii art" from the user's link and from the source below. The images weren't stored. Add the ones you want to the image prompt.

- **Image conversion:** most results are photos converted into dense character grids, often colored characters on black, like generator output.
- **Monochrome:** many are black or gray characters on white, or green and white characters on black, like old terminals.
- **Line art:** classic hand-typed ASCII art uses sparse outlines made of slashes, underscores, and parentheses on white, closer to a drawing.
- **Emoticons:** some results are small text faces and animals, such as a shrugging face, which this style doesn't follow.
- **Glitch:** some posters mix characters with glitchy streaks, symbols, or pixel blocks.
- **Overlap:** `retro-game-pixel-art` and `pixel-sticker` build images from square pixels, while this style builds them from text characters.

## Sources

- [Wikipedia: ASCII art](https://en.wikipedia.org/wiki/ASCII_art)

## Examples

- [bicycle-repair.webp](examples/bicycle-repair.webp): conversion of a generated photo of two people repairing a bicycle on a street, made with `gpt-image` using the no-photo-underneath, 100-to-130-column, black-gap, and flat-color rules now in the prompt, given as overriding requirements at the time. Without them, an earlier attempt looked like the photo with a fine character grid laid over it. This result has no words, keeps the 3:2 ratio and the source's people, poses, clothing colors, bicycle, and street, and shows colored characters such as 8, @, #, and * on black. Some photographic shading still shows in the faces and hands, and a thin black edge runs around the frame.
