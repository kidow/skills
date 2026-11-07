#!/usr/bin/env python3
"""Synthesize the Sound Glossary's demo clips into ../assets. Requires ffmpeg.

Usage: make_samples.py [clip-name ...]   (no names = all clips)

ponytail: these are synthesized approximations; swap in CC0 recordings for any
sound that needs to be realistic. cowbell-120bpm.mp3 is not generated here; its
ffmpeg recipe is in REFERENCE.md.
"""
import math
import random
import subprocess
import sys
from array import array
from pathlib import Path

SR = 44100
LENGTH = 8.0
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def lowpass(x, cutoff):
    a = 1 - math.exp(-2 * math.pi * cutoff / SR)
    out, y = [], 0.0
    for s in x:
        y += a * (s - y)
        out.append(y)
    return out


def highpass(x, cutoff):
    return [s - l for s, l in zip(x, lowpass(x, cutoff))]


def noise(dur, seed):
    rng = random.Random(seed)
    return [rng.uniform(-1, 1) for _ in range(int(dur * SR))]


def shaped(x, decay, attack=0.0):
    out = []
    for i, s in enumerate(x):
        t = i / SR
        rise = min(1.0, t / attack) if attack else 1.0
        out.append(s * rise * math.exp(-t * decay))
    return out


def swept(dur, freq, decay):
    """Sine whose frequency follows freq(t), with exponential decay."""
    out, phase = [], 0.0
    for i in range(int(dur * SR)):
        t = i / SR
        phase += 2 * math.pi * freq(t) / SR
        out.append(math.sin(phase) * math.exp(-t * decay))
    return out


def partials(dur, ratios, base, decay):
    out = []
    for i in range(int(dur * SR)):
        t = i / SR
        v = sum(math.sin(2 * math.pi * base * r * t) / (n + 1) for n, r in enumerate(ratios))
        out.append(v * math.exp(-t * decay))
    return out


def mix(*layers):
    out = [0.0] * max(len(x) for x in layers)
    for x in layers:
        for i, s in enumerate(x):
            out[i] += s
    return out


def gain(x, g):
    return [s * g for s in x]


def kick():
    return swept(0.35, lambda t: 50 + 100 * math.exp(-t * 35), 9)


def kick_808():
    return [math.tanh(1.6 * s) for s in swept(1.2, lambda t: 48 + 70 * math.exp(-t * 30), 2.2)]


def snare():
    return mix(
        gain(swept(0.25, lambda t: 190, 22), 0.5),
        gain(shaped(highpass(noise(0.25, "snare"), 1200), 18), 0.9),
    )


def hat(open_hat=False):
    return gain(shaped(highpass(noise(0.3, "hat"), 7000), 14 if open_hat else 60), 0.5)


def clap():
    burst = highpass(lowpass(noise(0.25, "clap"), 3500), 900)
    env = []
    for i in range(len(burst)):
        t = i / SR
        env.append(max(math.exp(-(t - start) * 200) for start in (0, 0.012, 0.024) if t >= start) if t < 0.036 else math.exp(-(t - 0.036) * 16))
    return [s * e for s, e in zip(burst, env)]


def tambourine_hit():
    return mix(
        gain(shaped(highpass(noise(0.15, "tamb"), 6000), 25), 0.7),
        gain(partials(0.15, [1, 1.37, 1.65, 1.98], 5200, 28), 0.4),
    )


def shaker_hit():
    return gain(shaped(highpass(noise(0.1, "shaker"), 5000), 30, attack=0.02), 0.7)


def conga(freq):
    return mix(
        swept(0.3, lambda t: freq * (1 + 0.25 * math.exp(-t * 60)), 14),
        gain(shaped(lowpass(noise(0.02, "conga"), 3000), 200), 0.3),
    )


def triangle_hit():
    return partials(1.0, [1, 2.76, 5.4, 8.93], 1200, 3)


def woodblock(freq):
    return partials(0.12, [1, 1.5], freq, 45)


def clave_hit():
    return partials(0.1, [1], 2500, 50)


def gated_snare():
    tail = highpass(lowpass(noise(0.3, "gate"), 5000), 300)
    return mix(snare(), [s * 0.45 for s in tail])


def groove(bpm, *parts):
    """parts: (voice samples, beats within a 4-beat bar, level). Loops for LENGTH."""
    out = [0.0] * int(LENGTH * SR)
    beat = 60 / bpm
    for voice, beats, level in parts:
        bar = 0
        while bar * 4 * beat < LENGTH:
            for b in beats:
                start = int((bar * 4 + b) * beat * SR)
                for i, s in enumerate(voice):
                    if start + i >= len(out):
                        break
                    out[start + i] += s * level
            bar += 1
    return out


