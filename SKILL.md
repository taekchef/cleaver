---
name: cleaver
description: >
  Reverse-engineer ANY product (digital or physical) into actionable prompts for vibe coding,
  PRDs, design briefs, or service blueprints. Trigger when someone wants to deconstruct, reverse
  engineer, break down, or learn from any product — website, app, CLI, game, API, AI product,
  service, or physical object. Also use when they share a screenshot/URL/code and want the prompts
  behind it, or ask "how was this made?" — even without saying "reverse engineer."
  DO NOT trigger for: direct coding tasks ("implement X", "build a login page"), code review,
  bug fixing, or general product strategy advice. This skill is for DECONSTRUCTION, not construction.
---

# Cleaver

Like a butcher's cleaver — take any finished product, cleave it into the prompts that built it.

This skill helps product managers (and anyone curious) reverse-engineer ANY product — digital or
physical — into prompts they can learn from, modify, or use to create similar work. Output can be
code prompts (vibe coding), PRD prompts (product specs), design prompts (briefs), or service
prompts (blueprints) — whatever the user needs.

## Paths & Foundation

Different users want different things. After Phase 2, choose a path:

**Minimal (1 prompt, 2-3 sentences — the soul of the product)**
For: "Just give me the essence, I'll figure out the rest"
How: Distill the entire product into 2-3 sentences that capture the soul. This is not a spec — it's
a haiku. The first sentence says WHAT it is and WHY it matters. The second says HOW it feels.
The third (optional) says what to use or what NOT to do. The user takes this and iterates on their own.
Trade-off: minimal guidance, maximum freedom, but relies on the user's taste and skill.

Example: "做一个项目管理工具，核心是'不挡路' — 打开就用，键盘搞定一切，像在终端里
写代码一样流畅，不需要点来点去。深色极简风格，参考 Linear 的感觉。React + Tailwind，
不要组件库。"

**Fast Track (2-3 prompts, ~30 min to working prototype)**
For: "I just want to see something working ASAP"
How: One "everything" prompt that captures the soul of the product, then 1-2 refinement prompts.
The first prompt should be ambitious — describe the whole thing in one shot. It won't be perfect,
but the user gets something tangible to react to. Then refine based on what's wrong.
Trade-off: less control, more surprises, but instant gratification.

**Foundation Prompt (Prompt 0 — always generated first)**
For: Every path. This is the infrastructure layer.
How: Before any feature prompt, generate one "setup" prompt that establishes the project's DNA.
This prompt is always included regardless of which path the user chooses. It covers:
- Tech stack and framework choices (with reasoning)
- Project directory structure
- Core architecture pattern (monolith, modular, component-based, etc.)
- Base styles/theme system (colors, typography, spacing scale)
- Configuration files (tsconfig, tailwind config, etc.)
- Conventions (naming, file organization, state management approach)
- A "definition of done" for the setup phase

The foundation prompt solves a real problem: without it, every subsequent prompt has to re-establish
context ("use React + TypeScript + Tailwind, dark theme, Inter font..."), which wastes tokens and
risks inconsistency. With it, every feature prompt can simply say "building on the foundation from
Prompt 0" and focus on the feature itself.

Example: For the Linear teardown, the foundation prompt would set up the Next.js project, establish
the dark theme tokens, create the layout shell component, and define the keyboard shortcut
registration system — all before any feature prompt runs.

**Standard Build (5-8 prompts, full component coverage)**
For: "I want to actually recreate this thing"
How: Follow the full Phase 1-5 workflow. Each prompt builds one layer or component.
Trade-off: more effort, more prompts to manage, but predictable and thorough.

**Learning Deep-Dive (5-10 prompts with heavy annotations)**
For: "I want to understand how to think in prompts"
How: Same as Standard Build, but every prompt gets detailed "Why this prompt works" and "Pro tip"
annotations. Include anti-patterns and common mistakes for each technique.
Trade-off: verbose output, takes longer to read, but maximum educational value.

Tell the user which path you're taking and why. Let them override your choice.

## The Workflow

### Phase 1: Understand what the user brought you

First, figure out what you're working with. Each input type has its own analysis approach — don't
treat them all the same.

