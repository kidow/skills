# Bauhaus Modular

A photo rebuilt on a modular grid of Bauhaus geometric tiles, with circles, half circles, quarter circles, triangles, and squares in primary colors and black on cream.

## Prompt

```text
Convert the attached photo into an original geometric composition in the style of Bauhaus graphic art. Avoid copying any specific existing artwork.

Grid: divide the whole image into a coarse modular grid of large, equal square tiles, about 12 tiles across the width, with no thin lines drawn between tiles. Fill each tile with one or two simple flat geometric shapes: a full circle, a half circle, a quarter circle, a triangle, a square, or a stripe, rotated in 90-degree steps.

Subject: build the photo's subject, setting, and composition entirely from whole tiles, so the subject's silhouette and main parts are readable as a pattern of blocky geometric pieces. Simplify the subject boldly to fit the tiles: round forms become rings or groups of quarter-circle tiles, and long thin parts become rows of stripe or half-circle tiles. Don't draw free curves, thin lines, or illustration on top of the tiles.

Color: a limited Bauhaus palette of red, yellow, blue, and black on a cream or off-white ground, plus one or two of the photo's main colors, such as orange or green, if needed. Keep the subject's main color recognizable, and use the cream ground for empty tiles.

Shapes: flat, solid color with crisp, precise geometric edges and no outlines, shading, gradients, or texture beyond a faint print grain.

Don't include any text, letters, numbers, logos, or watermarks.

Keep the same aspect ratio as the attached image.
```

## Observed in references

These traits come from viewing Google image results for "bauhaus art". The images weren't stored. Add the ones you want to the image prompt. This style follows the modular tile prints that dominate those results.

- **Tiles:** many prints are grids of quarter circles and half circles in one or a few colors, such as red and orange, or black and cream.
- **Posters:** many prints add "BAUHAUS" and a year in bold sans-serif type, which this style leaves out because it uses no text.
- **Figures:** some build faces and figures from flat geometric pieces, with a large eye as the focal point.
- **Paintings:** results also include Kandinsky-like abstract paintings with circles, lines, and soft color, and Oskar Schlemmer-like figure paintings, which this style doesn't follow.
- **Overlap:** `piet-mondrian` uses only straight lines and rectangles, and `midcentury-cut-paper` uses irregular hand-cut shapes, while this style uses a strict grid of curved and straight tiles.

## Examples

- [bicycle.webp](examples/bicycle.webp): conversion of a generated photo of a red bicycle against a wall, made with `gpt-image` using the coarse grid, whole-tile subject, and bold simplification rules now in the prompt, given as additions at the time. Without those rules, an earlier attempt drew the bicycle freely over a thin grid. This result has no text, keeps the 3:2 ratio and the source's composition, and builds the bicycle from bold flat pieces that follow the tile grid, with ring-shaped wheels, cross-shaped spokes, and triangle-tile foliage. Some pieces, such as the handlebar curve and the frame's dip, still cross tile edges as free shapes, so it's closer to tiles than before but not strictly modular.