EIGHTHS = [i / 2 for i in range(8)]
SIXTEENTHS = [i / 4 for i in range(16)]
CHORDS = [(57, 60, 64), (53, 57, 60), (48, 52, 55), (55, 59, 62)]  # Am F C G


def midi(n):
    return 440 * 2 ** ((n - 69) / 12)


def supersaw():
    out = [0.0] * int(LENGTH * SR)
    chord_len = int(LENGTH * SR / len(CHORDS))
    for c, chord in enumerate(CHORDS):
        for note in chord:
            for detune in (1, 0.994, 1.006, 0.985, 1.015):
                f, phase = midi(note + 12) * detune, random.Random(f"{note}{detune}").random()
                for i in range(chord_len):
                    phase = (phase + f / SR) % 1
                    out[c * chord_len + i] += 2 * phase - 1
    return lowpass(out, 6000)


def pads():
    out = [0.0] * int(LENGTH * SR)
    chord_len = int(LENGTH * SR / len(CHORDS))
    for c, chord in enumerate(CHORDS):
        for note in chord:
            for detune in (0.998, 1.002):
                f = midi(note) * detune
                for i in range(chord_len):
                    t = i / SR
                    rise = min(1.0, t / 0.6, (chord_len / SR - t) / 0.3)
                    w = 2 * math.pi * f * t
                    out[c * chord_len + i] += rise * (math.sin(w) + 0.3 * math.sin(2 * w))
    return lowpass(out, 1800)


def sub_bass():
    out = [0.0] * int(LENGTH * SR)
    note_len = int(LENGTH * SR / 4)
    for n, f in enumerate((55.0, 43.65, 49.0, 41.2)):
        for i in range(note_len):
            t = i / SR
            rise = min(1.0, t / 0.02, (note_len / SR - t) / 0.05)
            out[n * note_len + i] = math.tanh(1.5 * math.sin(2 * math.pi * f * t)) * rise
    return mix(out, groove(120, (hat(), EIGHTHS, 0.12)))


def tape():
    """First half clean, second half the same phrase through a tape-style chain."""
    phrase = [0.0] * int(LENGTH / 2 * SR)
    for n, note in enumerate((69, 72, 76, 72, 67, 71, 74, 71)):
        start = int(n * 0.5 * SR)
        for i, s in enumerate(partials(0.9, [1, 2, 3], midi(note), 4)):
            if start + i < len(phrase):
                phrase[start + i] += s
    wobbled = []
    for i in range(len(phrase)):
        t = i / SR
        pos = i + 14 * math.sin(2 * math.pi * 0.7 * t) + 3 * math.sin(2 * math.pi * 6 * t)
        j = min(len(phrase) - 2, max(0, int(pos)))
        wobbled.append(phrase[j] + (phrase[j + 1] - phrase[j]) * (pos - int(pos)))
    peak = max(abs(s) for s in wobbled) or 1.0
    warm = [math.tanh(2.2 * s / peak) * peak for s in lowpass(wobbled, 2800)]
    hiss = highpass(noise(LENGTH / 2, "tape"), 3000)
    return phrase + [w + 0.015 * peak * h for w, h in zip(warm, hiss)]


def ride_hit():
    return mix(
        gain(partials(0.9, [1, 1.48, 1.83, 2.4, 2.9, 3.6], 2900, 5), 0.5),
        gain(shaped(highpass(noise(0.9, "ride"), 6000), 8), 0.3),
    )


def crash_hit():
    return mix(
        gain(shaped(highpass(noise(1.9, "crash"), 3000), 2), 0.8),
        gain(partials(1.9, [1, 1.41, 1.87, 2.31, 3.17], 1700, 2.6), 0.25),
    )


def tom(freq):
    return mix(
        swept(0.5, lambda t: freq * (1 + 0.4 * math.exp(-t * 35)), 8),
        gain(shaped(lowpass(noise(0.03, "tom"), 2500), 120), 0.3),
    )


def bongo(freq):
    return swept(0.18, lambda t: freq * (1 + 0.15 * math.exp(-t * 80)), 28)


def timbale(freq):
    return mix(
        swept(0.3, lambda t: freq, 15),
        gain(partials(0.3, [1.7, 2.6, 3.9], freq, 18), 0.35),
        gain(shaped(highpass(noise(0.05, "timbale"), 3000), 70), 0.3),
    )


