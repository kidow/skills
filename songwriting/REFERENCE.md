# Songwriting Reference (ACE-Step 1.5)

## Custom Mode Fields

ACE-Step has two brains: an optional 5Hz LM planner (infers metadata, rewrites the caption) and a DiT executor (renders audio). Output fields map to the UI like this:

| Output | UI field | Sent to model as |
|--------|----------|------------------|
| `Title` | Title | Not sent; library label only |
| `Style` | Style | `caption` — the most important input |
| `Lyrics` | Lyrics | `lyrics` — the temporal script |
| `Params` | BPM / Key / Time Signature / Vocal Language / Duration / Instrumental | metadata fields |

- `Title`: short, memorable, aligned with the hook or central image
- `Style`: global portrait — genre, emotion, instruments, timbre, era, production, vocal character, rhythm feel
- `Lyrics`: structure tags, lyric lines, and brief section modifiers
- `Params`: exact values the user wants pinned; use `auto` for anything the LM should infer

## Style (Caption) Dimensions

Combine several dimensions; single-dimension captions leave too much to chance.

| Dimension | Examples |
|-----------|----------|
| Genre | pop, rock, jazz, electronic, hip-hop, R&B, folk, classical, lo-fi, synthwave |
| Emotion | melancholic, uplifting, energetic, dreamy, dark, nostalgic, euphoric, intimate |
| Instruments | acoustic guitar, piano, synth pads, 808 drums, strings, brass, electric bass |
| Timbre | warm, bright, crisp, airy, punchy, lush, raw, polished |
| Era | 80s synth-pop, 90s grunge, 2010s EDM, vintage soul, modern trap |
| Production | lo-fi, high-fidelity, live recording, studio-polished, bedroom pop |
| Vocal | female vocal, male vocal, breathy, powerful, falsetto, raspy, choir |
| Rhythm | slow tempo, mid-tempo, fast-paced, groovy, driving, laid-back |
| Structure hints | building intro, catchy chorus, dramatic bridge, fade-out ending |

## Style Template

```md
[genre], [era/subgenre], [emotion],
[instrument 1], [instrument 2], [rhythm feel],
[vocal character or instrumental],
[timbre], [production style], [structure hint]
```

Example:

```md
progressive house, euphoric, festival energy,
layered supersaw synths, four-on-the-floor kick, deep sub bass,
instrumental, bright, wide stereo, polished club mix, big build into drop
```

BPM, key, and time signature go in `Params`, not in Style.

## Specificity And Control

- Specific beats vague: "sad piano ballad with female breathy vocal" beats "a sad song".
- More detail = more control, less surprise. Fewer words = more model freedom.
- Repeat a word to reinforce it in a hybrid style.
- Avoid conflicting descriptors ("classical strings" + "hardcore metal"). Resolve conflict as time evolution instead: "starts with soft strings, builds into heavy metal rock in the middle".

## Exclusions

ACE-Step has no negative prompt for the audio model. Writing `no brass` may still pull brass in.

- Replace exclusions with positive, specific choices: instead of `no acoustic instruments`, write `all-synth arrangement, electronic drums`.
- Instead of `no vocals`, set `Instrumental: on`.
- The UI's "LM Negative Prompt" (Advanced) only steers the LM planner's caption/lyrics/metadata, not the audio. Use it only for text-level avoidance, e.g. `sad lyrics, slow tempo`.

## Structure Tags

| Category | Tags |
|----------|------|
| Basic | `[Intro]`, `[Verse]` / `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]` |
| Dynamic | `[Build]`, `[Drop]`, `[Breakdown]` |
| Instrumental | `[Instrumental]`, `[Guitar Solo]`, `[Piano Interlude]` |
| Special | `[Fade Out]`, `[Silence]` |

Tags anchor arrangement. Without them, structure is unpredictable. Separate sections with blank lines and keep each section's lyrics inside its tag.

## Section Modifiers

Attach one or two modifiers with `-`:

```md
[Intro - ambient piano]

[Verse 1 - whispered]

[Chorus - anthemic]

[Bridge - stripped back]

[Outro - fade out]
```

Do not stack modifiers: `[Chorus - anthemic - stacked harmonies - high energy - epic]` risks the model singing the tag or ignoring it. Complex style belongs in Style.

Do not use parenthesized notes like `(soft, no drums)` under a tag. ACE-Step treats parentheses as background vocals and may sing them.

Useful modifier vocabulary:

- Vocal: `raspy vocal`, `whispered`, `falsetto`, `powerful belting`, `spoken word`, `harmonies`, `call and response`, `ad-lib`
- Energy: `high energy`, `low energy`, `building energy`, `explosive`, `melancholic`, `euphoric`, `dreamy`, `aggressive`

## Style ↔ Lyrics Consistency

The model does not resolve conflicts well. Keep tags aligned with Style:

- instruments in Style ↔ instrumental section tags
- emotion in Style ↔ energy modifiers
- vocal description in Style ↔ vocal modifiers

```md
❌ Style: violin solo, classical, intimate chamber music
   Lyrics: [Guitar Solo - distorted]

✅ Style: violin solo, classical, intimate chamber music
   Lyrics: [Violin Solo - expressive]
```

## Lyric Line Techniques

- Parentheses = background vocals / echoes: `We rise together (together)`
- UPPERCASE = stronger intensity or shouting: `THIS IS OUR MOMENT!`
- Vowel stretching (`Feeeling so aliiive`) is unstable; use sparingly.

