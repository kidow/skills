---
name: setup-harness
description: Build agent harness infrastructure (Constrain, Inform, Verify, Correct) on a project step by step. Generates AGENTS.md as the canonical rules file with a CLAUDE.md import stub, configures Claude Code permissions and a session-end verify hook, scaffolds optional CI gates, and seeds a Past Failures section for the "1 failure = 1 prevention rule" loop. Optimized for Claude Code; AGENTS.md is the cross-tool standard so OpenAI Codex reads the same file. Use when user wants to set up agent guardrails, harden an AI coding agent setup, write or improve AGENTS.md/CLAUDE.md, configure agent permissions/hooks, or asks "how do I make my agent safer", "set up harness engineering", "configure agent rules for this project".
---

# Harness Engineering Setup

Build harness in 3 stages, ordered by impact. Stop after any stage if user is satisfied — each delivers value standalone. See [REFERENCE.md](REFERENCE.md) for theory.

## Stage 1 — Inform (AGENTS.md + CLAUDE.md stub)

1. Detect project stack from `package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`.
2. Draft `AGENTS.md` (≤ 60 lines) using [templates/AGENTS.md](templates/AGENTS.md). Pre-fill **Project Stack** only.
3. Mark **Forbidden** and **Past Failures** as `# DRAFT — review required`.
4. Write `CLAUDE.md` containing one line: `@AGENTS.md` (Claude Code import directive).
5. Show diff. Require explicit confirmation before save.
   - Warn: "ETH Zurich research: LLM-generated AGENTS.md drops agent performance 3% and raises cost 20%. Past Failures must come from real incidents — leave empty if none."

**Pnpm is the standard.** AGENTS.md fixes `Package manager: pnpm`. Refuse to set otherwise.

## Stage 2 — Constrain (permissions)

1. Create `.claude/settings.json` from [templates/settings.json](templates/settings.json).
2. `permissions.allow`: read/edit/write/test/git basics.
3. `permissions.deny`: `rm -rf *`, `curl *`, `wget *`, `sudo *`, `chmod 777 *`, `git push --force *`, `Read(.env*)`, `Read(**/secrets/**)`.
4. No `PreToolUse` hooks. `permissions.deny` is the single defense layer for dangerous commands.

## Stage 3 — Verify (Stop hook required, CI optional)

Pick one variant from [templates/settings.json](templates/settings.json):

- **lite** (default): Stop hook runs `pnpm lint` once at session end.
- **strict**: Stop hook runs `pnpm lint && pnpm typecheck && pnpm test --run`.

Never use `PostToolUse` to run tests/typecheck — runs on every edit, kills throughput.

**Optional**: Scaffold `.github/workflows/agent-pr-checks.yml` from [templates/agent-pr-checks.yml](templates/agent-pr-checks.yml). Hooks give immediate feedback per session. CI is the merge gate.

## Correct (no extra files)

Failure handling lives inside AGENTS.md `Past Failures` and the workflow rule:

- After any agent mistake, ask user: "Add a one-line prevention rule to Past Failures?"
- On repeated failure, restart in a clean context (new session). Do not patch forward.

No edit-count hook, no automated doom-loop counter — agents do not self-track edits, and a hook adds maintenance with little real-world payoff. Add later only after observing repeated incidents.

## Operating Rules

- **60-line rule**: AGENTS.md ≤ 60 lines. To add a line, remove a line.
- **Failure → rule**: every confirmed agent mistake earns one Past Failures line.
- **Read before write**: never overwrite `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json`, or workflows. Show diff, ask, then write.
- **Stage skip warning**: if user wants Stage 3 before Stage 2, confirm: "Skipping Constrain leaves the agent unbounded. Proceed?"

## Quick Start

User says "set up harness on this project":

1. Run Stage 1 → confirm AGENTS.md + CLAUDE.md.
2. Ask: "Continue to Stage 2 (permissions)?"
3. Continue stage by stage until user stops.

## Reference

- 4 pillars deep dive: [REFERENCE.md](REFERENCE.md)
- AGENTS.md template: [templates/AGENTS.md](templates/AGENTS.md)
- CLAUDE.md import stub: [templates/CLAUDE.md](templates/CLAUDE.md)
- Settings template (lite + strict): [templates/settings.json](templates/settings.json)
- CI workflow template: [templates/agent-pr-checks.yml](templates/agent-pr-checks.yml)