def saw_note(f, dur, decay=0.0, vibrato=False):
    out, phase = [], random.Random(f).random()
    for i in range(int(dur * SR)):
        t = i / SR
        wobble = 1 + 0.006 * math.sin(2 * math.pi * 5.5 * t) * min(1.0, t / 0.3) if vibrato else 1
        phase = (phase + f * wobble / SR) % 1
        rise = min(1.0, t / 0.005, (dur - t) / 0.01)
        out.append((2 * phase - 1) * rise * math.exp(-t * decay))
    return out


def square_note(f, dur, decay=0.0):
    out = []
    for i in range(int(dur * SR)):
        t = i / SR
        rise = min(1.0, t / 0.002, (dur - t) / 0.005)
        out.append((1 if (f * t) % 1 < 0.5 else -1) * rise * math.exp(-t * decay))
    return out


def triangle_note(f, dur):
    out = []
    for i in range(int(dur * SR)):
        t = i / SR
        rise = min(1.0, t / 0.002, (dur - t) / 0.005)
        out.append((4 * abs((f * t) % 1 - 0.5) - 1) * rise)
    return out


def sequence(notes, step, voice, level=1.0):
    """Place voice(midi note) every step seconds. None is a rest; loops for LENGTH."""
    out = [0.0] * int(LENGTH * SR)
    for n in range(int(LENGTH / step)):
        note = notes[n % len(notes)]
        if note is None:
            continue
        start = int(n * step * SR)
        for i, s in enumerate(voice(note)):
            if start + i >= len(out):
                break
            out[start + i] += s * level
    return out


LINE = [69, 72, 76, 74, 72, 69, 67, 69]


def synth_lead():
    return lowpass(sequence(LINE, 0.5, lambda n: saw_note(midi(n + 12), 0.48, vibrato=True)), 4000)


def synth_pluck():
    return lowpass(sequence(LINE, 0.25, lambda n: saw_note(midi(n), 0.24, decay=14)), 3000)


def arpeggio():
    up_down = [
        note + 12
        for r, third, fifth in CHORDS
        for note in (r, third, fifth, r + 12, third + 12, fifth + 12, third + 12, r + 12) * 2
    ]
    return lowpass(sequence(up_down, 0.125, lambda n: square_note(midi(n), 0.12, decay=10)), 5000)


def acid_note(note):
    """Saw through a resonant low-pass whose cutoff sweeps down."""
    dur, low, band, out = 0.24, 0.0, 0.0, []
    for s in saw_note(midi(note), dur):
        t = len(out) / SR
        f = 2 * math.sin(math.pi * (250 + 2600 * math.exp(-t * 16)) / SR)
        high = s - low - 0.22 * band
        band += f * high
        low += f * band
        out.append(math.tanh(low))
    return out


def acid_bass():
    return sequence([33, 33, 45, 33, None, 33, 36, 33, 33, 45, 33, 43, None, 33, 31, 36], 0.25, acid_note)


def chiptune():
    return mix(
        sequence(LINE, 0.25, lambda n: square_note(midi(n + 12), 0.22, decay=3), 0.5),
        sequence([45, None, 57, None, 41, None, 53, None, 48, None, 60, None, 43, None, 55, None], 0.25,
                 lambda n: triangle_note(midi(n), 0.24), 0.7),
    )


def chord_clip(tone, seconds=2.0):
    out = [0.0] * int(LENGTH * SR)
    for c, chord in enumerate(CHORDS):
        start = int(c * seconds * SR)
        for note in chord:
            for i, s in enumerate(tone(midi(note), seconds)):
                out[start + i] += s
    return out


def rhodes_tone(f, dur):
    out = []
    for i in range(int(dur * SR)):
        t = i / SR
        w = 2 * math.pi * f * t
        release = min(1.0, (dur - t) / 0.05)
        v = math.sin(w + 1.1 * math.exp(-t * 4) * math.sin(w)) * math.exp(-t * 1.3)
        out.append((v + 0.12 * math.exp(-t * 22) * math.sin(14 * w)) * release)
    return out


def organ_tone(f, dur):
    out = []
    for i in range(int(dur * SR)):
        t = i / SR
        w = 2 * math.pi * f * t
        rise = min(1.0, t / 0.008, (dur - t) / 0.02)
        rotary = 1 + 0.18 * math.sin(2 * math.pi * 6 * t)
        drawbars = sum(g * math.sin(h * w) for h, g in ((1, 1), (2, 0.8), (3, 0.6), (4, 0.3), (6, 0.2), (8, 0.2)))
        out.append(drawbars * rise * rotary)
    return out