## Lyric Writing Rules

- keep lines around 6–10 syllables so they align with beats
- keep syllable counts similar for lines in the same position (±1–2)
- keep verses around 4–8 lines, choruses 4–6, bridges 2–4
- prefer rhyme or near-rhyme for stronger melody anchoring
- repeat the hook line when the chorus needs to stick
- stick to one core metaphor per song and explore its facets
- avoid AI-flavored lyrics: adjective stacking, forced rhymes, sections bleeding into each other, lines too long to sing in one breath, mixed metaphors
- put difficult or personal names near the beginning of a line
- for non-English lyrics, set `Language` to match (e.g. `ko`) so pronunciation is correct

If the user provides lyrics, preserve the words unless asked to edit. You may add structure tags and modifiers around them.

## Instrumental Tracks

Set `Instrumental: on` in Params. Lyrics can be just:

```md
[Instrumental]
```

Or describe development with instrumental tags only:

```md
[Intro - ambient]

[Main Theme - piano]

[Climax - powerful]

[Outro - fade out]
```

## Params

| Param | UI values | Guidance |
|-------|-----------|----------|
| BPM | 30–300, `auto` | 60–180 is stable. Slow 60–80, mid 90–120, fast 130–180 |
| Key | `C major` … `B minor` (sharps and flats), `auto` | common keys (C, G, D, A minor, E minor) are most stable |
| Time | `2`, `3`, `4`, `6`, `auto` | `4` (4/4) most reliable; `3` waltz; `6` 6/8 swing feel |
| Language | ISO code: `en`, `ko`, `ja`, `zh`, … | must match lyric language |
| Duration | 30–240 s, `auto` | 30–60 s and 2–4 min are stable |
| Instrumental | `on` / `off` | `on` sends empty lyrics |

Params are guidance, not exact commands. Leave a value `auto` when the user has no preference; AI Enhance or Thinking mode lets the LM infer it.

## Emotion To Music Anchors

Map mood words to concrete choices in Style and Params:

- dark: minor key, low register, sparse arrangement
- happy: major key, bright timbre, upbeat tempo
- groovy: syncopated rhythm, off-beat hi-hat, funky bass
- epic: orchestral swell, big drums, building intro
- tense: driving pulse, dissonant pads, unresolved ending

```md
Style: melancholic, sparse piano, soft strings, intimate
Params: Key A minor · BPM 72
```

## Reference Translation

If the user names an artist or song, use it for analysis only. Convert it into traits:

- vocal treatment: breathy, raspy, falsetto, vocoded, auto-tuned, choir, layered
- rhythm: four-on-the-floor, syncopated, half-time, off-beat hi-hat, breakbeat
- harmony feel: bright major, dark minor, tense, unresolved
- production: analog synths, tape warmth, gated reverb, dry close vocal, wide stereo, lo-fi drums
- arrangement: sparse intro, bass drop, call-and-response, stripped bridge, final chorus lift

Do not include the artist or song name in the final Style block.

## Energy Curve Pattern

```md
[Intro - soft]

[Verse 1]
...

[Pre-Chorus - building energy]
...

[Chorus - high energy]
...

[Bridge - stripped back]
...

[Final Chorus - explosive]
...

[Outro - fade out]
```

Use modifiers for contrast instead of one energy level for the whole song.

## Complete Example

```md
Title:
Fireworks

Style:
female vocal, piano ballad, emotional, intimate atmosphere, strings,
warm, studio-polished, building to powerful chorus

Lyrics:
[Intro - piano]

[Verse 1]
Moonlight spills across the sill
I can hear you breathing slow
All the city's gone to sleep
Only we are still awake

[Pre-Chorus]
Everything is quiet now
But my heart is running loud

[Chorus - powerful]
Let us burn tonight
Like the fireworks in the sky
Brief but shining bright
This is our time

[Bridge - whispered]
If tomorrow fades away
We will know we shone today

[Final Chorus]
Let us burn tonight
Like the fireworks in the sky
Brief but shining bright
THIS IS OUR TIME!

[Outro - fade out]

Params:
BPM 72 · Key C major · Time 4 · Language en · Duration 180s · Instrumental off
```

Tags (piano, powerful, whispered) agree with Style (piano ballad, building to powerful chorus, intimate).

## UI Generation Toggles

- `AI Enhance`: LM expands the caption and fills BPM/key/time. Recommend when genre output drifts (e.g. pop tags coming out as ballads) or when Params are mostly `auto`.
- `Thinking`: full LM reasoning with audio codes. Slowest, best quality; disabled when a LoRA is loaded.
- Leave both off when the prompt already pins every Param and the user wants the caption used verbatim.

## A/B Testing

Change one variable at a time:

1. genre or subgenre
2. BPM
3. key or mode
4. instrumentation
5. energy modifiers
6. vocal character

Generation is probabilistic. Keep the best prompt, and use seeds or batch size to sample variations before rewriting the prompt.

## Cover And Repaint

Use these as workflow advice when the user wants to improve a generated result:

- `Cover` (source audio + cover strength 0.0–1.0): keep structure and melody, change Style or Lyrics. Good for remixes, restyling, or re-singing with edited lyrics.
- `Repaint` (source audio + start/end time): regenerate only a weak section while keeping the rest. Use for awkward transitions or a bad chorus take.
- Instrumentals tolerate repaint more naturally than vocal-heavy sections.
- Source audio must be the user's own or properly licensed material.
