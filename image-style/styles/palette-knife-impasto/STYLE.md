# Palette Knife Impasto

A subject converted into a thick palette-knife oil painting that stands out in relief from warm cream paper, with no text.

## Prompt

```text
Convert the subject in the attached photo into a square miniature painting in palette knife impasto oil style.

[Style - emphasize dimensionality]
- Impasto technique with paint boldly built up with a palette knife, thick enough to look like it actually protrudes 3-5 mm from the surface
- Each mass of paint must clearly keep directional stroke marks (the grooves and ridges left by the knife)
- Assume lighting from the upper left: raised paint gets bright highlights, and recessed or overlapping areas get distinct shadows, so that light and shadow contrast strongly as on a real oil painting surface
- Add a slight shadow at the paint edges so each mass of color looks stacked on a different layer (so it does not look flat like a photo)
- Follow the original photo's subject silhouette, colors, and composition, but simplify the form into thick masses of paint rather than realistic rendering
- Keep a restrained density where the form reads from just a few bold, dimensional knife strokes, without excessive detail

[Background]
- Fixed warm ivory/cream watercolor paper background with a slightly bumpy visible texture
- Keep the background flat so it contrasts with the subject's dimensionality

[Text]
- No text, handwriting, captions, or signatures anywhere in the image

[Ratio/composition]
- Output ratio fixed at 1:1
- Place the subject at the center of the frame with generous margins, simply the single subject with no props
```

## Observed in references

The user's original reference images aren't stored. They showed these traits, which the prompt doesn't state. Add the ones you want to the image prompt.

- **Paint surface:** strokes are chunky, broken shards with rough, crackled edges rather than smooth ribbons.
- **Silhouette:** subjects sit cut out on the paper, often with a thin raised halo of cream paint following the outline.
- **Scale:** subjects take up about 60–80% of the frame, leaving clear paper on every side.
- **Scenes:** a landscape becomes an irregular square patch of paint with rough edges, floating on the paper.
- **Ground:** the cream ranges from pebbled paper to plaster-like knife marks, and stays pale rather than orange.
- **Fine detail:** where a subject has key small marks, such as eyes or emblems, they stay legible in small dabs of paint.

## Examples

- [teapot.webp](examples/teapot.webp): conversion of a generated photo of a blue enamel teapot on a kitchen table, made with `gpt-image` from the prompt above plus the surface, silhouette, ground, and scale traits and a request to keep source colors true. Without those additions, an earlier attempt had smoother strokes, brighter blue, and peach paper. This result matches the references better, but the teapot still spans about 85–90% of the width despite a 60–70% request, and its cream halo is more even and sticker-like than the references.
