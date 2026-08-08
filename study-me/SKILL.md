---
name: study-me
description: Freely study knowledge already saved in the current repo by extracting as many content-based questions as each note section supports and asking them one at a time, with no grading or scheduling — just self-check against the original text. Use when the user wants to freely study, self-test, or quiz themselves on notes without spaced-repetition tracking, or says "study me", "자유 학습", "편하게 공부해볼게".
---

Freely study knowledge already saved in this repository. Companion to teach-me and review-me: teach-me writes notes, review-me quizzes with spaced-repetition grading, study-me quizzes with no grading at all — pure self-check, stop and resume freely.

## Scope

Decide *what* to study before building the queue — same logic as review-me:

- If I gave a topic/file as context → study exactly that.
- If I gave no context:
  - Read `levels.md` and propose the weakest topics first (Blank/Glimpsed before Grounded before Fluent). Ask: "Study [weak topics] today?" Stop and wait.
  - If `levels.md` doesn't exist → ask me once which topic, folder, or file pattern to study. Stop and wait.

Don't queue the entire knowledge base by default — a growing KB makes that unusable.

## Targets

Knowledge notes live under the `notes/` folder (any depth): every `.md` in `notes/` within scope is a note. Each `## section` inside a matched note is a source for questions.

## Building the question queue

For each `## section` in scope:

1. Extract **as many content-based questions as the section's content supports** — no upper limit. A short section (one fact) yields one question; a dense section yields several, one per distinct fact or concept inside it.
2. Base every question on the content itself, never just the section heading.
3. Order: sections in file order; files in the order they appear in `_data/notes_order.yml` when the scope falls under `notes/` (fallback: filesystem order if that file doesn't cover the scope). Within a section, ask questions in the order the underlying facts appear in the text.

## Study loop

1. Pick the next question from the queue. Ask it. Stop and wait.
2. When I answer, reveal the relevant section content as the self-check reference — no verdict, no grade, no "correct/incorrect" label. Just the source text so I can compare it against my own answer.
3. Wait for me to say "다음"/"next" (or similar) before asking the next question. Never ask two questions at once.
4. Repeat until the queue is empty or I say I want to stop.

## Ending

1. When the queue is empty, or I say to stop, give a short summary: how many questions covered, out of how many sections.
2. Never modify `levels.md` — study-me has no grading signal to base a level update on. Level tracking belongs to place-me/review-me.
3. Never modify the knowledge notes themselves — study-me only reads them.
4. No session state is persisted anywhere. If the session is interrupted, the next `study-me` run simply starts a fresh queue — there is no dot-folder, no resume.
