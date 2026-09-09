# Impact, Consumer Encounter, Exposure & Consequence

**Canonical key:** `operations.impact-exposure-consequence`

**Kind:** CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `stable_family.OPS`

**Owns current question:** How are downstream candidate, encounter opportunity, actual exposure, effect and consequence evidenced without collapsing them into one affected flag or causal attribution?

**Stable IDs:** OPS-067–OPS-085

## Current semantics

Operational reasoning chain: **bounded originating state + consumer/use context → encounter opportunity/availability/publication → actual encounter/exposure → downstream effect → consequence evidence → optional Causal Claim attribution**.

### OPS-067 — Impact Proposition: Origin, Consumer, State & Scope
Bind Impact to exact originating state/version/window, consumer/use/interface/population, historical path, encounter mode, time and knowledge cut.

### OPS-068 — Encounter Opportunity, Availability, Publication & Actual Encounter
Separate encounter opportunity, state availability, publication/serving and actual encounter; each can exist without the next.

### OPS-069 — Consumer Encounter Modes & Evidence Specificity
Use consumer-mode-specific evidence for execution input, refresh/materialization, query/read, cache/replica, application/report and business use.

### OPS-070 — Exposure Resolution Vocabulary & Bounded State
Resolve exact exposure as exposed/not exposed/safe-other-state encounter/encountered-state unknown/no relevant opportunity/indeterminate/conflicting/unavailable.

### OPS-071 — Execution, Refresh & Materialization Version Binding
Use run-specific execution/refresh/materialization version evidence to bind actual encountered state; schedule or latest-output proximity is insufficient.

### OPS-072 — Publication, Serving, Query, Application & Business-Use Chain
Preserve publication → serving/query → application/report → business-use chain as separate evidence boundaries.

### OPS-073 — Cache, Replica, Snapshot & Stale Safe-State Semantics
Model cache/replica/snapshot state explicitly; safe V-1 can mean not exposed to suspect V while freshness fails separately.

### OPS-074 — Multi-Hop Encounter Chain & Non-Transitive Exposure
Exposure is not transitive through multi-hop Lineage; indirect exposure requires sufficient intermediary transmission and downstream encounter evidence.

### OPS-075 — Alternate Encounter Paths, Partial Path Coverage & Aggregation
Evaluate all material alternate paths before consumer-wide non-exposure; one path's safe result does not resolve unresolved alternates.

### OPS-076 — Non-Exposure, No Opportunity, Safe-State & Unknown Negative Claims
Distinguish not exposed, no relevant opportunity, safe-state encounter and unknown; strong negative exposure claims retain REF-023 coverage burden.

### OPS-077 — Repeated Encounter, First Exposure & Exposure Interval
Represent repeated encounters, first exposure and exposure intervals proposition-by-proposition rather than one permanent consumer flag.

### OPS-078 — Downstream Effect Binding & Dimension Scope
Bind downstream effect to exact dimension/scope/time and source-owned Observation/Assessment/Change evidence; exposure does not imply effect.

### OPS-079 — No-Effect / Unchanged Claims & Downstream Coverage
`No effect` or unchanged conclusions require bounded downstream evidence coverage across the claimed dimensions.

### OPS-080 — Consequence Categories: Technical, Analytical & Business
Organize consequence evidence as technical/operational, analytical and business/process without turning categories into causal or severity truth.

### OPS-081 — Business Use, Decision & Customer Consequence Provenance
Publication/view/business use/decision reliance/customer consequence remain separate provenance-bearing steps.

### OPS-082 — Origin→Effect/Consequence Causal Attribution & Multiple Origins
Statements that an origin caused/contributed to downstream effect or consequence become Causal Claims; multiple origins remain explicit.

### OPS-083 — Impact Priority, Criticality, Severity & Aggregation Discipline
Priority, Criticality, Classification and severity context do not establish exposure, effect, consequence or probability; no universal Impact score is accepted.

### OPS-084 — Historical Impact Replay, Correction & Restricted Projection
Historical Impact replay is bitemporal; late consumer evidence may revise current retrospective exposure/consequence while current authorization controls disclosure.

### OPS-085 — Impact Cross-Concept Ownership & Group 07 Handoff
Impact owns candidate/exposure/effect/consequence association; source facts and causal attribution retain their separate owners.

## Invariants / boundaries

- candidate/reachable ≠ encounter opportunity ≠ exposed.
- available/published/served ≠ actual use.
- refresh/run timing ≠ consumed-version proof.
- stale safe state ≠ suspect-state exposure.
- upstream exposure ≠ transitive downstream exposure.
- one safe path ≠ global non-exposure.
- `not exposed` requires bounded path/opportunity/version coverage.
- exposed ≠ downstream effect.
- downstream effect ≠ consequence.
- consequence ≠ causal attribution.
- Criticality/Classification/priority ≠ realized Impact.
- restricted ≠ absent.

## Cross-concept ownership

Impact remains the downstream candidate/exposure/effect/consequence association owner. Lineage, Execution History, Observation, Assessment and Change retain source facts; Causal Claim owns attribution.

## Historical / disclosure rule

Historical Impact is bitemporal/non-rewriting. Restricted consumer/path/use evidence remains restricted rather than absent; safe projection cannot strengthen unknown/conflicting state.

## Architecture boundary

This contract does not select consumer/query/cache instrumentation, event stores, BI/application integrations, exposure algorithms, scoring models or technical architecture.

## Provenance

- `docs/concepts/phase_007/06_impact_consumer_encounter_exposure_consequence/README.md`
- Phase 007 Group 06 accepted OPS-067–OPS-085.
