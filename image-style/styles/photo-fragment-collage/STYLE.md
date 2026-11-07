# Photo Fragment Collage

One photo split into six crops and views, arranged in a neatly aligned grid on pale paper like a quiet magazine layout.

## Prompt

```text
Turn the attached photo into a minimal, emotive photo collage poster according to the rules below.

[Overall mood]
A refined magazine editorial design with photo fragments precisely arranged on bright off-white paper. Express a calm, sophisticated mood with wide margins, natural photo texture, and restrained color.

[Photo composition]
Build the composition around the main subject of the attached photo, such as food, a product, a person, an animal, or a landscape.
From the original photo, choose the whole view, characteristic parts, surface textures, and the surrounding environment, and make 6 photo fragments with different crops.

Combine 1-2 images in which the subject is recognizable with close-up detail images. Don't repeat the same crop, and don't arbitrarily add new major objects or places that aren't in the photo. Preserve a person's face, an animal's markings, the shape of products and food, and the main features of a landscape.

[Layout]
Gather the 6 photo fragments at the center of the frame as one small collage.
The whole collage takes up about 55-65% of the frame width and about 55-60% of its height, leaving generous margins outside.

Arrange the collage in three rows of two photos: two vertical photos on top, a long horizontal photo and a small vertical photo in the middle, and a small detail photo and a relatively large photo on the bottom.
Align everything precisely to one grid. Photos in the same row have the same height and the same top and bottom edges, and all three rows share the same left and right edges so the collage forms one clean rectangle. Vary the balance only through the photos' widths and each row's height. Don't offset photos' sizes or starting positions.

Render every photo as a straight rectangle, with thin, uniform off-white gaps between photos. Don't tilt or overlap photos, and don't include rounded corners, shadows, borders, torn paper, or tape.

[Color]
Extract the main colors from the original photo and keep the color temperature and contrast consistent across all photo fragments.
Avoid excessive saturation and strong retouching, and bring out natural light, soft shadows, and delicate material textures.
Don't turn every photo brown or apply a vintage filter by default; keep colors that suit the subject.

[Background]
The entire background is a solid bright off-white or very pale warm gray.
Render the paper texture so subtly it's almost unnoticeable. Don't add decoration to the margins around the photos.

[Text rules]
Text is optional. Without wording or a request for text, include no text at all.
If text is included, place it only at the top, the bottom, or both.
Render it as small, crisp dark gray text, and keep spelling and grammar accurate.
Don't copy wording from references. Don't include arbitrary dates, brand names, numbers, logos, watermarks, or extra explanations.

[Output]
Generate only one finished poster.
The poster itself fills the frame, with no frame, wall-hung mockup, or open magazine.
```

## Observed in references

The user's original reference images aren't stored. They showed these traits, which the prompt doesn't state. Add the ones you want to the image prompt. The references also offset their photos, which this style replaces with an aligned grid by the user's choice.

- **Ratio:** posters are 3:4.
- **Text:** when text is used, short lowercase phrases in a spaced typewriter or monospace font sit centered at top and bottom, such as a brief poetic line that fits the subject.
- **Crops:** the fragments mix one wide shot, a close portrait or object view, a texture such as fur or fabric, and an environment detail such as a window or wall.
- **Light:** the same soft, warm side light runs across all fragments, so they read as one photo shoot.
- **New views:** some fragments show angles beyond a simple crop of one photo.

## Examples

- [bicycle.webp](examples/bicycle.webp): conversion of a generated photo of a red bicycle against a wall, made with `gpt-image` from the prompt above plus a 3:4 ratio, a collage size of about 60%, and lowercase typewriter text. Without those additions, an earlier attempt came out about 11:12 with a larger collage and serif title-case text. This result is exactly 3:4, its rows share the same left and right edges to within about 2 px, and the collage takes about 65% of the width and 62% of the height, slightly over the request. The collage sits a little below center, and its subject, flowers, and shadows come from the source.
