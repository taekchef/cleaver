# Physical Product & Service Deconstruction Strategies

Strategies for physical and real-world products.

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

---

See shared decision framework in any domain file under "Choosing the Right Strategy".
