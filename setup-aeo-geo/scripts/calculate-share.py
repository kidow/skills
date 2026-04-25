#!/usr/bin/env python3
"""
Calculate AI answer share from share-tracker.csv. Writes a dated markdown report
to reports/YYYY-MM-DD.md alongside console output.

Usage:
  python3 calculate-share.py <path-to-share-tracker.csv> [--reports-dir reports]

Input CSV columns:
  question_id, question, ai, run, brand_mentioned (1/0 or o/x),
  competitor_a, competitor_b, competitor_c, sentiment (positive/neutral/negative)
"""
import csv
import os
import sys
from collections import defaultdict
from datetime import date


STAGE_RULES = [
    (10, "RISK", "Immediate GEO intervention required"),
    (30, "GROWTH", "Sustained content reinforcement"),
    (50, "COMPETE", "Take or defend #1"),
    (101, "DOMINATE", "Maintain and monitor"),
]


def to_bool(value: str) -> bool:
    return str(value).strip().lower() in {"1", "o", "yes", "true", "y"}


def stage_for(share: float):
    for threshold, name, action in STAGE_RULES:
        if share < threshold:
            return name, action
    return STAGE_RULES[-1][1], STAGE_RULES[-1][2]


def aggregate(rows):
    total = len(rows)
    brand_hits = sum(1 for r in rows if to_bool(r.get("brand_mentioned", "")))
    per_ai = defaultdict(lambda: [0, 0])
    competitor_hits = defaultdict(int)
    sentiment_counts = defaultdict(int)
    for r in rows:
        ai = r["ai"].strip().lower()
        per_ai[ai][1] += 1
        if to_bool(r.get("brand_mentioned", "")):
            per_ai[ai][0] += 1
        for col in ("competitor_a", "competitor_b", "competitor_c"):
            if to_bool(r.get(col, "")):
                competitor_hits[col] += 1
        s = (r.get("sentiment") or "").strip().lower() or "unknown"
        sentiment_counts[s] += 1
    return total, brand_hits, per_ai, competitor_hits, sentiment_counts


def render_console(total, brand_hits, per_ai, competitor_hits, sentiment_counts):
    overall = brand_hits / total * 100
    stage, action = stage_for(overall)
    print(f"\n=== Brand AI Answer Share ===")
    print(f"Total runs: {total}")
    print(f"Brand mentions: {brand_hits} ({overall:.1f}%)")
    print(f"Stage: {stage} — {action}\n")
    print("Per AI:")
    for ai, (h, n) in sorted(per_ai.items()):
        pct = h / n * 100 if n else 0
        print(f"  {ai:10s} {h:3d}/{n:3d}  {pct:5.1f}%")
    print("\nCompetitor mentions:")
    for name, h in sorted(competitor_hits.items(), key=lambda x: -x[1]):
        pct = h / total * 100
        print(f"  {name:14s} {h:3d}  {pct:5.1f}%")
    print("\nSentiment:")
    for s, n in sorted(sentiment_counts.items(), key=lambda x: -x[1]):
        pct = n / total * 100
        print(f"  {s:10s} {n:3d}  {pct:5.1f}%")


def render_markdown(total, brand_hits, per_ai, competitor_hits, sentiment_counts, csv_path):
    overall = brand_hits / total * 100
    stage, action = stage_for(overall)
    today = date.today().isoformat()
    lines = [
        f"# AEO/GEO Share Report — {today}",
        "",
        f"Source: `{os.path.basename(csv_path)}`",
        "",
        "## Summary",
        "",
        f"- Total runs: **{total}**",
        f"- Brand mentions: **{brand_hits}** ({overall:.1f}%)",
        f"- Stage: **{stage}** — {action}",
        "",
        "## Per AI",
        "",
        "| AI | Hits | Total | Share |",
        "|----|------|-------|-------|",
    ]
    for ai, (h, n) in sorted(per_ai.items()):
        pct = h / n * 100 if n else 0
        lines.append(f"| {ai} | {h} | {n} | {pct:.1f}% |")

    lines += ["", "## Competitor mentions", "",
              "| Slot | Mentions | Share |",
              "|------|----------|-------|"]
    for name, h in sorted(competitor_hits.items(), key=lambda x: -x[1]):
        pct = h / total * 100
        lines.append(f"| {name} | {h} | {pct:.1f}% |")

    lines += ["", "## Sentiment", "",
              "| Sentiment | Count | Share |",
              "|-----------|-------|-------|"]
    for s, n in sorted(sentiment_counts.items(), key=lambda x: -x[1]):
        pct = n / total * 100
        lines.append(f"| {s} | {n} | {pct:.1f}% |")

    lines += ["", "## Action", "",
              f"- {action}"]

    return "\n".join(lines) + "\n", today


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 calculate-share.py <share-tracker.csv> [--reports-dir DIR]")
        sys.exit(1)
    csv_path = sys.argv[1]
    reports_dir = "reports"
    if "--reports-dir" in sys.argv:
        reports_dir = sys.argv[sys.argv.index("--reports-dir") + 1]

    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("ai") or not row.get("question"):
                continue
            if "<" in (row.get("question") or ""):
                continue
            rows.append(row)

    if not rows:
        print("No filled rows. Replace placeholders and fill brand_mentioned.")
        sys.exit(1)

    total, brand_hits, per_ai, competitor_hits, sentiment_counts = aggregate(rows)
    render_console(total, brand_hits, per_ai, competitor_hits, sentiment_counts)

    md, today = render_markdown(total, brand_hits, per_ai, competitor_hits, sentiment_counts, csv_path)
    os.makedirs(reports_dir, exist_ok=True)
    out_path = os.path.join(reports_dir, f"{today}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"\nReport written: {out_path}")


if __name__ == "__main__":
    main()
