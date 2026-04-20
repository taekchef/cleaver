<h1 align="center">Cleaver</h1>

<p align="center"><strong>任意产品，一刀拆成构建它的 prompt。</strong></p>

<p align="center">
  一个 <a href="https://docs.anthropic.com/en/docs/claude-code/skills">Claude Code 技能</a>，把产品逆向工程为可执行的 vibe coding prompt、PRD、设计简报或服务蓝图。
</p>

<p align="center">
  <a href="./README.md">English</a> | <strong>中文</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/测试场景-16-green" />
  <img src="https://img.shields.io/badge/质量维度-12-blue" />
  <img src="https://img.shields.io/badge/使用Cleaver-82%25通过率-brightgreen" />
  <img src="https://img.shields.io/badge/未使用-34%25通过率-lightgrey" />
  <img src="https://img.shields.io/badge/license-MIT-yellow" />
</p>

---

## 为什么需要 Cleaver？

Vibe coding 很强大，但大多数人**写不出好 prompt**。要么太模糊（"做一个仪表盘"）→ 产出平庸；要么过度指定（"用 CSS grid 三列布局…"）→ 跟 AI 打架。

Cleaver 的做法是：**研究那些已经成功的产品，提取出"能构建它们的 prompt"。** 你通过逆向工程最好的产品来学习写 prompt。

就像身边坐了一个资深 prompt 工程师，跟你说："看到 Stripe 怎么处理错误了吗？这是能产出那种效果的 prompt。这是为什么它管用。这是大多数人搞错的地方。"

---

## 它能做什么？

给 Cleaver **任何产品** —— 截图、URL、代码仓库、口头描述，甚至实物 —— 它会：

1. **分析**产品的架构、设计决策和灵魂
2. **拆解**成层次（基础、结构、视觉、交互、数据）
3. **生成**可直接复制粘贴的 prompt

适应**你想要的输出**：
- Vibe coding prompt（构建它）
- PRD prompt（规划它）
- 设计简报（设计它）
- 服务蓝图（运营它）
- 学习材料（理解它）

---

## 效果验证

### 16 场景整体对比

16 个测试场景，评估最多 12 个质量维度。绿色条 = 使用 Cleaver（已有场景），橙色 = 使用 Cleaver（新增场景），灰色 = 不使用。

<img src="./docs/benchmark.svg" alt="benchmark comparison chart" width="100%" />

**关键数据：**
- 使用 Cleaver 平均通过率 **82%**，不使用 **34%**，提升 **+48 个百分点**
- 3 个新增场景使用 Cleaver 均达到 **100%**（Landing Page、Web App、Remix）
- 最大提升：CLI Tool（+78pp）、Design System / Landing Page / Web App（+67pp）

### 12 质量维度详细对比

<img src="./docs/dimensions.svg" alt="dimension coverage chart" width="100%" />

**Cleaver 价值最大的维度：**
| 维度 | 使用 Cleaver | 不使用 | 差距 |
|------|-------------|--------|------|
| Why Annotations（教学注释） | 15/16 (94%) | 0/16 (0%) | **+94pp** |
| Not-To-Do（范围控制） | 16/16 (100%) | 6/16 (38%) | **+63pp** |
| Done Criteria（完成标准） | 8/16 (50%) | 0/16 (0%) | **+50pp** |
| Pro Tips（实战洞察） | 12/16 (75%) | 3/16 (19%) | **+56pp** |
| Build Order（构建顺序） | 10/16 (63%) | 1/16 (6%) | **+56pp** |
| Soul Capture（灵魂捕捉） | 16/16 (100%) | 7/16 (44%) | **+56pp** |
| 目的地而非路线 * | 3/3 (100%) | 0/3 (0%) | **+100pp** |
| 使用建议 * | 3/3 (100%) | 0/3 (0%) | **+100pp** |

*\* 新增维度，在 3 个额外场景中测试*

---

## 5 种路径

| 路径 | Prompt 数 | 耗时 | 适合 |
|------|-----------|------|------|
| **极简** | 1（2-3 句话） | 即时 | "只给我灵魂" |
| **快速** | 2-3 | ~30 分钟 | "我现在就要能用的东西" |
| **标准构建** | 5-8 | 数小时 | "我要复刻这个" |
| **学习深潜** | 5-10（带注释） | 数小时 | "教我怎么用 prompt 思考" |
| + **基础 Prompt** | +1（始终包含） | — | 项目 DNA（技术栈、结构、规范） |

---

## 10 个领域

| | | | | |
|---|---|---|---|---|
| Web App / SaaS | Mobile App | Landing Page | Animation | CLI Tool |
| Design System | Game | API / Backend | AI Product | Service / 实体产品 |

