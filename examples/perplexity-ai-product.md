# Perplexity — 牛刀拆解

**路径：Learning Deep-Dive** | **6 个 prompt（带注释）** | **领域：AI Product**

> 用户说"教我怎么用 prompt 思考"，选 Learning Deep-Dive。
> Perplexity 是一个 AI 搜索产品——拆它能展示 AI Product 的特殊拆解策略：
> 不只是 UI，更重要的是系统 prompt 架构和 RAG 管道。

---

## Phase 1: 理解产品

### 我观察到的

- **搜索界面**：一个搜索框，输入问题后返回带引用的回答，引用来源以编号标注
- **引用机制**：回答中的每个事实/数据后面有 `[1]`、`[2]` 等脚注，点击跳转到来源
- **来源列表**：回答下方列出所有引用的网页，带标题和 URL
- **追问能力**：回答底部有 "Ask follow-up" 输入框，可以追问
- **Pro Search**：高级搜索模式，会先理解问题再分步搜索
- **Collection**：可以把搜索线程保存为"集合"

### 我推断的

- **灵魂是"每个回答都有证据"**：不是"AI 说"，而是"证据说"。引用不是附加功能，是核心承诺
- **系统 prompt 架构**：大概率是 "搜索 → 筛选 → 综合 → 引用标注" 四步管道，而不是让 LLM 自由发挥
- **RAG 管道**：先做 query decomposition（拆问题）、再做 web search、再 rank 结果、再 feed 给 LLM 带引用生成
- **技术选型**：不像是纯浏览器端，需要服务端搜索 API + LLM + 引用对齐

### Prompt 翻译思路

Perplexity 的核心不是 UI（UI 很简单），而是 AI 管道。所以 prompt 要先建立"搜索+引用"的数据流，
再建 UI。顺序是 pipeline → UI → 追问 → 引用交互。

---

## Phase 2: 理解你想要什么

**假设：**
- **目的**：学习 AI 产品拆解 + 学会写这类 prompt
- **灵魂**："每个回答都有证据"——如果你觉得 Perplexity 的灵魂是"快速"而不是"可信"，告诉我

**为什么选 Learning Deep-Dive：** 你说要学，所以我会在每个 prompt 后面解释为什么这样写，不止是写出来。

---

## Phase 3: 拆解

**AI Product 特殊拆解层：**
- 替换 Visual 层 → "System Prompt Architecture"（AI 的"大脑"怎么工作）
- 替换 Interaction 层 → "Context Pipeline"（信息怎么流过系统）
- 新增 "Guardrails"（AI 安全边界）

**构建顺序：**
1. Foundation（技术栈 + 数据模型）
2. 搜索管道（模拟 RAG）
3. 搜索 UI
4. 引用标注交互
5. 追问线程
6. 搜索体验打磨

**Not-To-Do：**
- 不做真正的 web 搜索 API（用 mock 数据模拟）
- 不做用户认证/付费
- 不做 Pro Search 的多轮搜索
- 不做 Collection 功能
- 不做移动端

---

## Phase 4: Prompts

### Prompt 0: Foundation

> 做一个 AI 搜索工具，核心承诺是"每个回答都有证据"。用户输入问题，系统返回带引用来源的回答。
>
> React + TypeScript + Tailwind。Mock 搜索结果（不要调真实 API）。
> 数据结构：
> - SearchResult: { id, title, url, snippet }
> - Answer: { content (markdown), citations: [{ index, searchResultId, text }] }
>
> Mock 数据：5 个预设搜索查询，每个返回 3-5 个搜索结果。当用户输入匹配预设关键词时返回对应结果，否则返回通用结果。
>
> Done when：输入一个查询，看到 mock 搜索结果和带引用的 mock 回答。

**What this adds:** 项目 DNA——数据模型定义了整个产品的形状。SearchResult + Answer + Citation 是 Perplexity 的骨骼。
**Why this prompt works:** 先定义数据模型再写 UI，是 Spec-driven 模式（Pattern 2）。AI 产品的核心是数据流，不是视觉效果。数据模型正确了，后面每一步都顺。
**Pro tip:** AI 产品的 Foundation prompt 一定要包含"Mock 策略"。如果让 AI 自由选择 mock 方式，它大概率会尝试调真实 API，然后失败。

---

### Prompt 1: 搜索管道（RAG 模拟）

