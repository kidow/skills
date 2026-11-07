#!/usr/bin/env python3
"""Build the glossary's recorded samples from VSCO 2 Community Edition (CC0-1.0).

Downloads only the listed WAV files from a pinned commit into a temporary folder,
writes 8-second MP3s to ../assets, then deletes the WAVs. Requires ffmpeg.

Usage: build_recorded_samples.py [clip-name ...]   (no names = all clips)
"""
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from array import array
from pathlib import Path

sys.dont_write_bytecode = True
from make_samples import LENGTH, SR, write_mp3  # noqa: E402

COMMIT = "440300901dfe9275fd84e0b7763af1f8443ae62e"
RAW = f"https://raw.githubusercontent.com/sgossner/VSCO-2-CE/{COMMIT}/"

# clip: (kind, folder, file names without .wav)
# "held" plays four long notes in turn; "struck" loops them as ringing eighth notes.
SOURCES = {
    "acoustic-piano": ("struck", "Keys/Upright Piano", [f"Player_dyn2_rr1_{n:03d}" for n in (20, 22, 24, 26)]),
    "violin": ("held", "Strings/Solo Violin/Arco Vib", [f"LLVln_ArcoVib_{n}_f" for n in ("A4", "C5", "E5", "A5")]),
    "cello": ("held", "Strings/Cello Section/susvib", [f"susvib_{n}_v3_1" for n in ("A2", "C3", "E3", "G3")]),
    "string-section": ("held", "Strings/Violin Section/susVib", [f"VlnEns_susVib_{n}_v2" for n in ("A3", "C4", "E4", "G4")]),
    "harp": ("struck", "Strings/Harp", [f"KSHarp_{n}_mf" for n in ("A4", "C5", "E5", "G5")]),
    "trumpet": ("held", "Brass/Trumpet/sus", [f"Sum_SHTrumpet_sus_{n}_v1_rr1" for n in ("D4", "F4", "A4", "C5")]),
    "trombone": ("held", "Brass/Tenor Trombone/sus", [f"tenortbn_sus_{n}_v2_1" for n in ("F2", "C3", "D#3", "F3")]),
    "french-horn": ("held", "Brass/F Horn/sus", [f"MOHorn_sus_{n}_v2_1" for n in ("D2", "F2", "A2", "C3")]),
    "flute": ("held", "Woodwinds/Flute/susvib", [f"LDFlute_susvib_{n}_v1_1" for n in ("A4", "C5", "E5", "A5")]),
    "clarinet": ("held", "Woodwinds/Clarinet/susLong", [f"DCClar_susLong_{n}_v2_rr1_sum" for n in ("D4", "F4", "A#4", "D5")]),
    "marimba": ("struck", "Percussion/Marimba", [f"Marimba_hit_Outrigger_{n}_loud_01" for n in ("F3", "C4", "G4", "C6")]),
    "glockenspiel": ("struck", "Percussion/Glock", [f"glock_medium_{n}" for n in ("G4", "C5", "G5", "C6")]),
}


def fetch(folder, name, dest):
    url = RAW + urllib.parse.quote(f"{folder}/{name}.wav")
    path = dest / f"{len(list(dest.iterdir())):03d}.wav"
    with urllib.request.urlopen(url, timeout=120) as response:
        path.write_bytes(response.read())
    return path


def decode(path):
    """Mono float samples, peak-normalized, with leading silence removed."""
    raw = subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-i", str(path),
         "-af", "silenceremove=start_periods=1:start_threshold=-50dB",
         "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True,
        check=True,
    ).stdout
    samples = array("f")
    samples.frombytes(raw[: len(raw) - len(raw) % 4])
    peak = max((abs(s) for s in samples), default=0.0) or 1.0
    return [s / peak for s in samples]


def place(out, note, start, length, fade):
    """Mix note into out at start, cut to length with a linear fade at each end."""
    n = min(len(note), length)
    edge = int(fade * SR)
    for i in range(n):
        if start + i >= len(out):
            break
        level = min(1.0, (i + 1) / edge, (n - i) / edge)
        out[start + i] += note[i] * level


def held(notes):
    out = [0.0] * int(LENGTH * SR)
    step = int(LENGTH * SR / len(notes))
    overlap = int(0.1 * SR)
    for n, note in enumerate(notes):
        place(out, note, n * step, step + overlap, 0.1)
    return out


def struck(notes):
    out = [0.0] * int(LENGTH * SR)
    pattern = [0, 1, 2, 3, 2, 1]
    step = int(0.5 * SR)
    for n in range(int(LENGTH / 0.5)):
        place(out, notes[pattern[n % len(pattern)]], n * step, int(1.2 * SR), 0.005)
    return out


def main():
    names = sys.argv[1:] or list(SOURCES)
    with tempfile.TemporaryDirectory(prefix="vsco-") as tmp:
        total = 0
        for clip in names:
            kind, folder, files = SOURCES[clip]
            dest = Path(tmp) / clip
            dest.mkdir()
            paths = [fetch(folder, f, dest) for f in files]
            total += sum(p.stat().st_size for p in paths)
            notes = [decode(p) for p in paths]
            lengths = " ".join(f"{len(n) / SR:.1f}s" for n in notes)
            write_mp3(clip, (held if kind == "held" else struck)(notes))
            print(f"{clip}: {lengths}", flush=True)
        print(f"downloaded {total / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
