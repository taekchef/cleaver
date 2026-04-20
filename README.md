<h1 align="center">Cleaver <sup><code>牛刀</code></sup></h1>

<p align="center"><strong>Take any product, cleave it into the prompts that built it.</strong></p>

<p align="center">
  A <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code skill</a> that reverse-engineers products into actionable prompts for vibe coding, PRDs, design briefs, and service blueprints.
</p>

<p align="center">
  <strong>English</strong> | <a href="./README.zh-CN.md">中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/tested-16_scenarios-green" />
  <img src="https://img.shields.io/badge/dimensions-12-blue" />
  <img src="https://img.shields.io/badge/with_Cleaver-82%25_pass_rate-brightgreen" />
  <img src="https://img.shields.io/badge/without-34%25_pass_rate-lightgrey" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
</p>

> Cleaver does not claim to know the original prompts, specs, or internal decisions behind a product.
> It turns observable product decisions and explicit assumptions into rebuildable prompts.

---

## Why Cleaver?

Vibe coding is powerful, but most people struggle with **writing good prompts**. They either:
- Write vague prompts ("make a dashboard") → generic output
- Write over-specified prompts ("use CSS grid with 3 columns...") → fight with the AI

Cleaver solves this by studying products that already work — extracting the **prompts that would have built them**. You learn by reverse-engineering the best.

### Bad prompt vs. Cleaver prompt

```
Bad:
> Make a dashboard like Linear.

Why it fails:
- Copies surface style but misses speed, keyboard flow, issue triage, and state transitions.
- No scope boundary, no "done" condition, no soul.

Cleaver:
> Build an issue tracker whose core promise is "nothing slows you down".
> The first screen is an inbox-like issue list, keyboard-first, with instant command palette,
> fast status changes, and no modal-heavy editing. Done when a user can create, assign,
> prioritize, and close an issue without touching the mouse.
> Do not add roadmap, docs, chat, or analytics yet.
```

---

## Proof it works

### 16-Scenario Benchmark

16 test scenarios, graded on up to 12 quality dimensions. Green = with Cleaver, Orange = with Cleaver (new scenarios), Gray = without.

<img src="./docs/benchmark.svg" alt="benchmark comparison chart" width="100%" />

**Key numbers:**
- With Cleaver: **82%** average pass rate | Without: **34%** | **+48pp improvement**
- 3 new scenarios scored **100%** with Cleaver (Landing Page, Web App, Remix)
- Biggest gains: CLI Tool (+78pp), Design System (+67pp), Landing Page / Web App (+67pp)

> Methodology: each scenario was run with and without the skill active, graded by Claude against
> a 12-dimension rubric covering product analysis, prompt quality, scope control, and teaching value.

### 12 Quality Dimensions

<img src="./docs/dimensions.svg" alt="dimension coverage chart" width="100%" />

**Where Cleaver adds the most:**

| Dimension | With Cleaver | Without | Gap |
|-----------|-------------|---------|-----|
| Why Annotations (teaching) | 15/16 (94%) | 0/16 (0%) | **+94pp** |
| Not-To-Do (scope control) | 16/16 (100%) | 6/16 (38%) | **+63pp** |
| Done Criteria (acceptance) | 8/16 (50%) | 0/16 (0%) | **+50pp** |
| Pro Tips (practical insight) | 12/16 (75%) | 3/16 (19%) | **+56pp** |
| Build Order (sequencing) | 10/16 (63%) | 1/16 (6%) | **+56pp** |
| Soul Capture (core identity) | 16/16 (100%) | 7/16 (44%) | **+56pp** |
| Destination Not Route * | 3/3 (100%) | 0/3 (0%) | **+100pp** |
| Usage Guidance * | 3/3 (100%) | 0/3 (0%) | **+100pp** |

*\* New dimensions, tested on 3 additional scenarios*

---

## What it does

Give Cleaver **any product** — a screenshot, a URL, a code repo, a verbal description, even a physical object — and it will:

1. **Analyze** the product's architecture, design decisions, and soul (separating observed facts from inferred intent)
2. **Deconstruct** it into layers (foundation, structure, visual, interaction, data)
3. **Generate** copy-paste-ready prompts you can use to recreate or learn from it

It adapts to **what you want**:
- Vibe coding prompts (build it)
- PRD prompts (spec it)
- Design briefs (design it)
- Service blueprints (operate it)
- Learning material (understand it)

## 5 Paths

| Path | Prompts | Time | Best for | Prompt 0? |
|------|---------|------|----------|-----------|
| **Minimal** | 1 (2-3 sentences) | instant | "Just give me the soul" | No |
| **Fast Track** | 2-3 | ~30 min | "I want something working now" | Yes |
| **Standard Build** | 5-8 | hours | "I want to recreate this" | Yes |
| **Learning Deep-Dive** | 5-10 (annotated) | hours | "Teach me how to think in prompts" | Yes |

