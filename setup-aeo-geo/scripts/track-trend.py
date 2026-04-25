#!/usr/bin/env python3
"""
Track monthly AEO/GEO share trend across multiple monthly-monitor.csv files.

Usage:
  python3 track-trend.py <monthly-monitor.csv> [<monthly-monitor.csv> ...]

Each CSV must have a `month` column (YYYY-MM). Combine 2+ months to see deltas.

Output:
  - Per-month share % (overall + per AI)
  - Month-over-month delta
  - Sentiment shift
  - Action triggers (no info / outdated / competitor first / negative tone)
"""
import csv
import sys
from collections import defaultdict


def to_bool(value: str) -> bool:
    return str(value).strip().lower() in {"1", "o", "yes", "true", "y"}


def load(paths):
    rows = []
    for path in paths:
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if not row.get("month") or "<" in (row.get("question") or ""):
                    continue
                rows.append(row)
    return rows


def aggregate(rows):
    by_month = defaultdict(lambda: {"hits": 0, "total": 0, "per_ai": defaultdict(lambda: [0, 0]), "sentiment": defaultdict(int)})
    for r in rows:
        m = r["month"].strip()
        ai = r["ai"].strip().lower()
        bm = to_bool(r.get("brand_mentioned", ""))
        by_month[m]["total"] += 1
        if bm:
            by_month[m]["hits"] += 1
        by_month[m]["per_ai"][ai][1] += 1
        if bm:
            by_month[m]["per_ai"][ai][0] += 1
        s = (r.get("sentiment") or "").strip().lower() or "unknown"
        by_month[m]["sentiment"][s] += 1
    return by_month


def main(paths):
    rows = load(paths)
    if not rows:
        print("No filled rows. Replace placeholders and fill brand_mentioned.")
        sys.exit(1)

    by_month = aggregate(rows)
    months = sorted(by_month.keys())

    print("\n=== Monthly Share Trend ===")
    prev = None
    for m in months:
        d = by_month[m]
        pct = d["hits"] / d["total"] * 100
        delta = ""
        if prev is not None:
            delta = f" (Δ {pct - prev:+.1f}pp)"
        print(f"\n{m}: {d['hits']}/{d['total']} = {pct:.1f}%{delta}")
        for ai, (h, n) in sorted(d["per_ai"].items()):
            ai_pct = h / n * 100 if n else 0
            print(f"  {ai:10s} {h:3d}/{n:3d}  {ai_pct:5.1f}%")
        print("  Sentiment:", ", ".join(f"{s}={c}" for s, c in d["sentiment"].items()))
        prev = pct

    # Action triggers based on most recent month
    last = by_month[months[-1]]
    last_pct = last["hits"] / last["total"] * 100
    print("\n=== Action Triggers ===")
    if last_pct < 10:
        print("- 0–10% RISK: ship foundational content (Wikipedia, blog, press release)")
    elif last_pct < 30:
        print("- 10–30% GROWTH: increase authority density across open web")
    elif last_pct < 50:
        print("- 30–50% COMPETE: target #1 — produce comparison content vs leading competitor")
    else:
        print("- 50%+ DOMINATE: maintain monitoring cadence")
    if last["sentiment"].get("negative", 0) > 0:
        print("- Negative tone detected: generate positive-context content (case studies, wins)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 track-trend.py <monthly-monitor.csv> [...more]")
        sys.exit(1)
    main(sys.argv[1:])
