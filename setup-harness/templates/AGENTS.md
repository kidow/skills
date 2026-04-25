# AGENTS.md

> 60-line limit. To add a line, remove a line. Read by Claude Code (via CLAUDE.md `@AGENTS.md` import) and OpenAI Codex.

## Project Stack
<!-- Auto-fill from package.json / Cargo.toml / pyproject.toml / go.mod -->
- Language: <e.g., TypeScript 5.x>
- Framework: <e.g., Next.js 15>
- Package manager: pnpm (npm/yarn/bun forbidden)
- Test runner: <vitest | jest | playwright>

## Code Style
- <Naming: PascalCase for components, camelCase for functions>
- <Imports: external → internal → types. Absolute paths preferred.>
- <Type policy: TypeScript strict, no `any`. Use `unknown` + type guard.>

## Forbidden
<!-- DRAFT — review required. Concrete bans, not principles. -->
- No `any` type.
- No `console.log` in committed code. Use the project logger.
- No direct DB writes outside the repository layer.

## Conventions
- Commits: Conventional Commits (`feat:`, `fix:`, `chore:`, ...). Subject ≤ 50 chars.
- Branches: `feat/<topic>`, `fix/<topic>`.
- API responses: `{ success, data, error }` JSON shape.

## Past Failures
<!-- DRAFT — leave empty unless real incidents. Each line is a permanent rule learned from one failure. -->
- On repeated failure, restart in a clean context (new session) instead of patching forward.

## Known Pitfalls
- <Framework-specific gotchas, e.g., Next.js App Router 'use client' directive>
- <Migration safety, e.g., never edit supabase/migrations/ directly; use `supabase db diff`>
