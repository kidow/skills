[![skills.sh](https://skills.sh/b/kidow/skills)](https://skills.sh/kidow/skills)

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

## Framework Scaffolding

- **nextjs-route-scaffold** — Scaffolds Next.js App Router route files and route-level SEO metadata for a given path.

  ```
  npx skills@latest add kidow/skills/nextjs-route-scaffold
  ```

- **create-nextjs-specification** — Creates an AI-ready `spec.md` file inside a Next.js `app/` route folder for a given path.

  ```
  npx skills@latest add kidow/skills/create-nextjs-specification
  ```

## Agent Infrastructure

- **setup-harness** — Build agent harness infrastructure (Constrain, Inform, Verify, Correct) on a project step by step. Generates AGENTS.md, configures Claude Code permissions and hooks, scaffolds CI gates, adds doom-loop prevention.

  ```
  npx skills@latest add kidow/skills/setup-harness
  ```

- **perfect-prompt** — Stress-test and refine user prompts until they are specific, unambiguous, and execution-ready.

  ```
  npx skills@latest add kidow/skills/perfect-prompt
  ```

## Brand & Marketing

- **setup-aeo-geo** — Build a brand's AEO/GEO strategy step by step over a 3-phase roadmap. Measures AI answer share, builds canonical entity definition, scaffolds JSON-LD schema and monthly monitoring assets.

  ```
  npx skills@latest add kidow/skills/setup-aeo-geo
  ```

## Creative

- **songwriting** — Builds AI music generation prompts through an interview-driven songwriting workflow, producing Custom Mode-ready Title, Style, and Lyrics blocks.

  ```
  npx skills@latest add kidow/skills/songwriting
  ```

## Visual Collaboration

- **visualstorming** — Adds an optional HTML-first visual reference for brainstorming with mockups, diagrams, wireframes, and side-by-side visual choices.

  ```
  npx skills@latest add kidow/skills/visualstorming
  ```

- **step-by-step** — Interview the user relentlessly about a plan or design one question at a time, and draw `visualstorming` HTML references when a question needs a UI reference.

  ```
  npx skills@latest add kidow/skills/step-by-step
  ```

## Learning

- **teach-me** — Teach one piece of knowledge at a time about a chosen topic, following a foundational-to-advanced curriculum, advancing only when you ask, auto-saving each lesson as a committed markdown note, offering audio pronunciation aids for foreign language topics, and notifying you when a topic is fully covered.

  ```
  npx skills@latest add kidow/skills/teach-me
  ```

- **review-me** — Review knowledge already saved in the current repo by quizzing one item at a time with spaced-repetition scheduling, keeping all session state in a throwaway dot-folder that is deleted when the session ends.

  ```
  npx skills@latest add kidow/skills/review-me
  ```

- **place-me** — Run a short adaptive diagnostic to gauge how much you already know about a topic before learning it, saving a prose level summary to a git-tracked `levels.md` that teach-me reads and review-me keeps updated.

  ```
  npx skills@latest add kidow/skills/place-me
  ```

## Install all skills

```
npx skills@latest add kidow/skills
```