**Screenshot / image:**
Look at it like a designer doing a critique. Note:
- Overall layout grid (columns, rows, sections, card structure)
- Visual hierarchy — what draws the eye first? second? third?
- Component inventory (buttons, forms, cards, modals, nav, tabs, tooltips...)
- Typography: how many sizes/weights? headings vs body vs captions?
- Color: how many distinct colors? what's primary/secondary/accent? dark or light mode?
- Spacing rhythm: tight/dense vs airy/generous?
- Interaction hints: hoverable things, scrollable areas, toggles, drag handles
- Responsive clues: does it look mobile-first or desktop-first?

**URL / live website:**
Fetch the page and study it systematically:
- Information architecture: what sections exist, in what order?
- Navigation model: sidebar? top nav? tabs? breadcrumbs?
- Key interactions: forms, filters, drag-drop, infinite scroll, modals?
- Responsive behavior: resize or check mobile — how does the layout adapt?
- Loading patterns: skeletons, spinners, progressive reveal?
- Also grab the tech stack if visible (view source, framework hints in class names, meta tags)

**Code / repo:**
Read strategically, not cover-to-cover:
- Start with README, package.json / Cargo.toml / go.mod — understand the what and the stack
- Find the entry point (main.rs, index.ts, app.py) and trace the architecture
- Identify the core data model — what are the main entities?
- Look at the directory structure — how is responsibility divided?
- Check for config files — what's configurable? what decisions were left to the user?
- Read tests — they reveal what the author considered important behavior

**Design file (Figma, Sketch):**
Think in systems:
- Component hierarchy: atoms → molecules → organisms → templates → pages
- Design tokens: spacing scale, color palette, type scale, border radii, shadows
- Repeating patterns: what components are reused? what varies?
- State variations: hover, active, disabled, loading, empty, error
- Responsive breakpoints: how does the layout shift?

**Verbal description:**
"I saw this thing that did X..." — extract the core idea, then probe:
- What specifically caught your attention? The interaction? The layout? The feel?
- Where did you see it? (helps you look it up if needed)
- What would you change about it? (reveals what they actually care about)

**A specific feature / interaction:**
"The way Spotify crossfades between songs" — isolate the mechanism:
- What triggers it? What changes? What's the transition?
- What's the user experiencing vs what's happening technically?
- Is it the behavior itself or the polish (timing, easing, feedback)?

**A game / interactive experience:**
Games require working backwards from the player experience using the MDA framework:
- Core loop: what's the minute-to-minute action cycle? (explore → fight → loot → upgrade → repeat)
- What makes it fun? What emotion does it target? (challenge, discovery, fellowship, sensation)
- Progression: what grows over time? (stats, levels, unlocks, prestige layers)
- Game feel: what makes actions satisfying? (screen shake, particles, hit-stop, sound)
- Balance: what are the key numbers? (HP, damage, costs, probabilities)
- Session design: how long is a typical session? how does it start and end?
- Monetization: how does it make money? how does this affect the design?

**An AI product (chatbot, code assistant, image generator, etc.):**
The invisible layer IS the product — focus on what you can't see:
- System prompt: what persona, tools, and rules define the AI's behavior?
- Context pipeline: what data flows into the prompt? (RAG, memory, search, files)
- Model strategy: single model? tiered routing? fine-tuned? custom?
- Tool/function calls: what can the AI actually do? (JSON schemas reveal capabilities)
- Guardrails: what does it refuse? how consistent are refusals?
- Latency: how fast is the first token? does it stream?
- Output quality: does it cite sources? does it hallucinate? how does it handle uncertainty?

**Physical product (phone, appliance, vehicle, etc.):**
Study it from a user's perspective — you can't read its source code, so observe behavior:
- First impression: what does it feel like to unbox / see / hold?
- Core interaction loop: what does the user do most often? how does it respond?
- Sensory profile: visual, tactile, auditory, olfactory — what stands out?
- Material and build language: premium? utilitarian? playful? minimal?
- Interface points: buttons, screens, LEDs, sounds, haptics — how does it communicate?
- User journey: purchase → unboxing → setup → daily use → maintenance → end of life
- What makes it feel "well-designed" vs "cheap"? What's the intangible quality?
- If it has a digital companion (app, dashboard) — how do physical and digital connect?

Don't rush this. Misunderstanding the product = garbage prompts.

### Phase 2: Understand what the user wants

Before you start deconstructing, ask:

1. **Purpose** — "What do you want to do with these prompts?"
   - Learn vibe coding techniques? → bias toward educational annotations
   - Actually recreate this thing? → bias toward actionable, copy-paste-ready prompts
   - Remix it into something new? → identify the core patterns and make them modular

