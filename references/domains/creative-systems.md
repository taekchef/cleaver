# Creative System Deconstruction Strategies

Strategies for Games, Animations, and Design Systems.

## Games / Interactive Entertainment

Games are fundamentally different from other products: the product IS the emotion. You're not
deconstructing a workflow or an interface — you're reverse-engineering fun, frustration, and flow.
The MDA framework (Mechanics → Dynamics → Aesthetics) is your primary tool: work backwards from
what the player feels (Aesthetics) to what creates those feelings (Dynamics) to the concrete rules
(Mechanics).

### Sub-types

**Puzzle** (like Tetris, Portal, Wordle): Logic and problem-solving, rule discovery.
Key decisions: rules & constraints, difficulty curve, "aha moment" design.
Deconstruct: rules and win/lose conditions first, then level progression, then difficulty tuning.

**RPG** (like Skyrim, Final Fantasy, Disco Elysium): Character progression, stats, narrative.
Key decisions: stat system design, skill trees, combat math, branching dialogue.
Deconstruct: stat/progression system first (it's the backbone), then combat/interaction, then narrative.

**FPS / Action** (like Doom, Celeste, Hollow Knight): Real-time combat, spatial navigation.
Key decisions: control feel, weapon/ability balance, enemy AI, level layout.
Deconstruct: core feel first (movement + combat responsiveness), then enemy design, then level design.

**Strategy** (like Civilization, Starcraft, XCOM): Resource management, planning, tactical decisions.
Key decisions: economy balance, unit diversity, tech tree depth, AI opponents.
Deconstruct: economy model first (currencies, sinks, sources), then unit/tech balance, then AI behavior.

**Casual / Match-3** (like Candy Crush, Gardenscapes): Simple mechanics, short sessions.
Key decisions: core loop tightness, session length, monetization integration, onboarding flow.
Deconstruct: core loop first, then session design, then monetization hooks.

**Idle / Incremental** (like Cookie Clicker, Universal Paperclips): Exponential growth, automation.
Key decisions: growth formulas, prestige layer design, unlock thresholds, offline calculation.
Deconstruct: growth curve first (the math), then prestige system, then automation unlocks.

**Roguelike / Roguelite** (like Hades, Slay the Spire, Balatro): Procedural generation + permadeath.
Key decisions: proc-gen algorithms, meta-progression between runs, run variance, build diversity.
Deconstruct: run structure first (what a single run looks like), then meta-progression, then proc-gen rules.

**Simulation** (like The Sims, Stardew Valley, Cities: Skylines): Modeled systems, emergent behavior.
Key decisions: system interdependencies, simulation depth, time mechanics.
Deconstruct: system map first (how systems connect), then individual system rules, then emergent interactions.

**Party / Social** (like Among Us, Overcooked, Jackbox): Multiplayer interaction, social dynamics.
Key decisions: player role asymmetry, communication mechanics, session pacing.
Deconstruct: social dynamics first (what creates the fun between players), then mechanics, then session flow.

### What to look for

- **Core loop**: the minute-to-minute action cycle — "explore → fight → loot → upgrade → repeat"
- **Progression system**: what grows over time? XP, levels, unlocks, prestige layers
- **Economy**: currencies, sources, sinks, exchange rates — often the hardest system to balance
- **Difficulty curve**: how challenge scales over time; too easy = boring, too hard = quit
- **Feedback / juice**: screen shake, particles, hit-stop, sound effects — what makes actions feel good
- **Content generation**: hand-crafted levels vs procedural vs player-created
- **Session design**: expected play session length, save system, mobile-friendly breakpoints
- **Failure states**: game over, death, permadeath — these are features, not bugs
- **Monetization integration**: how revenue mechanics weave into gameplay (energy, gacha, battle pass)
- **Onboarding / FTUE**: first-time user experience — if players don't "get it" fast, they leave

### Deconstruction order

1. **Core loop diagram** — draw the minute-to-minute action cycle; this is the heartbeat
2. **Aesthetic goals** — what emotions does the game target? (challenge, discovery, fellowship, narrative,
   sensation, expression, submission — from the MDA framework)
3. **Mechanics inventory** — every distinct mechanic: movement, combat, crafting, building, etc.
4. **Progression map** — what grows, how it grows, when it unlocks
5. **Economy model** — currencies, sources, sinks, key formulas
6. **Difficulty and balance** — challenge over time; extract actual numbers where possible
7. **Feel and polish** — feedback systems, visual/audio style, "game feel"
8. **Content scope** — number of levels/items/enemies; proc-gen rules if applicable
9. **Business and social** — monetization, multiplayer, retention mechanics

### Prompt tip

**The MDA Principle**: Start from the player's experience and work backwards. Don't start a game
prompt with "build a combat system with 50 HP and 3 weapons." Start with "build a game where
every fight feels like a puzzle — you need to read the enemy's pattern, find the opening, and
strike at exactly the right moment. Think Sekiro's posture system meets Slay the Spire's turn
structure." Let the mechanics emerge from the feeling.

**Core loop first**: The single most important artifact from game deconstruction is the core loop
diagram. If you can't draw the minute-to-minute cycle in 5 boxes or less, you don't understand
the game yet. Everything else — progression, economy, narrative — hangs off this loop.

**Balance is content**: In games, the numbers ARE the design. "Sword does 10 damage" isn't an
implementation detail — it's a product decision. Include actual numbers in prompts when possible,
and always specify the relationships between systems ("weapon damage scales with level, enemy HP
scales slightly faster").

**Cut ruthlessly**: Games have enormous scope. When writing recreation prompts, explicitly cut
everything that isn't essential to the core feel. "For the MVP, skip the crafting system, the
skill tree, and all secondary quests. Just nail the core combat loop."

---


## Animations / Interactions

Animation work is about timing, easing, and feel. These are hard to describe in words — use
comparisons and metaphors.

### Sub-types

**Page / Route Transitions** (like mobile app navigation, SPA transitions): Full-screen state changes.
Key decisions: enter/exit choreography, shared elements, duration vs perceived speed.
Deconstruct: identify each transition pair (A→B), then choreograph the movement.

**Micro-interactions** (like button feedback, toggle animations, hover effects): Small, frequent feedback.
Key decisions: timing curve, visual feedback type, consistency across the app.
Deconstruct: catalog every interactive element, then define the "feel system."

**Scroll-Driven** (like parallax, scroll-snap, reveal-on-scroll): Tied to scroll position.
Key decisions: trigger points, scroll-linked vs scroll-triggered, performance budget.
Deconstruct: map scroll positions to visual states, define threshold behavior.

**Data Visualization Animation** (like chart transitions, real-time updates): Data-driven motion.
Key decisions: enter/exit of data points, axis transitions, real-time update smoothness.
Deconstruct: define the data change types, then animate each type.

**Loading / Progress** (like skeleton screens, progress bars, optimistic UI): Perceived performance.
Key decisions: content-aware vs generic, progress accuracy, completion transition.
Deconstruct: identify each loading scenario, choose the right feedback type per scenario.

### What to look for

- **Trigger**: what causes the animation? (hover, click, scroll, load, state change, data update)
- **Duration**: how long? (under 300ms = instant, 300-500ms = smooth, over 500ms = slow)
- **Easing**: linear? ease-in? ease-out? spring? bounce? how does it "feel"?
- **Sequencing**: simultaneous? staggered? chained? what's the orchestration?
- **Physical metaphor**: gravity? rubber? water? glass? paper? magnetism?
- **Performance**: GPU-accelerated (transform, opacity) vs layout-triggering properties?
- **Reduced motion**: what happens when the user prefers reduced motion?

### Deconstruction order

1. **Catalog all animations** — list every animated thing on the page/screen
2. **Group by type** — page transitions, micro-interactions, scroll-driven, loading
3. **For each animation**: trigger → what changes → timing → easing → sequence → end state
4. **Identify the feel system** — is there a consistent timing/easing language?
5. **Edge cases** — interrupted, rapid-fire, reduced motion, low-performance devices

### Prompt tip

Use physical metaphors and comparisons. "Like a rubber ball bouncing to rest" conveys timing and
easing better than "use a custom cubic-bezier(0.68, -0.55, 0.265, 1.55)."

Reference real products by name: "The way iOS folders open" or "Stripe's page transitions" or
"the way Notion's sidebar collapses." The AI knows these products and can match the feel.

**Timing vocabulary cheat sheet** for your prompts:
- "Instant" → 0-100ms
- "Snappy" → 100-200ms
- "Smooth" → 200-400ms
- "Lush" → 400-600ms
- "Dramatic" → 600ms+

---


## Design Systems / Component Libraries

Design systems are about constraints and consistency. Deconstruct by identifying the system's
rules, not individual components.

### Sub-types

**Token System** (like design tokens, theme files): Pure constraints — colors, spacing, typography.
Key decisions: scale system (4px base? 8px?), color generation algorithm, semantic vs raw tokens.
Deconstruct: define scales first, then semantic mappings.

**Component Library** (like Radix, Headless UI, shadcn): Reusable UI primitives and composites.
Key decisions: composable API design, variant system, controlled vs uncontrolled, accessibility.
Deconstruct: primitives first, then composites, then patterns.

**Full Design System** (like Material UI, Ant Design): Tokens + components + patterns + docs.
Key decisions: theming model, customization escape hatches, documentation structure.
Deconstruct: tokens → primitives → composites → patterns → docs.

**Brand Style Guide** (like corporate brand guidelines): Visual identity rules, not code.
Key decisions: color usage rules, typography hierarchy, logo usage, do/don't examples.
Deconstruct: voice/tone → color rules → typography → layout principles → application examples.

### What to look for

- **Token system**: spacing scale, type scale, color palette, radii, shadows, z-index scale
- **Component hierarchy**: primitives → composites → patterns → templates → pages
- **Variant system**: how do components vary? (size, color, state, emphasis) — is it systematic?
- **Spacing rhythm**: consistent padding/margin patterns — is there a scale?
- **Responsive breakpoints**: where and how does the layout shift?
- **Documentation style**: Storybook? isolated pages? interactive playground?
- **Customization model**: CSS variables? theme object? style props? CSS-in-JS?

### Deconstruction order

1. **Design tokens** — colors, spacing, typography, radii, shadows (the rules everything follows)
2. **Primitives** — Button, Input, Badge, Avatar, Icon (the building blocks)
3. **Composites** — Card, Modal, Dropdown, DataTable, Form (combinations of primitives)
4. **Layout patterns** — Grid, Stack, Sidebar, responsive containers (how things arrange)
5. **Animation/motion system** — timing, easing, choreography rules
6. **Documentation** — how to present the system, usage examples

### Prompt tip

Define the constraints first. "All spacing is a multiple of 4px. Buttons come in 3 sizes and
4 variants. The color palette has 10 shades per hue." This gives the AI a rule engine to follow,
and every component it builds will be consistent automatically.

**Critical insight**: The system IS the value. Don't prompt for individual components without
establishing the system first. A "Button" prompt without the variant system and token system
will produce a one-off button, not a system button.

---


---

## Choosing the Right Strategy

When you identify the project's domain, ask yourself:

1. **What domain?** — 10 domains: CLI Tools, Web Apps, Landing Pages, Animations, Design Systems,
   Mobile Apps, Physical Products, Games, API/Backend, AI/ML Products. Some products span multiple
   domains (Tesla = vehicle + dashboard UI + autonomous agent) — ask which aspect the user cares about,
   or cover each in separate prompt sets.

2. **What sub-type is this?** — Most projects fit one sub-type clearly. If it's a hybrid, decompose
   by the dominant sub-type and note the secondary influences. Games are often genre hybrids (Hades =
   roguelike + action RPG + narrative).

3. **What output does the user want?** — Code prompts? PRD? Design brief? Game Design Document?
   API spec? System prompt? This determines everything about how you write the prompts. AI products
   can output code (the wrapper), a system prompt (the invisible layer), or an architecture spec
   (the full stack).

4. **What's the deconstruction priority?** — Each domain has a different "what matters most."
   Productivity tools → interaction model. Games → core loop + feel. Landing pages → emotional arc.
   APIs → data model + error design. AI products → system prompt + context pipeline. Physical
   products → sensory + interaction loop. Get this wrong and the prompts will feel off.

5. **Where does complexity live?** — Is the hard part the data model (APIs), the interaction design
   (web/mobile), the game balance (games), the prompt architecture (AI products), the physical feel
   (hardware), or the service process (experiences)? Focus your detailed prompts on where the
   complexity is.

6. **What would the user miss if they built it without this skill?** — That's what your prompts
   need to capture. The obvious stuff doesn't need detailed prompts. The non-obvious stuff does:
   why Linear feels fast (keyboard-first design), why Stripe feels premium (micro-interactions),
   why Hades is addictive (core loop + meta-progression), why Perplexity cites sources (RAG pipeline,
   not just system prompt), why the iPhone feels designed for your hand (material + weight + radius).
