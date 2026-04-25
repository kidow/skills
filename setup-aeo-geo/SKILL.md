---
name: setup-aeo-geo
description: Build a brand's AEO/GEO (Answer Engine Optimization / Generative Engine Optimization) strategy step by step over a 3-phase roadmap. Generates measurement spreadsheets and a share calculator script for week 1, runs an interview to build a canonical entity definition sentence in weeks 2-4, scaffolds JSON-LD Organization schema markup and monthly monitoring assets in weeks 5-8. Use when user wants to set up AEO/GEO, optimize brand mentions in ChatGPT/Claude/Gemini answers, measure AI answer share, build entity definition or schema markup for AI visibility, or asks "how do I get AI to recommend my brand", "AEO 셋업", "GEO 전략 만들어줘", "AI 답변 점유율 측정".
---

# AEO/GEO Strategy Setup

3-phase roadmap. Each phase delivers value standalone — stop after any phase. See [REFERENCE.md](REFERENCE.md) for theory (4-stage funnel, 7-step framework).

## Phase 1 — Measure (Week 1)

Goal: know where the brand stands in AI answers today.

1. Interview user for 5 candidate questions a customer would ask AI **without naming the brand**. Examples:
   - "Best <category> for <use case>?"
   - "<competitor A> vs <competitor B> — which is better?"
   - "Is <category> safe / legal / reliable?"
2. Generate [templates/share-tracker.csv](templates/share-tracker.csv) — 5 questions × 3 AIs (ChatGPT, Claude, Gemini) = 15 rows.
3. Tell user: "Run each question 3 times in incognito mode (no login). Record brand mentions in CSV."
4. After user fills CSV, run [scripts/calculate-share.py](scripts/calculate-share.py) — outputs share %, ranking, stage (risk / growth / compete / dominate), and sentiment breakdown.

Stage thresholds: 0–10% risk · 10–30% growth · 30–50% compete · 50%+ dominate.

## Phase 2 — Define (Weeks 2–4)

Goal: a single canonical sentence used everywhere.

1. Interview 5 slots one at a time:
   - **Company name**: legal + alternate name
   - **Target customer**: who specifically
   - **Concrete metric/outcome**: numbers, not adjectives ("3만 명 작가" not "많은 작가")
   - **Core value**: what they get
   - **Category**: noun phrase that names the market
2. Assemble: `[Company] is a [category] for [target customer], delivering [core value] backed by [metric/outcome].`
3. Save to `entity-definition.md` at project root. Tell user: "Use this verbatim on website, press releases, LinkedIn, Wikipedia. Inconsistency = AI sees multiple companies."
4. Distribute checklist (open web only — see [REFERENCE.md](REFERENCE.md) channel list):
   - Wikipedia / Namu Wiki entry
   - Medium / Brunch posts (10+)
   - LinkedIn company page + founder profile
   - Press releases via wire services
   - YouTube videos with subtitles + descriptions

## Phase 3 — Systematize (Weeks 5–8)

Goal: schema markup + ongoing monitoring loop.

1. **JSON-LD Organization schema**: scaffold [templates/organization-schema.json](templates/organization-schema.json).
   - Required: `name`, `url`, `description` (reuse Phase 2 sentence), `sameAs` (social/wiki URLs)
   - Optional: `logo`, `foundingDate`, `founder`, `numberOfEmployees`, `areaServed`, `knowsAbout`
   - Warn if required fields empty. Inject into site `<head>` as `<script type="application/ld+json">`.
2. **Monthly monitor**: copy [templates/monthly-monitor.csv](templates/monthly-monitor.csv) — same 5 questions plus brand-name probes:
   - "Tell me about <brand>"
   - "<brand> vs <competitor> compare"
   - "Downsides of <brand>?"
3. After 2+ months of data, run [scripts/track-trend.py](scripts/track-trend.py) — share % delta per AI, sentiment shift, action triggers.

## Operating Rules

- **No brand-name in Phase 1 questions**: customers don't search by your brand. Strip any candidate that includes it.
- **Numbers beat adjectives**: refuse vague metric slots in Phase 2. "fast delivery" → "within 1 hour citywide".
- **Open web only**: never recommend login-walled platforms (private Slack, app-only content). AI cannot read them.
- **Reuse Phase 2 sentence**: `description` field in schema and bios must match it character-for-character.

## Quick Start

User says "set up GEO for our brand":

1. Phase 1 → measure first. Confirm CSV results before moving on.
2. Ask: "Continue to Phase 2 (entity definition)?"
3. Continue phase by phase until user stops.

## Reference

- Theory deep dive: [REFERENCE.md](REFERENCE.md)
- Share tracker: [templates/share-tracker.csv](templates/share-tracker.csv)
- Schema scaffold: [templates/organization-schema.json](templates/organization-schema.json)
- Monthly monitor: [templates/monthly-monitor.csv](templates/monthly-monitor.csv)
- Share calculator: [scripts/calculate-share.py](scripts/calculate-share.py)
- Trend tracker: [scripts/track-trend.py](scripts/track-trend.py)
