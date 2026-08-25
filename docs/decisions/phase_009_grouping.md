# Decision Records — Phase 009 Logical Grouping

Continues after D-890.

### D-891 — Review Phase 009 as eight dependency-ordered integration-contract groups
**Status:** Accepted — Phase 009 foundation
The groups are: contract vocabulary/source roles; identity/governance/authority/authorization; change/deployment/execution/version/runtime; health/schema/metrics/reference/reconciliation; Lineage/consumer/Impact; Investigation/causality/controls; Explanation/history/basis/disclosure; cross-source consolidation/exit.

### D-892 — Use INTG-### for Phase 009 integration-contract refinements
**Status:** Accepted — Phase 009 foundation
The namespace maps accepted product semantics to source capability. It does not define adapter/service/storage/event architecture or create new truth concepts.

### D-893 — Organize Phase 009 by evidence responsibility rather than vendor silo
**Status:** Accepted — Phase 009 foundation
Databricks, Unity Catalog, GitHub, DQX, Metric Views, Collibra, Immuta and downstream instrumentation may each support multiple concepts; one proposition may require multiple source families.

### D-894 — Source availability, authority, sufficiency and authorization remain separate
**Status:** Accepted — Phase 009 foundation
A queryable source is not automatically authoritative; an authoritative assertion is not automatically sufficient evidence; accessible evidence is not automatically authorized for disclosure.

### D-895 — Identity joins, temporal semantics and coverage are first-class integration-contract dimensions
**Status:** Accepted — Phase 009 foundation
Cross-system association must preserve source-local identity/reconciliation evidence, event/effective versus recorded/knowledge time and the exact population/path/opportunity coverage required by the proposition.

### D-896 — Negative-evidence capability must be evaluated explicitly
**Status:** Accepted — Phase 009 foundation
A source that can establish positive events may still be unable to prove `no run`, `no path`, `not exposed`, `no effect` or `not enforced`. Missing telemetry cannot satisfy a strong-negative burden.

### D-897 — Unsupported or partially supported product requirements are valid Phase 009 outcomes
**Status:** Accepted — Phase 009 foundation
Integration gaps must be recorded explicitly rather than hidden by weakening the accepted REF/AUTH/HLTH/OPS/EXPL semantics.

### D-898 — Phase 009 remains architecture-neutral
**Status:** Accepted — Phase 009 foundation
No SDK, adapter, polling/streaming, event bus, persistence schema, graph store, cache, credential, LLM/retrieval or deployment topology is selected. Phase 010 owns technical architecture.

### D-899 — Phase 009 grouping is accepted; Group 01 is next
**Status:** Accepted — Phase 009 foundation
No INTG contracts are accepted yet. Canonical repository status may remain `NEXT — not started` until Group 01 semantic contract work begins.
