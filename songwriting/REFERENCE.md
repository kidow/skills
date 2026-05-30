# Songwriting Reference

## Custom Mode Fields

Use three user-facing fields:

- `Title`: short, memorable, and aligned with the hook or central image
- `Style`: global sound instructions, genre, BPM, key, instrumentation, vocal style, production texture, and exclusions
- `Lyrics`: lyrics, structure tags, section-level performance notes, or `[instrumental]`

## Structure Tags

Common tags:

```md
[Intro]
[Verse]
[Pre-Chorus]
[Chorus]
[Bridge]
[Instrumental]
[Outro]
```

Use tags to anchor arrangement and energy changes. Without tags, the model may decide the structure unpredictably.

## Section Notes

Place section-specific sonic instructions in parentheses:

```md
[Intro]
(soft, minimal synth, no drums, building tension)

[Verse]
(mid-energy, kick drum enters, restrained vocal)

[Chorus]
(full energy, wide hook, layered harmonies, heavy bass)
```

Global Style controls the whole song. Parenthetical section notes control local contrast.

## Instrumental Tracks

For instrumental tracks, make the instruction explicit:

```md
Lyrics:
[instrumental]

[Intro]
(minimal motif, filtered synth, no drums)
```

Also include `no vocals` in Style when vocal bleed would be harmful.

## Style Template

```md
[genre], [BPM] BPM, [key], [chord progression],
[instrument 1], [instrument 2], [rhythm],
[vocal style or instrumental],
[energy], [texture], [production notes],
no [unwanted sound 1], no [unwanted sound 2]
```

Example:

```md
progressive house, 128 BPM, A minor, i-VI-III-VII,
layered synths, four-on-the-floor kick, sub bass,
instrumental, euphoric, full texture, high energy,
no acoustic instruments, no jazz harmony, no vocals
```

## Reference Translation

If the user gives an artist or song reference, use it for analysis only. Convert it into traits:

- vocal treatment: breathy, raspy, falsetto, vocoded, auto-tuned, choir, layered
- rhythm: four-on-the-floor, syncopated, half-time, off-beat hi-hat, breakbeat
- harmony: major key, minor key, diminished chords, tritone tension, unresolved progression
- production: analog synths, tape warmth, gated reverb, dry close vocal, wide stereo, lo-fi drums
- arrangement: sparse intro, bass drop, call-and-response, stripped bridge, final chorus lift

Do not include the artist or song name in the final Style block unless the user explicitly asks to keep it outside the prompt for notes.

## Negative Prompting

Use concrete exclusions:

```md
no distorted guitar, no acoustic drums, no jazz chords,
no slow tempo, no ambient pads, no brass
```

Avoid relying on broad phrases such as:

```md
avoiding direct artist imitation, no cloning, no replication
```

Those phrases are weak sound controls. Sound-level exclusions are stronger.

## Music Theory Controls

Replace vague mood words with musical anchors when useful:

- dark: minor key, diminished chords, low register
- happy: major key, bright chord voicings
- groovy: syncopated rhythm, off-beat hi-hat
- epic: orchestral swell, rising fifth interval
- tense: tritone harmony, unresolved chord progression

Use both feeling and theory when possible:

```md
melancholic, A minor, i-VI-III-VII, unresolved chorus cadence
```

## Lyric Writing Rules

When writing lyrics:

- use clear section tags
- keep verses around 4-8 lines
- keep choruses around 4-6 lines
- keep bridges around 2-4 lines
- keep line length roughly consistent inside each section
- prefer rhyme or near-rhyme for stronger melody anchoring
- repeat the hook line multiple times when the chorus needs to stick
- put difficult names or personal names near the beginning of a line for clearer pronunciation
- read the lyrics aloud mentally and fix awkward stress patterns

If the user provides lyrics, preserve the words unless asked to edit. You may add section tags and parenthetical notes around them.

## Energy Curve Patterns

Common curve:

```md
[Intro]
(soft, minimal, building)

[Verse]
(mid-energy, groove enters)

[Chorus]
(full energy, hook, layered arrangement)

[Bridge]
(stripped back, anticipation)

[Chorus]
(maximum energy, final lift)

[Outro]
(gradual fade, reverb tail)
```

Use section notes to create contrast instead of applying one energy level to the whole song.

## A/B Testing

When refining a prompt, change one variable at a time:

1. genre or subgenre
2. BPM
3. key or mode
4. instrumentation
5. energy descriptors
6. exclusions

Keep the best prompt text. Generation is probabilistic, so prompt quality and repeated sampling both matter.

## Extend, Remaster, And Inpainting

Use these as workflow advice when the user asks how to improve a generated result:

- `Extend`: continue after a timestamp with new section tags or lyrics
- `Remaster`: preserve structure and melody while improving mix or fidelity
- `Inpainting`: replace a weak middle section while keeping surrounding material

For awkward section transitions, recommend regenerating a smaller region when possible. Instrumentals usually tolerate inpainting more naturally than vocal-heavy sections.
