# Technical Contract Prompt Patterns

Patterns for technical specifications: System Prompt Architecture, API Contract Specification.

- [Pattern 11: System Prompt](#pattern-11-system-prompt-architecture) — AI product prompts
- [Pattern 12: API Contract](#pattern-12-api-contract-specification) — Backend API specs

---

## Pattern 11: System Prompt Architecture

**For AI products.** When the user wants to deconstruct or recreate an AI product's invisible layer —
the system prompt, context pipeline, and model strategy. The system prompt IS executable code in
modern AI products.

**When to use:** Chatbots, code assistants, AI search engines, any product built on an LLM.

**Structure:**
```
## Product Overview
[What the AI product does, for whom]

## Layer 1: Identity & Persona
[Who the AI is, tone, constraints]

## Layer 2: Tool Definitions
[JSON schemas of available capabilities]

## Layer 3: Behavioral Rules
[Decision trees, safety rules, formatting requirements]

## Context Pipeline
[What data flows into the prompt, from where, when]

## Model Strategy
[Which model(s), routing logic, when to escalate]

## Guardrails
[What it refuses, how it handles edge cases]
```

**Example:**
> I want to recreate the feel of Perplexity AI — an answer engine that always cites sources.
>
> **Layer 1 (Identity):** You are a research assistant. You never state facts without a source.
> If you can't find a source, say "I couldn't verify this" instead of guessing. Your tone is
> concise and academic — no filler, no hedging, just answers with citations.
>
> **Layer 2 (Tools):** You have access to web search (returns URLs + snippets + publication dates).
> You can make up to 5 searches per query. Each search returns 10 results. You must cite at least
> 2 sources per answer.
>
> **Layer 3 (Rules):**
> - Never say anything you didn't retrieve from search results
> - Always format citations as [1], [2] inline with a numbered reference list at the end
> - If results conflict, present both viewpoints with their respective sources
> - If no results found, say "I couldn't find reliable information on this" — never fabricate sources
> - For time-sensitive queries, check the publication date of sources and prefer recent ones
>
> **Context pipeline:** User query → query rewriting (break into sub-questions) → parallel search
> for each sub-question → assemble context from top results → generate answer with inline citations.
>
> **Model strategy:** Use a fast model for query rewriting, a capable model for answer synthesis.
> If the query requires reasoning (math, logic), escalate to the frontier model.
>
> Don't: Add a chat mode, image generation, or file upload. Don't implement the "Collections"
> feature. Don't add a pro/standard tier toggle.

**Why it works:** System prompts in production AI products follow a universal 3-layer structure
(analysis of 120+ leaked prompts confirms this). Specifying all three layers gives the AI a
complete recreation blueprint. The context pipeline section captures the real moat (how data
flows, not just what the prompt says). Model strategy addresses cost optimization — a critical
production concern that hobbyist prompts miss. The "never fabricate sources" rule demonstrates
how behavioral rules encode safety guardrails.

---

## Pattern 12: API Contract Specification

**For backend/API recreation.** When the user wants to recreate or design an API based on
observing an existing one. The API contract (endpoints, request/response shapes, error codes)
replaces the UI as the primary analysis surface.

**When to use:** REST APIs, GraphQL services, WebSocket APIs, SDKs, any backend service.

**Structure:**
```
## Service Overview
[What the API does, who consumes it]

## Data Model
[Core entities and relationships]

## API Surface
[Endpoints/operations with request/response shapes]

## Error Model
[Error structure, codes, recovery guidance]

## Operational Contracts
[Auth, rate limits, pagination, idempotency, versioning]

## Developer Experience
[Docs, SDKs, playground, onboarding flow]
```

**Example:**
> I want to recreate the Stripe Payments API — specifically the simplicity of integrating payments.
> Stripe's magic is that you can go from "never used it" to "accepting money" in under 30 minutes.
>
> **Data model:** Customer → has many PaymentMethods → has many Payments. Payment has status
> (requires_payment_method → requires_confirmation → processing → succeeded OR failed).
> This state machine is the backbone.
>
> **Core endpoint:**
> `POST /v1/payments` — Create a payment intent.
> Request: { amount (cents, not dollars), currency, customer_id?, payment_method?,
>   metadata: { any key-value pairs the merchant wants } }
> Response: { id, status, amount, next_action? }
>
> The key insight: always use amounts in cents (integer), never floats. This prevents rounding bugs.
> The `metadata` field is genius — merchants can attach any data without schema changes.
>
> **Error model:** Errors are always:
> { type: "card_error" | "invalid_request_error" | "api_error",
>   message: "human readable",
>   code: "card_declined" | "insufficient_funds" | ...,
>   decline_code?: "generic_decline" | "insufficient_funds" | ... }
> Every error tells the developer exactly what happened and what to do about it.
>
> **Don't:** Implement the full Stripe API (too many endpoints). Start with: create payment,
> confirm payment, list payments, refund. That's the 80/20. Don't add Stripe Connect (marketplace
> payments) or Stripe Billing (subscriptions) yet.

**Why it works:** Backend deconstruction needs to start from the data model (unlike frontend,
which starts from the UI). The example demonstrates several key API design decisions: cents
instead of dollars (prevents floating point bugs), a state machine for payment status (clarifies
the lifecycle), and the metadata field (extensibility without schema changes). The error model
gets detailed treatment because error quality is what separates good APIs from great ones.
"Don't implement the full API" is the critical scope constraint.
