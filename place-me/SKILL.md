---
name: place-me
description: Run a short adaptive diagnostic to gauge how much the user already knows about a topic before learning it, then save a prose level summary to a single git-tracked levels.md. Use when the user is about to learn a topic and wants a level check first, asks to be tested on what they know, or says "place me".
---

Find out how much I already know about a topic before teaching me. Companion to teach-me: place-me sizes me up, teach-me then teaches at the right level.

## Topic

- No topic given → ask which topic to test. Stop and wait.
- Context given but not a concrete topic → ask me to name a specific topic. Stop and wait.
- Before testing, read `levels.md` at the repo root if it exists; use any prior summary for this topic as a starting guess.

## Test loop

1. Ask **one** question about the topic. Stop and wait.
2. Read my answer. Judge whether it was below, at, or above the difficulty you just probed.
3. Adapt: if I answered easily, go harder; if I struggled, go easier.
4. Repeat, one question at a time, never two at once.
5. Stop as soon as you are confident about my level — there is no fixed question count. Don't drag it out once the signal is clear.

Match the question language to the language I gave the topic in.

## Saving the level (only if the working folder is a git repo)

When confident, persist the result:

1. Check `git rev-parse --is-inside-work-tree`. If not a repo, just tell me the result — do not save or commit.
2. Write to a single unified file `levels.md` at the repo root (git-tracked, no date in the name):
   - One `## topic_name` section per topic.
   - Content: open with one of four level labels, then a prose summary of what I clearly know, what I'm shaky on, and what I don't know yet.
     - **Blank** — no prior exposure to the concept.
     - **Glimpsed** — seen it before but cannot reproduce or explain it reliably.
     - **Grounded** — explains it independently and applies it correctly in new contexts.
     - **Fluent** — handles exceptions, nuance, and edge cases without hesitation.
   - Example: `Level: Grounded — Knows X and Y, applies them correctly, shaky on Z, hasn't encountered W yet.`
   - If a section for this topic exists, update it in place; never duplicate.
3. Commit just that file: `place: <topic_name> level assessment`.

## Handoff

After saving, hand off to teach-me for the same topic, telling it to calibrate to the level summary just written.
