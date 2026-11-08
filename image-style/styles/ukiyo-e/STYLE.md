# Ukiyo-e

A photo redrawn as an Edo-period Japanese woodblock print, with crisp black keyblock outlines, flat areas of color, soft color gradations, and aged paper.

## Prompt

```text
Convert the attached photo into an original Japanese ukiyo-e woodblock print from the Edo period. Avoid copying any specific existing artwork, and don't add Mount Fuji, a great wave, or other famous motifs unless they're in the photo.

Line: clear, confident black keyblock outlines around every shape, with smooth, flowing curves and slightly varied thickness, as if carved into a woodblock.

Color: flat, unshaded areas of color printed from separate blocks, in a muted traditional palette such as Prussian blue, indigo, vermilion, soft red, ochre, sage green, and cream. Use bokashi, a soft printed gradation, only in skies, water, and ground. No modeled shading or cast shadows.

Patterns: fill clothing and fabric with simple printed patterns, such as checks, stripes, or small motifs, and render water, clouds, rain, and plants with stylized, repeating lines and shapes.

Composition: a flat, decorative composition with a high or bold viewpoint, strong diagonals, and experimental cropping. Keep the photo's subject, setting, composition, and main colors recognizable, and redraw people with simplified faces and elegant, stylized features. Don't add major objects, people, or animals that aren't in the photo.

Surface: the look of a printed woodblock on handmade washi paper, with soft paper fiber, slight wood grain in flat areas, and gently aged, warm tones. No photographic detail, smooth digital rendering, or 3D.

Don't include any text, calligraphy, signature, seals, cartouches, or watermarks.

Keep the same aspect ratio as the attached image.
```

## Observed in references

These traits come from viewing Google image results for ukiyo-e pictures, searched in Korean. The images weren't stored. Add the ones you want to the image prompt.

- **Portraits:** many show kabuki actors and women in patterned kimono against plain mica-gray or cream backgrounds.
- **Landscapes:** famous landscapes show stylized waves with claw-like foam, mountains with gradated skies, and rain as fine parallel lines.
- **Snow:** snow scenes leave much of the paper bare, with soft gray shading.
- **Text:** most prints have calligraphy, title cartouches, and red seals, which this style leaves out.
- **Parodies:** results also include modern parodies with pop characters and athletes, which this style doesn't follow.

## Sources

The line, color, and composition rules come from these sources:

- [The Art Story: Ukiyo-e Japanese Prints](https://www.theartstory.org/movement/ukiyo-e-japanese-woodblock-prints/)
- [Birmingham Museum of Art: Quick Guide to Japanese Woodblock Prints](https://learn.artsbma.org/resource/quick-guide-to-japanese-woodblock-prints/)

## Examples

- [bicycle-repair.webp](examples/bicycle-repair.webp): conversion of a generated photo of two people repairing a bicycle on a street, made with `gpt-image` from the prompt above plus overriding requests to keep the source's clothing, add patterns only where the photo has them, and leave out any border. Those overrides replace the prompt's rule to fill clothing with printed patterns. Without them, an earlier attempt turned the sweaters into patterned kimono-like jackets and added a rounded border. This result has no text, seals, or border, keeps the 3:2 ratio and the source's people, poses, sweaters, jeans, sneakers, bicycle, and street, and shows keyblock outlines, flat muted colors, bokashi on the road, and stylized ivy and trees on aged paper. With plain modern clothing, it reads closer to a modern illustration in ukiyo-e style than to an Edo print.