CLIPS = {
    "snare-drum": lambda: groove(120, (snare(), [1, 3], 1.0)),
    "ride-cymbal": lambda: groove(120, (ride_hit(), [0, 1, 1.5, 2, 3, 3.5], 0.8)),
    "crash-cymbal": lambda: groove(120, (crash_hit(), [0], 1.0)),
    "toms": lambda: groove(120, (tom(220), [0, 0.5], 1.0), (tom(165), [1, 1.5], 1.0), (tom(110), [2, 2.5, 3], 1.0)),
    "bongos": lambda: groove(120, (bongo(520), [0, 1, 2, 2.5, 3.5], 0.9), (bongo(390), [0.5, 1.5, 3], 1.0)),
    "timbales": lambda: groove(120, (timbale(440), [0, 0.75, 2, 2.75], 0.9), (timbale(330), [1.5, 3, 3.5], 1.0)),
    "synth-lead": synth_lead,
    "synth-pluck": synth_pluck,
    "arpeggio": arpeggio,
    "acid-bass": acid_bass,
    "chiptune": chiptune,
    "electric-piano": lambda: chord_clip(rhodes_tone),
    "electric-organ": lambda: chord_clip(organ_tone),
    "tambourine": lambda: groove(120, (tambourine_hit(), EIGHTHS, 0.6), (tambourine_hit(), [1, 3], 0.6)),
    "shaker": lambda: groove(120, (shaker_hit(), SIXTEENTHS, 0.6), (shaker_hit(), EIGHTHS, 0.5)),
    "congas": lambda: groove(120, (conga(330), [0.5, 1.5, 2.5, 3, 3.5], 0.8), (conga(220), [0, 2], 1.0)),
    "handclap": lambda: groove(120, (clap(), [1, 3], 1.0)),
    "triangle": lambda: groove(120, (triangle_hit(), [0, 2], 1.0), (triangle_hit(), [1, 3], 0.5)),
    "woodblock": lambda: groove(120, (woodblock(1000), [0, 1, 2, 3], 1.0), (woodblock(1500), [1.5, 3.5], 0.8)),
    "claves": lambda: groove(120, (clave_hit(), [0, 1.5, 3], 1.0)),
    "four-on-the-floor": lambda: groove(120, (kick(), [0, 1, 2, 3], 1.0)),
    "off-beat-hi-hat": lambda: groove(120, (kick(), [0, 1, 2, 3], 1.0), (hat(True), [0.5, 1.5, 2.5, 3.5], 0.8)),
    "syncopated": lambda: groove(120, (kick(), [0, 1.75, 2.5], 1.0), (snare(), [1, 3], 0.7), (hat(), EIGHTHS, 0.4)),
    "half-time": lambda: groove(120, (kick(), [0], 1.0), (snare(), [2], 0.8), (hat(), EIGHTHS, 0.4)),
    "breakbeat": lambda: groove(140, (kick(), [0, 0.5, 2.5], 1.0), (snare(), [1, 1.75, 3, 3.75], 0.7), (hat(), EIGHTHS, 0.35)),
    "808-drums": lambda: groove(120, (kick_808(), [0, 1.5, 2.5], 1.0), (clap(), [1, 3], 0.5), (hat(), SIXTEENTHS, 0.25)),
    "sub-bass": sub_bass,
    "supersaw": supersaw,
    "synth-pads": pads,
    "gated-reverb": lambda: groove(90, (kick(), [0, 2], 0.9), (gated_snare(), [1, 3], 0.8)),
    "tape-warmth": tape,
}


def write_mp3(name, samples):
    peak = max(abs(s) for s in samples) or 1.0
    pcm = array("h", (int(s / peak * 0.89 * 32767) for s in samples))
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-",
         "-af", "afade=t=out:st=7.97:d=0.03", "-codec:a", "libmp3lame", "-q:a", "2", str(ASSETS / f"{name}.mp3")],
        input=pcm.tobytes(),
        check=True,
    )


def main():
    names = sys.argv[1:] or list(CLIPS)
    ASSETS.mkdir(exist_ok=True)
    for name in names:
        write_mp3(name, CLIPS[name]()[: int(LENGTH * SR)])
        print(name)


if __name__ == "__main__":
    main()
