# Stripe API — Standard Build

**Input:** "拆解 Stripe 的 API 设计理念"
**Path:** Standard Build (6 prompts)
**Domain:** API / Backend (API Contract pattern)

---

# Stripe API 设计理念拆解 — 可复用 Prompt 模板

> 基于 Cleaver 技能（API Contract 模式 + API/Backend 领域策略）拆解 Stripe 的 API 设计哲学，
> 输出可直接用于设计类似品质 API 的 prompt。

---

## 拆解：Stripe API 的设计理念

### Layer 1: 核心哲学 — Stripe 的"灵魂"

Stripe 的 API 有一个贯穿始终的设计信念：**开发者是用户，API 就是产品。** 每一个决策都围绕"让开发者从零到成功收款不超过 30 分钟"展开。

具体体现为五个原则：

1. **一致性压倒灵活性** — 同一个模式学会一次，到处适用。所有资源用相同的 URL 结构、相同的分页方式、相同的错误格式。
2. **渐进式复杂度** — 简单的事情一行代码搞定（`stripe.charges.create()`），复杂的事情有清晰的升级路径（Connect、Billing、Sigma），但简单路径永远不会变复杂。
3. **金额永远是整数** — 用美分（cents），不用美元。一刀切地消灭浮点精度 bug。
4. **可扩展的元数据** — 每个对象都有 `metadata` 字段，商户可以挂任意 key-value，API 永远不需要为此改 schema。
5. **错误是教学，不是惩罚** — 每个 error 都告诉开发者：发生了什么、为什么、下一步该怎么做。

### Layer 2: 数据模型 — 一切的基础

```
Account (Stripe Connect 商户账户)
  └── Customer (终端用户)
        ├── PaymentMethod (支付方式: 卡、银行账户、钱包)
        ├── Subscription (订阅)
        │     └── Invoice (账单)
        │           └── InvoiceItem (账单明细)
        ├── PaymentIntent (支付意图 — 支付的状态机)
        │     └── Charge (扣款记录)
        │           └── Refund (退款)
        └── Dispute (争议/拒付)
```

核心设计决策：
- **PaymentIntent 是灵魂** — 它是一个状态机：`requires_payment_method` → `requires_confirmation` → `processing` → `succeeded | failed`。开发者不需要理解支付网络，只需要推进这个状态机。
- **扁平 ID + 前缀** — `cus_xxx`、`pm_xxx`、`pi_xxx`。看一眼就知道这是什么类型的资源。
- **时间戳统一用 Unix epoch** — 无时区歧义。

### Layer 3: API Surface — 接口设计

**URL 结构：**
```
POST   /v1/customers          — 创建
GET    /v1/customers/:id      — 读取
POST   /v1/customers/:id      — 更新（不是 PATCH）
DELETE /v1/customers/:id      — 删除
GET    /v1/customers           — 列表
```

每个资源都遵循完全相同的 CRUD 五件套。没有例外。

**核心操作模式：**
- **创建即默认触发** — `POST /v1/charges` 直接扣款。想要两步确认？用 `capture: false`。
- **列表操作统一返回格式** — `{ object: "list", data: [...], has_more: true, url: "/v1/charges" }`。
- **游标分页** — `starting_after=ch_xxx`，不用 offset。稳定、可缓存、不怕数据变动。
- **可展开对象** — 默认返回 `{ customer: "cus_xxx" }`，加 `expand[]=customer` 就返回完整对象。一个 query param 解决 N+1 问题。

### Layer 4: Operational Contracts — 运营契约

- **幂等性键** — `Idempotency-Key` header。网络重试不会重复扣款。这是支付 API 的生命线。
- **测试/生产双环境** — 同一套 API，两套 key（`sk_test_` / `sk_live_`）。测试环境的数据和生产完全隔离。
- **速率限制** — 通过 `X-RateLimit-*` headers 暴露状态，而不是突然断连。
- **版本控制** — URL 路径版本（`/v1/`），不是 header 版本。简单、可缓存、可理解。
- **Webhook 签名** — 每个 webhook 都带 HMAC 签名，用 `stripe-signature` header 验证来源。

### Layer 5: 错误模型 — Stripe 最被低估的设计

```json
{
  "error": {
    "type": "card_error",
    "code": "card_declined",
    "message": "Your card was declined.",
    "decline_code": "insufficient_funds",
    "charge": "ch_xxx",
    "param": "source"
  }
}
```

三层错误分类：
- `type` — 错误的类别（`card_error` | `invalid_request_error` | `authentication_error` | `api_connection_error` | `rate_limit_error`）
- `code` — 具体是什么错（`card_declined`、`expired_card`、`invalid_cvc`）
- `decline_code` — 银行返回的原始原因（开发者可以据此给用户显示有意义的提示）

