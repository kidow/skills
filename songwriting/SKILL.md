---
name: songwriting
description: Builds ACE-Step 1.5 music generation prompts through an interview-driven songwriting workflow, producing Custom Mode-ready Title, Style (caption), Lyrics, and Params blocks. Use when the user asks to make, write, compose, prompt, structure, or refine a song, track, beat, instrumental, lyrics, or AI music prompt.
---

# Songwriting

Create a complete ACE-Step 1.5 prompt from any song request. Output maps directly onto the ACE-Step UI Custom Mode fields: Title, Style, Lyrics, and the music parameter controls (BPM, Key, Time Signature, Vocal Language, Duration, Instrumental).

## Core Behavior

Start from the user's smallest viable request, even if it is only "make me a song." Keep adding missing information until the prompt is complete enough to generate.

If information is missing, ask one question at a time. For every question, provide a recommended answer the user can accept or edit.

Do not keep asking preference questions after the prompt has enough control points to work. Once the minimum brief is complete, produce the final prompt.

## Minimum Brief

Resolve these fields before final output:

- `purpose`: scene, use case, story, or emotional target
- `genre`: genre, hybrid genre, era, or reference sound
- `vocal`: instrumental, vocal gender, range, delivery, or effects
- `language`: lyric/vocal language when vocals are used
- `energy`: intensity, mood, and section-level energy curve
- `structure`: song form such as Intro, Verse, Chorus, Bridge, Outro
- `tempo_key`: BPM, key, and time signature, or "auto" to let ACE-Step infer them

For lyrical songs, also resolve `lyrics_theme`. Write full lyrics only when the user asks for lyrics or when full lyrics are required by the request.

## Workflow

1. Extract every usable clue from the request before asking anything.
2. If a reference artist or song is provided, translate it into sound traits instead of copying the name into the final Style block. Show the traits you chose in `Sound guide`.
3. Ask the highest-impact missing question first, following Sound Vocabulary below.
4. Prefer concrete musical controls over vague adjectives: instrumentation, vocal delivery, timbre texture, rhythm feel, production style.
5. Describe what should be present. Do not rely on `no X` exclusions in Style; ACE-Step has no DiT negative prompt, and naming an unwanted instrument can pull it in.
6. Put BPM, key, time signature, language, and duration in `Params`, not in Style.
7. For section control, use structure tags with at most one or two modifiers: `[Chorus - anthemic]`. Never use parentheses for performance notes; ACE-Step sings parenthesized text as background vocals.
8. Keep Style and Lyrics consistent: instruments, energy, and vocal descriptors in tags must match Style.
9. For instrumental tracks, set `Instrumental: on` and use instrumental section tags only.
10. If the user asks for iteration, change one variable at a time and explain what changed.

## Sound Vocabulary

Assume the user may not know instrument or production terms. Never make them choose by jargon alone.

- Ask by feel or effect in the user's language, with the term in parentheses:

  ```md
  What should add fun to the rhythm?
  A. Bouncy metallic tapping (cowbell) ← recommended
  B. Bright jingling (tambourine)
  C. Warm hand drums (congas)
  D. Nothing, keep just the drums
  ```

- Translate the answer into terms yourself, using the Sound Glossary in [REFERENCE.md](REFERENCE.md).
- When an option has a sample in the glossary, give its absolute file path so the user can listen before answering.
- Cite only samples and listening examples from the glossary. Do not invent song examples; omit them when the glossary has none.
- If words cannot settle a choice, offer a comparison by ear. See Hear A Comparison in [REFERENCE.md](REFERENCE.md). Skip it when the ACE-Step API is not running; do not start the server yourself.

## Final Output

Return this format:

```md
Title:
...

Style:
...

Lyrics:
...

Params:
BPM ... · Key ... · Time ... · Language ... · Duration ...s · Instrumental on|off

Why this works:
...

Sound guide:
- [term]: [what it sounds like]. [what it does in this track]. Sample: [absolute path, if any]. Listen: [glossary example, if any].
```

List in `Sound guide` the Style terms a non-musician may not know, in the user's language. Omit the block if there are none.

If the user asks for "prompt only", omit `Why this works` and `Sound guide`.

## Constraints

- Preserve user-provided lyrics unless the user asks to rewrite them.
- Do not place living artist names, band names, or exact song titles in the final Style block; convert them to musical descriptors.
- Keep Style concise but specific; prefer comma-separated musical descriptors.
- Parentheses in Lyrics are only for echoed or background vocal lines.
- Key uses ACE-Step UI format: `C major`, `A minor`, `F# minor`.
- Time signature uses the UI's beats-per-bar values: `2`, `3`, `4`, `6` (e.g. `4` = 4/4, `6` = 6/8). Prefer `4`; odd meters are unreliable.
- Language uses ISO codes: `en`, `ko`, `ja`, `zh`, etc.
- Duration in the final prompt stays within 30–240 seconds. Comparison clips may be shorter.
- See [REFERENCE.md](REFERENCE.md) for the sound glossary, tag lists, prompt templates, section design, and refinement strategies.
