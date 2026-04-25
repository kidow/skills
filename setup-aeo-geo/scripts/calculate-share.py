#!/usr/bin/env python3
"""
Calculate AI answer share from share-tracker.csv.

Usage:
  python3 calculate-share.py <path-to-share-tracker.csv>

Input CSV columns:
  question_id, question, ai, run, brand_mentioned (1/0 or o/x),
  competitor_a, competitor_b, competitor_c, sentiment (positive/neutral/negative)

Output:
  - Overall brand share %
  - Per-AI share %
  - Competitor ranking
  - Stage classification (risk / growth / compete / dominate)
  - Sentiment breakdown
"""
import csv
import sys
from collections import defaultdict


STAGE_RULES = [
    (10, "RISK — immediate GEO intervention required"),
    (30, "GROWTH — sustained content reinforcement"),
    (50, "COMPETE — take or defend #1"),
    (101, "DOMINATE — maintain and monitor"),
]


def to_bool(value: str) -> bool:
    return str(value).strip().lower() in {"1", "o", "yes", "true", "y"}


def stage_for(share: float) -> str:
    for threshold, label in STAGE_RULES:
        if share < threshold:
            return label
    return STAGE_RULES[-1][1]


def main(csv_path: str) -> None:
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("ai") or not row.get("question"):
                continue
            if "<" in (row.get("question") or ""):
                continue  # placeholder row, skip
            rows.append(row)

    if not rows:
        print("No filled rows found. Replace <question> placeholders and fill brand_mentioned column.")
        sys.exit(1)

    total = len(rows)
    brand_hits = sum(1 for r in rows if to_bool(r.get("brand_mentioned", "")))

    per_ai = defaultdict(lambda: [0, 0])  # [hits, total]
    for r in rows:
        ai = r["ai"].strip().lower()
        per_ai[ai][1] += 1
        if to_bool(r.get("brand_mentioned", "")):
            per_ai[ai][0] += 1

    competitor_hits = defaultdict(int)
    for r in rows:
        for col in ("competitor_a", "competitor_b", "competitor_c"):
            if to_bool(r.get(col, "")):
                competitor_hits[col] += 1

    sentiment_counts = defaultdict(int)
    for r in rows:
        s = (r.get("sentiment") or "").strip().lower() or "unknown"
        sentiment_counts[s] += 1

    overall = brand_hits / total * 100
    print(f"\n=== Brand AI Answer Share ===")
    print(f"Total runs: {total}")
    print(f"Brand mentions: {brand_hits} ({overall:.1f}%)")
    print(f"Stage: {stage_for(overall)}\n")

    print("Per AI:")
    for ai, (hits, n) in sorted(per_ai.items()):
        pct = hits / n * 100 if n else 0
        print(f"  {ai:10s} {hits:3d}/{n:3d}  {pct:5.1f}%")

    print("\nCompetitor mentions:")
    ranking = sorted(competitor_hits.items(), key=lambda x: -x[1])
    for name, hits in ranking:
        pct = hits / total * 100
        print(f"  {name:14s} {hits:3d}  {pct:5.1f}%")

    print("\nSentiment:")
    for s, n in sorted(sentiment_counts.items(), key=lambda x: -x[1]):
        pct = n / total * 100
        print(f"  {s:10s} {n:3d}  {pct:5.1f}%")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 calculate-share.py <path-to-share-tracker.csv>")
        sys.exit(1)
    main(sys.argv[1])
