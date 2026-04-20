---
name: cleaver
description: >
  Reverse-engineer ANY product (digital or physical) into actionable prompts for vibe coding,
  PRDs, design briefs, or service blueprints. Trigger when someone wants to deconstruct, reverse
  engineer, break down, or learn from any product — website, app, CLI, game, API, AI product,
  service, or physical object. Also use when they share a screenshot/URL/code and want the prompts
  behind it, or ask "how was this made?" — even without saying "reverse engineer."
  DO NOT trigger for: direct coding tasks ("implement X", "build a login page"), code review,
  bug fixing, or general product strategy advice. This skill is for DECONSTRUCTION, not construction.
---

# Cleaver

Take any finished product, cleave it into the prompts that built it.

Output can be code prompts (vibe coding), PRD prompts, design briefs, or service blueprints —
whatever the user needs. You're not just writing prompts — you're teaching the user how to think
in prompts. The goal is that eventually they won't need this skill anymore.

## Paths & Foundation

After Phase 2, choose a path. Tell the user which path you picked and why.

| Path | Prompts | For | Trade-off |
|------|---------|-----|-----------|
| **Minimal** | 1 (2-3 sentences) | "Just give me the soul" | Max freedom, relies on user's taste |
| **Fast Track** | 2-3 (~30 min) | "I want something working now" | Ambitious first prompt, then refine |
| **Standard Build** | 5-8 | "I want to recreate this" | Thorough but more to manage |
| **Learning Deep-Dive** | 5-10 (annotated) | "Teach me how to think in prompts" | Verbose but maximum educational value |

**Foundation Prompt (Prompt 0) — always included.** Before any feature prompt, generate one
"setup" prompt establishing the project's DNA: tech stack, directory structure, architecture,
base styles, config, conventions, and a "done" condition. This prevents every subsequent prompt
from re-establishing context and keeps things consistent.

Example: "做一个项目管理工具，核心是'不挡路' — 打开就用，键盘搞定一切。React + Tailwind，不要组件库。"

## The Workflow

### Phase 1: Understand what the user brought you

Each input type needs a different lens. For detailed domain-specific analysis, read
`references/domain-strategies.md`.

- **Screenshot / image** — Visual hierarchy, component inventory, typography, colors, spacing, interaction hints
- **URL / live website** — Info architecture, navigation, key interactions, responsive behavior, tech stack clues
- **Code / repo** — README → entry point → data model → directory structure → config → tests
- **Verbal description** — Extract core idea, probe for what caught their attention and what they'd change
- **Design file** — Component hierarchy, design tokens, repeating patterns, state variations
- **A specific feature** — Isolate trigger → change → transition
- **A game** — MDA framework: core loop, target emotions, progression, game feel, balance
- **An AI product** — System prompt architecture, context pipeline, model strategy, guardrails
- **A physical product** — First impression, interaction loop, sensory profile, materials, user journey

Don't rush this. Misunderstanding the product = garbage prompts.

### Phase 2: Understand what the user wants

**Infer what you can, only ask what you can't.** "拆解 Stripe" in Claude Code → code prompts.
"教我怎么写 prompt" → learning material. Skip the obvious.

When ambiguous, ask:
1. **Purpose** — Learn? Recreate? Remix?
2. **Output type** — Code (default), PRD, design brief, service blueprint
3. **Depth** — "最少的话" = Minimal, "完整拆解" = Standard Build

**Always ask:**
4. **Soul question** — "如果只能保留一个特点，你会选什么？" Can't be inferred.
5. **What would you change?** — Reveals taste, unlocks remix.

### Phase 3: Deconstruct

Cleave the project into layers. Think like the product manager who built this — what decisions
did they make, in what order?

Use the 6-layer framework: **Foundation → Structure → Visual Design → Interaction → Polish → Data**.
Not every layer applies. Adapt the order per domain:

- **Games**: Replace Visual with "Core Loop & Feel", add "Balance & Numbers"
- **APIs**: Replace Visual with "API Surface", replace Interaction with "Operational Contracts"
- **AI Products**: Add "System Prompt Architecture" and "Context Pipeline" layers

For the full framework with prompt templates per layer, read `references/prompt-patterns.md`.

### Phase 4: Write the prompts

Write like you're describing the feature to a colleague over coffee, not writing a spec.
**Destination, not route** — "Make a sidebar that slides in" beats "Use CSS transform translateX".

Key principles:
- **Reference real things** — "Think Stripe's landing page energy" conveys more than abstract descriptions
- **Include a "done" condition** — "You'll know it's working when you see..."
- **Include a not-to-do** — "Don't add authentication yet" prevents scope creep
- **Make them composable** — Each prompt works alone but builds on previous ones

Use this format for each prompt:

```
### Prompt [N]: [What this builds]

> [The actual prompt text — ready to copy-paste]

**What this adds:** [What this step contributes]
**Why this prompt works:** [The technique used — especially for learning]
**Pro tip:** [Optional vibe coding insight]
```

For 12 specialized prompt patterns (Spec-driven, Iterative chain, Test-first, PRD generator,
GDD generator, API contract, etc.), read `references/prompt-patterns.md`.

### Quality Gate

Check every prompt before delivery:

1. Non-technical person could understand it? (unless user asked for technical)
2. Describes destination, not route?
3. Works on its own?
4. Has a "done" condition?
5. Has a not-to-do?
6. Is the simplest version? (remove any sentence you can without losing quality)
7. Explains why? (especially for learning)

Wrap up with: overview paragraph → numbered prompts → suggested order vs alternatives → next steps.

## Edge Cases

- **Incomplete input** — Work with what you have, note what you're guessing
- **Massive project** — Ask which feature they care about, focus there
- **User's own work** — Interview them about their decisions, translate to prompts
- **Multiple products** — Identify cross-product patterns, synthesize the best ideas
- **Remix ("X but for Y")** — Don't just clone X. Deconstruct X's soul, map patterns to Y's domain, identify Y-specific constraints. Output should feel like a new product inspired by X
- **"I just want to learn vibe coding"** — Pick a well-known product they use daily, walk through as tutorial

## Known Pitfalls

- **Over-deconstructing simple products** — A login page doesn't need 8 prompts
- **Skipping Phase 2** — "Deconstruct Stripe" could mean learn API design or build payments — totally different outputs
- **Missing the soul** — Linear = "keyboard-first speed", Notion = "blocks as LEGO", Stripe = "developer is user". Name it explicitly
- **Foundation Prompt bloat** — Keep it lean (stack, structure, styles, conventions). No feature implementation
