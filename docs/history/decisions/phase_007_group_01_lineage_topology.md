# Decision Records — Phase 007 Group 01 Lineage / Historical Topology

Continues after D-405.

### D-406 — Phase 007 Group 01 requires no new concept
**Status:** Accepted — Phase 007 Group 01
The accepted Lineage concept remains the correct truth owner for typed temporal relationship state, traversal and topology history. Group 01 requires refinements rather than a 25th concept.

### D-407 — A Lineage relationship is a bounded proposition, not a generic edge
**Status:** Accepted
Relationship identity includes source/target Entity Identity, relationship family, material semantic scope/role/context/version and effective interval. Same endpoints can have several different relationships simultaneously.

### D-408 — Adopt five minimum operational Lineage relationship families
**Status:** Accepted
The minimum families are `data_derivation`, `production`, `operational_dependency`, `publication` and `consumption_path`. Relationship roles qualify these families rather than multiplying source/vendor-specific edge types.

### D-409 — Do not turn every ecosystem association into Lineage
**Status:** Accepted
Repository membership, Deployment provenance/activation, realized Change, execution lifecycle, specific version encounter, Gate/Safeguard state, responsibility, authority/authorization and causality remain owned by their existing concepts. Graph representability is not a reason to move truth into Lineage.

### D-410 — Lineage is field/key/population/consumer/version capable without requiring universal fine-grained source support
**Status:** Accepted
Relationship semantics support narrow source/target scope. Asset-level evidence cannot be silently upgraded to field-level derivation, and field-level evidence cannot automatically generalize to the whole asset. Concrete integration/MVP support is later work.

### D-411 — Planned topology, effective topology and runtime encounter remain distinct
**Status:** Accepted
Proposed relationships remain Change Intent context until sufficient realization evidence establishes effective Lineage. Effective topology does not itself prove a particular run/consumer used a particular version.

### D-412 — Effective-time and knowledge-time topology are both first-class
**Status:** Accepted
Historical Lineage preserves effective intervals plus framework knowledge/correction time. Late discovery can revise retrospective topology without rewriting the as-known-then topology state.

### D-413 — Replace generic Lineage confidence with Phase 004 evidence semantics
**Status:** Accepted
The earlier `evidence quality/confidence` shorthand is superseded by proposition-specific evidence applicability, provenance, opportunity/coverage, corroboration/conflict and conclusion-specific sufficiency. No universal Lineage confidence/trust score is accepted.

### D-414 — Relationship existence supports explicit established/absent/unknown/conflicting/unavailable results
**Status:** Accepted
`Absent` is a strong bounded negative conclusion requiring adequate opportunity to observe and coverage. Missing metadata/query failure/source outage is not absence.

### D-415 — Lineage source disagreement has no hidden source hierarchy
**Status:** Accepted
Runtime, catalog, code, human and platform assertions do not have default precedence. Assertion Authority resolves governed assertion standing where applicable; evidence sufficiency remains independent. Phase 009 maps concrete sources.

### D-416 — Operational relevance is traversal-question bound
**Status:** Accepted
Graph reachability alone does not establish relevance. Traversals bind relationship families, direction, time/cut, semantic scope/version/consumer/use and authorization. Relevance is `relevant`, `not relevant` or `indeterminate` for the exact question, not a global score.

### D-417 — Multi-hop Lineage relevance requires semantic scope composition and bounded traversal
**Status:** Accepted
Intermediate relationship scopes must compose meaningfully. Missing granularity remains indeterminate rather than broadening a path. Lineage is not assumed to be a DAG; traversal is semantically bounded/cycle-safe.

### D-418 — Topology completeness is conclusion-relative and authorization-aware
**Status:** Accepted
Completeness is evaluated only for a bounded relationship universe/time/scope/depth/evidence coverage. Restricted/opaque projections cannot be presented as globally complete, and `no path found` cannot become `no path exists` without adequate negative coverage.

### D-419 — Relationship transitions preserve cross-concept ownership
**Status:** Accepted
Lineage owns relationship history. Establishing/ending a relationship can support realized Change, but Change owns the state transition; Change Intent owns proposed topology; Deployment owns activation; Execution History owns actual runs; Impact owns encounter/effect/consequence; Gate/Safeguard own active control truth.

### D-420 — OPS-001–OPS-009 and L01-01–L01-18 are accepted
**Status:** Accepted
The nine Group 01 operational refinement contracts and eighteen scenario checks compose without a new concept, universal score, hidden source precedence, blind propagation, exposure shortcut, causal shortcut or architecture selection.

### D-421 — Phase 007 Group 01 exits complete
**Status:** Accepted
Group 01 is complete with OPS-001–OPS-009 final for the accepted Group 01 scope. The concept catalog remains 24; SYN-001–SYN-035, REF-001–REF-030, AUTH-001–AUTH-053 and HLTH-001–HLTH-066 remain unchanged. Phase 007 Group 02 — Change Intent, Deployment Realization & Realized Change is next.