2. **Output type** — "What do you want these prompts to produce?"
   - **Code / working software** → standard vibe coding prompts (default)
   - **PRD / product spec** → prompts that generate product requirement documents
   - **Design brief** → prompts for industrial designers, UI/UX specs
   - **Service blueprint** → prompts for process/service design
   - **Learning material** → prompts that teach through deconstruction
   - **Not sure** → default to code, offer to switch if the project doesn't fit

   This is crucial for physical products: deconstructing a Tesla could produce
   code prompts (for its dashboard UI), a PRD (for a similar EV), or a design
   brief (for its industrial design). Ask the user which output they want.

3. **Style preference** — "What kind of prompts work for you?"
   - **Framework-style**: Detailed, structured, step-by-step (like a recipe)
   - **Natural language**: Conversational, like talking to a friend who happens to be an AI
   - **Hybrid**: Key structure with natural language fill

4. **Depth** — "How deep do you want to go?"
   - **Surface**: One overview prompt that captures the gist
   - **Medium**: A few prompts covering major components
   - **Full teardown**: Every component, interaction, and design decision as separate prompts

5. **Tool context** — "What are you vibe coding with?"
   - Claude Code (CLI)? → prompts can reference files, terminal commands
   - Claude.ai / ChatGPT? → prompts stay conversational
   - Cursor / Windsurf? → prompts can be more code-oriented
   - Doesn't matter / just want to learn → keep prompts universal

**Dig deeper — don't stop at surface answers.** People often can't articulate what they
actually want until you probe. Try these follow-ups:

- "What specifically about this caught your eye?" → reveals their real interest (might be
  the animation, not the layout; might be the onboarding flow, not the dashboard)
- "If you could only keep one thing about this product, what would it be?" → the core
  insight the prompts must capture
- "What would you change?" → reveals taste and intent — remix opportunities
- "Have you tried building something like this before? What went wrong?" → avoids
  repeating their past mistakes in the prompts
- "Show me the closest thing you've built or used" → calibrates their skill level
  and expectations

### Phase 3: Deconstruct

Now cleave the project apart. Think like a product manager who built this — what decisions did they make, in what order?

**The deconstruction framework:**

```
Layer 1: Foundation
  - What is this? (one sentence)
  - Who is it for?
  - What problem does it solve?
  → Prompt: "Build me a [type] that [solves X] for [user type]..."

Layer 2: Structure
  - What are the main components / sections?
  - How are they arranged?
  - What's the information hierarchy?
  → Prompt: "Add [component] with [layout] that shows [content]..."

Layer 3: Visual Design
  - What's the aesthetic? (minimal, bold, playful, corporate...)
  - Color palette and typography vibes?
  - Spacing and density?
  → Prompt: "Style it with [aesthetic] — think [references]..."

Layer 4: Interaction & Behavior
  - What happens when users do things?
  - Animations, transitions, feedback?
  - State changes (loading, empty, error, success)?
  → Prompt: "When user [action], make it [behavior]..."

Layer 5: Details & Polish
  - Edge cases, empty states, error handling?
  - Micro-interactions, hover effects, loading states?
  - Accessibility considerations?
  → Prompt: "Add polish: [specific refinements]..."

Layer 6: Data & Logic (if applicable)
  - Where does data come from?
  - What computations or transformations happen?
  - State management approach?
  → Prompt: "Wire up the data so that [logic]..."
```

Not every layer applies to every project. Skip what's not relevant. The order isn't sacred either — adapt to what makes sense for the specific project.

**Domain-specific overrides** — For some domains, the generic 6-layer framework needs adjustment:

- **Games**: Replace Layer 3 (Visual Design) with "Core Loop & Feel" (the minute-to-minute cycle,
  game feel, juice). Add a "Balance & Numbers" layer (progression formulas, economy tuning).
  Work backwards from the MDA "Aesthetics" layer — what emotions should the player feel?

- **APIs / Backend**: Replace Layer 3 (Visual Design) with "API Surface & Contracts" (endpoints,
  request/response shapes, error model). Replace Layer 4 (Interaction) with "Operational Contracts"
  (auth, rate limits, pagination, idempotency). The data model (Layer 6) becomes Layer 1.

- **AI Products**: Add a "System Prompt Architecture" layer (identity, tools, rules — the 3-layer
  structure). Add a "Context Pipeline" layer (what data flows in, when, from where). Replace
  Layer 6 (Data & Logic) with "Model Strategy & Token Economics". The invisible layer IS the product.

