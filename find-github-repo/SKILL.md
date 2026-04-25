---
name: find-github-repo
description: Search GitHub repositories by functionality using gh CLI, iteratively refining the query until the user finds the right one. Use when user wants to find a GitHub repository, library, or tool for a specific purpose, or says things like "is there a repo that does X" or "find me a library for Y".
---

# GitHub Repository Finder

## Quick Start

Extract 2–4 keywords from user's description, then search:

```bash
gh search repos "<keywords>" --sort stars --limit 10 --json name,description,url,stargazerCount
```

## Workflow

1. **Extract keywords** — pick nouns/verbs most specific to the desired functionality
2. **Search** with `gh search repos`
3. **Present results** as list (see Output Format)
4. **Ask**: "Did you find what you were looking for? If not, what's different from what you need?"
5. **Refine** based on feedback → repeat from step 2
6. **No limit** on rounds — keep going until user confirms they found it

## Refinement Strategy

Ask one focused question per round based on what's missing:

| Situation | Question |
|-----------|----------|
| Results too generic | "What specific feature must it have?" |
| Wrong language/runtime | "What language or runtime are you targeting?" |
| Wrong category | "Is it a library, CLI tool, or framework?" |
| Too many irrelevant results | "Any keywords or features to exclude?" |
| User knows similar tools | "Do you know a similar tool — what's different about what you need?" |

Then incorporate the answer into the next search query.

## gh Search Options

```bash
# Basic
gh search repos "<query>" --sort stars --limit 10

# With language filter
gh search repos "<query>" --language typescript --sort stars --limit 10

# Full JSON output
gh search repos "<query>" --sort stars --limit 10 \
  --json name,description,url,stargazerCount
```

## Output Format

Present results as:

- **owner/name** — description (⭐ N,NNN)  
  https://github.com/owner/name

Sort by star count descending. If description is empty, note "(no description)".
