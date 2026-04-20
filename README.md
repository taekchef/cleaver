<h1 align="center">Cleaver</h1>

<p align="center"><strong>Take any product, cleave it into the prompts that built it.</strong></p>

<p align="center">
  A <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code skill</a> that reverse-engineers products into actionable prompts for vibe coding, PRDs, design briefs, and service blueprints.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/tested-13_scenarios-green" />
  <img src="https://img.shields.io/badge/pass_rate-100%25-brightgreen" />
  <img src="https://img.shields.io/badge/domains-10-blue" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
</p>

---

## What it does

Give Cleaver **any product** — a screenshot, a URL, a code repo, a verbal description, even a physical object — and it will:

1. **Analyze** the product's architecture, design decisions, and soul
2. **Deconstruct** it into layers (foundation, structure, visual, interaction, data)
3. **Generate** copy-paste-ready prompts you can use to recreate or learn from it

It adapts to **what you want**:
- Vibe coding prompts (build it)
- PRD prompts (spec it)
- Design briefs (design it)
- Service blueprints (operate it)
- Learning material (understand it)

## 5 Paths

| Path | Prompts | Time | Best for |
|------|---------|------|----------|
| **Minimal** | 1 (2-3 sentences) | instant | "Just give me the soul" |
| **Fast Track** | 2-3 | ~30 min | "I want something working now" |
| **Standard Build** | 5-8 | hours | "I want to recreate this" |
| **Learning Deep-Dive** | 5-10 (annotated) | hours | "Teach me how to think in prompts" |
| + **Foundation Prompt** | +1 (always) | — | Project DNA (tech stack, structure, conventions) |

## 10 Domains

Cleaver has domain-specific deconstruction strategies for:

| | | | | |
|---|---|---|---|---|
| Web App / SaaS | Mobile App | Landing Page | Animation | CLI Tool |
| Design System | Game | API / Backend | AI Product | Service / Physical |

Each domain has its own analysis framework — games use MDA, APIs use contract-driven design, AI products use system prompt architecture, services use blueprint methodology.

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
做一个万物皆 block 的协作工具。核心是"乐高式自由"——页面里嵌页面，数据库变看板，AI 随叫随到。
技术灵魂：block 为原子单元的图数据库引擎 + OT/CRDT 实时协同。
一句话：卖的不是功能，是你可以自己搭的创造力。
```

### Fast Track — "Tinder for restaurants" (verbal-only, 3 prompts)

User says: "全屏卡片左右滑选餐厅" — Cleaver infers the product archetype, identifies it as a "decision fatigue killer", and generates a Foundation Prompt + 2 feature prompts for a React Native swipe-card app.

### Standard Build — Stripe API (6 prompts)

Full API design teardown: philosophy, data model, API surface (CRUD five-tuple, cursor pagination, expand), operational contracts (idempotency, webhook signatures), error model (three-layer classification with doc_url), and developer experience design.

See [`examples/`](examples/) for complete outputs.

## How it works

```
Input                Analysis              Output
─────────────────────────────────────────────────────
Screenshot  ──┐
URL          ──┤
Code/repo    ──┼──► Phase 1: Understand ──► Phase 3: Deconstruct
Verbal desc  ──┤    Phase 2: What user    (6-layer framework +
Design file  ──┤             wants         domain overrides)
Physical obj ──┘
                                         ► Phase 4: Write prompts
                                           (12 prompt patterns)
                                         ► Quality Gate (7 checks)
```

**12 prompt patterns**: Intent-first, Spec-driven, Iterative chain, Not-to-dos, Example-driven, Test-first, PRD generator, Design brief, Experience-to-Spec, GDD generator, System prompt, API contract. See [`references/prompt-patterns.md`](references/prompt-patterns.md).

## Architecture

```
cleaver/
├── SKILL.md                          # Main skill (423 lines)
├── references/
│   ├── domain-strategies.md          # 10 domain-specific strategies (800 lines)
│   └── prompt-patterns.md            # 12 prompt pattern templates (729 lines)
└── examples/                         # Sample outputs
    ├── stripe-api.md                 # API/Backend — Standard Build
    ├── tinder-restaurant.md          # Verbal-only — Fast Track
    └── notion-minimal.md             # Minimal Path — 3 sentences
```

## Quality

Tested across 13 scenarios covering all 5 paths, 10 domains, and 2 edge cases:

- **107/107 assertions pass** (9 quality dimensions per eval)
- Every output has: product analysis, done criteria, "why this works" annotations, pro tips, build order
- Domain frameworks applied correctly: MDA for games, API Contract for backends, Service Blueprint for services, System Prompt Architecture for AI products

## License

MIT