> 实现搜索管道的模拟逻辑。不要写 UI，只写逻辑层。
>
> 管道步骤：
> 1. `searchWeb(query)` → 返回 SearchResult[]（从 mock 数据匹配）
> 2. `generateAnswer(query, results)` → 返回 Answer
>    - 在回答文本中插入 `[1]`、`[2]` 等引用标记
>    - 引用标记对应 results 数组的 index
>    - 每个 claim 至少有一个引用
> 3. `formatAnswer(answer)` → 将 markdown + 引用标记渲染为可交互格式
>
> 关键规则——引用纪律：
> - 每个事实性陈述必须对应至少一个搜索结果
> - 没有搜索结果支持的内容不应该出现在回答中
> - 如果 mock 数据不足以回答，回答应该说"根据现有信息无法完全回答"
> - 不要编造引用——每个 [N] 必须对应真实的搜索结果
>
> Done when：调用 `searchWeb("What is React")` 返回结果，`generateAnswer` 生成带 `[1][2]` 引用的 markdown 回答，每个引用指向真实搜索结果。

**What this adds:** AI 产品的"大脑"——搜索 → 筛选 → 综合 → 引用的数据流。
**Why this prompt works:** 把管道拆成纯逻辑层，跟 UI 解耦。这样 AI 不会在实现搜索逻辑时被 CSS 分心。"引用纪律"这个规则是 Perplexity 的灵魂在代码里的体现。
**Pro tip:** "不要编造引用"这半句话是 AI 产品 prompt 里最重要的约束。没有它，LLM 会自信地编造 `[3]` 指向一个不存在的来源。

---

### Prompt 2: 搜索 UI

> 做搜索界面。
>
> 布局：
> - 顶部居中：大搜索框（Perplexity 风格——圆角、有阴影、placeholder "Ask anything..."）
> - 搜索框下方：几个建议查询的 pill 按钮
> - 搜索后：搜索框缩小到顶部，下方展示回答
>
> 回答区域：
> - 回答文本以 markdown 渲染
> - 引用标记 `[1]` 显示为蓝色小方块，hover 显示来源摘要
> - 回答下方：来源列表，每项显示 favicon + 标题 + URL + snippet
> - 来源卡片可点击
>
> Done when：输入查询后，搜索框动画缩小，回答带蓝色引用方块渲染，hover 引用显示来源，底部有来源列表。

**What this adds:** 用户能"看到"搜索结果了。
**Why this prompt works:** 描述了 Perplexity 的标志性交互——搜索框从页面中心缩小到顶部。这个动画本身就是产品身份的一部分。用 "Perplexity 风格" 比 "400px 宽度圆角输入框" 更有效。
**Pro tip:** AI 产品的 UI 往往比传统产品简单，因为核心价值在管道不在界面。搜索框 + 回答区就够了，不要加 sidebar、不要加导航。

---

### Prompt 3: 引用交互

> 让引用变得可交互。
>
> 行为：
> - 点击回答中的 `[1]` 引用方块 → 滚动到下方来源列表对应项，高亮 1 秒
> - 点击来源列表中的某项 → 弹出一个小的来源预览面板（显示完整 snippet，可点击跳转）
> - 鼠标悬停在回答中的某段文字上 → 如果这段文字有引用，在旁边显示一个小 tooltip 显示来源标题
>
> 引用同步：
> - 当回答正在"流式输出"时（模拟——用 setInterval 逐字显示），引用方块实时出现
> - 已经出现的引用在来源列表中也实时出现
>
> Done when：点击引用方块能跳转到来源，悬停在有引用的文本上显示 tooltip，来源列表与回答引用同步。

**What this adds:** Perplexity 的核心交互——阅读回答时随时能看到证据来源。
**Why this prompt works:** 分三层——点击（导航）、悬停（预览）、流式（实时感）。每一层解决"信任"的一个维度：点击让你验证，悬停让你快速判断，流式让你感觉 AI 在实时工作。
**Pro tip:** 引用交互是 AI 产品和普通聊天的分水岭。普通聊天说"据我所知"，Perplexity 说"根据 [1][2]"。这个交互比任何动画都重要。

---

### Prompt 4: 追问线程

