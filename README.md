# Agent Skills

A collection of agent skills for discovering and exploring open source packages and repositories.

## Discovery

- **find-github-repo** — Search GitHub repositories by functionality using gh CLI, iteratively refining the query until you find the right one.

  ```
  npx skills@latest add kidow/skills/find-github-repo
  ```

- **find-npm-package** — Search npm packages by functionality using the npm registry API, iteratively refining the query until you find the right one.

  ```
  npx skills@latest add kidow/skills/find-npm-package
  ```

## Agent Infrastructure

- **setup-harness** — Build agent harness infrastructure (Constrain, Inform, Verify, Correct) on a project step by step. Generates AGENTS.md, configures Claude Code permissions and hooks, scaffolds CI gates, adds doom-loop prevention.

  ```
  npx skills@latest add kidow/skills/setup-harness
  ```

## Install all skills

```
npx skills@latest add kidow/skills
```
