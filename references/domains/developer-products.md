# Developer Product Deconstruction Strategies

Strategies for CLI Tools and API / Backend Architecture.

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

---

See shared decision framework in any domain file under "Choosing the Right Strategy".
