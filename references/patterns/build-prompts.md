# Build Prompt Patterns

Patterns for writing prompts that build things: Intent-First, Spec-Driven, Iterative Chain, Not-To-Dos, Example-Driven, Test-First.

- [Pattern 1: Intent-First](#pattern-1-intent-first) — Default, start with why
- [Pattern 2: Spec-Driven](#pattern-2-spec-driven) — Complex projects, define everything upfront
- [Pattern 3: Iterative Chain](#pattern-3-iterative-chain) — Multi-step sequential builds
- [Pattern 4: Not-To-Dos](#pattern-4-not-to-dos) — Scope control via exclusions
- [Pattern 5: Example-Driven](#pattern-5-example-driven) — Show input/output pairs
- [Pattern 6: Test-First](#pattern-6-test-first) — Write tests, then implement

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