每个错误都附带 `doc_url`，直接链接到对应的文档页。

### Layer 6: 开发者体验 — 无形的护城河

- **可执行的文档** — 每个端点都有侧边栏可以填写参数并直接发请求。
- **Dashboard 和 API 一一对应** — Dashboard 里能看到的数据，API 里都能拿到；API 里能做的操作，Dashboard 里都有按钮。
- **CLI 工具** — `stripe listen` 转发 webhook 到本地，`stripe trigger` 模拟事件。本地开发不再需要 ngrok。
- **SDK 一致性** — Ruby、Python、Node、Go、Java、PHP……所有 SDK 的 API 风格完全一致。

---

## 可复用 Prompt 模板

以下是 5 个 prompt，按照 API Contract 模式组织。每个 prompt 可以独立使用，也可以按顺序组成完整的 API 设计流程。

---

### Prompt 0 (Foundation): 建立项目 DNA

> 我要设计一个 [描述你的服务，例如：项目管理 SaaS 的后端 API]。技术栈用 [例如：Node.js + PostgreSQL + Redis]。
>
> 请帮我搭建项目骨架：
> - 目录结构（按领域模块组织，不按技术层组织）
> - 基础中间件：请求日志、错误捕获、CORS、速率限制
> - 配置系统：环境变量 + .env，所有配置集中管理
> - 数据库迁移框架（不要 ORM，用 query builder 或 raw SQL）
> - 一个健康检查端点 `GET /health`
>
> 设计理念参照 Stripe API：一致性优先，每个资源遵循相同的模式，开发者看一个端点就能猜出其他端点的行为。
>
> **不要：** 加认证系统、加业务逻辑、加 Docker 配置、加 CI/CD。这一步只搭骨架。

**What this adds:** 项目基础架构，后续所有 prompt 都在这个骨架上构建。
**Why this prompt works:** 用 Stripe 的"一致性"理念作为设计约束，AI 不会自由发挥出 10 种不同的 URL 风格。明确的"不要"列表防止 AI 把整个 DevOps 工具链也搭了。

---

### Prompt 1: 数据模型 + API Surface

> 现在设计数据模型和 API 接口。这个 API 的核心资源是 [列出你的核心资源，例如：Team → Project → Task → Comment]。
>
> ## 数据模型要求
> - 每个实体有 `id`（前缀 + 随机字符串，如 `task_xxx`）、`created_at`、`updated_at`
> - 所有时间用 ISO 8601 字符串，所有金额用整数（最小单位，如美分）
> - 每个实体支持 `metadata` 字段 — `JSONB`，用户可以挂任意数据，API 不过问内容
> - 关系用外键，但 API 层面用嵌套资源 URL 表达（如 `/v1/projects/proj_xxx/tasks`）
>
> ## 接口设计规则（参照 Stripe）
> - 每个资源五件套：`POST`（创建）、`GET :id`（读取）、`POST :id`（更新）、`DELETE :id`（删除）、`GET`（列表）
> - 更新用 `POST` 不是 `PATCH` — 简化客户端实现
> - 列表统一返回格式：`{ object: "list", data: [...], has_more: boolean }`
> - 游标分页：`starting_after=id`，不用 offset
> - 支持 `expand[]` 参数 — 默认返回 ID 引用，加 expand 返回完整对象
> - URL 路径版本控制：`/v1/` 前缀
>
> ## 输出
> 1. 完整的数据库 schema（SQL migration 文件）
> 2. 每个资源的 API 端点列表（URL + method + 简述）
> 3. 两个代表性端点的完整 request/response 示例
>
> **不要：** 实现代码、加认证、考虑性能优化。专注在模型和接口的设计上。

**What this adds:** API 的骨架 — 所有实体、关系、端点定义。这是整个 API 最重要的部分。
**Why this prompt works:** Spec-driven 模式。数据模型、约束、验收标准全部写清楚，AI 没有猜测空间。Stripe 的具体模式（前缀 ID、游标分页、expand）作为具体约束直接引用，比说"设计一个 RESTful API"有效 10 倍。

---

### Prompt 2: 错误模型 + 幂等性

