# AI Product Deconstruction Strategies

Strategies for AI / ML Products.

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
