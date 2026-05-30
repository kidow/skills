---
name: songwriting
description: Builds AI music generation prompts through an interview-driven songwriting workflow, producing Custom Mode-ready Title, Style, and Lyrics blocks. Use when the user asks to make, write, compose, prompt, structure, or refine a song, track, beat, instrumental, lyrics, or AI music prompt.
---

# Songwriting

Create a complete AI music prompt from any song request. Assume a Suno-like Custom Mode workflow, but do not name the platform unless the user does.

## Core Behavior

Start from the user's smallest viable request, even if it is only "make me a song." Keep adding missing information until the prompt is complete enough to generate.

If information is missing, ask one question at a time. For every question, provide a recommended answer the user can accept or edit.

Do not keep asking preference questions after the prompt has enough control points to work. Once the minimum brief is complete, produce the final prompt.

## Minimum Brief

Resolve these fields before final output:

- `purpose`: scene, use case, story, or emotional target
- `genre`: genre, hybrid genre, era, or reference sound
- `vocal`: instrumental, vocal type, range, delivery, or effects
- `language`: lyric/vocal language when vocals are used
- `energy`: intensity, mood, and section-level energy curve
- `structure`: song form such as Intro, Verse, Chorus, Bridge, Outro
- `avoid`: specific unwanted sounds or traits

For lyrical songs, also resolve `lyrics_theme`. Write full lyrics only when the user asks for lyrics or when full lyrics are required by the request.

## Workflow

1. Extract every usable clue from the request before asking anything.
2. If a reference artist or song is provided, translate it into sound traits instead of copying the name into the final Style block.
3. Ask the highest-impact missing question first.
4. Prefer concrete musical controls over vague adjectives: BPM, key, chord progression, rhythm, instrumentation, vocal delivery, production texture.
5. Use negative prompting as sound-level exclusions, not legal disclaimers.
6. For instrumental tracks, use `[instrumental]` and skip vocal/lyric questions unless needed.
7. For section control, place structure tags and section-specific performance notes in the Lyrics block.
8. If the user asks for iteration, change one variable at a time and explain what changed.

## Final Output

Return this format:

```md
Title:
...

Style:
...

Lyrics:
...

Why this works:
...
```

If the user asks for "prompt only", omit `Why this works`.

## Constraints

- Preserve user-provided lyrics unless the user asks to rewrite them.
- Do not place living artist names, band names, or exact song titles in the final Style block; convert them to musical descriptors.
- Do not use broad disclaimers like "avoiding direct artist imitation" as the main control mechanism.
- Keep Style concise but specific; prefer comma-separated musical descriptors.
- See [REFERENCE.md](REFERENCE.md) for tag patterns, prompt templates, section design, and refinement strategies.
