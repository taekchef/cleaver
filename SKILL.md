---
name: cleaver
description: >
  Reverse-engineer any product into source-aware prompts, PRDs, design briefs, or service blueprints.
  Trigger when someone wants to deconstruct, break down, learn from, remix, or understand a finished
  product — website, app, CLI, game, API, AI product, service, or physical object. Also use when
  they share a screenshot/URL/code and ask "how was this made?" — even without saying "reverse engineer."
  Do NOT trigger for: direct coding tasks, code review, bug fixing, or general strategy advice without
  a product to deconstruct.
---

# Cleaver / 牛刀

Take any finished product, cleave it into the prompts that built it.

Output can be code prompts (vibe coding), PRD prompts, design briefs, or service blueprints —
whatever the user needs. You're not just writing prompts — you're teaching the user how to think
in prompts. The goal is that eventually they won't need this skill anymore.

Cleaver does not claim to know the original prompts or internal decisions behind a product.
It turns observable product decisions and explicit assumptions into rebuildable prompts.

## Paths & Foundation

After Phase 2, choose a path. Tell the user which path you picked and why.

| Path | Prompts | For | Trade-off |
|------|---------|-----|-----------|
| **Minimal** | 1 (2-3 sentences) | "Just give me the soul" | Max freedom, relies on user's taste |
| **Fast Track** | 2-3 (~30 min) | "I want something working now" | Ambitious first prompt, then refine |
| **Standard Build** | 5-8 | "I want to recreate this" | Thorough but more to manage |
| **Learning Deep-Dive** | 5-10 (annotated) | "Teach me how to think in prompts" | Verbose but maximum educational value |

**Foundation Prompt (Prompt 0).** Generates a "setup" prompt establishing the project's DNA:
tech stack, directory structure, architecture, base styles, config, conventions, and a "done"
condition. This prevents every subsequent prompt from re-establishing context.

Example: "做一个项目管理工具，核心是'不挡路' — 打开就用，键盘搞定一切。React + Tailwind，不要组件库。"

| Path | Prompt 0? | Why |
|------|-----------|-----|
| Minimal | No | User wants the soul, not a build plan |
| Fast Track | Yes | Quick prototype needs unified DNA |
| Standard Build | Yes | Full build needs consistent foundation |
| Learning Deep-Dive | Yes | Teaching needs context for each prompt |
| PRD / brief / blueprint | Use "Product DNA" summary instead | Document output ≠ build output |

## The Workflow

### Phase 1: Understand what the user brought you

Separate what you **saw** from what you **inferred**:
- **Observed**: Visible in the screenshot, repo, URL, or user-provided description
- **Inferred**: Product intent, constraints, likely architecture, design philosophy
- **Prompt translation**: How observations + inferences become prompts

If the source can't be fully inspected, say so and proceed from explicit assumptions.
Do not claim to know private roadmaps, internal prompts, or proprietary implementation details.

Each input type needs a different lens. For detailed domain-specific analysis, read
only the relevant domain file:

- Web/SaaS/Mobile/Landing Page → `references/domains/digital-products.md`
- CLI/API/Backend → `references/domains/developer-products.md`
- Game/Animation/Design System → `references/domains/creative-systems.md`
- AI Product → `references/domains/ai-products.md`
- Physical Product/Service → `references/domains/physical-services.md`

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
"教我怎么写 prompt" → learning material. "最少的话" → Minimal. Skip the obvious.

Proceed without asking when the path, product, and output type are clear from context.
Only ask when the answer materially changes the output:

1. **Purpose** — Learn? Recreate? Remix? (only when ambiguous)
2. **Soul question** — "如果只能保留一个特点，你会选什么？" (can't be inferred)
3. **What would you change?** — Reveals taste, unlocks remix

If proceeding without answers, state assumptions at the top of your output.

### Phase 3: Deconstruct

Cleave the project into layers. Think like the product manager who built this — what decisions
did they make, in what order?

Use the 6-layer framework: **Foundation → Structure → Visual Design → Interaction → Polish → Data**.
Not every layer applies. Adapt the order per domain:

- **Games**: Replace Visual with "Core Loop & Feel", add "Balance & Numbers"
- **APIs**: Replace Visual with "API Surface", replace Interaction with "Operational Contracts"
- **AI Products**: Add "System Prompt Architecture" and "Context Pipeline" layers

For the full framework with prompt templates per layer, read the relevant pattern file:

- Build prompts → `references/patterns/build-prompts.md`
- Product docs (PRD, brief, GDD) → `references/patterns/product-docs.md`
- Technical contracts (system prompt, API spec) → `references/patterns/technical-contracts.md`

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
GDD generator, API contract, etc.), read `references/patterns/build-prompts.md` (patterns 1-6),
`references/patterns/product-docs.md` (patterns 7-10), or `references/patterns/technical-contracts.md`
(patterns 11-12).

### Quality Gate — per path

**Minimal:**
- Captures the product soul in 2-3 sentences
- Names the main user experience, not just a feature inventory
- May include one boundary or anti-pattern if it fits naturally
- Does NOT force Prompt 0, done condition, or build order

**Fast Track:**
- Includes Prompt 0
- Each feature prompt has a done condition and at least one not-to-do
- The sequence can produce a working prototype in one sitting

**Standard Build:**
- Includes Prompt 0
- Each prompt is standalone, copy-paste-ready, and scoped
- Each prompt has a done condition and not-to-do
- Build order is explicit
- Output distinguishes observed facts from inferred product intent

**Learning Deep-Dive:**
- All Standard Build checks pass
- Explains why each prompt works (the technique, not just what it does)
- Shows at least one bad-prompt → Cleaver-prompt transformation when useful

All paths: wrap up with overview → numbered prompts → suggested order vs alternatives → next steps.

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

## Responsible Use

Cleaver is for learning, inspiration, legitimate remixing, and product understanding.
Do not use it to copy proprietary assets, impersonate brands, bypass access controls,
or clone products in ways that violate licenses, terms, or user trust.

When remixing a real product, preserve the lesson, not the identity.
Extract patterns, interaction principles, and architectural decisions —
avoid copying names, branding, proprietary content, or private implementation details.
