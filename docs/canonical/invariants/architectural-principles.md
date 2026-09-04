# Architectural Principles & Cross-Cutting Invariants

**Canonical key:** `foundation.architectural_principles`

**Kind:** INVARIANT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `foundation.architectural_principles`

**Owns current question:** Which cross-cutting semantic and architectural constraints must every DMTZ realization preserve?

**Stable IDs:** N/A

## Current semantics

These principles constrain DMTZ architecture and implementation. They are not a list of preferred technologies. The final Phase 010 architecture realizes them, but later code, adapters, caches, models, user experiences, or active-control integrations may not weaken them by convenience.

## Accepted principles

### AP-01 — Conceptual architecture precedes technical realization
Technical modules realize accepted concepts/synchronizations/contracts; they do not redefine those concepts by implementation shape.

### AP-02 — The ecosystem is the reasoning boundary
DMTZ reasons across repository/job/workspace/pipeline/domain boundaries while preserving those boundaries for identity, provenance, responsibility, authorization, and source authority.

### AP-03 — Time and history are first-class
Material product state supports point-in-time/as-known questions across intent, Deployment, execution, Lineage, evaluation, Investigation, causal/Impact/control/authorization/Explanation state as applicable.

### AP-04 — Evidence, interpretation, intent, and causality remain distinct
Change Intent, source/runtime facts, Observations, Baselines, Expectations, Assessments, realized Changes, Causal Claims, Annotations, Impact, control state, and Explanation cannot collapse into one generic fact type.

### AP-05 — Provenance is part of every material fact
Material facts/assertions/results retain source/actor/process, temporal/version, derivation, correction/supersession, and authority context appropriate to their use.

### AP-06 — Lineage is typed
Data derivation, operational dependency, production/consumption, deployment provenance, and other accepted relationship classes remain distinguishable rather than becoming one ambiguous edge.

### AP-07 — Monitoring models degradation, not only failure
Successful execution can coexist with lateness, freshness violations, structural incompatibility, or poor data quality; atypicality alone is not normative degradation.

### AP-08 — Expectation, Baseline, Observation, and Assessment remain separate
What should happen, descriptive reference behavior, observed fact, and interpretation are distinct states with distinct provenance and lifecycles.

### AP-09 — Historical comparisons and assessments are reproducible
Historical reasoning resolves the applicable evidence/reference versions and knowledge cut; late/corrected evidence creates traceable retrospective state without deleting prior knowledge.

### AP-10 — Security boundaries follow data/authority semantics, not monitoring convenience
Monitoring does not broaden raw-data, metadata, causal, Impact, control, or authorization visibility merely because those facts were synchronized into DMTZ.

### AP-11 — Data minimization is a design requirement
Prefer metadata, aggregates, checks, fingerprints, references, and other bounded evidence over copied row-level sensitive data when they satisfy the proposition.

### AP-12 — Governance metadata participates in reasoning without owning health truth
Semantics, responsibility, criticality, Classification, and Policy Context may affect prioritization, Explanation, disclosure, and escalation while remaining distinct from health evidence and authorization.

### AP-13 — Policy/control transparency is not compliance certification
Classification, policy applicability, authorization, and control evidence do not mechanically become a legal/compliance conclusion.

### AP-14 — Tool integration is replaceable at concept/contract boundaries
Databricks, GitHub, Collibra, Immuta, DQX, model/search systems, and future providers supply or realize accepted semantics; they do not define those semantics.

### AP-15 — Databricks-native capabilities are favored, not worshipped
Prefer verified native capability where it cleanly satisfies accepted contracts; add missing functionality only where required and keep vendor capability instance/time-specific.

### AP-16 — Question answering is a view over evidence
Conversational, report, API, and UI experiences derive from authorized evidence/semantic state and do not become independent truth or authority sources.

### AP-17 — Unknown is a valid result
Incomplete, insufficient, conflicting, non-comparable, unavailable, stale, unauthorized, or otherwise unknown state is legitimate and must not be coerced into reassuring certainty.

### AP-18 — Human/planned intervention has explicit semantics
Expectation revision, Change Intent, comparability decisions, Causal Claim review/confirmation, Annotation, override, and other human actions remain attributable and distinct from machine-derived Observation.

### AP-19 — Business and engineering views share underlying state
Different authorized projections may expose different detail, but they derive from the same semantic/evidence state and cannot intentionally contradict it.

### AP-20 — Optional systems degrade enrichment, not core meaning
Absence of Collibra, Immuta, model/search assistance, graph technology, or other optional integrations cannot invalidate core DMTZ semantics; capability is narrowed explicitly when evidence is unavailable.

### AP-21 — Intent, deployment, execution, realized change, and health are distinct
Preserve Change Intent → Deployment activation → Execution → Observation/realized Change → Assessment without treating chronology as equivalence or causality.

