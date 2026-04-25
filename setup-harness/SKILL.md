---
name: setup-harness
description: Build agent harness infrastructure (Constrain, Inform, Verify, Correct) on a project step by step. Generates AGENTS.md from the project stack, configures Claude Code permissions and lifecycle hooks, scaffolds CI verification gates, and adds doom-loop prevention rules. Optimized for Claude Code with secondary support for OpenAI Codex (which shares AGENTS.md). Use when user wants to set up agent guardrails, harden an AI coding agent setup, write or improve AGENTS.md/CLAUDE.md, configure agent permissions/hooks, or asks "how do I make my agent safer", "set up harness engineering", "configure agent rules for this project".
---

# Harness Engineering Setup

Build harness in 4 stages, ordered by impact. Stop after any stage if user is satisfied — each stage delivers value standalone. See [REFERENCE.md](REFERENCE.md) for theory and 4-pillar rationale.

## Workflow

### Stage 1 — Inform (AGENTS.md, ~10 min)

1. Detect project stack from `package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`, `composer.json`.
2. Draft `AGENTS.md` (max 60 lines) using [templates/AGENTS.md](templates/AGENTS.md). Pre-fill **Project Stack** section only.
3. Mark **Forbidden** and **Past Failures** as `# DRAFT — review required`.
4. Show diff to user. Require explicit confirmation before save.
   - Warn: "ETH Zurich research shows LLM-generated AGENTS.md drops agent performance by 3% and raises cost 20%. Past Failures must come from real incidents — leave empty if none yet."
5. For Codex projects: AGENTS.md location is identical, no extra step.

### Stage 2 — Constrain (permissions + hooks, ~15 min)

1. Create `.claude/settings.json` from [templates/settings.json](templates/settings.json).
   - `permissions.allow`: read/edit/test/git basics
   - `permissions.deny`: `rm -rf *`, `curl *`, `sudo *`, `.env` reads
2. Add token budget hint to AGENTS.md: `Token budget: 500k input / 100k output per session`.
3. Codex note: MicroVM isolation is native, no settings file. Mirror deny rules into project README for human review.

### Stage 3 — Verify (hooks required, CI optional)

1. **Required**: Add Claude Code lifecycle hook in `.claude/settings.json` to run tests after edits. See [templates/settings.json](templates/settings.json) `hooks.PostToolUse`.
2. **Optional**: Scaffold `.github/workflows/agent-pr-checks.yml` from [templates/agent-pr-checks.yml](templates/agent-pr-checks.yml) — lint + test + typecheck on PR.
3. Tell user: "Hooks give immediate feedback. CI is the merge gate. Start with hooks; add CI when team workflow needs it."

### Stage 4 — Correct (doom-loop prevention)

1. Append to AGENTS.md `Past Failures` section:
   ```
   - Doom loop guard: if the same file is edited 5+ times in one session, stop and report to user.
   ```
2. Add Ralph Loop note to AGENTS.md:
   ```
   - On repeated failure, restart in a clean context (new session) instead of patching forward.
   ```
3. Do not auto-build a counter hook. Upgrade to enforced hook only after observing real doom loops.

## Operating Rules

- **60-line rule**: AGENTS.md must stay under 60 lines. Refuse to add a line without removing one if at limit.
- **Failure → rule**: After any user-reported agent mistake, ask: "Add a one-line prevention rule to Past Failures?"
- **No skipping stages without acknowledgment**: If user wants Stage 3 before Stage 2, confirm: "Skipping Constrain leaves the agent unbounded. Proceed?"
- **Read existing files first**: Never overwrite `AGENTS.md`, `.claude/settings.json`, or workflows. Show diff, ask, then write.

## Quick Start

User says "set up harness on this project":

1. Run Stage 1 → confirm AGENTS.md
2. Ask: "Continue to Stage 2 (permissions + hooks)?"
3. Continue stage by stage until user stops.

## Reference

- 4 pillars deep dive: [REFERENCE.md](REFERENCE.md)
- AGENTS.md template: [templates/AGENTS.md](templates/AGENTS.md)
- Settings template: [templates/settings.json](templates/settings.json)
- CI workflow template: [templates/agent-pr-checks.yml](templates/agent-pr-checks.yml)