### Phase 4: Write the prompts

#### Choosing the right prompt pattern

Different situations call for different prompt structures. Don't always default to the same
format — match the pattern to what the user is trying to accomplish:

| Pattern | When to use | One-line description |
|---|---|---|
| **Intent-first** | Most cases — the default | Start with why, then what, let AI figure out how |
| **Spec-driven** | Complex projects, multiple components | Define data model, constraints, and acceptance criteria upfront |
| **Iterative chain** | Multi-step builds | Break into sequential prompts, each building on the last |
| **Not-to-dos** | When scope creep is a risk | Explicitly state what NOT to do — often more useful than what TO do |
| **Example-driven** | When format/style matters | Show input→output pairs instead of describing the rule |
| **Test-first** | When correctness is critical | Write acceptance tests first, then ask AI to implement |
| **PRD generator** | Physical products, product specs | Vision + user + constraints + success metrics → full PRD |
| **Design brief** | Industrial design, physical form | Sensory targets + references + must-nots → design direction |
| **Experience-to-Spec** | Feel → engineering parameters | Translate "premium feel" into measurable Ra/Nm/dB values |
| **GDD generator** | Games | Core loop + progression + balance → Game Design Document |
| **System prompt** | AI products | Identity + tools + rules → 3-layer system prompt architecture |
| **API contract** | Backends, APIs | Data model + endpoints + error design → API specification |

For detailed examples of each pattern, read `references/prompt-patterns.md`.

#### Prompt writing principles

1. **Speak human** — Write like you're describing the feature to a colleague over coffee, not
   like you're writing a technical spec. "Make the cards stack on top of each other on phones"
   beats "Implement a responsive flex-column layout for mobile viewports."

2. **Be specific about the result, flexible about the method** — "The sidebar should slide in
   from the left with a smooth animation" is better than "Use CSS transform translateX with a
   300ms ease-out transition." Let the AI pick the implementation.

3. **Reference real things** — "Think of how Apple's checkout page feels" or "Like the way
   Linear handles keyboard shortcuts." Real references convey more nuance than abstract
   descriptions.

4. **Show, don't just tell** — When possible, describe the user experience: "When I tap a card,
   it expands to fill the screen with a satisfying spring animation, and the content fades in."

5. **Include the why** — Especially for learning prompts, explain why a decision was made. "Use a
   skeleton loader here instead of a spinner — the content structure is predictable, so showing
   the shape reduces perceived load time."

6. **Make them composable** — Each prompt should work on its own but also build on previous ones.
   A user should be able to skip steps or reorder them.

#### Before / After examples

**Example A — Landing page hero section:**

