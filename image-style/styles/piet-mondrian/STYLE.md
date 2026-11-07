# Piet Mondrian

In the style of Dutch painter Piet Mondrian: a photo abstracted into an asymmetrical grid of horizontal and vertical black lines with primary-color rectangles on layered paper.

## Prompt

```text
Convert the attached photo into an original abstract geometric composition inspired by the neoplastic paintings of Piet Mondrian. Avoid copying any specific existing artwork.

Abstraction: reduce the photo's subject to its essential structure, the way Mondrian abstracted trees step by step into horizontals and verticals. Base the placement and size of the rectangles on the subject's main masses and position, and base the color choices on its main colors. Don't draw the subject literally. It should still read clearly at thumbnail size as a strong composition.

Vocabulary: use only straight horizontal and vertical black lines and rectangles. No diagonals, curves, circles, or tilted shapes.

Color: use only red, blue, and yellow, plus white, black, and gray. Use white or pale gray for most of the area, and keep color blocks limited, with one as the strong focal accent.

Composition: an asymmetrical but carefully balanced arrangement of large and small rectangles, with no central symmetry. Vary spacing to create a crafted visual rhythm.

Grid precision - critical: the black lines form one precise, continuous grid. Every line is perfectly straight and keeps one constant thickness along its whole length, and it ends only at another line or at the frame edge, never in open space. Lines meet in clean T and cross junctions with no gaps, steps, or offsets. Every color or gray rectangle exactly fills one grid cell, edge to edge, bounded by black lines on all sides. Rectangles never overlap lines or each other, never sit on top of another shape, never extend past a cell, and are never broken or misaligned.

Medium: handmade paper-cut illustration, with the paper pieces fitted flush like an inlay rather than stacked. Keep any shadow extremely subtle, only along the edges of the black lines. Keep the surface matte, with slight paper texture.

Use a clean composition and purposeful details. No text, signature, or watermark.

Keep the same aspect ratio as the attached image.
```

## Observed in references

The user's original reference image isn't stored. It showed these traits, which this style removes because they conflict with Mondrian's rules. Add them to the image prompt only if you want that look.

- **Diagonals:** the whole composition is tilted about 30 degrees.
- **Circles:** concentric white, red, and yellow circles form the focal point.
- **Layout:** shapes float on a pale background instead of forming a grid.
- **Medium:** layered matte paper with small soft shadows, which this style keeps.

## Sources

The line, color, balance, and abstraction rules come from these sources:

- [Harvard Art Museums: Composition with Blue, Black, Yellow, and Red](https://harvardartmuseums.org/art/181354)
- [MoMA: Piet Mondrian](https://www.moma.org/artists/4057)
- [Wikipedia: Piet Mondrian](https://en.wikipedia.org/wiki/Piet_Mondrian)
- [National Galleries of Scotland: De Stijl](https://www.nationalgalleries.org/art-and-artists/glossary-terms/de-stijl-style)

## Examples

- [bicycle.webp](examples/bicycle.webp): conversion of a generated photo of a red bicycle against a wall, made with `gpt-image` from the prompt above plus requests for one line thickness, no black bars for parts of the subject, and a check of every line end. Without those additions, an earlier attempt left a thick black bar ending in open space. Before the grid precision rule, rectangles overlapped and broke the lines. This result has no text, keeps the 3:2 ratio, and uses only horizontal and vertical lines with red, yellow, blue, gray, black, and white. Its lines are even and connected, but a few red areas near the frame's center and pedal are L-shaped rather than true rectangles. The flush inlay also reads flatter than layered paper. The bicycle stays recognizable as a frame, which is more literal than Mondrian's abstract paintings.
