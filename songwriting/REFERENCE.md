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

## Sound Glossary

Use this to ask by feel and to explain terms. Sample paths are relative to this skill's folder. A term without a sample is explained in words only.

### Percussion, Rhythm, And Production

| Feel or effect | Term | What it sounds like | Sample | Listen |
|----------------|------|---------------------|--------|--------|
| Bouncy, playful, retro | cowbell | Metallic "tok-tok" tapping on the beat | `assets/cowbell-120bpm.mp3` (synthesized, drum-machine style) | Opening of "Honky Tonk Women" by The Rolling Stones |
| Bright, festive | tambourine | Jingling metal discs, shaken or struck | `assets/tambourine.mp3` | |
| Warm, Latin, organic | congas | Tall hand drums with a round, warm tone | `assets/congas.mp3` | |
| Light, airy motion | shaker | Soft "chk-chk" of a rattle, like grains in a tube | `assets/shaker.mp3` | |
| Crowd-like, uplifting backbeat | handclap | Sharp clapping on beats 2 and 4 | `assets/handclap.mp3` | |
| Sparkling, delicate | triangle | Thin, ringing metal "ting" that lingers | `assets/triangle.mp3` | |
| Dry, clicky, playful | woodblock | Hollow wooden "tock" | `assets/woodblock.mp3` | |
| Latin rhythm backbone | claves | Two hard sticks making a sharp, high "click" | `assets/claves.mp3` | |
| Steady dance pulse | four-on-the-floor | Kick drum on every beat: boom, boom, boom, boom | `assets/four-on-the-floor.mp3` | |
| Bouncy, danceable lift | off-beat hi-hat | Crisp "tss" between the kicks: boom-tss, boom-tss | `assets/off-beat-hi-hat.mp3` | |
| Funky, unexpected | syncopated | Accents land between the main beats | `assets/syncopated.mp3` | |
| Heavy, slowed-down weight | half-time | Snare hits half as often, so the groove feels slower | `assets/half-time.mp3` | |
| Busy, raw, chopped | breakbeat | Fast, broken drum pattern instead of a steady pulse | `assets/breakbeat.mp3` | |
| Deep hip-hop or trap punch | 808 drums | Drum-machine kit with a long, booming low kick | `assets/808-drums.mp3` | |
| Felt more than heard | sub bass | Very low bass that shakes rather than plays a clear note | `assets/sub-bass.mp3` (use headphones; laptop speakers may not play it) | |
| Huge, euphoric, trance-like | supersaw | Many slightly detuned synths stacked into one wide, bright sound | `assets/supersaw.mp3` | |
| Soft background cushion | synth pads | Long, sustained synth chords with no sharp attack | `assets/synth-pads.mp3` | |
| Big 80s drums | gated reverb | Huge echo on the drums that cuts off abruptly | `assets/gated-reverb.mp3` | Drum fill in "In the Air Tonight" by Phil Collins |
| Old, cozy, slightly worn | tape warmth | Soft highs and gentle saturation, like a cassette | `assets/tape-warmth.mp3` (first 4 seconds clean, last 4 with the effect) | |

### Drum Kit And Hand Drums

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Sharp backbeat snap | snare drum | Tight "crack" with a buzzy rattle | `assets/snare-drum.mp3` |
| Jazzy, flowing shimmer | ride cymbal | Steady metallic "ting-ting" with a soft wash | `assets/ride-cymbal.mp3` |
| Big moment, section change | crash cymbal | Loud splash that fades slowly | `assets/crash-cymbal.mp3` |
| Rolling, dramatic fills | toms | Round drums stepping from high to low | `assets/toms.mp3` |
| Light, lively Latin chatter | bongos | Small, high, quick hand drums | `assets/bongos.mp3` |
| Hot, metallic Latin accents | timbales | Bright drums with a ringing metal shell | `assets/timbales.mp3` |

### Keys

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Classic, emotional, clear | acoustic piano | Struck strings, from soft to powerful | `assets/acoustic-piano.mp3` (upright piano) |
| Mellow, soulful, late-night | electric piano | Soft bell-like chords with a round glow | `assets/electric-piano.mp3` |
| Churchy, soulful, sustained | organ | Rich chords that hold steady with a slow swirl | `assets/electric-organ.mp3` (electric organ) |
| Funky, percussive keys | clavinet | Short, twangy, biting keyboard notes | |
| Baroque, ornate, antique | harpsichord | Crisp plucked notes with no soft or loud | |

### Guitar And Bass

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Campfire, folk, intimate | acoustic guitar | Woody strummed or picked strings | |
| Clean, jangly, relaxed | clean electric guitar | Clear, bright electric strings without grit | |
| Loud, rebellious, heavy | distorted electric guitar | Thick, fuzzy, roaring guitar | |
| Groove foundation | electric bass | Low, round plucked notes under the band | |
| Punchy, funky, showy | slap bass | Popping, percussive bass notes | |
| Woody jazz walk | upright bass | Warm, deep plucked notes from a large standing bass | |

### Strings

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Yearning, expressive solo | violin | High, singing bowed melody | `assets/violin.mp3` |
| Deep, human, sorrowful | cello | Warm, low bowed voice | `assets/cello.mp3` (cello section) |
| Cinematic, sweeping | string section | Many bowed strings blending into one lush sound | `assets/string-section.mp3` (violin section) |
| Playful, tiptoeing | pizzicato strings | Short plucks on bowed-string instruments | |
| Dreamy, flowing, magical | harp | Rippling plucked notes | `assets/harp.mp3` |

