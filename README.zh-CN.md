<h1 align="center">牛刀</h1>

<p align="center"><strong>任意产品，一刀拆成能重建它的 prompt。</strong></p>

<p align="center">
一个 <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code 技能</a>，把成品逆向工程为可执行的 vibe coding prompt。
</p>

<p align="center">
<strong>中文</strong> · <a href="./README.md">English</a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/测试场景-17-green" />
<img src="https://img.shields.io/badge/质量维度-12-blue" />
<img src="https://img.shields.io/badge/使用牛刀-85%25通过率-brightgreen" />
<img src="https://img.shields.io/badge/未使用-32%25通过率-lightgrey" />
<img src="https://img.shields.io/badge/license-MIT-yellow" />
</p>

> **牛刀不读心。** 它读产品。
> 可观察的决策、显式的假设、可重建的 prompt。
> 没有泄露的内部信息，没有声称的秘密。

---

## "做个像 Linear 的仪表盘" —— 为什么不行

```
❌  Make a dashboard like Linear.

    → 抄了壳，丢了引擎。
    → 没有速度哲学，没有键盘流，没有灵魂。
    → 做出来长得像 Linear，用起来像 Jira。

✅  做一个 issue tracker，核心承诺是"不让你慢下来"。
    首屏是 inbox 式列表，键盘优先，即时命令面板，不要模态编辑。
    完成标准：不用鼠标就能完成创建、分配、排优先级、关闭。
    不要加：roadmap、文档、聊天、分析。
```

大多数 vibe coding 不是死在代码上，是死在 prompt 上。
牛刀研究已经成功的产品——提取出"能构建它们的 prompt"。

---

## 什么都能拆

给它**任何成品** —— 它给你能重建它的 prompt。

| 输入 | 输出 |
|------|------|
| 截图 | 逐层视觉拆解 → 构建 prompt |
| URL | 在线产品分析 → 范围明确的重建 prompt |
| 代码仓库 | 架构提取 → spec + 构建链 |
| 口头描述 | 产品原型推断 → 原型 prompt |
| 单个功能 | 触发 → 变化 → 过渡 → prompt |
| 实体产品 | 感官 + 交互画像 → 体验 spec |

**输出模式** — vibe coding prompt、PRD、设计简报、服务蓝图、或引导式学习材料。

---

## 17 场景。85% 通过率。

<img src="./docs/benchmark.svg" alt="benchmark comparison chart" width="100%" />

| 指标 | 使用牛刀 | 未使用 | 差距 |
|------|---------|--------|------|
| 平均通过率 | **85%** | 32% | **+53pp** |
| 灵魂捕捉 | 17/17 (100%) | 7/17 (41%) | +59pp |
| 范围控制 | 17/17 (100%) | 6/17 (35%) | +65pp |
| 教学注释 | 16/17 (94%) | 0/17 (0%) | +94pp |

<img src="./docs/dimensions.svg" alt="dimension coverage chart" width="100%" />

> 每个场景按 12 个维度评分：产品分析、prompt 质量、范围控制、构建顺序、领域框架、教学价值等。完整评分标准见 [`evals/rubric.md`](evals/rubric.md)。

---

## 四条路径。选你的深度。

| 路径 | Prompt 数 | 耗时 | 适合 |
|------|-----------|------|------|
| **极简** | 1（2-3 句话） | 即时 | "只要灵魂" |
| **快速** | 2-3 | ~30 分钟 | "今晚就要能跑的" |
| **标准构建** | 5-8 | 数小时 | "完整复刻" |
| **学习深潜** | 5-10（带注释） | 数小时 | "教我用 prompt 思考" |

每条路径（除极简外）都以 **Prompt 0** 开头——一个 foundation prompt，建立项目 DNA（技术栈、结构、约定、完成标准），让后续每个 prompt 都在基础上累加，而不是重新交代背景。

---

## 十个领域。十套框架。

| | | | | |
|---|---|---|---|---|
| Web App / SaaS | Mobile App | Landing Page | 动画 | CLI Tool |
| Design System | 游戏 | API / Backend | AI 产品 | 服务 / 实体 |