每个领域有专属拆解策略——游戏用 MDA 框架，API 用契约驱动设计，AI 产品用系统 prompt 架构，服务用蓝图方法论。

### 测试覆盖

| 领域 | 测试场景 | 通过率 |
|------|---------|--------|
| AI Product | System prompt 架构 + context pipeline | 8/9 (89%) |
| Animation | iOS 删除 app 抖动动画 | 6/9 (67%) |
| API / Backend | Stripe API 设计理念 | 7/9 (78%) |
| CLI Tool | Rust 命令行代理工具 | **9/9 (100%)** |
| Design System | 设计系统 + 组件库 | 8/9 (89%) |
| Game | 游戏核心循环 + MDA | 8/9 (89%) |
| Mobile App | Tinder 式滑卡餐厅 App | 8/9 (89%) |
| Service | Dyson 吹风机实体产品 | 7/9 (78%) |
| **Landing Page** | Vercel 首页拆解 | **12/12 (100%)** |
| **Web App / SaaS** | Linear 项目管理工具 | **12/12 (100%)** |
| **Remix** | Uber → 遛狗 App 跨域映射 | **12/12 (100%)** |
| **Learning Path** | 带"为什么"注释的完整拆解 | **9/9 (100%)** |
| Verbal Only | 口头描述 → 推断产品 | 6/9 (67%) |

---

## 安装

```bash
npx skills add taekchef/cleaver
```

然后在 Claude Code 里直接说你想拆什么：

```
> 拆解 Stripe 的 API 设计理念
> Deconstruct Figma — I want to build something similar in 30 minutes
> 帮我用最少的话拆解 Notion
> Break down the iOS delete-app wiggle animation
```

---

## 示例

### 极简路径 — Notion（3 句话）

```
做一个"万物皆 block"的工作空间：每一段文字、每一张图、每一行数据库都是同一颗原子积木，
可以嵌套、拖拽、变形、关联——像乐高一样拼出笔记、文档、看板、日历、Wiki 任何形态。
打开是一张白纸，干净到没有存在感，但底层是一个图结构的数据库引擎，
让个人和团队在同一块画布上实时协作、自定义任何工作流。
不要做固定模板的 SaaS，要做用户自己造工具的平台——Notion 卖的不是功能，是"你可以自己搭"的创造力。
```

### 快速路径 — "Tinder for restaurants"（3 个 prompt）

用户说："全屏卡片左右滑选餐厅"——Cleaver 推断产品原型，识别为"决策疲劳杀手"，生成 1 个 Foundation Prompt + 2 个功能 Prompt。

→ [完整输出](examples/tinder-restaurant.md)

### 标准构建 — Stripe API（6 个 prompt）

完整的 API 设计拆解：哲学、数据模型、API Surface（CRUD 五件套、游标分页、expand）、运营契约（幂等性、webhook 签名）、错误模型（三层分类 + doc_url）、开发者体验设计。

→ [完整输出](examples/stripe-api.md)

---

## 工作原理

```
输入                分析                输出
──────────────────────────────────────────────────
截图    ──┐
URL     ──┤
代码仓库 ──┼──► Phase 1: 理解产品 ──► Phase 3: 拆解
口头描述 ──┤    Phase 2: 理解用户     （6 层框架 +
设计文件 ──┤              想要什么     领域定制）
实体产品 ──┘
                                ► Phase 4: 写 prompt
                                  （12 种 prompt 模式）
                                ► 质量门禁（7 项检查）
```

**12 种 prompt 模式**：Intent-first、Spec-driven、Iterative chain、Not-to-dos、Example-driven、Test-first、PRD generator、Design brief、Experience-to-Spec、GDD generator、System prompt、API contract。详见 [`references/prompt-patterns.md`](references/prompt-patterns.md)。

---

## 文件结构

```
cleaver/
├── SKILL.md                    # 主技能（140 行）
├── README.md                   # English README
├── README.zh-CN.md             # 中文 README（本文件）
├── LICENSE                     # MIT
├── docs/
│   ├── benchmark.svg           # 16 场景对比图
│   ├── dimensions.svg          # 12 维度对比图
│   └── generate_charts.py      # 图表生成脚本
├── references/
│   ├── domain-strategies.md    # 10 领域策略（800 行）
│   └── prompt-patterns.md      # 12 种 prompt 模式（744 行）
└── examples/
    ├── stripe-api.md           # API/Backend — 标准构建
    ├── tinder-restaurant.md    # 口头描述 — 快速路径
    └── notion-minimal.md       # 极简路径 — 3 句话
```

---

## License

MIT
