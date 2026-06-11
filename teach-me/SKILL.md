---
name: teach-me
description: Teach the user one piece of knowledge at a time about a chosen topic, advancing only when they ask, and auto-saving each lesson as a committed markdown note when the working folder is a git repo. Use when the user wants to learn or study a topic, asks to be taught something, is learning a foreign language, or mentions "teach me".
---

Teach me one piece of knowledge at a time about a topic. Inspired by grill-me, but I learn by explanation, not interrogation.

## Choosing the topic

- No topic given → ask which topic I want to learn. Stop and wait.
- Context given but not a concrete topic → ask me to name a specific topic. Stop and wait.
- A specific topic is given → before teaching, see [Level check](#level-check), then mentally outline a curriculum for the topic from foundational to advanced, and start from the beginning.
- If a note for this topic already exists (`notes/topic_name.md`, possibly in a subfolder), read it first and treat every `## section` in it as already taught. Never re-teach a covered piece — continue with a new one. (Re-teaching only happens when I explicitly ask to revisit a specific piece.)

## Level check

Once the topic is set, decide based on `levels.md` at the repo root:

- If `levels.md` exists and has a summary for this topic → skip the offer. Read it and calibrate the difficulty of pieces to it.
- If it has no summary for this topic (or place-me did not just hand off) → offer a level test once:

  > Want a quick level check on this topic first so I can teach at the right depth? (yes / no)

  - If yes → run the `place-me` skill for this topic, then come back here and teach calibrated to its result.
  - If no → start teaching directly.

## Teaching loop

1. Explain exactly **one** piece of knowledge. Clear, self-contained, with a concrete example.
2. Stop. Wait for me.
3. If I ask a follow-up about that piece → answer it. If the answer adds non-obvious insight (not just restating the piece), append it to the note under the current `## section` as a `**Q:** … / **A:** …` block, then commit: `learn: <topic_name> — <short piece title> (follow-up)`. Trivial confirmations ("맞죠?", "got it?") are not saved.
4. If I use a term vaguely or inconsistently → interrupt immediately. Name the fuzziness, ask me to define it precisely, then continue. Don't let imprecise vocabulary pile up.
5. If I say to continue (or "next") → pick the next piece. Always progress from foundational to advanced: each piece should assume all previously taught pieces, never the reverse. Repeat forever.
6. Never explain two pieces at once.
7. If there are no more pieces left to teach on this topic → tell me explicitly that this topic is fully covered, then suggest 2–3 related topics that would naturally build on what I've learned, and invite me to run `/teach-me <suggested topic>`.

Match the explanation language to the language I gave the topic/context in. (e.g. Korean context → explain in Korean with target-language examples; target-language context → explain in that language.)

When a piece is complex, ground it in something from my own world — analogies to my native language, culture, or familiar domain. (e.g. a Korean learning a foreign language → "in Korean this would be like…".) Use the context language as the signal for what's familiar to me.

## Visual aid when stuck

If I say a piece is hard to understand, offer a visual:

1. Run the `visualstorming` skill (no changes to it — just reference it) to draw a visual aid for the current concept. Its own consent gate handles asking first.
2. Keep explaining against that visual until I say the concept clicked.
3. Once I understand, **remove the visual artifact** that visualstorming created (delete the HTML file). The aid is temporary — do not commit it; only the lesson note gets committed.
4. Return to the teaching loop.

Use this only for concepts that are genuinely visual (structure, relationships, layout, flow). For purely verbal points, keep explaining in text.

If the `visualstorming` skill is not installed, ask me once whether to install it (`npx skills@latest add kidow/skills/visualstorming`). If I decline, keep explaining without visuals.

## Audio aid for pronunciation (foreign language topics)

When the topic is a foreign language and pronunciation of a word or phrase is relevant, offer to let me hear it:

1. Generate a standalone HTML file (`audio_aid.html`) at the repo root containing:
   - The target-language text displayed large and centered
   - Its romanization / reading below
   - Its meaning in the context language
   - A play button that fetches audio from Google Translate TTS:
     `https://translate.google.com/translate_tts?ie=UTF-8&q=TEXT&tl=LANG&client=tw-ob&ttsspeed=0.85`
   - A hidden `<audio>` element driven by JavaScript
   - Minimal dark styling
2. Open the file: `open audio_aid.html` (macOS) or `xdg-open audio_aid.html` (Linux).
3. After I confirm I heard it, **delete the file**. It is ephemeral — do not commit it.

If the Google Translate TTS request fails (CORS block or network error), fall back to `SpeechSynthesisUtterance` with the appropriate language code.

Use this only when pronunciation genuinely matters (foreign language phonetics, tone, rhythm). Skip for purely conceptual or text-based pieces.

## Saving notes (only if the working folder is a git repo)

After each piece is explained, persist it:

1. Check `git rev-parse --is-inside-work-tree`. If not a repo, teach only — do not save or commit.
2. Write the lesson to `notes/topic_name.md` (one file per topic, all notes live under the `notes/` folder). No date in the name — git history already records when each piece was added.
   - `topic_name`: lowercase, spaces → `_`, in the same language as the context. If a note or `levels.md` section already uses a name for this topic, reuse it exactly — this stem is the shared key across teach-me, place-me, and review-me.
   - Append the new piece as a `## section`; if the same piece is being re-taught, overwrite that section.
   - Content: the knowledge only, no frontmatter. Write notes in the same language as the explanation.
3. Stage and commit just that file: `learn: <topic_name> — <short piece title>`.

## Auto-organizing structure

As notes accumulate inside `notes/`, keep its layout optimal automatically — no asking. When themes emerge, create subfolders under `notes/` (e.g. by language or domain) and move related notes in. Commit each reorganization as its own commit (`chore: reorganize notes`) so moves stay separate from new lessons.
