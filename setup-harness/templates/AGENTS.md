# AGENTS.md

> 60-line limit. If adding a line, remove a line.

## Project Stack
<!-- Auto-fill from package.json / Cargo.toml / pyproject.toml / go.mod -->
- Language: <e.g., TypeScript 5.x>
- Framework: <e.g., Next.js 15>
- Package manager: <pnpm | npm | yarn | uv | cargo> (others forbidden)
- Test runner: <vitest | jest | pytest | go test>

## Code Style
- <Naming conventions: PascalCase for components, camelCase for functions>
- <Import order: external → internal → types, absolute paths preferred>
- <Type policy: e.g., TypeScript strict mode, no `any`>

## Forbidden
<!-- DRAFT — review required. List concrete bans, not principles. -->
- No `any` type. Use `unknown` + type guard.
- No `console.log` in committed code. Use the project logger.
- No direct DB writes outside the repository layer.

## Conventions
- Commits: Conventional Commits (`feat:`, `fix:`, `chore:`, ...). Subject ≤ 50 chars.
- Branches: `feat/<topic>`, `fix/<topic>`.
- API responses: `{ success, data, error }` JSON shape.

## Token Budget
- 500k input / 100k output per session. Stop and report when exceeded.

## Past Failures
<!-- DRAFT — leave empty unless you have real incidents. Each line is a permanent rule learned from one failure. -->
- YYYY-MM-DD: <what broke> → <permanent rule to prevent>
- Doom loop guard: if the same file is edited 5+ times in one session, stop and report.
- On repeated failure, restart in a clean context (new session) instead of patching forward.

## Known Pitfalls
- <Framework-specific gotchas, e.g., Next.js App Router 'use client' directive>
- <Migration safety, e.g., never edit supabase/migrations/ directly; use `supabase db diff`>
