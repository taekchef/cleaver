<h1 align="center">Cleaver</h1>

<p align="center"><strong>Take any product. Cleave it into the prompts that built it.</strong></p>

<p align="center">
A <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code skill</a> that reverse-engineers finished products into buildable prompts.
</p>

<p align="center">
<a href="./README.zh-CN.md">中文</a> · <strong>English</strong>
</p>

<p align="center">
<img src="https://img.shields.io/badge/scenarios-17-green" />
<img src="https://img.shields.io/badge/quality_dimensions-12-blue" />
<img src="https://img.shields.io/badge/pass_rate-85%25-brightgreen" />
<img src="https://img.shields.io/badge/without-32%25-lightgrey" />
<img src="https://img.shields.io/badge/license-MIT-yellow" />
</p>

---

> **Cleaver doesn't read minds.** It reads products.
> Observable decisions, explicit assumptions, rebuildable prompts.
> No leaked internals, no claimed secrets.

## The problem with "make it like X"

```
❌  Make a dashboard like Linear.

    → Copies the chrome, misses the engine.
    → No speed philosophy, no keyboard flow, no soul.
    → Ship something that looks like Linear but feels like Jira.

✅  Build an issue tracker whose promise is "nothing slows you down".
    Keyboard-first inbox, instant command palette, no modal editing.
    Done when you can triage 50 issues without reaching for the mouse.
    Not yet: roadmap, docs, chat, analytics.
```

Most vibe coding fails at the prompt, not the code.
Cleaver studies products that already work — and extracts the prompts that would have built them.

---

## What it cleaves

Give it **anything finished** — it hands you the prompts to rebuild it.

| Input | Output |
|-------|--------|
| Screenshot | Layer-by-layer visual deconstruction → build prompts |
| URL | Live product analysis → scoped rebuild prompts |
| Code repo | Architecture extraction → spec + build chain |
| Verbal description | Product archetype inference → prototype prompts |
| A single feature | Trigger → change → transition → prompt |
| A physical object | Sensory + interaction profile → experience spec |

**Output modes** — prompts for vibe coding, PRDs, design briefs, service blueprints, or guided learning.

---

## 17 scenarios. 85% pass rate.

<img src="./docs/benchmark.svg" alt="benchmark comparison chart" width="100%" />

| Metric | With Cleaver | Without | Delta |
|--------|-------------|---------|-------|
| Average pass rate | **85%** | 32% | **+53pp** |
| Soul capture | 17/17 (100%) | 7/17 (41%) | +59pp |
| Scope control | 17/17 (100%) | 6/17 (35%) | +65pp |
| Teaching annotations | 16/17 (94%) | 0/17 (0%) | +94pp |

<img src="./docs/dimensions.svg" alt="dimension coverage chart" width="100%" />

> Each scenario graded on 12 dimensions: product analysis, prompt quality, scope control, build order, domain framework, teaching value, and more. Full rubric in [`evals/rubric.md`](evals/rubric.md).

---

## Four paths. Pick your depth.

| Path | Prompts | Time | When |
|------|---------|------|------|
| **Minimal** | 1 (2-3 sentences) | instant | "Just the soul" |
| **Fast Track** | 2-3 | ~30 min | "Ship something tonight" |
| **Standard Build** | 5-8 | hours | "Rebuild the whole thing" |
| **Learning Deep-Dive** | 5-10 (annotated) | hours | "Teach me to think in prompts" |

Every path (except Minimal) starts with **Prompt 0** — a foundation prompt that establishes project DNA (stack, structure, conventions, done condition) so every subsequent prompt builds instead of re-establishing context.

---

## Ten domains. Ten frameworks.

| | | | | |
|---|---|---|---|---|
| Web App / SaaS | Mobile App | Landing Page | Animation | CLI Tool |
| Design System | Game | API / Backend | AI Product | Service / Physical |

Games get MDA analysis. APIs get contract-driven decomposition. AI products get system prompt architecture. Every domain has its own lens — one framework doesn't fit all.

---

## Install

```bash
npx skills add taekchef/cleaver
```

Then just describe what you want to deconstruct:

```
> 拆解 Stripe 的 API 设计理念
> Deconstruct Figma — I want to build something similar in 30 minutes
> 帮我用最少的话拆解 Notion
> Break down the iOS delete-app wiggle animation
```

---

## Examples

### Minimal — Notion in 3 sentences

```
做一个"万物皆 block"的工作空间：每一段文字、每一张图、每一行数据库都是同一颗原子积木，
可以嵌套、拖拽、变形、关联——像乐高一样拼出笔记、文档、看板、日历、Wiki 任何形态。
打开是一张白纸，干净到没有存在感，但底层是一个图结构的数据库引擎，
让个人和团队在同一块画布上实时协作、自定义任何工作流。
不要做固定模板的 SaaS，要做用户自己造工具的平台——Notion 卖的不是功能，是"你可以自己搭"的创造力。
```

### Fast Track — Wordle (3 prompts, MDA framework)

Soul: "one sentence explains the rules". Foundation (grid + keyboard) → Game logic (with duplicate-letter edge cases) → Animation + Share (the viral engine).

→ [Full output](examples/wordle-game.md)

### Standard Build — Stripe API (6 prompts)

Philosophy → Data model → API surface (CRUD, cursor pagination, expand) → Operational contracts (idempotency, webhook signatures) → Error model (three-layer classification) → Developer experience.

→ [Full output](examples/stripe-api.md)

### Learning Deep-Dive — Perplexity (6 annotated prompts)

AI product deconstruction with system prompt architecture. Soul: "every answer has evidence". Each prompt comes with a "why this works" annotation.

→ [Full output](examples/perplexity-ai-product.md)

### Fast Track — "Tinder for restaurants" (verbal-only, 3 prompts)

User says one sentence — Cleaver infers the product archetype, identifies "decision fatigue killer", and builds.

→ [Full output](examples/tinder-restaurant.md)

---

## How it works

```
Anything  ──►  Read the product  ──►  Cleave into layers  ──►  Write prompts
finished       (observe + infer)      (6-layer framework,      (12 prompt patterns,
                                      domain-specific)         path-specific gate)
```

**12 prompt patterns** across three categories:

| Build prompts | Product docs | Technical contracts |
|---|---|---|
| Intent-first | PRD generator | System prompt |
| Spec-driven | Design brief | API contract |
| Iterative chain | Experience-to-Spec | |
| Not-to-dos | GDD generator | |
| Example-driven | | |
| Test-first | | |

→ [`references/patterns/build-prompts.md`](references/patterns/build-prompts.md) · [`product-docs.md`](references/patterns/product-docs.md) · [`technical-contracts.md`](references/patterns/technical-contracts.md)

---

## Architecture

```
cleaver/
├── SKILL.md                          # The skill itself (~195 lines)
├── evals/
│   ├── rubric.md                     # 12-dimension grading criteria
│   ├── benchmark.json                # Aggregated results
│   └── build_benchmark.py            # Eval → benchmark pipeline
├── docs/
│   ├── benchmark.svg                 # Scenario comparison chart
│   ├── dimensions.svg                # Dimension coverage chart
│   └── generate_charts.py            # Benchmark → SVG pipeline
├── references/
│   ├── domains/                      # 10 domain-specific strategies
│   └── patterns/                     # 12 prompt pattern references
└── examples/                         # Real teardown outputs
```

---

## Responsible use

For learning, inspiration, and legitimate remixing.
Not for copying proprietary assets, impersonating brands, or bypassing access controls.

**Preserve the lesson, not the identity.**
Extract patterns and principles — avoid copying names, branding, or proprietary implementation.

---

## License

MIT