> 现在设计错误处理和操作安全机制。参照 Stripe 的错误模型 — 错误不是 bug 报告，是给开发者的教学。
>
> ## 错误结构
> 每个错误响应必须是：
> ```json
> {
>   "error": {
>     "type": "[错误类别]",
>     "code": "[具体错误码]",
>     "message": "[人类可读的描述]",
>     "param": "[触发错误的参数，可选]",
>     "doc_url": "[指向文档的链接]"
>   }
> }
> ```
>
> ## 错误类别（type）
> - `invalid_request_error` — 请求参数有问题（400）
> - `authentication_error` — 认证失败（401）
> - `authorization_error` — 权限不足（403）
> - `not_found_error` — 资源不存在（404）
> - `rate_limit_error` — 被限流（429）
> - `conflict_error` — 并发冲突（409）
> - `internal_error` — 服务端错误（500）
>
> ## 幂等性
> - 支持 `Idempotency-Key` 请求头
> - 相同 key 的重复请求返回第一次的结果，不重复执行
> - key 的有效期 24 小时
> - 服务端用 Redis 存储 key → result 映射
>
> ## 验收标准
> 1. 每种错误类别至少有一个示例
> 2. 幂等性在并发场景下正确工作（两个相同 key 的请求同时到达，只有一个执行）
> 3. 错误响应中没有技术栈泄漏（不暴露 stack trace、SQL、内部服务名）
>
> **不要：** 实现完整的错误处理中间件。先设计协议，实现留到后面。

**What this adds:** 错误处理协议 + 幂等性设计。这是区分"能用"和"好用"的分界线。
**Why this prompt works:** "错误是教学，不是惩罚"这个 Stripe 理念作为指导思想，比列一堆 HTTP 状态码更有方向感。具体的错误结构模板让 AI 不需要发明格式。验收标准确保关键场景被覆盖。

---

### Prompt 3: 认证 + Webhook + 事件系统

> 设计认证和事件通知系统。
>
> ## 认证
> - API Key 认证：`Authorization: Bearer sk_xxx`
> - 两种 key：`sk_test_`（测试）和 `sk_live_`（生产），用 URL path 前缀区分或用 key 前缀自动路由
> - Key 绑定到 Account，支持权限范围（scope）：`read_only`、`read_write`、`full_access`
> - 每个请求的认证信息写入请求日志（key 的前 8 位 + scope）
>
> ## Webhook 系统
> 事件类型命名：`resource.action`（如 `task.created`、`project.updated`、`task.deleted`）
>
> 每个 webhook 事件包含：
> ```json
> {
>   "id": "evt_xxx",
>   "type": "task.created",
>   "created": 1234567890,
>   "data": { "object": { ...完整资源对象 } },
>   "livemode": false,
>   "pending_webhooks": 2
> }
> ```
>
> 投递保证：
> - 至少投递一次（at-least-once）
> - 失败后指数退避重试（1min → 2min → 4min → 8min → 放弃，共 5 次）
> - 每个请求带 `webhook-signature` header（HMAC-SHA256），密钥在注册 webhook 时生成
> - 消费者必须返回 200，否则视为投递失败
>
> ## 输出
> 1. API Key 的数据模型和管理端点（创建、吊销、列表）
> 2. Webhook 注册端点（`POST /v1/webhook_endpoints`）
> 3. 事件投递的实现伪代码（重试逻辑 + 签名验证）
>
> **不要：** 实现 OAuth 流程。不要做 webhook 的 UI 管理界面。

**What this adds:** API 安全层 + 实时通知系统。这两个是生产级 API 的必需品。
**Why this prompt works:** 把认证和 webhook 放在一起设计，因为它们共同解决"谁在调用 + 调用后发生什么"这两个问题。Stripe 的 `livemode` 模式被保留——这是测试/生产隔离的优雅方案。具体的事件结构模板避免 AI 发明不一致的格式。

---

### Prompt 4: 开发者体验 — 文档 + SDK 模式

> 最后设计开发者体验层。这个 API 的成功标准是：一个新开发者能在 15 分钟内完成第一次成功调用。
>
> ## API 文档
> 为以下 2 个核心端点生成可执行的 API 文档（Markdown 格式）：
> - `POST /v1/{你的核心资源}` — 创建资源
> - `GET /v1/{你的核心资源}` — 列表（含分页和过滤）
>
> 文档格式（参照 Stripe 风格）：
> - 顶部：端点、方法、一句话描述
> - 参数表格：参数名、类型、必填/可选、描述
> - 右侧（或下方）：cURL 示例，填入真实参数值
> - 响应示例：成功（200/201）和至少一种错误（400）
> - 每个参数如果有取值范围，明确列出
>
> ## SDK 设计原则
> 如果要为这个 API 写 SDK（以 [语言，如 Python] 为例）：
> - 方法名 = 资源名 + 动词：`client.tasks.create()`、`client.tasks.list()`、`client.tasks.retrieve("task_xxx")`
> - 初始化：`Client(api_key="sk_xxx")` — 一个参数搞定
> - 错误用异常类层次表达：`APIError` → `AuthenticationError` / `InvalidRequestError` / ...
> - 分页用迭代器封装：`for task in client.tasks.list(limit=100).auto_paging_iter()`
>
> **不要：** 生成完整的 SDK 代码。给出设计原则和核心接口定义即可。

