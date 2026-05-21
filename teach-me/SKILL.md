---
name: teach-me
description: Teach the user one piece of knowledge at a time about a chosen topic, advancing only when they ask, and auto-saving each lesson as a committed markdown note when the working folder is a git repo. Use when the user wants to learn or study a topic, asks to be taught something, is learning a foreign language, or mentions "teach me".
---

Teach me one piece of knowledge at a time about a topic. Inspired by grill-me, but I learn by explanation, not interrogation.

## Choosing the topic

- No topic given → ask which topic I want to learn. Stop and wait.
- Context given but not a concrete topic → ask me to name a specific topic. Stop and wait.
- A specific topic is given → before teaching, see [Level check](#level-check), then pick one worthwhile piece of knowledge and explain it.

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
3. If I ask a follow-up about that piece → answer it, then continue.
4. If I say to continue (or "next") → pick the next piece and explain it. Repeat forever.
5. Never explain two pieces at once.

Match the explanation language to the language I gave the topic/context in. (e.g. Korean context → explain in Korean with target-language examples; target-language context → explain in that language.)

## Visual aid when stuck

If I say a piece is hard to understand, offer a visual:

1. Run the `visualstorming` skill (no changes to it — just reference it) to draw a visual aid for the current concept. Its own consent gate handles asking first.
2. Keep explaining against that visual until I say the concept clicked.
3. Once I understand, **remove the visual artifact** that visualstorming created (delete the HTML file). The aid is temporary — do not commit it; only the lesson note gets committed.
4. Return to the teaching loop.

Use this only for concepts that are genuinely visual (structure, relationships, layout, flow). For purely verbal points, keep explaining in text.

If the `visualstorming` skill is not installed, ask me once whether to install it (`npx skills@latest add kidow/skills/visualstorming`). If I decline, keep explaining without visuals.

## Saving notes (only if the working folder is a git repo)

After each piece is explained, persist it:

1. Check `git rev-parse --is-inside-work-tree`. If not a repo, teach only — do not save or commit.
2. Get today's date with `date +%Y-%m-%d`.
3. Write the lesson to a markdown file at the repo root:
   - Filename: `yyyy-MM-dd-topic_name.md` (topic_name in snake_case).
   - One file per topic. If a file for this topic already exists (any date), update that file — never create a second file for the same topic. Append the new piece; if the same piece is being re-taught, overwrite it. Keep the original date in the filename.
   - Content: the knowledge only, no frontmatter. Write notes in the same language as the explanation.
4. Stage and commit just that file: `learn: <topic_name> — <short piece title>`.

## Auto-organizing structure

As notes accumulate, keep the folder layout optimal automatically — no asking. When themes emerge, create subfolders (e.g. by language or domain) and move related notes in. Commit each reorganization as its own commit (`chore: reorganize notes`) so moves stay separate from new lessons.
