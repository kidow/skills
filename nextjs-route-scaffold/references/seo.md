# Route SEO Patterns

Use these patterns when `nextjs-route-scaffold` needs to add SEO settings without expanding into a full site SEO setup.

## Route-level metadata

Prefer the Metadata API in `page.tsx` or `layout.tsx`.

- Static routes: `metadata`
- Dynamic routes: `generateMetadata`

Include the fields that matter for the route:

- `title`
- `description`
- `alternates.canonical`
- `openGraph`
- `twitter`
- `robots`

## Root layout defaults

Use `metadataBase` in `app/layout.tsx` or `src/app/layout.tsx` when the project needs absolute metadata URLs.

Set a title template at the root so route titles can stay short and consistent.

## Noindex routes

Use `robots.index = false` and `robots.follow = false` for:

- auth pages
- admin pages
- internal tools
- preview-only routes

## Dynamic routes

For parameterized pages, generate canonical URLs from params inside `generateMetadata`.

Only add SEO metadata that is meaningful for the route. Do not add sitemap or robots files here unless the user explicitly asks for site-wide SEO files.
