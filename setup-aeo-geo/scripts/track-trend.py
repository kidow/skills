#!/usr/bin/env python3
"""
Track monthly AEO/GEO share trend from a single accumulating monitoring.csv.

Usage:
  python3 track-trend.py <path-to-monitoring.csv> [--reports-dir reports]

CSV must have a `month` column (YYYY-MM). Combine 2+ months to see deltas.
Writes a dated markdown report to reports/YYYY-MM-DD-trend.md.
"""
import csv
import os
import sys
from collections import defaultdict
from datetime import date


def to_bool(value: str) -> bool:
    return str(value).strip().lower() in {"1", "o", "yes", "true", "y"}


def aggregate(rows):
    by_month = defaultdict(lambda: {
        "hits": 0,
        "total": 0,
        "per_ai": defaultdict(lambda: [0, 0]),
        "sentiment": defaultdict(int),
    })
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


def action_for(pct: float, sentiment: dict) -> list:
    triggers = []
    if pct < 10:
        triggers.append("0–10% RISK: ship foundational content (Namu Wiki, blog, press release)")
    elif pct < 30:
        triggers.append("10–30% GROWTH: increase authority density across open web")
    elif pct < 50:
        triggers.append("30–50% COMPETE: target #1 — produce comparison content vs leading competitor")
    else:
        triggers.append("50%+ DOMINATE: maintain monitoring cadence")
    if sentiment.get("negative", 0) > 0:
        triggers.append("Negative tone detected: generate positive-context content (case studies, wins)")
    return triggers


def render_console(by_month):
    months = sorted(by_month.keys())
    print("\n=== Monthly Share Trend ===")
    prev = None
    for m in months:
        d = by_month[m]
        pct = d["hits"] / d["total"] * 100
        delta = "" if prev is None else f" (Δ {pct - prev:+.1f}pp)"
        print(f"\n{m}: {d['hits']}/{d['total']} = {pct:.1f}%{delta}")
        for ai, (h, n) in sorted(d["per_ai"].items()):
            ai_pct = h / n * 100 if n else 0
            print(f"  {ai:10s} {h:3d}/{n:3d}  {ai_pct:5.1f}%")
        print("  Sentiment:", ", ".join(f"{s}={c}" for s, c in d["sentiment"].items()))
        prev = pct
    last = by_month[months[-1]]
    last_pct = last["hits"] / last["total"] * 100
    print("\n=== Action Triggers ===")
    for t in action_for(last_pct, last["sentiment"]):
        print(f"- {t}")


def render_markdown(by_month, csv_path):
    months = sorted(by_month.keys())
    today = date.today().isoformat()
    lines = [
        f"# AEO/GEO Trend Report — {today}",
        "",
        f"Source: `{os.path.basename(csv_path)}`",
        f"Months covered: {', '.join(months)}",
        "",
        "## Monthly share",
        "",
        "| Month | Hits | Total | Share | Δ vs prev |",
        "|-------|------|-------|-------|-----------|",
    ]
    prev = None
    for m in months:
        d = by_month[m]
        pct = d["hits"] / d["total"] * 100
        delta = "—" if prev is None else f"{pct - prev:+.1f}pp"
        lines.append(f"| {m} | {d['hits']} | {d['total']} | {pct:.1f}% | {delta} |")
        prev = pct

    lines += ["", "## Per-AI share by month", ""]
    for m in months:
        d = by_month[m]
        lines.append(f"### {m}")
        lines.append("")
        lines.append("| AI | Hits | Total | Share |")
        lines.append("|----|------|-------|-------|")
        for ai, (h, n) in sorted(d["per_ai"].items()):
            ai_pct = h / n * 100 if n else 0
            lines.append(f"| {ai} | {h} | {n} | {ai_pct:.1f}% |")
        lines.append("")

    last = by_month[months[-1]]
    last_pct = last["hits"] / last["total"] * 100
    lines += ["## Action triggers (latest month)", ""]
    for t in action_for(last_pct, last["sentiment"]):
        lines.append(f"- {t}")
    lines.append("")
    return "\n".join(lines), today


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 track-trend.py <monitoring.csv> [--reports-dir DIR]")
        sys.exit(1)
    csv_path = sys.argv[1]
    reports_dir = "reports"
    if "--reports-dir" in sys.argv:
        reports_dir = sys.argv[sys.argv.index("--reports-dir") + 1]

    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("month") or "<" in (row.get("question") or ""):
                continue
            rows.append(row)

    if not rows:
        print("No filled rows. Replace placeholders and fill brand_mentioned.")
        sys.exit(1)

    by_month = aggregate(rows)
    render_console(by_month)

    md, today = render_markdown(by_month, csv_path)
    os.makedirs(reports_dir, exist_ok=True)
    out_path = os.path.join(reports_dir, f"{today}-trend.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"\nReport written: {out_path}")


if __name__ == "__main__":
    main()
