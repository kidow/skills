---
name: step-by-step
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree, and drawing HTML visual references when a question is easier answered visually. Use when user wants to stress-test a plan, get grilled on their design, or mentions "step by step".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

If a question needs a UI reference — layout, spacing, hierarchy, flow, or design direction — use the `visualstorming` skill to draw an HTML reference instead of asking in text.

If the `visualstorming` skill is not installed, ask the user once whether to install it (`npx skills@latest add kidow/skills/visualstorming`). If they decline, draw the HTML reference yourself using your own judgment.