## 10 Domains

| | | | | |
|---|---|---|---|---|
| Web App / SaaS | Mobile App | Landing Page | Animation | CLI Tool |
| Design System | Game | API / Backend | AI Product | Service / Physical |

Each domain has its own analysis framework — games use MDA, APIs use contract-driven design, AI products use system prompt architecture, services use blueprint methodology.

---

## Install

```bash
npx skills add taekchef/cleaver
```

Then in Claude Code, just say what you want to deconstruct:

```
> 拆解 Stripe 的 API 设计理念
> Deconstruct Figma — I want to build something similar in 30 minutes
> 帮我用最少的话拆解 Notion
> Break down the iOS delete-app wiggle animation
```

## Examples

### Minimal Path — Notion (3 sentences)

```
做一个"万物皆 block"的工作空间：每一段文字、每一张图、每一行数据库都是同一颗原子积木，
可以嵌套、拖拽、变形、关联——像乐高一样拼出笔记、文档、看板、日历、Wiki 任何形态。
打开是一张白纸，干净到没有存在感，但底层是一个图结构的数据库引擎，
让个人和团队在同一块画布上实时协作、自定义任何工作流。
不要做固定模板的 SaaS，要做用户自己造工具的平台——Notion 卖的不是功能，是"你可以自己搭"的创造力。
```

### Fast Track — "Tinder for restaurants" (verbal-only, 3 prompts)

User says: "全屏卡片左右滑选餐厅" — Cleaver infers the product archetype, identifies it as a "decision fatigue killer", and generates a Foundation Prompt + 2 feature prompts for a React Native swipe-card app.

→ [Full output](examples/tinder-restaurant.md)

### Standard Build — Stripe API (6 prompts)

Full API design teardown: philosophy, data model, API surface (CRUD five-tuple, cursor pagination, expand), operational contracts (idempotency, webhook signatures), error model (three-layer classification with doc_url), and developer experience design.

→ [Full output](examples/stripe-api.md)

---

## How it works

```
Input                Analysis              Output
─────────────────────────────────────────────────────
Screenshot  ──┐
URL          ──┤
Code/repo    ──┼──► Phase 1: Understand ──► Phase 3: Deconstruct
Verbal desc  ──┤    Phase 2: What user    (6-layer framework +
Design file  ──┤             wants         domain overrides)
Physical obj ──┘    (infer, don't ask)
                                         ► Phase 4: Write prompts
                                           (12 prompt patterns)
                                         ► Quality Gate (path-specific)
```

**12 prompt patterns**: Intent-first, Spec-driven, Iterative chain, Not-to-dos, Example-driven, Test-first, PRD generator, Design brief, Experience-to-Spec, GDD generator, System prompt, API contract. See [`references/prompt-patterns.md`](references/prompt-patterns.md).

## Architecture

```
cleaver/
├── SKILL.md                    # Main skill (190 lines)
├── README.md                   # This file
├── README.zh-CN.md             # Chinese README
├── LICENSE                     # MIT
├── evals/
│   ├── benchmark.json          # Aggregated eval results
│   ├── rubric.md               # 12-dimension scoring criteria
│   └── build_benchmark.py      # Reads grading JSONs, outputs benchmark.json
├── docs/
│   ├── benchmark.svg           # 16-scenario comparison chart
│   ├── dimensions.svg          # 12-dimension coverage chart
│   └── generate_charts.py      # Reads benchmark.json → generates SVGs
├── references/
│   ├── domains/
│   │   ├── digital-products.md    # Web/SaaS, Landing Page, Mobile
│   │   ├── developer-products.md  # CLI, API/Backend
│   │   ├── creative-systems.md    # Game, Animation, Design System
│   │   ├── ai-products.md         # AI/ML Products
│   │   └── physical-services.md   # Physical products & services
│   └── patterns/
│       ├── build-prompts.md       # Patterns 1-6 (Intent-first, Spec-driven, etc.)
│       ├── product-docs.md        # Patterns 7-10 (PRD, Design Brief, GDD, etc.)
│       └── technical-contracts.md # Patterns 11-12 (System Prompt, API Contract)
└── examples/
    ├── stripe-api.md           # API/Backend — Standard Build
    ├── tinder-restaurant.md    # Verbal-only — Fast Track
    └── notion-minimal.md       # Minimal Path — 3 sentences
```

---

## Responsible Use

Cleaver is for learning, inspiration, legitimate remixing, and product understanding.
Do not use it to copy proprietary assets, impersonate brands, bypass access controls,
or clone products in ways that violate licenses, terms, or user trust.

When remixing a real product, preserve the lesson, not the identity.
Extract patterns, interaction principles, and architectural decisions —
avoid copying names, branding, proprietary content, or private implementation details.

---

## License

MIT
