# Crayon Kid Drawing

A photo redrawn as a very clumsy crayon drawing, as if a kindergartener scribbled it in a hurry.

## Prompt

```text
[Conversion goal]
Convert the attached photo into a very clumsy drawing that looks like a kindergartener roughly drew it with crayons.

[Style]
- Very clumsy, unskilled drawing with wobbly, broken lines
- Distorted proportions (big head, small body, uneven arm lengths)
- Faces are only dot eyes and a smiling mouth
- No shading, shadows, or realistic rendering
- Coloring may spill outside the lines
- Crayon texture (rough, imperfect coloring)

[People]
- Turn real people into simple child-drawing characters
- Make each person distinguishable from the others
- Keep their original positions and approximate poses

[Background]
- Keep the original composition, but simplify it
- Buildings: rectangles with random windows
- Sky: scribbled clouds
- Sun: a circle with lines
- Ground: flat coloring
- Doodles such as hearts and flowers may be added

[Color]
- Mostly primary colors such as red, blue, yellow, and green
- No gradients
- Rough, uneven lines and coloring

[Overall feel]
It should feel like a real young child drew it in a hurry. Low polish is fine. The cruder and sloppier, the better.
```

## Observed in references

The user's original reference images aren't stored. They showed these traits, which the prompt doesn't state. Add the ones you want to the image prompt.

- **Coloring:** dense, diagonal back-and-forth scribbles fill almost the whole page, with white paper showing through as flecks.
- **Outlines:** thick, waxy black lines surround most figures and objects.
- **Text:** signs, banners, and jerseys stay readable as wobbly hand lettering, in Hangul and Latin alike.
- **Faces:** expressions go beyond a plain smile when the scene calls for it, such as a wide-open shouting mouth.
- **Crowds:** large groups become many tiny figures in repeated colors.

## Examples

- [park-kite.webp](examples/park-kite.webp): conversion of a generated photo of a person flying a kite with a dog near a house, made with `gpt-image` from the prompt above plus the coloring and outline traits. Without those two traits, an earlier text-only test left large white areas and had thin colored outlines, so add them to match the references. The person is larger than in the source, and the sun, hearts, and flowers were added by the model.
