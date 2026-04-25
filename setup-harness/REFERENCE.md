# Harness Engineering Reference

## Core formula

```
Agent = Model + Harness
```

Same model varies wildly by harness quality. TerminalBench 2.0: identical Opus 4.6 ranked 33rd vs 5th depending on harness. LangChain experiment with GPT-5.2-Codex showed 52.8% → 66.5% from harness changes alone.

## 4 Pillars

### 1. Constrain — design the action surface

Narrow the solution space to raise accuracy. Not about limiting capability.

- **Sandbox**: Firecracker MicroVM (Codex), Git worktree (Claude Code), workspace shells (Devin)
- **Allowlist permissions**: 3-tier model — Manual / Semi-Auto / Auto
- **Path restrictions**: block access outside `$PROJECT_ROOT`; never read `.env`
- **Token budget**: cap input ~500k / output ~100k per session to prevent runaway cost

### 2. Inform — precise context injection

Give a map, not an encyclopedia.

- **AGENTS.md**: 60-line golden rule. Above 60 lines → context rot kicks in
- **JIT discovery**: tools surface only on demand, not pre-loaded
- **MCP**: standard for external context. Lazy by default
- **SSoT**: repo as single source of truth. No conflicting docs

⚠ ETH Zurich finding: LLM-auto-generated AGENTS.md degrades agent performance 3% and inflates cost 20%. Humans must author Past Failures from real incidents.

### 3. Verify — automated quality gates

Probabilistic outputs require deterministic checks.

- **Lifecycle hooks**: Claude Code PostToolUse to run tests/typecheck after edits
- **CI gates**: lint, test, typecheck, security scan on every PR
- **Eval thresholds**: 95%+ pass rate required for security-sensitive tasks

### 4. Correct — failure recovery and learning

Failures must become permanent rules.

- **Doom loop detection**: stop after N repeated edits to same file
- **Ralph Loop**: restart in clean context on repeated failure, don't patch forward
- **Failure → rule**: Mitchell Hashimoto's principle — every mistake adds one prevention line

## Tool orchestration patterns

| Pattern | When |
|---------|------|
| **Router** | Input maps to clearly distinct categories (billing vs tech support) |
| **Chain** | Sequential pipeline (generate → lint → test → report) |
| **Parallel** | Independent tasks (frontend + backend refactor simultaneously) |
| **Orchestrator-SubAgent** | Complex multi-domain work; subagents act as context firewall — 99.6% token savings (50k raw → 200 token summary) |
| **Evaluator-Optimizer** | High-stakes output; separate evaluator iterates until quality threshold met |

## 5-layer security defense

1. **Prompt guardrails**: explicit behavior limits in system prompt
2. **Schema-level limits**: tool param whitelist
3. **Runtime approval**: user gate before dangerous commands
4. **Tool-level validation**: input check inside the tool
5. **Lifecycle hooks**: pre/post execution security scripts

## Platform comparison

| Platform | Constrain | Inform | Verify/Correct |
|----------|-----------|--------|----------------|
| **Claude Code** | 3-tier permissions, lifecycle hooks | CLAUDE.md hierarchy | Skills system (markdown + bundled scripts) |
| **OpenAI Codex** | Firecracker MicroVM per task | "Give the map" SSoT | Auto verify gates + doc garbage collection |
| **Cursor** | `.cursor/rules/` MDC files | Path-filtered conditional rules | IDE-integrated, real-time |
| **Devin** | Workspace sandbox (shell + editor) | — | Autonomous task execution |

## Cost optimization

- **Model tiering**: Opus for planning, Sonnet for execution. Cuts cost without quality loss.
- **JIT context**: ~70% token reduction vs pre-loading.
- **Subagent context firewall**: parent stays clean, subagent absorbs raw output.

## Implementation checklist

- [ ] AGENTS.md ≤ 60 lines, human-authored Past Failures
- [ ] One prevention rule added per real failure
- [ ] Vague directives replaced with measurable rules
- [ ] Orchestration pattern matches task shape
- [ ] JIT loading reduces tokens vs pre-load
- [ ] Eval threshold ≥ 95% for security tasks
- [ ] Ralph Loop retry path implemented
- [ ] 5-layer defense covers all dangerous tool calls
- [ ] Worktree or MicroVM isolation per task
- [ ] Model tiering applied (Opus/Sonnet split)

## Why harness is the moat

Models are commodity — swap with one API key change. Harness encodes project-specific failure history and engineering investment. Manus rebuilt their harness 5 times in 6 months before reaching production stability. Harness is the durable competitive advantage; model intelligence is rented.
