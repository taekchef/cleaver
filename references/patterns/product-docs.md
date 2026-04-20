# Product Document Prompt Patterns

Patterns for generating product documents: PRD, Design Brief, Experience-to-Spec, GDD.

- [Pattern 7: PRD Generator](#pattern-7-prd--product-spec-generator) — Physical products, specs
- [Pattern 8: Design Brief](#pattern-8-design-brief-generator) — Industrial design direction
- [Pattern 9: Experience-to-Spec](#pattern-9-experience-to-spec-translator) — Feel to measurements
- [Pattern 10: GDD Generator](#pattern-10-game-design-document-gdd-generator) — Game design docs

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