**What this adds:** 开发者体验设计——文档和 SDK。Stripe 的真正护城河不是 API 设计，是 DX。
**Why this prompt works:** "15 分钟内完成第一次成功调用"是一个可测试的验收标准，比"文档要写好"有力得多。具体的文档格式要求确保输出和 Stripe 的文档风格对齐。SDK 部分只要求接口定义不要求实现，保持输出聚焦。

---

### Prompt 5 (Optional): Stripe 设计理念速查卡片

> 我在设计一个 REST API，需要在设计过程中不断参照 Stripe 的设计理念做决策。请给我生成一个"API 设计决策速查卡"——每当我要做一个设计选择时，可以问自己对应的问题。
>
> 速查卡格式：
> ```
> ## [设计维度]
> Stripe 的做法：[具体行为]
> 设计问题：[问自己的问题]
> 正确答案倾向：[如果符合 Stripe 理念，应该怎么做]
> 反模式：[常见错误]
> ```
>
> 覆盖这些维度：
> 1. URL 命名（资源名用单数还是复数？嵌套还是扁平？）
> 2. HTTP 方法选择（更新用 POST 还是 PATCH？删除返回什么？）
> 3. 分页策略（cursor vs offset vs page）
> 4. 错误处理（错误格式、状态码选择、错误信息粒度）
> 5. 版本控制（URL vs header vs content type）
> 6. 认证（放在哪里？key 格式？scope 怎么设计？）
> 7. 可扩展性（自定义字段、metadata、webhook 事件类型）
> 8. 幂等性（哪些操作需要？怎么实现？）
> 9. 测试环境（如何隔离测试数据？mock 还是真实环境？）
> 10. 响应体积控制（展开、字段过滤、嵌套深度限制）

**What this adds:** 一个可反复使用的设计决策工具，不只是一次性的 prompt。
**Why this prompt works:** 把 Stripe 的隐式设计原则显式化为可回答的问题。这不是生成代码的 prompt，而是辅助思考的工具——每次遇到设计分歧时查阅。覆盖了 API 设计中最容易做出不一致决策的 10 个维度。

---

## 使用建议

1. **顺序执行** — Prompt 0 → 1 → 2 → 3 → 4，每一步都在上一步的基础上构建。Prompt 5 独立使用。
2. **按需裁剪** — 如果你的 API 不是支付相关的，去掉 `Idempotency-Key` 的复杂度；如果是内部 API，可以简化认证模型。
3. **"Stripe" 是形容词** — 在所有 prompt 中，"参照 Stripe" 传达的不仅是 REST 规范，而是一整套设计哲学：一致性、渐进复杂度、错误即教学、DX 优先。保持这个约束不变，替换掉支付领域的具体内容即可。
4. **验收标准不要删** — 每个 prompt 的"验收标准"或"Done looks like"是质量门禁。删掉它们，AI 的输出质量会显著下降。

---

## Stripe API 设计理念总结（一张图）

```
                    Stripe API 设计金字塔
                    
                        ┌─────────┐
                        │  DX 优先  │  ← 文档可执行、SDK 一致、15 分钟上手
                        └────┬────┘
                     ┌──────┴──────┐
                     │  错误即教学   │  ← 三层分类 + doc_url + 恢复指引
                     └──────┬──────┘
                  ┌─────────┴─────────┐
                  │  操作安全（幂等性）  │  ← 网络重试不等于重复操作
                  └─────────┬─────────┘
             ┌──────────────┴──────────────┐
             │  一致的接口模式（CRUD 五件套） │  ← 学一次，用到处
             └──────────────┬──────────────┘
          ┌─────────────────┴─────────────────┐
          │  实体模型（状态机 + 前缀 ID + expand） │  ← PaymentIntent 是灵魂
          └─────────────────┬─────────────────┘
       ┌────────────────────┴────────────────────┐
       │  渐进式复杂度（简单路径永远简单，复杂路径可选） │
       └────────────────────┬────────────────────┘
    ┌───────────────────────┴───────────────────────┐
    │  金额整数化 + metadata 可扩展 + 测试/生产隔离     │
    └───────────────────────────────────────────────┘
```