> 添加追问功能。
>
> 交互：
> - 回答底部有 "Ask follow-up" 输入框
> - 输入追问后，当前回答向上收起（显示完整但缩小），新回答出现在下方
> - 新回答可以引用之前的搜索结果，也可以引用新的搜索结果
> - 侧边显示一个迷你时间线（小圆点），点击可以跳回之前的问答
>
> 上下文传递：
> - 追问时，之前的搜索结果和回答作为上下文传入（模拟——在 mock 数据中硬编码）
> - 新回答开头不应该重复之前已经说过的内容
>
> Done when：追问后新回答出现在旧回答下方，迷你时间线可以导航，新回答能引用之前的结果。

**What this adds:** 从"单次搜索"变成"搜索对话"——这是 Perplexity 和传统搜索引擎的关键区别。
**Why this prompt works:** 描述了信息架构（旧回答收起 + 新回答 + 时间线导航）而不是 CSS。AI 能自己想出怎么实现收起和导航。
**Pro tip:** 追问的难点不是 UI，是上下文管理——怎么把之前的搜索结果和回答传给新的 LLM 调用。在 mock 里简单硬编码就行，但 prompt 里要说清楚这个意图。

---

### Prompt 5: 搜索体验打磨

> 打磨搜索体验。
>
> 感知优化：
> - 搜索开始时：搜索框显示"Searching..."动画（三个跳动的点）
> - 回答生成时：逐字流式显示（用 setInterval，每 30ms 加一个字符）
> - 来源加载时：先显示骨架占位，加载完渐入
> - 引用方块出现时：从透明到不透明，100ms 渐入
>
> 空状态：
> - 初始页面（未搜索时）：搜索框下方显示 4 个建议查询的卡片，点击直接搜索
> - 搜索无结果时：显示"No results found" + 建议换关键词
>
> 错误处理：
> - Mock 搜索失败时（模拟 10% 概率）：显示 "Search failed. Please try again." + 重试按钮
> - 回答生成失败时：显示已生成的部分 + "Generation stopped" 提示
>
> Done when：搜索时有 loading 动画，回答逐字显示，来源渐入，空状态和错误状态都有处理。

**What this adds:** 让搜索"感觉"像真正的 AI 在工作，而不是等一个 API 返回。
**Why this prompt works:** 分三类：感知优化（让用户觉得快）、空状态（新用户引导）、错误处理（信任维护）。每一类解决体验的一个断点。
**Pro tip:** AI 产品的感知速度比实际速度更重要。"逐字流式显示"这个 trick 让用户觉得 AI 在思考，即使总时间一样。

---

## 构建顺序

```
Prompt 0: Foundation（数据模型）     ← AI 产品的骨骼
Prompt 1: 搜索管道（RAG 模拟）       ← 核心数据流
Prompt 2: 搜索 UI                    ← 用户界面
Prompt 3: 引用交互                   ← 信任层
Prompt 4: 追问线程                   ← 对话能力
Prompt 5: 体验打磨                   ← 感知优化
```

**替代路径：**
- **极速版**：只做 Prompt 0 + 1 + 2，跳过引用交互和追问
- **如果你想学 AI 管道**：重点研究 Prompt 1 的"引用纪律"规则——这是 AI 产品 prompt 设计的核心技巧

**下一步：**
- 把 mock 搜索换成真实 API（Tavily、SerpAPI、或 Bing Search API）
- 把 mock 回答生成换成真实 LLM 调用（带引用标记的 system prompt）
- 或者改变灵魂——把"每个回答都有证据"换成"每个回答都有代码"，看管道怎么变成代码搜索工具

---

## Bad prompt vs Cleaver prompt — Perplexity

```
坏的：
> 做一个 Perplexity 的克隆。搜索框，AI 回答，引用。

为什么不行：
- "Perplexity 克隆" 只指定了表面，没有指定灵魂
- 没有说引用是核心承诺（不只是"也要引用"）
- 没有区分 UI 和管道——AI 会先写搜索框，跳过数据流
- 没有引用纪律约束——LLM 会编造来源

Cleaver：
> 做一个 AI 搜索工具，核心承诺是"每个回答都有证据"。
> 管道步骤：search → rank → synthesize → cite。
> 引用纪律：每个 [N] 必须对应真实搜索结果，没有来源的 claim 不应该出现。
> 这就是 Perplexity 的灵魂不是"AI 搜索"，而是"可验证的搜索"。
```

**关键教训：** AI 产品的 prompt 设计不是"加个 AI 调用"。核心是设计管道规则——什么可以出现在回答中、什么不行、引用怎么对齐、幻觉怎么防止。这些规则才是产品的灵魂。