游戏用 MDA 框架。API 用契约驱动。AI 产品用系统 prompt 架构。每个领域有自己的透镜——一种框架不能套所有。

---

## 安装

```bash
npx skills add taekchef/cleaver
```

然后在 Claude Code 里说你想拆什么：

```
> 拆解 Stripe 的 API 设计理念
> Deconstruct Figma — I want to build something similar in 30 minutes
> 帮我用最少的话拆解 Notion
> Break down the iOS delete-app wiggle animation
```

---

## 示例

### 极简 — Notion 三句话

```
做一个"万物皆 block"的工作空间：每一段文字、每一张图、每一行数据库都是同一颗原子积木，
可以嵌套、拖拽、变形、关联——像乐高一样拼出笔记、文档、看板、日历、Wiki 任何形态。
打开是一张白纸，干净到没有存在感，但底层是一个图结构的数据库引擎，
让个人和团队在同一块画布上实时协作、自定义任何工作流。
不要做固定模板的 SaaS，要做用户自己造工具的平台——Notion 卖的不是功能，是"你可以自己搭"的创造力。
```

### 快速 — Wordle（3 个 prompt，MDA 框架）

灵魂："一句话就能解释规则"。Foundation（网格+键盘）→ 游戏逻辑（含重复字母边界情况）→ 动画+分享（社交裂变引擎）。

→ [完整输出](examples/wordle-game.md)

### 标准构建 — Stripe API（6 个 prompt）

哲学 → 数据模型 → API Surface（CRUD、游标分页、expand）→ 运营契约（幂等性、webhook 签名）→ 错误模型（三层分类）→ 开发者体验。

→ [完整输出](examples/stripe-api.md)

### 学习深潜 — Perplexity（6 个带注释 prompt）

AI 产品拆解，含系统 prompt 架构分析。灵魂："每个回答都有证据"。每个 prompt 附带"为什么这样写"的教学注释。

→ [完整输出](examples/perplexity-ai-product.md)

### 快速 — "Tinder for restaurants"（口头描述，3 个 prompt）

用户说一句话——牛刀推断产品原型，识别为"决策疲劳杀手"，开始构建。

→ [完整输出](examples/tinder-restaurant.md)

---

## 工作原理

```
任何成品  ──►  读产品           ──►  拆成层          ──►  写 prompt
              （观察 + 推断）       （6 层框架，          （12 种 prompt 模式，
                                   领域定制）            路径分级门禁）
```

**12 种 prompt 模式**，三类：

| 构建 prompt | 产品文档 | 技术契约 |
|---|---|---|
| Intent-first | PRD generator | System prompt |
| Spec-driven | Design brief | API contract |
| Iterative chain | Experience-to-Spec | |
| Not-to-dos | GDD generator | |
| Example-driven | | |
| Test-first | | |

→ [`references/patterns/build-prompts.md`](references/patterns/build-prompts.md) · [`product-docs.md`](references/patterns/product-docs.md) · [`technical-contracts.md`](references/patterns/technical-contracts.md)

---

## 文件结构

```
cleaver/
├── SKILL.md                          # 主技能（~195 行）
├── evals/
│   ├── rubric.md                     # 12 维度评分标准
│   ├── benchmark.json                # 聚合结果
│   └── build_benchmark.py            # Eval → benchmark 管道
├── docs/
│   ├── benchmark.svg                 # 场景对比图
│   ├── dimensions.svg                # 维度覆盖图
│   └── generate_charts.py            # Benchmark → SVG 管道
├── references/
│   ├── domains/                      # 10 个领域策略
│   └── patterns/                     # 12 种 prompt 模式
└── examples/                         # 真实拆解输出
```

---

## 负责任地使用

用于学习、启发、和合法的 remix。
不用于复制专有资产、冒充品牌、或绕过访问控制。

**保留教训，不要保留身份。**
提取模式和原则——避免复制名称、品牌或私有实现。

---

## License

MIT