### Brass And Woodwinds

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Bold, bright, announcing | trumpet | Piercing, brilliant melody | `assets/trumpet.mp3` |
| Brassy, sliding, comic or heavy | trombone | Broad low brass that can slide between notes | `assets/trombone.mp3` |
| Noble, heroic, distant | French horn | Round, warm, mellow brass | `assets/french-horn.mp3` |
| Punchy, celebratory hits | brass section | Several horns striking together | |
| Smoky, sensual, jazzy | saxophone | Breathy, vocal-like reed melody | |
| Airy, gentle, pastoral | flute | Light, pure, breathy tone | `assets/flute.mp3` |
| Woody, wistful, agile | clarinet | Smooth, hollow reed tone | `assets/clarinet.mp3` |

### Mallets

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Cool jazz, floating | vibraphone | Soft metal bars with a slow shimmer | |
| Warm, woody, bubbly | marimba | Round notes on wooden bars | `assets/marimba.mp3` |
| Twinkling, childlike | glockenspiel | Tiny, high, bell-like metal notes | `assets/glockenspiel.mp3` |

### World Instruments

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Psychedelic, Indian classical | sitar | Buzzing, bending plucked strings over a drone | |
| Serene, Japanese traditional | koto | Delicate, clear plucked zither | |
| Graceful, Korean traditional | gayageum | Plucked zither with expressive bending notes | |
| Intricate, talking rhythm | tabla | Pitched hand drums with bending low tones | |
| Sunny, Caribbean | steel drums | Bright, ringing melodic metal pans | |

### Synths

| Feel or effect | Term | What it sounds like | Sample |
|----------------|------|---------------------|--------|
| Main melody that cuts through | synth lead | Buzzy, sustained electronic melody | `assets/synth-lead.mp3` |
| Short, catchy, bouncy | synth pluck | Quick notes that snap and fade fast | `assets/synth-pluck.mp3` |
| Driving, sparkling motion | arpeggio | A chord played one note at a time in a fast pattern | `assets/arpeggio.mp3` |
| Squelchy, hypnotic rave | acid bass | Rubbery bass with a "wow" sweep on each note | `assets/acid-bass.mp3` |
| Retro video game | chiptune | Simple square-wave beeps from old consoles | `assets/chiptune.mp3` |

All samples are 8 seconds long. These are recordings from [VSCO 2 Community Edition](https://github.com/sgossner/VSCO-2-CE) (CC0-1.0): acoustic piano, violin, cello, string section, harp, trumpet, trombone, French horn, flute, clarinet, marimba, and glockenspiel. The rest are synthesized approximations, not recordings; tell the user so. Remove or replace any sample the user rejects.

These terms have not all been tested with ACE-Step. If one has little effect, name it earlier in Style, describe its role, or try another seed.

Do not use a generated ACE-Step clip as proof of what an instrument sounds like; in testing, a `solo cowbell` caption came out dominated by low frequencies.

To regenerate synthesized samples, or add one after defining it in `CLIPS`, run `python3 scripts/make_samples.py [name ...]` (needs `ffmpeg`). Recorded samples come from `python3 scripts/build_recorded_samples.py [name ...]`, which downloads about 100 MB for all twelve.

The cowbell sample is made separately: two square waves at 540 Hz and 800 Hz with a fast decay, at 120 BPM.

```bash
ffmpeg -y -f lavfi -i "aevalsrc='0.35*exp(-18*mod(t,0.5))*(sgn(sin(2*PI*540*t))+sgn(sin(2*PI*800*t)))':s=48000:d=8" -af "highpass=f=400,lowpass=f=6000,alimiter=limit=0.89" -codec:a libmp3lame -q:a 2 cowbell-120bpm.mp3
```

## Hear A Comparison

Use this to hear how one change feels in a track. It requires a running ACE-Step API at `http://localhost:8001`; check `GET /health` first and skip this section if it does not respond.

Never start the server without the user's say-so. If they want to start it, suggest this command from their ACE-Step folder. The default startup can auto-select the 4B language model and begin a download of about 8 GB on the first request if that model is missing.

```bash
ACESTEP_INIT_LLM=false uv run acestep-api --host 127.0.0.1 --port 8001
```

1. Create two prompts that differ by one element, and keep every other value the same.
2. `POST /release_task` once per prompt:

   ```json
   {
     "prompt": "funk groove, tight drum kit, slap bass, bright cowbell on every beat, dry studio recording",
     "lyrics": "[Instrumental]",
     "instrumental": true,
     "thinking": false,
     "bpm": 120,
     "time_signature": "4",
     "audio_duration": 12,
     "inference_steps": 8,
     "use_random_seed": false,
     "seed": 42,
     "batch_size": 1,
     "audio_format": "mp3"
   }
   ```

3. Read `data.task_id` from each response.
4. `POST /query_result` with `{"task_id_list": ["<task_id>"]}` every few seconds until `data[0].status` is `1` (success) or `2` (failed). The first request also loads the model.
5. Parse `data[0].result`, which is a JSON string. Download `http://localhost:8001` + `[0].file`, and save it to a temporary folder.
6. Give the user both absolute paths and say what differs.

Notes:

- The minimum duration is 10 seconds. Clips can end with about 2 seconds of silence, so 12 seconds yields about 10 of sound.
- The difference may be subtle. If the user cannot hear it, describe the element more prominently or try another seed before concluding it does not work.

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
