# Pixel Sticker

A photo's main subject reimagined as a cute, finely detailed pixel art sticker in soft warm colors on pure white, with no decorations.

## Prompt

```text
Deeply analyze the uploaded image and rebuild it as a very high-quality, cute, and lovable pixel sticker illustration.

Keep the same aspect ratio as the uploaded image.

# Core goal
This is not simply a pixel effect applied to a photo.
Keep the original subject's identity and features, and express it as a charming, cozy pixel art illustration that looks freshly taken from an emotive indie game or a premium pixel sticker collection.

The overall impression should feel like:
- Cute Pixel Art
- Premium Pixel Sticker
- Cozy Indie Game
- Soft Pastel Palette
- Handmade Pixel Illustration
- Kawaii Pixel Character
- Collectible Character Art

Don't directly imitate the design of a specific game or existing character. Make it entirely original cute pixel art.

# Applicable subjects
This applies to people, dogs, cats, animals, food, desserts, drinks, characters, figures, toys, products, plants, and objects.
Automatically analyze the uploaded image, naturally separate the most important main subject, and rebuild it in a form suited to pixel art.

# Preserve the original
Very important. Always keep these elements of the uploaded subject: identity, form, silhouette, overall proportions, pose, expression, direction, main colors, clothing, hairstyle, markings, ingredient composition, characteristic props, and unique details.

Don't arbitrarily change a face, expression, clothing, or hairstyle; add or remove food ingredients; change a product design or an animal's breed; excessively change colors; distort forms; add unnecessary characterization; or add new props.

Reinterpret it cutely only through pixel art, without losing the original's features.

# Subject extraction
Cleanly and naturally extract the most important main subject from the image.
Keep elements that form one composition with the main subject together with it. For example:
- Keep a drink with its cup and toppings
- Keep a cake with its plate or stand
- Keep food with a naturally connected bowl
- Keep a person with the main prop they hold
- Keep an animal with the leash or clothing it wears
- Keep a product's whole package form

Remove unnecessary backgrounds and surrounding objects.

# Pixel art style
Express the whole subject as cute, finely made pixel art. It must not look like a simple low-resolution image.
Always apply:
- Regular, clean pixel units
- A crisp silhouette
- Tidy pixel outlines
- Round, soft forms
- Soft pixel shading
- Rich but uncomplicated detail
- Intentionally placed pixels, down to small parts
- Clearly visible faces and main features
- Precise pixel construction that holds its form when enlarged

Don't make the pixels too large or rough. It should look like refined, high-resolution pixel art overall.

# Cute proportions
Keep the original's identity and silhouette, but refine the overall form to be slightly more lovable:
- Round silhouette
- Short, stable proportions
- Soft, curved forms
- Small, cute hands and feet
- Plump, appetizing forms for food
- Cutely emphasized fur and ear features for animals
- Clear, lovable expressions for characters

For people, don't make the head excessively large or shrink the body too far like an SD character. Keep the person's unique proportions and features while naturally converting them into a cute pixel character.

# Expression
Prioritize keeping the original expression.
For subjects whose expression is hard to see or absent, aim for comfort, warmth, innocence, slight shyness, and pleasant calm.
Avoid excessively wide smiles or forced cuteness.
Don't arbitrarily add a face, eyes, or a mouth to food or products. Keep an existing face and expression only when the original is a character.

# Color
Color is very important. Keep the original's representative colors while arranging everything into cute, harmonious colors:
- Soft pastel colors
- A warm color temperature
- Clear, clean saturation
- Creamy color combinations
- A cozy, sweet mood
- Colors that connect naturally with one another
- A bright, positive impression

Avoid overly murky or strongly gray colors, and don't use fluorescent colors or excessively strong primary colors.
Don't completely change the original colors; adjust them to be a little more lovable based on the original.

# Shading and texture
Keep shading uncomplicated:
- Simple pixel shading in 2-4 levels
- Soft, round volume
- Warm highlights
- Natural shadows
- Clear but not excessive dimensionality

Remove fine, photo-like texture. Instead, simplify only the core textures that identify the subject into pixels.
Express food as moist and soft, and animal fur's direction and volume as small pixel clusters.
Plastic-like 3D rendered texture is forbidden.

# Background
The background must be pure white #FFFFFF.
Don't add scenery, rooms, furniture, patterns, colored backgrounds, gradients, floors, walls, game maps, UI screens, or decorative frames.
It should look like a clean white studio background overall.

# Layout
Place the main subject large at the center of the frame.
The subject takes up about 80% of the image area, and the remaining 20% or so stays clean breathing room.
The subject must not touch or be cut off by the image edges. Main parts such as the head, ears, hands, feet, plates, cups, and packaging must not be cropped out of the frame.
Center it by default, adjusting the position very slightly to suit the subject's pose and direction.

# Shadow
Add only a very small, subtle elliptical pixel shadow under the subject. It only serves to connect the subject naturally and keep it from looking like it's floating.
Forbidden shadows: dark black shadows, widely spreading shadows, realistic shadows, strongly directional shadows, multiple layers of shadow, and excessive reflected light.

# Decorations
Don't add any decorations around the subject, such as hearts, flowers, stars, sparkles, paw prints, ingredient pieces, or motifs derived from the subject. The final image has only the main subject on a clean white background.

# Mood
It should feel warm, cozy, soft, lovable, comfortable, charming, collectible, cute like a small game item, and like a sticker worth keeping.
At first sight, it should naturally draw the reaction "this is so cute."

# Forbidden
Never add text, sentences, names, prices, logos, brand names, watermarks, speech bubbles, dialogue boxes, game interfaces, health bars, item windows, buttons, frames, borders, card designs, complex backgrounds, or actual game screens.
Never use 3D rendering, vector illustration, cel animation, realistic rendering, oil paint texture, watercolor texture, rough dots, blurry pixels, uneven pixel sizes, excessive noise, fake detail, or typical AI smearing.
Avoid duplicated body parts, incorrect hands and feet, abnormal faces, and faces added where the original has none.

# Final result
The final image should look like a high-resolution premium pixel sticker illustration, with one main subject placed large on a pure white background.
Clearly keep the original subject's identity and features, and complete it as original pixel art with cute, warm colors and refined pixel work.
It should be finished enough to use right away as a social media profile image, sticker, emoticon, merchandise, character card, brand symbol, or pixel character collection.
```

## Observed in references

The user's original reference images aren't stored. They showed these traits, which the prompt doesn't state. Add the ones you want to the image prompt. The references also have small decorations, such as hearts and sparkles, which this style removes by the user's choice.

- **Pixel size:** pixels are visibly blocky, coarser than "high-resolution" suggests, with stepped edges that stay obvious at full view.
- **Outlines:** dark subjects have near-black outlines, while light subjects often use a darker tone of their own color.
- **Sticker edge:** some subjects have a thin white die-cut outline.
- **Scene elements:** a landmark can keep a small base of trees and a path, forming a self-contained scene.
- **Rendering:** color steps stay soft, with little dithering, so subjects read as painted pixels rather than strict retro game sprites.

## Examples

- [bicycle.webp](examples/bicycle.webp): conversion of a generated photo of a red bicycle against a wall, made with `gpt-image` from the prompt above. It has no decorations or text, keeps the 3:2 ratio, removes the wall and flowers, and spans about 83% of the width and 86% of the height without being cut off. Its red is stronger than the prompt's soft pastel, and its corners measure near-white (253–255) rather than exactly #FFFFFF, so don't rely on it where pure white matters.
