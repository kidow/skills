# AEO/GEO Reference

## Definitions

- **AEO (Answer Engine Optimization)**: optimize so AI cites the brand when answering user questions directly.
- **GEO (Generative Engine Optimization)**: broader. Optimize so the brand is selected and recommended in conversational AI dialogue (ChatGPT, Claude, Gemini, Perplexity).

> Traffic loss is acceptable. What matters is how AI defines the brand.

## Core principles

1. **Structured data over prose**: "service A, B, C features at $X/month" beats "great service".
2. **Probabilistic positive adjectives**: seed the web so words like "best", "reasonable", "essential" co-occur with the brand. AI is lazy and picks the safe, frequent answer.
3. **Measurable iteration**: track mentions per AI per week. Sentiment scoring. Per-AI competitor positioning.

## 4-stage GEO funnel

| Stage | Question |
|-------|----------|
| 1. Existence | Does AI know us? |
| 2. Context | Does AI know what we do? |
| 3. Recency | Does AI think we're still active? |
| 4. Recommendation | Does AI present us as the answer? |

## 7-step GEO framework 1.0

1. **Entity mapping**: convert vague ("fast company") to measurable ("1-hour last-mile across Seoul").
2. **Source diversification**: presence in 4 channels — official, press, academic/professional, community.
3. **Authority density**: repeat consistent positioning across high-authority sources.
4. **Schema markup**: JSON-LD Organization, Product, Article, FAQ.
5. **Content seeding**: Namu Wiki, Medium, LinkedIn, YouTube (subtitles count).
6. **Multilingual presence**: at least Korean + English. Same entity definition translated faithfully.
7. **AI verification loop**: monthly prompts to LLMs, log gaps, ship corrections.

## Channels

### AI reads well
- Namu Wiki (open Korean wiki, low barrier)
- Medium, Brunch (open blogs)
- LinkedIn profiles + posts
- YouTube (subtitles + description)
- Official site with schema markup
- News articles, press releases
- Crunchbase

### AI reads partially
- Naver Blog (limited crawling)
- Google Business Profile
- App Store / Play Store descriptions

### AI cannot read (zero GEO value)
- Login-walled communities
- In-app content
- DMs, emails, private channels

## Long-term goal: Wikipedia

Wikipedia is high-impact but **not a short-term target**. English Wikipedia requires 5+ independent reliable secondary sources covering the brand in depth. Most small brands fail notability and get deleted within days. Pursue only after 12+ months of press coverage and academic mentions.

Korean Namu Wiki has far lower barriers — start there.

## Share thresholds (Phase 1)

| Share | Stage | Action |
|-------|-------|--------|
| 0–10% | Risk | Immediate GEO intervention |
| 10–30% | Growth | Sustained content reinforcement |
| 30–50% | Compete | Take/defend #1 |
| 50%+ | Dominate | Maintain + monitor |

## Sentiment dictionary

- **Positive**: "best", "industry-leading", "trusted", "recommended"
- **Neutral**: simple listing, comparison cell
- **Negative**: "downside is", "alternative to", "expensive"

## Verification loop response matrix

| Finding | Response |
|---------|----------|
| "No info" | Ship foundational content (Namu Wiki, blog post, press release) |
| "Outdated info" | Update site + republish to authority sources |
| "Competitor first" | Increase authority density (more sources, repeated positioning) |
| "Negative tone" | Generate positive-context content (case studies, testimonials, comparison wins) |

## Why entity definition consistency matters

The same paragraph reworded across channels reads as **multiple different companies** to AI. Lexical drift dilutes signal. Treat the canonical sentence as immutable until a deliberate rebrand.

## Schema injection per stack

Detect stack from `package.json` (Next.js: `"next"`), `composer.json` + `wp-config.php` (WordPress), or absence of build files (static HTML).

### Next.js (App Router)

Add to `app/layout.tsx`:

```tsx
import schema from '@/organization-schema.json';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

### WordPress

Install **Schema & Structured Data for WP & AMP** (or **RankMath** SEO). Paste JSON in *Schema → Custom Schema → Organization*. Or paste raw `<script type="application/ld+json">…</script>` block into theme `header.php` before `</head>`.

### Static HTML

Paste before `</head>` in every page that should carry brand identity (at minimum `index.html` and `about.html`):

```html
<script type="application/ld+json">
{ ...contents of organization-schema.json... }
</script>
```

Validate with [validator.schema.org](https://validator.schema.org/) and Google [Rich Results Test](https://search.google.com/test/rich-results).
