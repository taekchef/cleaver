# Domain-Specific Deconstruction Strategies

The 6-layer framework in the main skill works for everything, but different project types benefit
from specialized deconstruction approaches. Use these as starting points when you identify the
project's domain.

**Each domain has sub-types** — identify which sub-type you're dealing with before choosing the
deconstruction order. The wrong sub-type leads to wrong prompts.

---

## CLI Tools

CLI tools have a unique structure: the interface IS the product. There's no visual UI to
deconstruct — instead, focus on the command design philosophy.

### Sub-types

**Filter / Proxy** (like RTK, proxychains): Intercepts and transforms existing commands.
Key decisions: what to intercept, how to transform, fallback behavior.
Deconstruct: pipeline first (intercept → transform → output), then breadth of coverage.

**Generator / Scaffold** (like create-react-app, cargo new): Creates project structure from templates.
Key decisions: what to generate, how to handle options, post-generation instructions.
Deconstruct: output structure first (what gets created), then option system, then hooks.

**DevOps / Automation** (like terraform, docker): Manages infrastructure or automates workflows.
Key decisions: state management, idempotency, dry-run support.
Deconstruct: state model first (what's being managed), then operations, then output.

**Analysis / Query** (like ripgrep, jq, sqlite3): Queries and analyzes data.
Key decisions: query language design, output format flexibility, performance at scale.
Deconstruct: query model first (what can you ask), then output format, then performance.

**REPL / Interactive** (like python, node, psql): Interactive sessions with state.
Key decisions: session model, history, completion, multi-line input.
Deconstruct: interaction model first (how sessions work), then commands, then persistence.

### What to look for

- **Command hierarchy**: how are subcommands organized? (git-style: `tool <verb> <args>`)
- **Flag design**: which flags are short (`-v`) vs long (`--verbose`)? any flag groups?
- **Output philosophy**: human-readable vs machine-parseable? when do they differ? color usage?
- **Error handling**: how does it communicate failures? exit codes, stderr usage, helpful suggestions
- **Performance contract**: what's the overhead? startup time, memory usage
- **Installation story**: single binary? package manager? auto-update?
- **Fallback behavior**: what happens when things go wrong? graceful degradation?
- **Config system**: file-based? env vars? CLI flags? priority order?

### Deconstruction order

1. **Core value prop** — one sentence metaphor ("noise-canceling headphones for terminal output")
2. **Command interface** — verbs, flags, subcommands, the "grammar" of the tool
3. **Processing pipeline** — input → transform → output, the main data flow
4. **Output formatting** — how results are presented, compact vs verbose modes
5. **Error handling & fallback** — what happens when things go wrong
6. **Config & extensibility** — how users customize behavior
7. **Distribution** — installation, updates, platform support

### Prompt tip

Use metaphor-based descriptions. "Think of it as a noise-canceling headphone for terminal output"
conveys more than "a CLI proxy that filters command output." The AI understands metaphors and
will make better design decisions.

**Common trap**: describing the implementation instead of the behavior. "Apply regex-based filtering
with pattern grouping" is implementation. "Show me just the errors, grouped by type" is behavior.
Always prompt with behavior.

---

## Web Apps / SaaS Dashboards

Dashboards are information-dense and have complex state. The key challenge is decomposing the
information architecture.

### Sub-types

**Productivity Tool** (like Linear, Notion, Jira): High-frequency use, keyboard-first, data-dense.
Key decisions: keyboard shortcuts, inline editing, performance perception, command palette.
Priority: interaction model → data model → visual density → polish.
Tell-tale signs: CMD+K menu, extensive keyboard shortcuts, inline editing, compact lists.

**Data Dashboard** (like Grafana, Mixpanel, Metabase): Visualization-heavy, read-mostly, filter-driven.
Key decisions: chart types, filter system, time range handling, data refresh strategy.
Priority: data model → visualization → filters → sharing/export.
Tell-tale signs: charts everywhere, time range pickers, drill-down interactions, saved views.

**CRUD Admin** (like admin panels, back-office): Form-heavy, create/read/update/delete operations.
Key decisions: form design, validation patterns, bulk actions, search & pagination.
Priority: data model → list views → forms → validation → bulk ops.
Tell-tale signs: data tables with pagination, create/edit modals, simple filtering.

**Collaboration Hub** (like Slack, Figma, Google Docs): Real-time, multi-user, presence-aware.
Key decisions: real-time sync model, conflict resolution, presence indicators, notifications.
Priority: real-time architecture → core editing → collaboration features → notifications.
Tell-tale signs: user avatars/presence cursors, typing indicators, comment threads, activity feeds.

**Content Platform** (like Medium, Shopify storefront, WordPress): Content-first, layout-flexible.
Key decisions: content model, editor experience, rendering performance, SEO.
Priority: content model → editor → rendering → layout system → SEO.
Tell-tale signs: rich text editors, media management, template/theme system, URL structure.

### What to look for

- **Layout grid**: sidebar + main? top nav? tabs within tabs? resizable panels?
- **Information density**: how much data per screen? data tables? cards? charts? single-column?
- **Filtering and search**: global search? per-section filters? saved filters? CMD+K?
- **State machine**: what are the key states? (loading, empty, error, populated, editing)
- **Data freshness**: real-time? polling? manual refresh? optimistic updates?
- **Role-based views**: does different data show for different users?
- **Action patterns**: inline edit? modal edit? bulk actions? keyboard shortcuts? drag-and-drop?
- **Interaction complexity**: minimal (click to navigate) vs rich (shortcuts, drag, inline edit, gestures)?

### Decision: Data model first vs UI first?

This is the most important judgment call for web apps.

**Data model first** when:
- The app has clear entities with relationships (Issue → Project → Team)
- UI is predictable from data structure (if you know the entities, you know the screens)
- Most screens are "views of data" rather than "unique experiences"
→ Typical for: Productivity tools, CRUD admins, content platforms

**UI first** when:
- The app's value is in how it presents data, not what data it has (visualizations)
- Same data is shown differently in different contexts (dashboard vs detail)
- The "feel" matters more than the data model
→ Typical for: Data dashboards, collaboration tools

**Both equally** when:
- Complex data model AND unique visualizations of that data
→ Start with data model, then UI, but reference each other

### Deconstruction order

1. **Layout shell** — nav, sidebar, content area, panel system
2. **Information architecture** — what sections, what hierarchy, user's mental map
3. **Core data views** — tables/lists with sorting, filtering, pagination
4. **Detail/edit views** — forms, panels, inline editing patterns
5. **Visualization** (if applicable) — charts, status indicators, progress
6. **Interaction layer** — keyboard shortcuts, command palette, drag-and-drop
7. **State management** — loading, empty, error, optimistic updates
8. **Cross-cutting** — search, notifications, settings, team switching

### Prompt tip

Describe the "day in the life" — what the user does first, second, third. This gives the AI a
narrative to follow instead of a disconnected list of features.

**For productivity tools specifically**: Describe the keyboard flow. "The user opens the app,
presses C to create an issue, types the title, presses CMD+Enter to save, then presses J to
jump to the next item." This teaches the AI that keyboard is the primary interface.

**For dashboards specifically**: Describe the question the user is answering. "The user opens
the dashboard to answer 'are we on track this week?' — they look at the main metric, compare
to last week, drill into any anomaly." This teaches the AI what data to surface first.

---

## Landing Pages / Marketing Sites

Landing pages are about conversion — every section has a job. Deconstruct by section purpose,
not visual appearance.

### Sub-types

**SaaS Product Page** (like Linear, Vercel, Stripe): Product-led, feature showcase, pricing-driven.
Key decisions: hero message, feature presentation style, pricing psychology, social proof strategy.
Conversion model: value prop → features → proof → pricing → signup.

**Product Launch / Campaign** (like Apple events, product drops): Time-bound, story-driven, dramatic.
Key decisions: reveal sequence, visual drama, countdown/urgency, media assets.
Conversion model: tease → reveal → desire → pre-order/signup.

**Portfolio / Personal** (like developer portfolios, agency sites): Personality-driven, work showcase.
Key decisions: personal brand voice, project presentation, contact flow, unique visual identity.
Conversion model: who I am → what I've done → why I'm good → get in touch.

**Documentation / Product-Led Growth** (like Stripe docs, Tailwind CSS): Education-first, interactive.
Key decisions: code examples, interactive demos, search quality, progressive disclosure.
Conversion model: learn → try → adopt → pay.

### What to look for

- **Section sequence**: what story does the page tell? what's the emotional arc?
- **Hero strategy**: what's above the fold? headline + subhead + CTA + visual? animation?
- **Social proof placement**: testimonials, logos, metrics — where and how?
- **Pricing section**: tiers, feature comparison, anchor pricing, annual discount?
- **Animation philosophy**: scroll-triggered? subtle or dramatic? performance-conscious?
- **Mobile experience**: is mobile a truncated desktop or a different layout entirely?
- **Copy tone**: professional? casual? technical? playful? aspirational?
- **CTA strategy**: single vs multiple CTAs? primary vs secondary? button style?

### Deconstruction order

1. **Hero section** — headline, subhead, CTA, visual — the whole above-the-fold story
2. **Problem/Agitation** — why the user needs this (if present)
3. **Solution/Features** — what it does, usually with visuals or demos
4. **Social proof** — testimonials, case studies, metrics, logos
5. **Pricing** (if applicable) — tiers, comparison, anchor
6. **Final CTA / Footer** — the last push
7. **Animation & motion** — scroll behaviors, transitions, micro-interactions

### Prompt tip

Describe the emotional journey. "Start with tension — the user feels the problem. Then relief —
here's the solution. Then confidence — look at all these people who succeeded. Then urgency —
start now." The AI creates better copy when it understands the emotional arc.

**For SaaS pages**: Be specific about pricing psychology. "Show three tiers. The middle one should
be highlighted as 'most popular.' The expensive one makes the middle one look reasonable. The cheap
one exists so there's an entry point." This teaches the AI about anchoring.

**For portfolio sites**: Describe the personality, not the layout. "I want it to feel like walking
into my apartment — a bit messy but in a curated way, lots of personality, personal projects
displayed like souvenirs." This is more useful than "2-column grid with project cards."

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

## Mobile Apps

Mobile apps are defined by platform conventions and gesture-based interaction. Deconstruct by
screen flow and touch behavior.

### Sub-types

**Content Consumption** (like Instagram, TikTok, Kindle): Scroll-heavy, media-first, minimal UI.
Key decisions: content format, infinite scroll vs pagination, media loading, offline caching.
Deconstruct: content card → feed/list → detail view → sharing/engagement.

**Productivity / Utility** (like Todoist, 1Password, Apple Notes): Task-focused, quick interactions.
Key decisions: quick capture, widget support, Siri/shortcuts integration, data sync.
Deconstruct: primary action → list view → detail/edit → sync/notifications.

**Social / Communication** (like WhatsApp, Discord, Twitter): Real-time, message-focused, presence.
Key decisions: message format, notification strategy, media handling, threading model.
Deconstruct: conversation list → chat view → message input → media/presence.

**E-commerce / Marketplace** (like Amazon, Taobao, Airbnb): Browse → filter → detail → purchase.
Key decisions: product card design, filter UX, checkout flow, payment integration.
Deconstruct: browse/search → filters → product detail → cart → checkout.

**On-device / Offline-First** (like photo editors, note apps, fitness trackers): Works without network.
Key decisions: local storage model, sync strategy, conflict resolution, background processing.
Deconstruct: local data model → core features → sync layer → error recovery.

### What to look for

- **Navigation model**: tab bar? drawer? stack navigation? hybrid? gesture-based?
- **Screen flow**: what's the primary path? what are the branches? modal vs push?
- **Gesture vocabulary**: swipe, pull-to-refresh, long-press, pinch, drag? custom gestures?
- **Platform conventions**: iOS vs Android differences? Material vs Human Interface?
- **Offline behavior**: what works without network? how does sync happen? conflict resolution?
- **Input patterns**: bottom sheets, inline editing, floating action button, swipe actions?
- **Performance model**: lazy loading? image caching? virtualized lists? skeleton screens?

### Deconstruction order

1. **Navigation model and primary screen flow** — the main path through the app
2. **Key screens** — one at a time, by frequency of use (home screen first)
3. **Gesture interactions and transitions** — native gestures, custom gestures, screen transitions
4. **Data flow** — what loads when, what's cached, what's real-time
5. **Offline and error states** — no network, slow network, data conflicts
6. **Platform-specific adaptations** — iOS vs Android differences, responsive tablets
7. **Notifications and widgets** — push, deep links, home screen widgets

### Prompt tip

Describe the thumb zone. "The primary action should be reachable with one hand" conveys placement
better than "position at bottom of screen."

Reference platform conventions by name: "Use iOS-style swipe-to-go-back" saves you from describing
the entire animation. "Material bottom sheet" is universally understood.

**For cross-platform apps**: Decide early — shared codebase (React Native/Flutter) or native per
platform? Include this in the first prompt. It fundamentally changes every subsequent prompt.

---

## Physical / Real-World Products

Physical products have a different deconstruction challenge — you can't "read the source code."
Instead, observe behavior, feel, and user experience. The prompts you produce might target code
(the product's digital interface), a PRD (for building something similar), or a design brief
(for industrial designers).

### Sub-types

**Consumer Electronics** (like iPhone, AirPods, Dyson): Personal, tactile, daily-use.
Key decisions: material language, button/interaction design, unboxing experience, charging/battery UX.
Output options: PRD for similar product, UI code for companion app, design brief for industrial design.
Tell-tale signs: you hold it daily, it has buttons/ports/screens, unboxing matters.

**Vehicles / Mobility** (like Tesla, Xiaomi SU7, Segway): Complex, multi-system, safety-critical.
Key decisions: dashboard UI, driving dynamics, charging/fueling experience, cabin comfort.
Output options: PRD for vehicle spec, dashboard UI code, service blueprint for ownership experience.
Tell-tale signs: large price tag, safety matters, has both physical and digital interfaces.

**Home / Living** (like Nest thermostat, Philips Hue, rice cookers): Ambient, set-and-forget.
Key decisions: setup simplicity, indicator design (lights, sounds), app integration, mounting/install.
Output options: PRD for smart home product, companion app code, setup flow design.
Tell-tale signs: lives in your home, mostly automatic, occasional interaction.

**Apparel / Fashion** (like Uniqlo, Patagonia, Arc'teryx): Wearable, sensory, identity-expressive.
Key decisions: material choice, fit system, color palette, sizing, durability signals.
Output options: PRD for product line, brand positioning doc, e-commerce site prompts.
Tell-tale signs: you wear it, fabric/fit is the core experience, brand story matters.

**Food / Beverage** (like Starbucks, HeyTea, Coca-Cola): Consumable, ritual-driven, sensory.
Key decisions: flavor profile, ordering experience, packaging, pricing psychology, ritual design.
Output options: PRD for product, service blueprint for ordering experience, brand positioning.
Tell-tale signs: you consume it, preparation matters, repeat purchase is the goal.

**Service / Experience** (like Apple Store, Disneyland, airline lounge): Process-driven, human-centric.
Key decisions: customer journey stages, staff scripts, environment design, wait management.
Output options: service blueprint, staff training prompt, environment design brief.
Tell-tale signs: it's an experience not a thing, humans are part of the delivery, time matters.

### What to look for

- **First encounter**: how does the user discover, evaluate, and decide to buy?
- **Unboxing / onboarding**: what's the first 5 minutes like? delight or frustration?
- **Core interaction loop**: what does the user do most? what feedback do they get?
- **Sensory profile**: visual, tactile, auditory, olfactory, gustatory — what stands out?
- **Material language**: premium (metal, glass) vs utilitarian (plastic, rubber) vs natural (wood, fabric)?
- **Interface points**: buttons, screens, LEDs, sounds, haptics, labels — how does it communicate?
- **Error states**: what happens when something goes wrong? how does it recover?
- **Maintenance lifecycle**: charging, cleaning, replacing, upgrading — how does it age?
- **Social dimension**: does owning/using it say something about the user?
- **Digital companion**: does it have an app? how do physical and digital connect?

### Decision: What output does the user want?

Physical products can produce wildly different prompt outputs. Ask explicitly:

- **Code prompts** → for the product's digital interface (dashboard, app, website)
- **PRD prompts** → for building a similar product (requirements, specs, constraints)
- **Design brief prompts** → for industrial designers (materials, form, ergonomics)
- **Service blueprint prompts** → for the customer journey (process, touchpoints)
- **Learning prompts** → to understand the product thinking behind decisions

### Deconstruction order

1. **Product identity** — what is it, for whom, what job does it do (one sentence + metaphor)
2. **Sensory and material analysis** — what does it look/feel/sound like? what's the build language?
3. **Core interaction loop** — what does the user do most often? how does it respond?
4. **Onboarding journey** — purchase → unbox → setup → first use → mastery
5. **Interface points** — every way the product communicates with the user (physical + digital)
6. **Error and edge states** — low battery, misuse, wear and tear, accidents
7. **Lifecycle and maintenance** — daily → weekly → monthly → yearly → end of life
8. **Social and identity layer** — what does owning this say about the user?

### Prompt tip

**The Apple Principle**: Start with the experience, not the spec. Apple's iPod was defined as
"1,000 songs in your pocket" — not "5GB hard drive + FireWire." When deconstructing physical
products, always express the requirement as the user experience first, then let the AI figure
out the implementation. "It should feel like picking up a river stone — smooth, weighted,
comforting" is a better prompt than "aluminum body, 150g, anodized finish."

**For PRD output**: Hardware PRDs have unique structure that differs from software PRDs.
Include these sections when generating a physical product PRD:

- **Stakeholder map** — not just the user, but the buyer (often different), installer,
  maintainer, and recycler
- **Experience requirements** — what it must feel like (not technical specs)
- **Anti-use-cases** — what this product is explicitly NOT for (as important as use cases)
- **Validation milestones** — EVT (Engineering Validation Test) → DVT (Design Validation
  Test) → PVT (Production Validation Test) → Mass Production
- **Cross-cutting aspects** — hardware (mechanical/electrical/thermal), software (firmware/
  app/cloud), design (ID/CMF/ergonomics), manufacturing (process/tolerances/assembly),
  regulatory (certifications by market)
- **BOM cost target** — bill of materials budget per unit at volume

**For design brief output**: Describe the emotional target, not the form factor. "It should
look like it belongs on a CEO's desk, not in a teenager's backpack" gives the designer a
clear creative direction.

**For experience-to-spec translation**: When the user describes a feeling, help them translate
it into measurable parameters. "Premium feel" becomes: surface roughness (Ra < 0.4 μm),
weight (150-200g for handheld), actuation force (2-4N for buttons), acoustic signature
(< 45dB click sound). This bridges the gap between vibe and specification.

**For service blueprint output**: Walk through the journey in real time. "The customer walks in,
is greeted within 10 seconds, is offered a seat, has their order taken within 2 minutes,
receives their drink in under 5 minutes." This level of temporal detail is what makes service
blueprints actionable.

---

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

## API / Backend Architecture

Backend deconstruction is different from frontend because there's no visual surface to study.
Instead, the **interface contract** (API design, data model, error behavior) IS the product.
You're reverse-engineering architecture decisions from observable behavior: request patterns,
response structures, error messages, rate limit headers, and latency characteristics.

### Sub-types

**REST API** (like Stripe, GitHub, Twilio): Resource-oriented, HTTP verbs, predictable URLs.
Key decisions: resource naming, pagination strategy, idempotency, versioning approach.
Deconstruct: resource model first (what entities exist, how they relate), then endpoints, then error model.

**GraphQL API** (like Shopify, GitHub v4, Contentful): Query language, client-driven fetching.
Key decisions: schema design, resolver complexity, N+1 prevention, query depth limits.
Deconstruct: schema first (types, relations, mutations), then resolver patterns, then performance.

**Real-time / WebSocket** (like Slack, Discord, Figma): Persistent connections, push updates.
Key decisions: connection lifecycle, event taxonomy, conflict resolution, reconnection strategy.
Deconstruct: event model first (what events exist, when they fire), then connection management, then state sync.

**Event-Driven / Messaging** (like Kafka-based systems, Stripe webhooks): Async processing, event sourcing.
Key decisions: event schema design, ordering guarantees, consumer patterns, dead letter handling.
Deconstruct: event taxonomy first (what events, what payload), then topology, then failure handling.

**Data Pipeline / ETL** (like Fivetran, Airbyte): Extract, transform, load workflows.
Key decisions: connector architecture, transformation model, scheduling, data quality checks.
Deconstruct: data flow first (sources → transforms → destinations), then scheduling, then monitoring.

**SDK / Library** (like Stripe SDK, AWS SDK, Prisma): Developer-facing tooling.
Key decisions: API surface design, error handling pattern, configuration approach, documentation.
Deconstruct: public interface first (what developers call), then configuration, then error handling.

### What to look for

- **Data model**: what are the core entities? how do they relate? what's the cardinality?
- **Authentication model**: API keys? OAuth? JWT? session-based? what scopes exist?
- **Error design**: error response structure, error codes, error hierarchy, retry guidance
- **Pagination strategy**: cursor-based? offset? page-based? what are the trade-offs?
- **Rate limiting**: headers (X-RateLimit-*), backoff strategy, per-user vs per-key
- **Versioning approach**: URL path (/v1/)? header? query param? how do they deprecate?
- **Idempotency**: which operations are idempotent? idempotency keys? retry safety?
- **Consistency model**: eventual vs strong? read-after-write guarantees? caching layer?
- **Observability**: logging, metrics, tracing — what's visible to the user?
- **Webhooks / callbacks**: event types, delivery guarantees, retry logic, signature verification

### Deconstruction order

1. **Data model** — core entities, relationships, cardinality (the foundation of everything)
2. **API surface** — endpoints/operations, naming conventions, HTTP method usage
3. **Request/response patterns** — payload structure, content negotiation, encoding
4. **Auth and security** — how you authenticate, what you can do, scope model
5. **Error model** — error structure, codes, hierarchy, recovery guidance
6. **Operational contracts** — rate limits, pagination, filtering, sorting, idempotency
7. **Performance and scaling** — caching, async patterns, consistency guarantees
8. **Developer experience** — docs quality, SDK design, playground/sandbox, onboarding

### Prompt tip

**The Contract IS the spec**: When deconstructing backends, the API contract (endpoints, request/
response shapes, error codes) replaces the UI as the primary analysis surface. Treat OpenAPI specs,
GraphQL schemas, and WebSocket event lists like you'd treat a UI component inventory.

**Stripe as reference**: Stripe's API is widely considered the gold standard. Key patterns worth
capturing in prompts: consistent envelope structure (`{ object, data, has_more }`), expandable
relations (`?expand[]=customer`), idempotency keys, and the clearest error messages in the industry.
When writing backend prompts, "think Stripe's API design" conveys more than listing REST conventions.

**Error handling is a feature**: Most backend deconstructions under-invest in error design. But
error messages, retry headers, and failure guidance are what separate a good API from a great one.
Include error behavior in every prompt — "when the request fails because the resource doesn't exist,
return a structured error with the resource type, the attempted ID, and a suggestion for what
the user might have meant."

---

## AI / ML Products

AI products are a unique deconstruction challenge because the **system prompt + context pipeline + model
selection strategy** IS the product — not the UI. The interface is often a thin wrapper around an LLM.
A 2025 analysis of 200 funded AI startups found 73% are repackaged base models with new prompt layers.
This means the core IP is invisible: it lives in the system prompt, the context assembly logic,
and the model routing decisions — not in the frontend.

### Sub-types

**Chatbot / Assistant** (like ChatGPT, Claude, Gemini): Multi-turn conversation with tool use.
Key decisions: system prompt architecture, tool/function call schemas, memory management, safety guardrails.
Deconstruct: system prompt layers first (identity, tools, rules), then context pipeline, then tool orchestration.

**Image / Visual Generation** (like Midjourney, DALL-E, Flux): Text-to-image diffusion.
Key decisions: prompt enhancement pipeline, parameter mapping, style control, negative prompts.
Deconstruct: user-facing controls first (what parameters users can tweak), then the hidden prompt
enhancement pipeline, then output quality patterns.

**Code Assistant / AI IDE** (like Cursor, Copilot, Claude Code, v0): Code generation with tool access.
Key decisions: context window management, tool definitions, agentic loop pattern, error auto-fix.
Deconstruct: context strategy first (how code gets into the prompt), then tool schemas, then agentic behavior.

**Search / Answer Engine** (like Perplexity, Google AI Overview): Retrieval-augmented generation with citations.
Key decisions: retrieval pipeline, citation grounding, freshness management, multi-step reasoning.
Deconstruct: retrieval pipeline first (where data comes from), then synthesis strategy, then citation system.

**Writing / Content** (like Jasper, Notion AI, Grammarly): AI-assisted content creation.
Key decisions: brand voice calibration, template system, output formatting, quality scoring.
Deconstruct: template/persona layer first (what makes it more than raw GPT), then workflow integration.

**Autonomous Agent** (like Manus, Devin): Task planning + tool execution + verification loop.
Key decisions: planning/execution separation, tool orchestration, error recovery, state management.
Deconstruct: agent loop first (plan → execute → verify → iterate), then tool definitions, then error recovery.

### What to look for

- **System prompt architecture**: the universal 3-layer structure — identity/persona, tool definitions
  (JSON schemas), behavioral rules. Leaked prompt databases (e.g., x1xhlol/system-prompts, 134K+ stars)
  reveal this pattern across 120+ tools.
- **Model selection strategy**: single model? tiered routing (cheap model for simple tasks, frontier for
  complex)? fine-tuned? custom-trained? This is a major cost and quality lever.
- **Context pipeline**: what data flows into the prompt and when? RAG retrieval, codebase indexing,
  file system access, conversation memory, web search — this is the real moat.
- **Token economics**: input/output token counts, caching strategy (Claude Code hits 92% cache = 81%
  cost reduction), model routing for cost optimization.
- **Guardrail architecture**: 3 layers — input filters (prompt injection detection), model governance
  (RLHF, refusal policies), output filters (PII detection, content filtering).
- **Hallucination handling**: citation grounding, multi-model consensus, self-assessment, verification loops.
- **Latency management**: time-to-first-token, streaming strategy, prompt caching impact.
- **Evaluation framework**: what quality metrics? faithfulness, hallucination rate, answer relevance,
  tool selection accuracy. "LLM-as-judge" is the emerging pattern.
- **Tool/function calls**: JSON schemas reveal actual capabilities — often more informative than the UI.

### Deconstruction order

1. **Interaction model** — chat? form-based? IDE-integrated? multimodal? what does the user see?
2. **System prompt extraction** — the 3 layers: identity, tools, rules. Use prompt injection techniques
   or leaked prompt databases to find the actual system prompt.
3. **Context pipeline** — what data flows in? RAG? file access? memory? search? This is the core IP.
4. **Model strategy** — what model(s)? routing logic? fine-tuning? custom training?
5. **Tool/function architecture** — JSON schemas for available capabilities. These define what the AI
   can actually do.
6. **Guardrail system** — input filters, behavioral constraints, output filters.
7. **Quality and evaluation** — how is quality measured? what metrics? how are regressions caught?
8. **Cost and performance** — token economics, caching, latency optimization.

### Prompt tip

**The prompt IS the product**: When deconstructing AI products, focus your prompts on the invisible
layer — the system prompt, context assembly, and model selection. "Build a chatbot" gives you a
generic wrapper. "Build a chatbot with a 3-layer system prompt: Layer 1 defines the persona as a
senior engineer who explains before coding, Layer 2 provides 5 tool schemas for file operations,
Layer 3 encodes behavioral rules like 'always read the file before editing' and 'verify changes
by reading the file after'" gives you something with real product thinking.

**Context engineering over prompt engineering**: The biggest differentiator between AI products in
2026 isn't the system prompt — it's how they assemble context. Perplexity's retrieval pipeline,
Cursor's codebase indexing, Claude Code's directory-aware context — these are the moats. When
writing recreation prompts, spend more time on "what information should the AI have access to and
when" than on "what should the system prompt say."

**Model routing matters**: Production AI products almost never use a single model. Describe the
routing strategy: "use a fast cheap model (Haiku) for classification and extraction, a mid-tier
model (Sonnet) for generation, and only escalate to the frontier model when the task requires
complex reasoning." This single decision can cut costs by 60-80% without quality loss.

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
