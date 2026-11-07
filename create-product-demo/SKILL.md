---
name: create-product-demo
description: Creates or refines short feature-intro and how-to videos using the real product UI. Covers step-by-step draft agreement, natural cursor, typing, and processing waits, filming mockups, and MP4 verification. Use when the user wants to make or polish a product demo, feature intro, or tutorial video from actual screens.
---

# Product Demo Videos from Real Screens

Make a video that lets viewers understand, in one watch, where a feature starts and how it finishes. Build it around real UI interaction and feedback rather than relying on explanatory text placed over the screen.

This document defines the production process and quality bar. It does not authorize changing a service's data or publishing externally. The user's latest request, project rules, and choices already agreed on take priority.

## 1. Align on the goal and filming scope first

Check the current conversation and work so far, and don't re-ask what is already decided. Fill in only the information below that affects the result, asking about one important decision at a time with a recommendation attached.

- Who the feature is being introduced to, and what they should be able to do after watching.
- Where the video will be placed, and whether it shows the desktop or mobile screen.
- The start and end states to show, and the options that must be included.
- Length, aspect ratio, whether there is audio, and any movement the user likes in reference videos.

For a short desktop feature intro, **15 seconds / landscape 16:9 / 1920×1080 / 60fps / silent MP4** can be proposed as a starting point. Set length, ratio, and audio to suit the medium and content, and use a matching composition for mobile screens or vertical distribution. If the flow is long enough that actions overlap, shorten the input, drop less important steps, or extend the length. Don't force every action into 15 seconds at all costs.

## 2. Check the real flow and screens

1. In the app and environment the user specified, confirm the real path of entry → compose or select → options → run → done. Observe button names, placeholders, loading states, and the screen after submission.
2. If there is a reference site, look at the actual screens or videos you can access. Don't just copy the impression; extract the cursor deceleration, travel distance, pause lengths, and the purpose of each zoom in and out.
3. Keep the real product's fonts, colors, spacing, icons, buttons, and photo ratios. Don't arbitrarily redesign core UI.
4. When login or another user action is needed, guide the user through only the necessary steps. Don't create filming posts or data on the live service on your own.

Preserve the original screens separately. Handle filming text, photos, and personal-information cleanup in a copy or in local video compositing. If service code needs changing, flag that as separate development work.

## 3. Show a short motion draft first

Before rendering the whole video in detail, confirm speed and direction with a representative section. Keep speed and ratio already agreed on through later revisions.

Keep the real screen at the center, and zoom in only enough for the current action to read. Unneeded QR codes, surrounding panels, and personal information can be left out of the filming area. Adjust margins and camera position without hiding where buttons and inputs are. Use captions only when needed for understanding.

## 4. Tidy filming mockups and attached assets

Replace meaningless development strings, test account names, and repeated empty items with natural fictional content. Match the names, content, times, and figures you would expect to see in that product, and apply the same mockup to the background behind open menus and modals.

The default method is **local replacement for the video**. If filling real server data is needed, confirm the target environment and the scope of creation and changes with the user. Permission to create a test item once does not extend to further creation or production changes. State briefly in the result where mockups and real captures were used.

For attached photos, prefer real assets that fit the product context. When extracting thumbnails from a user's video, check the following.

- Distinguish rotation metadata from actual pixel orientation, and visually confirm the desired landscape or portrait orientation.
- Pick a sharp frame that doesn't cut off the subject or important parts of the screen. Don't lose needed information to an automatic center crop.
- Use the same image and content on the editing and completion screens.
- Match sample copy to the content of the asset used and to the product's purpose. Don't invent facts or features that can't be confirmed from the asset.

## 5. Tie all movement to a single action timeline

Pushing and pulling scenes, cursor, clicks, typing, and camera separately makes the order slip easily. Define the following events on a common time base, and compute related keyframes together from those events.

`Screen ready → cursor arrives → click → UI reacts → input complete → brief check → move to next → run click → processing → done`

### Camera and zoom