### AP-22 — Historical state has ledger-like semantics
Material facts/assertions are appended/corrected/superseded rather than silently overwritten; event/effective time and recorded/knowledge time remain distinct where material. This does not mandate blockchain/event sourcing/a specific temporal store.

### AP-23 — Relationship semantics are graph-compatible
Entity Identity plus typed temporal Lineage supports traversal, historical subgraphs, incomplete/uncertain paths, and authorization-aware opaque nodes without mandating a graph database.

### AP-24 — Inquiry containers do not own truth
Investigation organizes/links evidence, Causal Claims, Impact, and Annotations but does not become the authoritative copy of those states.

### AP-25 — Causality is explicit and evidence-bearing
Causal propositions remain Causal Claims with explicit epistemic status, support/contradiction, review provenance, and confirmation gates. Timing, reachability, ranking, Deployment, or Change cannot bypass claim semantics.

### AP-26 — Impact is multi-layered, not graph reachability
Preserve downstream candidate/reachability, actual exposure/encounter, observed effect, consequence evidence, and causal attribution as distinct strengths. Missing evidence cannot become `not affected`.

### AP-27 — Explanation is authorization- and time-aware projection
Explanation derives from authorized state, preserves material statement-to-basis traceability and epistemic/control labels, and distinguishes contemporaneous, retrospective, and reconstructed perspectives.

### AP-28 — Passive monitoring is non-blocking and out-of-band by default
Observation, collection, Assessment, Investigation, Impact analysis, and Explanation should not become hidden production critical-path dependencies. Ungated production is not stalled merely because monitoring is degraded.

### AP-29 — Baseline onboarding prefers production-repository independence
Where platform/source metadata can satisfy accepted evidence requirements, baseline monitoring should be independently deployable/versioned without requiring ETL-code, shared-library, or CI changes in every production repository. Exceptions are explicit and justified.

### AP-30 — Active execution control is explicit and separable from observation
Execution Gate is optional control, not an automatic consequence of monitoring/readiness/Lineage. Gate enablement, decision basis, failure/fallback semantics, authority, override, enforcement evidence, latency, and availability are explicit. Execution Gate and Propagation Safeguard remain separate control boundaries.

### AP-31 — Historical replay is bitemporal and non-mutating
Historical questions consider event/effective time and recorded/knowledge cutoff. Evidence learned later cannot appear in an earlier knowledge cut merely because its effective time was earlier; corrections create retrospective state while prior knowledge remains reconstructable.

### AP-32 — Actual history and replay-derived reconstruction remain distinguishable
A current computation over historical inputs is not proof that the result was actually assessed, believed, decided, controlled, enforced, exposed, confirmed, or communicated then. Retained historical state and reconstructed historical outputs remain distinguishable.

## Cross-cutting non-collapse rules

The principles above imply at least these durable constraints:

- ecosystem ≠ repository;
- Entity Identity ≠ source-local name/identifier;
- Observation ≠ Assessment;
- Expectation ≠ Baseline;
- execution success ≠ timeliness ≠ freshness ≠ quality;
- missing evidence ≠ negative truth;
- current ≠ historical/as-known;
- Lineage ≠ exposure ≠ Impact ≠ cause;
- Authentication ≠ Capability Authorization ≠ Assertion Authority;
- permission/configuration/decision ≠ action/enforcement/result;
- Gate ≠ Safeguard;
- model/search/routing/cache ≠ canonical truth.

## Synchronizations / related canonical resources

- [Product definition](../reference/product-definition.md)
- [Foundational terminology](../reference/terminology.md)
- [Security and governance policy](../policies/security-governance.md)
- [Ecosystem lifecycles](../reference/ecosystem-lifecycles.md)
- [MVP boundary](../policies/mvp-boundary.md)

Detailed ARCH-001–ARCH-500 ownership remains under the inventory-selected Phase 010 owners until CKR-I.

## Provenance

- Original owner and AP-01–AP-32 source: [`../../foundation/005_architectural_principles.md`](../../foundation/005_architectural_principles.md)
- Evidence/time refinement: [`../../concepts/phase_004/README.md`](../../concepts/phase_004/README.md)
- Governance/authority refinement: [`../../concepts/phase_005/README.md`](../../concepts/phase_005/README.md)
- Health/operations/Explanation/integration refinement: [`../../concepts/phase_006/README.md`](../../concepts/phase_006/README.md), [`../../concepts/phase_007/README.md`](../../concepts/phase_007/README.md), [`../../concepts/phase_008/README.md`](../../concepts/phase_008/README.md), [`../../concepts/phase_009/README.md`](../../concepts/phase_009/README.md)
- Final technical realization constraints: [`../../concepts/phase_010/README.md`](../../concepts/phase_010/README.md), [`../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](../../concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md)
