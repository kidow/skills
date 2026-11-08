# Low Poly

A photo rebuilt from a mesh of flat-colored triangles, like a faceted low-polygon digital illustration, with shading carried by the facets.

## Prompt

```text
Convert the attached photo into an original low-poly illustration, built entirely from a mesh of flat triangular facets.

Facets: cover the whole image with a triangle mesh. Each triangle is filled with one solid, flat color, sampled from the photo at that spot, with no gradients or texture inside a facet. Neighboring triangles share edges with no gaps and no outlines.

Mesh density: use a fairly coarse mesh, so the triangles are clearly visible at a glance. Use somewhat smaller triangles around important details, such as faces, eyes, and edges, and larger triangles on smooth or plain areas, such as skies, walls, and backgrounds.

Shading: express form, light, and shadow only through the different colors of neighboring facets, with strong light-to-dark contrast, so the subject looks faceted and slightly three-dimensional, like cut crystal. Keep the photo's light direction.

Subject: keep the photo's subject, setting, composition, and colors recognizable. The subject must be at least as clearly faceted as the background, with every part built from visible triangles and its silhouette following clean, angular facet edges. Simplify thin parts boldly into faceted shapes: render thin rings as thick faceted rings, and omit or reduce fine details such as spokes, wires, or strands. No thin smooth lines or smooth round curves anywhere. Don't add objects that aren't in the photo.

Surface: crisp, clean digital vector look. No photographic texture, painterly strokes, paper texture, or visible wireframe lines.

Don't include any text, logos, or watermarks.

Keep the same aspect ratio as the attached image.
```

## Observed in references

These traits come from viewing Google image results for "poly art". The images weren't stored. Add the ones you want to the image prompt.

- **Isolated subjects:** many show a single animal or face on a plain or white background, with the setting left out.
- **Colors:** some keep natural photo colors, while others use bold, saturated palettes such as blue, purple, and pink on a bird.
- **Portraits:** faces use many small triangles around the eyes and lips, sometimes blending into realistic detail.
- **3D versions:** results also include rendered 3D low-poly scenes and models, and wireframe line drawings, which this style doesn't follow.
- **Overlap:** `cubist-illustration` uses larger planes with outlines and multiple viewpoints, and `origami-paper-model` is a photographed paper model, while this style is a seamless flat triangle mesh.

## Examples

- [bicycle.webp](examples/bicycle.webp): conversion of a generated photo of a red bicycle against a wall, made with `gpt-image` using the faceted subject, bold simplification, and coarser mesh rules now in the prompt, given as additions at the time. Without those rules, an earlier attempt kept thin, smooth spokes and a lightly faceted frame. This result has no text, keeps the 3:2 ratio, the source's composition, and its natural colors, and shows the whole scene as clearly visible triangles. The wheels became thick faceted rings with the spokes omitted, and the frame is built from strong light-and-dark facets. The wheels' interiors share the wall's facets, so they read slightly transparent.