- Consider zooming not only for body text but also for key actions such as the FAB, menu selection, image upload, options, and save. Hold the zoom across consecutive clicks in the same framing to avoid needless back and forth. When body text is finished, return to the full screen to show where the next action is.
- Frame **body text so the whole text area reads at the center**, and **edge buttons so the surrounding UI and original layout stay visible**. Don't move every FAB, upload, toggle, and save button to dead center. Leave margin so the whole button and its label aren't cut off. Keep the cursor's click coordinates distinct from the camera's center coordinates.
- Zoom enough that text and actions read at the final playback size. The reference draft used about 2.2x for body text and about 1.9–2x for edge buttons. Don't enforce these as fixed values; fit them to the source resolution, target size, and surrounding context.
- Start camera moves at about **0.6–0.8 seconds of ease-out**. In the reference draft, a 0.25-second transition was too fast and about 0.7 seconds was right. [Out Cubic](https://www.easing.dev/out-cubic), `cubic-bezier(0.215, 0.61, 0.355, 1)`, is a useful reference. Tune cursor speed and camera speed separately. Don't just swap the curve name; check the real transition time and output motion.
- **Don't stack a zoom on top of an existing zoom.** If the input MP4 already has camera movement, check that first. If the source capture or timeline exists, replace its camera path and re-render. If not, check what can be recovered, and avoid any approach that produces a nested two-stage zoom.
- Apply one camera transform to both screen and cursor. Interpolate position and scale together based on the actual viewport rectangle, and don't round crop coordinates or sizes to integers per frame. Use resampling that supports fractional coordinates to reduce stair-stepping in small movements. Settle the final framing first so boundary clamps don't suddenly kick in mid-interpolation.
- When margin extension is needed, extend only the product's empty background, naturally. Don't stretch edge pixels containing icons, text, or toolbars into streaks, or invent features outside the screen. Avoid needless background extension just to center an edge button.

### Cursor and focus

- Default to a decelerating ease-out for movement. Example: `easeOutCubic(t) = 1 - (1 - t)^3`. Don't finish a long move instantly in a short time.
- Start tuning entry into an input at about 0.6–0.9 seconds, considering distance and screen transitions. Don't click right on arrival or bounce into the next action; let the cursor settle briefly.
- Target **the start of the placeholder's first character**, not the center of the textarea. Measure the actual text position, including inner padding, font, and line height, rather than the element's border coordinates.
- Make the mouse hotspot, click indicator, input caret, and first character's start point share one coordinate system. Apply zoom and crop transforms identically to the screen and cursor.
- Pause briefly after clicking, then start typing. In a focused empty input, match the placeholder and caret behavior to the product.
- If the pointer covers text, move it naturally to an empty area after typing starts. Begin moving to the next button only after that input is complete.

### Typing

- Avoid several characters appearing in a chunk or the whole screen cross-fading. For Korean, implement from readable syllable units. Use real IME composition only when it can be reproduced.
- Add small variation to the base typing interval, and give sentence ends, spaces, and line breaks room that fits the context. Avoid excessive random delay.
- Keep the caret steady while typing and blink it only when stopped. Match character counts and button enabled states to the amount typed.
- Compositing that reveals the source text's pixels in order is acceptable. Keep the real font and line breaks, and don't use this approach to restyle product UI.

### Input completion and the next action

- After the last character, wait about 0.25–0.4 seconds before moving to the next button. Don't click the photo upload button while typing is still in progress.
- Keep the order of button arrival → click → attachment appears. Don't show the attached state before the photo is applied.
- Don't only slow the cursor; adjust the related camera moves and scene transitions with it. The screen must not move down before the body text can be read.

### Run and completion

- Don't place the submit, save, or send click and the completion screen at the same instant. Use processing states the product has, such as a disabled button or "Saving…".
- For a short intro video, start by considering about 0.7–1.2 seconds of processing time. This is a directing starting point, not a claim about real performance. Don't present feedback UI the product lacks as if it were a real feature.
- Let the cursor and camera rest briefly during processing. After completion is confirmed, zoom out and leave time to read the final result.

## 6. Rendering and verification

Check available tools first. If the `browser-video-recording` skill is installed, use it for capture and rendering steps, but give priority to the ratio and length the user set. If not, use the browser capture and deterministic frame rendering currently available. If a skill or tool needs installing, confirm whether that falls within what the user asked to install.

Store source captures, video mockups and images, timeline settings, render code, and finished MP4s separately. Rather than changing an installed shared renderer for one video's fix, adjust per-video settings or a wrapper. Keep the previous MP4 when revising, and output the new one under a new name.

Before finishing, actually check the following.

- **Event order:** input complete < move to next < button arrival < click < result shown. The submit processing state falls after the run click and before the completion screen.
- **Landing position:** the click lands at the very start of the placeholder, and the first character starts in the same spot.
- **Continuity:** mockup data, typed content, attached assets, and selected options match across menu, editing, and completion screens.
- **Representative frames:** extract and visually inspect frames right after focus, at first input, at input complete, at the photo button click, during processing, and right after completion. Also check the cursor and camera before and after any revised section.
- **Camera:** check zoom start, middle, hold, and zoom out against the actual click moments. Inspect for nested zooms, moves that kink at boundaries, pixel-level jitter, cut-off targets or labels, excessive centering, and traces of background extension. Confirm framing with representative frames, and judge speed and smoothness by playing the transitions. Don't conclude it's smooth just because frame counts match or there are no duplicate frames.
- **Video file:** use ffprobe or similar to check length, resolution, frame count, and frame rate, and decode the whole video to check for corruption. At 15 seconds and 60fps, that is 900 frames.

Don't call it a success based on settings alone. Check the actual output frames and action order at the times the user pointed out, then deliver.

## 7. Applying feedback and delivery

When feedback says a certain second feels awkward, first find the cause in that section. Change the related event and its dependent keyframes together, and keep motion that was previously approved. Re-verify that the new fix doesn't pull the next step earlier or make steps overlap.

Show the finished MP4 so it can be played right away, and briefly explain only the behavior changed and the length and ratio kept. If local mockups or compositing were used on real screen captures, don't hide that. If server data or product features weren't changed, keep that distinct from the video deliverable.

## Example structure for a short demo

An example of introducing a feature with input and attachment in 15 seconds. It assumes no specific product's button names or coordinates. For flows with no attachment or option selection, drop those steps and extend the time for checking the result. Set the real timeline by each action's reading time and sequence.

| Section | Action to show |
| --- | --- |
| 0–3s | Enter the feature from the product screen |
| 3–4s | Decelerate, settle at the input start, and click |
| 4–6s | Type the key content |
| 6–8s | Check after input completes → move to and click the attach button → attachment appears |
| 8–11s | Select needed options and check the result |
| 11–13s | Run click → hold the processing state |
| 13–15s | Check the completion screen and final result |
