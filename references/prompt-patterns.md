# Prompt Patterns Reference

Detailed guide for the 6 prompt patterns referenced in the main skill. Use these as templates
when writing prompts — choose the pattern that matches the situation.

---

## Pattern 1: Intent-First

**The default.** Start with why, then what, let the AI figure out how.

This pattern works because LLMs are smart — they don't need you to specify implementation details.
When you describe the intent clearly, the AI can make better architectural decisions than if you
prescribe every step.

**When to use:** Most cases. Landing pages, simple features, prototypes, "I want something like X."

**Structure:**
```
[Why this exists / what problem it solves]
[What the user should experience]
[Feel / vibe / reference points]
[What NOT to do]
```

**Example:**
> I need a settings page for our team collaboration app. Right now people can't customize
> anything and it's driving them crazy. I want it to feel calm and organized — like opening
> a well-arranged desk drawer where everything has its place. Three sections: Profile (avatar,
> name, timezone), Notifications (toggle each type on/off with clear labels about what each
> one does), and Appearance (dark/light/auto with a live preview). Don't add any fancy
> animations — this should feel instant and reliable, like a settings page should.

**Why it works:** The AI understands the problem (customization), the experience (calm, organized),
the specifics (3 sections with items), and the boundary (no fancy animations). It has enough
freedom to choose the right implementation while staying on target.

---

## Pattern 2: Spec-Driven

**For complex projects with multiple moving parts.** Define the data model, constraints, and
acceptance criteria upfront, then let the AI implement against the spec.

This pattern comes from Thoughtworks' "Beyond Vibe Coding" methodology — the insight is that
AI coding agents perform dramatically better when given a spec to implement against, rather than
vague instructions.

**When to use:** Multi-component features, data-heavy apps, anything with complex state or
business logic. When "just figure it out" will lead to 3 rewrites.

**Structure:**
```
## Goal
[What this achieves]

## Data Model
[Key entities and their relationships]

## Components
[List of components and their responsibilities]

## Constraints
[Technical and business rules]

## Acceptance Criteria
[How to verify it works]
```