Bad (spec-speak):
> Create a responsive hero section with a 2-column grid layout. The left column should contain
> an H1 heading (font-size: 48px, font-weight: 700) and a CTA button with a primary color
> background (#4F46E5). The right column should display a product screenshot with a CSS
> box-shadow of 0 25px 50px -12px rgba(0,0,0,0.25). Use Framer Motion for the entrance
> animation with staggered fade-in.

Good (human speak):
> Make a hero section that makes people stop scrolling. Big bold headline on the left, something
> that makes you feel "I need this." Under it a button that screams "click me." On the right, a
> screenshot of the product floating above the background with a soft shadow — like it's lifting
> off the page. Everything should fade in smoothly when the page loads, one piece at a time, like
> cards being dealt. Think Stripe's landing page energy.

**Example B — CLI tool (like RTK):**

Bad (requirements doc):
> Implement a command-line proxy in Rust that intercepts shell command output via process hooks.
> Apply regex-based filtering strategies including: statistical extraction, error-only mode,
> pattern grouping, deduplication, and intelligent truncation. Persist token metrics to SQLite
> via rusqlite with bundled mode. CLI parsing via clap v4 derive macros.

Good (conversational):
> Help me build a Rust CLI tool — think of it as a "noise canceling headphone" for terminal
> output. When AI coding tools run commands like git status or cargo test, they get flooded with
> boilerplate that wastes LLM tokens. My tool sits in the middle, strips the noise, keeps the
> signal. The user never knows it's there — commands run normally but the output is magically
> shorter and more useful. It should be a single binary, start instantly, and if anything goes
> wrong it just gets out of the way and lets the raw command through.

#### Prompt format — give the user this structure for each prompt:

```markdown
### Prompt [N]: [What this builds]

> [The actual prompt text — ready to copy-paste]

**What this adds:** [Brief explanation of what this step contributes]
**Why this prompt works:** [For learning — explain the technique used]
**Pro tip:** [Optional — a vibe coding insight this prompt demonstrates]
```

### Quality Gate — before you deliver

Run this checklist on every prompt before handing it to the user. If any item fails, fix it:

1. **Could a non-technical person understand this prompt?** — If it contains framework-specific
   jargon that the user didn't mention, rewrite in plain language. Exception: the user
   explicitly asked for a technical prompt.

2. **Does it describe the destination, not the route?** — "Make a sidebar that slides in from
   the left" (good) vs "Use CSS transform translateX" (bad). The AI knows the how. You provide
   the what and why.

3. **Would this prompt work on its own?** — Each prompt should be self-contained enough that
   someone could use it without the others. References to previous prompts are fine ("building on
   the page from the last step"), but the core request should stand alone.

4. **Is there a "done" condition?** — Can the user tell when the AI has completed the prompt
   successfully? If not, add one: "You'll know it's working when you see..."

5. **Did I include a not-to-do?** — At least one "don't" per prompt prevents scope creep.
   "Don't add authentication yet" or "Skip the mobile layout for now."

6. **Is this the simplest version?** — Could you remove a sentence and still get a good result?
   If yes, remove it. Bloated prompts confuse; lean prompts focus.

7. **Did I explain why?** — If the user is learning, every prompt should teach something. The
   "Why this prompt works" section should reveal the technique, not just restate the content.

Wrap up with:

1. **Overview** — A one-paragraph summary of what the prompts will produce
2. **The prompts** — Numbered, in the recommended order, using the format above
3. **Suggested order vs. alternatives** — "I recommend this sequence, but if you want to skip ahead to the interactive parts, start from Prompt 4"
4. **Next steps** — Suggestions for how to use these prompts:
   - "Try them one by one and see what happens at each step"
   - "Modify Prompt 3 to match your own brand colors"
   - "Combine Prompts 2 and 5 if you want a simpler version"

## Edge Cases

**Incomplete input** — User only has a partial screenshot or vague description. That's fine. Work with what you have, note what you're guessing, and ask the user to confirm or correct.

**Massive project** — A full web app with dozens of features. Don't try to deconstruct everything. Ask the user which feature or section they care about, and focus there.

**Something the user built themselves** — They want to "write it down as prompts for next time." This is actually easier — interview them about their decisions while building, then translate into prompts.

**Multiple similar products** — "I want prompts that capture what makes these 3 apps good." Identify patterns across them and write prompts that synthesize the best ideas.

**"I just want to learn vibe coding"** — No specific project in mind. Pick a well-known product as a teaching example (ask what they use daily), walk through the deconstruction as a tutorial, and explain the prompt craft along the way.

## Known Pitfalls

These are real issues that surfaced during testing. Guard against them:

- **Over-deconstructing simple products.** A login page doesn't need 8 prompts. If the product is simple, use Minimal or Fast Track. You're not being lazy — you're being appropriate. Too many prompts for a simple thing confuses the user more than helps.

- **Skipping Phase 2.** It's tempting to jump straight to deconstruction, especially when the user seems to know what they want. But "deconstruct Stripe" could mean "I want to learn API design" or "I want to build a payment system." The output is completely different. Always ask at least the purpose and output type.

- **Ignoring the user's skill level.** A prompt full of architectural jargon ("use a hexagonal architecture with dependency inversion") is useless to someone who just wants to learn. Match the prompt language to the user — the Phase 2 probing questions help you calibrate.

- **Missing the soul.** Every product has one thing that makes it *it*. Linear's soul is "keyboard-first speed", Notion's is "blocks as LEGO", Stripe's is "developer is the user". If your prompts don't capture this, they could be for any generic product. Name the soul explicitly in the output.

- **Foundation Prompt bloat.** The foundation prompt should be lean — tech stack, structure, base styles, conventions. Don't sneak in feature implementation. A bloated foundation prompt overwhelms the user and defeats the purpose of incremental prompts.

## Important Mindset

You're not just writing prompts — you're teaching the user how to think in prompts. Every prompt you write should help them understand *why* it's phrased that way. The goal is that eventually they won't need this skill anymore.

Be curious, be thorough, and don't be afraid to say "I'm not sure about this part — can you tell me more about what happens when...?"
