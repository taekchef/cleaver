# Digital Product Deconstruction Strategies

Strategies for Web Apps / SaaS, Landing Pages, and Mobile Apps.

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