**Example:**
> ## Goal
> Build a task board for our 5-person team. Drag-and-drop between columns.
>
> ## Data Model
> Task { id, title, description, status (todo|in_progress|review|done),
>        assignee, priority (p0-p3), created_at, due_date }
> Column { id, name, position, wip_limit? }
>
> ## Components
> - Board: renders columns in order, handles drag-and-drop between them
> - Column: shows tasks, enforces WIP limit (show warning, don't block)
> - TaskCard: compact card with title, assignee avatar, priority badge
> - TaskModal: full edit view, opens on card click
>
> ## Constraints
> - Tasks persist to localStorage (no backend yet)
> - Maximum 200 tasks — don't over-engineer for scale
> - No external drag library — use native HTML5 drag-and-drop
> - Mobile: swipe between columns instead of drag
>
> ## Acceptance Criteria
> - Can create, edit, delete tasks
> - Can drag tasks between columns (desktop) or swipe (mobile)
> - WIP limit warning appears when exceeded
> - Data survives page refresh

**Why it works:** The AI can't misinterpret the requirements because they're explicit. The data
model prevents the AI from guessing at state management. Constraints eliminate entire categories
of wrong implementations. Acceptance criteria give the AI a way to self-verify.

---

## Pattern 3: Iterative Chain

**Break a complex build into a sequence of prompts**, each building on the last. Each prompt
is a complete step that produces working output.

This pattern comes from Andrew Chen's documented workflow and Teresa Torres' "avoid the doom
loop" advice. The key insight: **start a new conversation for each step** to prevent context rot.
Previous steps produce files/artifacts that the next step picks up.

**When to use:** Anything that takes more than 3 prompts. Full app builds, multi-page sites,
complex features with frontend + backend.

**Structure per prompt:**
```
[Context: what we've built so far and what file(s) to look at]
[This step's goal]
[What to do]
[What NOT to touch / change]
```

**Example chain:**

*Prompt 1 (new conversation):*
> Build me a personal portfolio site. Just the skeleton for now — a single page with sections
> for Hero, About, Projects, and Contact. No content yet, just the structure and navigation.
> Use React + Tailwind. Deploy-ready.

*Prompt 2 (new conversation):*
> Read the portfolio site in the current directory. Fill in the Hero section: my name is Alex,
> I'm a product designer, and the tagline is "Designing products that make complex things simple."
> Add a professional headshot placeholder and two CTAs: "See my work" (scrolls to Projects)
> and "Get in touch" (scrolls to Contact). The vibe should feel like a exhale — calm, confident,
> not shouty. Think: dark background, clean typography, lots of breathing room.

*Prompt 3 (new conversation):*
> Read the portfolio site. Now build the Projects section. I'll give you 3 projects, each with
> a screenshot, title, one-line description, and tech tags. Display them in a grid — each card
> should be clickable and expand to show more details. The hover effect should feel like the card
> is lifting slightly off the page, with a subtle shadow growing underneath.

**Why it works:** Each conversation starts clean with no accumulated confusion. The project files
carry the context forward instead of the conversation. If one step goes wrong, you only redo that
step — not the whole chain.

---

## Pattern 4: Not-To-Dos

**Explicitly define what's out of scope.** Sometimes the most powerful thing in a prompt is what
you say NOT to do.

This pattern comes from Anna Arteeva (Google engineer, 20 years experience), who says: "Defining
what's NOT in scope eliminates ambiguity faster than any amount of positive description."

**When to use:** When the AI tends to over-engineer. When scope creep has burned you before.
When you're building incrementally and need each step to stay focused.

**Structure:**
```
## Do
[What to build]

## Do NOT
[Explicit exclusions — be specific]
- Don't add [X]
- Don't worry about [Y] yet
- Don't use [Z library/approach]

## Done looks like
[Clear finish line]
```

**Example:**
> ## Do
> Build a user registration form: email, password, confirm password, and a "I agree to terms"
> checkbox. Validate inline — show errors below each field as the user types (not after submit).
>
> ## Do NOT
> - Don't add social login (Google/GitHub) — that's phase 2
> - Don't build a forgot password flow
> - Don't set up email verification
> - Don't create a full auth system — just the form component
> - Don't use form libraries (Formik, react-hook-form) — keep it simple
> - Don't style it yet — plain HTML with enough spacing to be usable
>
> ## Done looks like
> A single React component that validates the form and calls `onSubmit(data)` on success.
> No backend calls. No routing. Just the form.

**Why it works:** Without not-to-dos, the AI will often build the entire auth system when you
only asked for a form. Explicit boundaries are the most efficient way to focus AI effort.

---

## Pattern 5: Example-Driven

**Show input→output pairs instead of describing the rule.** LLMs generalize better from examples
than from abstract descriptions.

**When to use:** When format, style, or transformation rules matter more than the logic. Data
formatting, content generation, UI patterns, API response shaping.

**Structure:**
```
Transform/process [input type] into [output type].

Examples:
Input: [example 1 input]
Output: [example 1 output]

Input: [example 2 input]
Output: [example 2 output]

Input: [example 3 input — edge case]
Output: [example 3 output]
```

**Example:**
> I need a function that formats relative timestamps — like "2 minutes ago" or "yesterday."

> formatDate(new Date()) → "just now"
> formatDate(30 seconds ago) → "30 seconds ago"
> formatDate(5 minutes ago) → "5 minutes ago"
> formatDate(90 minutes ago) → "1 hour ago"
> formatDate(25 hours ago) → "yesterday"
> formatDate(3 days ago) → "3 days ago"
> formatDate(14 days ago) → "2 weeks ago"
> formatDate(60 days ago) → "Jan 15" (the actual date)
> formatDate(invalid) → null
> formatDate(null) → null

> Don't use a library. Keep it under 30 lines.

**Why it works:** The examples encode complex rules implicitly (rounding thresholds, boundary
conditions, fallback behavior) without you needing to specify each one. Edge cases shown in
examples are handled more reliably than edge cases described in prose.

---

## Pattern 6: Test-First

**Write acceptance tests before implementation.** The tests become the spec, and the AI
implements to pass them.

This is the vibe coding version of TDD. Instead of writing actual test code, you describe the
test cases in natural language — what should happen in each scenario.

**When to use:** When correctness matters (calculations, business logic, data processing).
When you want the AI to have a clear "done" condition. When you've been burned by AI generating
plausible-looking but subtly wrong logic.

**Structure:**
```
Build [thing] that passes these scenarios:

Scenario 1: [description]
  Given: [precondition]
  When: [action]
  Expected: [result]

Scenario 2: [description]
  Given: [precondition]
  When: [action]
  Expected: [result]

[...more scenarios including edge cases]

Then: implement the function/component that passes all scenarios.
```

**Example:**
> Build a shopping cart discount calculator. It should pass these scenarios:

> Scenario: Standard order
>   Cart total: $80, no coupon, not a VIP
>   Expected: $80 (no discount)

> Scenario: Bulk discount threshold
>   Cart total: $120, no coupon, not a VIP
>   Expected: $108 (10% off orders over $100)

> Scenario: VIP customer
>   Cart total: $80, no coupon, is a VIP
>   Expected: $64 (20% VIP discount)

> Scenario: VIP + bulk
>   Cart total: $150, no coupon, is a VIP
>   Expected: $120 (20% VIP discount — VIP rate beats bulk rate, they don't stack)

> Scenario: Coupon
>   Cart total: $80, coupon "SAVE5" for $5 off, not a VIP
>   Expected: $75 ($5 off, no percentage discount)

> Scenario: Maximum discount cap
>   Cart total: $1000, no coupon, is a VIP
>   Expected: $950 (20% would be $200, but cap is $50)

> Rules: discounts don't stack (best one wins), cap applies after discount calculation.

**Why it works:** The scenarios leave zero room for misinterpretation. The AI can verify its own
work by checking each scenario. You can easily add more scenarios to patch gaps without rewriting
the whole prompt.

---

## Pattern 7: PRD / Product Spec Generator

**For non-code outputs.** When the user wants a PRD, design brief, or product specification instead
of code. The prompt describes the product vision and asks the AI to generate a structured document.

This pattern applies when deconstructing physical products or when the user's output type is
"PRD" or "design brief" rather than code.

**When to use:** Physical products (phones, cars, appliances), service experiences, or any time
the deliverable is a document rather than working software.

**Structure:**
```
## Product Vision
[What this is, for whom, what problem it solves]

## Target User
[Who will use/buy this, their context and pain points]

## Core Experience
[The 3-5 things that MUST feel right]

## Constraints
[Physical, technical, regulatory, budget, timeline]

## Success Metrics
[How to know if this product succeeded]

## Out of Scope
[What this is NOT — just as important]

Generate a full PRD with: problem statement, user stories, requirements (functional + non-functional),
technical considerations, and milestone plan.
```

**Example:**
> I want to create a product spec inspired by the Dyson Airwrap. Not a hair dryer clone — I want to
> understand the PRODUCT THINKING behind it and apply that thinking to a different category.
>
> ## Product Vision
> A kitchen appliance that makes home cooking feel like a professional kitchen — specifically,
> a smart cooking station (like a combination of induction cooktop + precision oven + sous vide)
> that eliminates the #1 reason people don't cook: uncertainty about whether it'll turn out right.
>
> ## Target User
> Urban professionals aged 25-40 who want to cook at home but feel intimidated. They order delivery
> 4-5x/week not because they can't afford it but because cooking feels risky and time-consuming.
> They've bought appliances before (air fryer, Instant Pot) that are now gathering dust.
>
> ## Core Experience (must feel right)
> 1. **Certainty** — "I know this will turn out well" (not guessing, not hoping)
> 2. **Speed** — from decision to eating in under 30 minutes for most meals
> 3. **Cleanup** — less than 5 minutes, or the whole thing is pointless
> 4. **Learning** — each use makes me slightly better, without feeling like school
>
> ## Constraints
> - Fits on a standard kitchen counter (no larger than a microwave)
> - Under $500 retail price
> - No subscription required for core functions
> - Works with standard ingredients from any grocery store
> - Must pass food safety regulations (FDA, CE)
>
> ## Success Metrics
> - Users cook 3+ meals/week after 1 month (vs 1-2 before)
> - Meal success rate >90% ("turned out how I expected")
> - Average session: decision → eating in under 30 min
> - NPS >60 at 3 months
>
> ## Out of Scope
> - Not a meal kit delivery service
> - Not a recipe app (though it integrates with them)
> - Not replacing all cooking — just the "I want something good, fast, reliable" scenario
> - Not for professional chefs
>
> Generate a complete PRD covering: user research plan, core user stories, functional requirements,
> non-functional requirements, technical feasibility considerations, go-to-market milestones, and
> a risk assessment for the top 5 things that could go wrong.

**Why it works:** The PRD prompt itself follows good PM practice — clear vision, defined user,
non-negotiable experiences, explicit constraints, measurable success, and hard out-of-scope
boundaries. The AI produces a much better PRD when it understands the WHY behind each section.
The "inspired by Dyson Airwrap" reference gives the AI a quality benchmark to calibrate against.

---

## Pattern 8: Design Brief Generator

**For physical product design.** When the output is a brief for industrial designers, material
engineers, or manufacturing partners. Focuses on sensory experience, form language, and
manufacturing constraints.

**When to use:** When the user wants to translate a product experience into instructions for
designers, not engineers or coders.

**Structure:**
```
## What we're designing
[Product category and positioning]

## Who it's for
[User lifestyle, not demographics]

## How it should feel
[Sensory targets — touch, sight, sound, weight]

## What it communicates
[What owning/using this says about the person]

## What to reference
[3-5 real products that capture different aspects of the target feel]

## Must have / Must not have
[Hard constraints]

## Budget and manufacturing context
[Price target, volume, production method]
```

**Example:**
> Design brief for a premium travel coffee mug — the kind someone brings to a meeting and feels
> good about, not embarrassed.
>
> **Feel targets:**
> - When you pick it up: "this is satisfying to hold" — weighted bottom, tapered grip, matte surface
>   that doesn't show fingerprints
> - When you open it: a soft click, not a metallic clang — like closing a luxury car door
> - When you drink: the lip feel has to be right — thin enough that it doesn't feel like drinking
>   from a Thermos, thick enough to feel substantial
> - When you set it down: silent, doesn't wobble, stays put
>
> **References:** Apple's ceramic shield finish (surface feel), Fellow Carter mug (overall form),
> Zojirushi's lid mechanism (functionality), Aesop's packaging (brand aesthetic)
>
> **Must not:** have visible branding/logo on the outside, sweat condensation, feel like a camping
> product, be mistaken for a Yeti/Stanley
>
> **Context:** Target retail $45-60, manufactured in 50K+ units, ceramic or double-wall stainless.

**Why it works:** Design briefs need sensory language, not engineering specs. "Like closing a
luxury car door" tells a designer more about the target feel than "torque resistance of 2.5 Nm."
The references give concrete calibration points. The "must not" list prevents designers from
defaulting to the obvious category conventions.

---

## Pattern 9: Experience-to-Spec Translator

**Bridge from feel to measurement.** When the user describes a physical product feeling ("premium",
"satisfying click", "light but sturdy"), translate that into measurable engineering parameters.
This pattern is essential for physical product PRDs and design briefs where vague adjectives
need to become actionable specifications.

**When to use:** Physical product deconstructions where the output is a PRD or design brief.
Any time someone says "it should feel [adjective]" and needs that translated into something
engineers or manufacturers can work with.

**Structure:**
```
Translate this product feeling into measurable specifications:

Experience target: "[vague feeling description]"
Product category: [what kind of product]
Reference products: [1-3 real products with similar feel]

For each sensory dimension, provide:
- Parameter name
- Ideal value
- Acceptable range
- How to test/measure it

Sensory dimensions to cover:
- Visual: color, finish, transparency
- Tactile: surface roughness, temperature, hardness, weight
- Auditory: sound profile, volume, frequency
- Kinesthetic: actuation force, travel distance, return force
- Olfactory (if relevant): material off-gassing, scent
```

**Example:**
> I want a smart home thermostat that feels "premium but approachable — like a nice watch,
> not a spaceship." Reference: Nest thermostat, Bang & Olufsen remote, Dieter Braun calculator.
>
> Translate this into measurable specs for:
> - The front face (what you see and touch)
> - The rotation dial (primary interaction)
> - The click feedback (setting confirmation)
> - The weight and mounting (wall presence)

**Expected AI output would include:**
```
Front Face:
- Material: matte polycarbonate or aluminum (Ra 0.2-0.4 μm surface roughness)
- Color: warm neutral (not clinical white, not cold gray — think Pantone Warm Gray 2C)
- Temperature: should feel neutral to touch (thermal conductivity < 0.5 W/mK, avoid cold metal)
- Finish: fine matte bead-blast, no fingerprints visible

Rotation Dial:
- Diameter: 50-55mm (fits thumb and index finger comfortably)
- Edge: slightly rounded (radius 1-2mm), no sharp lip
- Rotation torque: 0.15-0.25 Nm (smooth, not loose, not stiff)
- Detent: subtle clicks every 1 degree of rotation (audible <35dB, tactile bump 0.05N)

Click Feedback:
- Actuation force: 2-3N (firm enough to confirm, light enough to not fatigue)
- Travel distance: 0.3-0.5mm (barely perceptible but satisfying)
- Sound: soft "thock" not "click" (frequency 2000-4000 Hz, <40dB)
- Haptic: short 10ms vibration pulse at 150Hz

Weight & Mounting:
- Total weight: 180-220g (substantial but not heavy, heavier than expected for size)
- Wall mount: flush, no visible screws, magnetic attachment for easy removal
- Wall gap: <2mm (feels like it grows from the wall, not stuck on)
```

**Why it works:** The vague feeling "premium but approachable" is hard to engineer against. But
"matte surface with Ra 0.2-0.4 μm, rotation torque 0.15-0.25 Nm, soft thock at 2000-4000 Hz"
is something a manufacturer can specify, test, and validate. The AI bridges the gap between
product manager language and engineering language. The reference products give calibration:
Nest = approachable tech, B&O = premium tactile, Braun = timeless simplicity.

---

## Pattern 10: Game Design Document (GDD) Generator

**For game recreation.** When the user wants to deconstruct a game into prompts that recreate it
(or something inspired by it). Focus on the core loop, progression, and balance — the stuff that
makes the game fun, not just what it looks like.

**When to use:** Games of any genre. When the output is a playable game, a game design document,
or a balance spec.

**Structure:**
```
## Game Overview
[One-sentence pitch: "It's a [genre] where you [core verb] to [core goal]"]
[Reference game(s) and what to capture from each]

## Core Loop
[ASCII diagram of the minute-to-minute cycle — this is the most important artifact]

## Mechanics
[Specific rules with numbers — HP, damage, costs, probabilities]

## Progression
[What grows, how it grows, unlock thresholds]

## Economy
[Currencies, sources, sinks, key formulas]

## Feel Targets
[What the game should feel like — references to real games for calibration]

## MVP Scope (3 milestones)
1. [Core mechanic playable]
2. [Full loop with progression]
3. [Polish: feedback, audio, UI]

## What to Cut
[Explicit scope exclusions — games have enormous scope, cutting is essential]
```

**Example:**
> I want to recreate the feel of Balatro — a poker roguelike where the core loop is "see hand →
> evaluate → discard → play → see score → shop → repeat." The fun comes from build diversity
> (different joker combinations create wildly different strategies) and the escalating tension
> as blinds get harder.
>
> Core loop: Deal 8 cards → Select up to 5 → Play or Discard (limited hands/discards per round)
> → Score calculated with multipliers → Beat the blind? → Shop phase → Next round
>
> Key numbers: Starting hand size 8, max plays 4, max discards 3. Jokers multiply score
> multiplicatively (a ×3 and a ×4 = ×12, not ×7). Money earned = interest (floor of gold/5, max 5)
> + remaining hands × 1.
>
> Feel: Every run should feel different because of joker synergies. The excitement comes from
> discovering broken combos. Think Slay the Spire's relic system but with poker hands.
>
> MVP: Just the core scoring loop + 20 jokers + basic shop. No boss blinds, no tarot/planet cards,
> no voucher system. Those come later.
>
> Don't: Add animations, sound effects, or visual polish yet. Don't implement all 150 jokers.
> Don't add the stakes/challenge system.

**Why it works:** Games are uniquely hard to specify because the fun comes from system interactions,
not individual features. The core loop diagram gives the AI the heartbeat. The actual numbers
(8 cards, 4 plays, 3 discards) give the AI the balance. The "what to cut" list prevents the AI
from building the entire game at once. "Feel" targets expressed through game references
("like Slay the Spire's relic system") convey more nuance than abstract descriptions.

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
