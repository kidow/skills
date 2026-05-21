---
name: review-me
description: Review knowledge already saved in the current repo by quizzing one item at a time with spaced-repetition scheduling, keeping all session state in a throwaway dot-folder that is deleted when done. Use when the user wants to review, quiz, or test themselves on previously learned notes, or says "review me".
---

Review knowledge that is already saved in this repository. Companion to teach-me: teach-me writes notes, review-me quizzes me on them. Every bit of scheduling/grading is ephemeral.

## Before starting

If `levels.md` does not exist at the repo root, offer a level check first:

> No level memory found. Want a quick level check with place-me before reviewing? (yes / no)

If yes → run `place-me`. If no → continue.

## Targets

A review item ("card") is **one `## section`** inside a knowledge note.

- Auto-detect notes by the teach-me pattern: `yyyy-MM-dd-*.md` (at repo root or in subfolders).
- If no such notes exist, ask me once which folder or file pattern to review. Stop and wait.
- Each `##` section across the matched notes becomes one card.

## Session state (ephemeral)

1. On session start, look for a `.review/` folder at the repo root.
   - If it exists (a previous session was interrupted), resume from its queue/grading data and continue.
   - Otherwise create `.review/` and keep all queue + grading data there.
2. Ensure `.review/` is gitignored: if `.gitignore` has no entry for it, add `.review/`.
3. Never commit this folder. When the session ends, delete it. No review history is persisted anywhere.

## Review loop

1. Pick the next due card from the queue.
2. Generate **one** question from that section's content (content-based, not just the heading). Ask it. Stop and wait.
3. When I answer, reveal the section as the correct answer so I can self-check.
4. Ask me to grade: **Again / Hard / Good / Easy**.

Each card has two learning steps. Since there is no clock, each step maps to a queue distance:

   - **Again** → reset to step 0; requeue after ~2 cards.
   - **Hard** → repeat the current step; requeue after ~4 cards.
   - **Good** → advance one step; requeue after ~8 cards. If already on the last step, the card **graduates** (removed from the queue).
   - **Easy** → graduate immediately (removed from the queue).
5. Repeat. One question at a time — never ask two at once.

## Ending

When the queue is empty (every card graded Good or Easy), there is nothing left to review:

1. Tell me the session is complete with a short summary (how many cards, how many needed repeats).
2. **Update the level memory.** If `levels.md` exists at the repo root, revise the prose summary for the reviewed topic(s) based on how this session went — what I recalled easily, what needed repeats. Update the section in place (never duplicate) and commit just that file: `review: update <topic_name> level`. If `levels.md` does not exist, skip this step.
3. Delete the `.review/` dot-folder.
4. Never modify the knowledge notes themselves — review-me only reads them. The only file it may write is `levels.md`.
