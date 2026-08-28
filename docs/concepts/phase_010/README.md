# Phase 010 — Technical Architecture

**Status:** IN PROGRESS — Groups 01–04 accepted; Group 05 next

## Purpose

Phase 010 converts the accepted functional and integration contracts from Phases 002–009 into a technical architecture without weakening their semantics.

Phase 010 owns architecture choices. It does **not** reopen the accepted product truth model. Any architecture that appears simpler only by collapsing authority, time, evidence, health, lineage, causality, Impact, control, historical replay, or disclosure boundaries is invalid.

## Stable incoming contract

Phase 010 inherits the complete accepted ranges:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270.

The Phase 009 exit review, consolidated source capability matrix, residual gap register, and `phase_010_handoff.md` are mandatory architecture inputs.

## Architecture contract namespace

Phase 010 uses **ARCH-###** for durable technical-architecture contracts.

`ARCH-###` records architecture constraints/decisions needed to realize accepted semantics. It must not redefine source facts, functional truth, evidence sufficiency, source authority, or product concepts already owned by earlier phases.

Current accepted range: **ARCH-001–ARCH-190** from Groups 01–04.

## Logical groups

### Group 01 — Architecture Frame, Environment Discovery & Decision Criteria

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-001–ARCH-032**. **AFE01-01–AFE01-60 pass.** Decisions D-1269–D-1298 accepted.

Group 01 establishes the deployment-bound capability model, architecture fact classes, environment verification/unknown discipline, MVP/enterprise boundary, hard constraints, decision-specific quality tradeoffs, six service classes, ADR discipline and GAP-009 ownership.

Its central rule is:

**documented capability ≠ deployment presence ≠ licensed entitlement ≠ enablement ≠ authorization ≠ reachability ≠ observable coverage ≠ proposition-specific usability**.

Path: [`01_architecture_frame_environment_discovery_decision_criteria/README.md`](01_architecture_frame_environment_discovery_decision_criteria/README.md)

### Group 02 — Evidence, Provenance, Temporal & Persistence Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-033–ARCH-080**. **EPT02-01–EPT02-72 pass.** Decisions D-1299–D-1336 accepted.

Group 02 selects a Delta Lake-first canonical structured evidence plane, selective cloud-object payload retention, explicit multi-coordinate/bitemporal history, non-rewriting correction/supersession, common-derivation provenance and tiered retention/relevance lifecycle.

Its central persistence rule is:

**source-owned evidence → framework-retained identity/provenance/time → canonical non-rewriting journals → policy-bound lifecycle → derived rebuildable graph/search/serving projections**.

Storage retention, retained detail and reporting/retrieval relevance remain independent. Ordinary reference retention defaults keep roughly 120 days recent detail, roughly 400 days detailed replay and up to roughly 24 months approved trend aggregates, while exact multi-year evidence is pinned/retained only for explicit product, incident, recurrence, audit, security, legal or other governed need.

Path: [`02_evidence_provenance_temporal_persistence_architecture/README.md`](02_evidence_provenance_temporal_persistence_architecture/README.md)

### Group 03 — Identity, Scope, Authority, Authorization & Disclosure Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-081–ARCH-132**. **IAD03-01–IAD03-84 pass.** Decisions D-1337–D-1382 accepted.

Group 03 realizes tenant-scoped canonical Entity/Principal identity, evidence-bearing source identity bindings, organization-owned Monitoring Scope, Assertion Authority and Capability Authorization policy-as-data, current/historical authorization decision semantics, and disclosure-dimensional safe projection.

Its central governance chain is:

**source-local identity → canonical ecosystem identity → Monitoring Scope → Assertion Authority → Capability Authorization → current/historical authorization evaluation → authorized disclosure projection → independently evidenced enforcement/action**.

It preserves source-local IDs after mapping; unknown scope membership is not exclusion; vendor roles/ownership are not automatic Assertion Authority; authorization is not enforcement; service-principal processing permission is not requester access; actual authorization decision is not replay-derived authorization; and safe abstraction cannot strengthen truth.

Path: [`03_identity_scope_authority_authorization_disclosure_architecture/README.md`](03_identity_scope_authority_authorization_disclosure_architecture/README.md)

### Group 04 — Source Acquisition, Adapter, Synchronization & Integration-Health Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-133–ARCH-190**. **AHI04-01–AHI04-96 pass.** Decisions D-1383–D-1432 accepted.

Group 04 establishes reconciliation-first hybrid source acquisition, durable acquisition-run/surface/plan/checkpoint/page/window provenance, versioned normalization, explicit collection coverage, source publication/acquisition lag, quota/cost-aware scheduling and multidimensional integration health.

Its central acquisition chain is:

**verified capability + governed scope → revisioned acquisition plan → reconciliation-first hybrid collection → durable source/request/page/checkpoint provenance → versioned normalization → coverage + source lag + integration-health dimensions → canonical evidence publication**.

Streams/webhooks accelerate freshness but do not replace reconciliation where completeness matters. Empty/partial/degraded collection never becomes domain absence; integration recovery does not rewrite historical evidence gaps; no global integration-health score is accepted.

Path: [`04_source_acquisition_adapter_synchronization_integration_health_architecture/README.md`](04_source_acquisition_adapter_synchronization_integration_health_architecture/README.md)

### Group 05 — Runtime Provenance, Health, Lineage & Impact Evidence Architecture

**Status:** Next — not started

Realize Git/change/deployment/run/implementation/input/output correlations, health measurement provenance, reconciliation, topology, consumer encounter, cache/copy paths, exposure, downstream effect, and consequence evidence using acquisition coverage/health as evidence conditions.

Path: [`05_runtime_provenance_health_lineage_impact_evidence_architecture/README.md`](05_runtime_provenance_health_lineage_impact_evidence_architecture/README.md)

### Group 06 — Investigation, Reasoning, Historical Replay & Explanation Architecture

**Status:** Planned

Realize Investigation/Causal Claim persistence, reasoning-graph traversal, historical/as-known replay, current retrospective reasoning, statement-to-basis composition, `inspectBasis`, authentic retained Explanation communication, and any retrieval/LLM architecture.

### Group 07 — Execution Gate, Propagation Safeguard & Active-Control Architecture

**Status:** Planned

Realize Execution Gate and Propagation Safeguard independently, including criterion/evidence suitability, readiness, decisions, delivery/acceptance, enforcement, actual execution, overrides/fallbacks, protected paths/cohorts, prevention evidence, release, and recovery.

### Group 08 — Serving, Security, Deployment, Observability & Cost Architecture

**Status:** Planned

Design API/service/UI-facing topology, authentication/credentials/secrets, runtime authorization enforcement, deployment topology, observability, operational SLOs, capacity/performance, quota/cost attribution, and optional-integration deployment behavior.

### Group 09 — Architecture Consolidation, Validation & Phase 010 Exit

**Status:** Planned

Replay the target architecture against Phases 002–009 contracts, scenarios, and GAP-009-01–GAP-009-40; resolve cross-group contradictions; freeze the target/reference architecture, ADR set, MVP topology, enterprise-extension boundaries, and implementation handoff.

## Dependency order

The review order is intentional:

**architecture frame/environment facts → durable evidence/time model → identity/governance/security semantics → acquisition/integration health → operational/health/lineage evidence → reasoning/replay/Explanation → active controls → serving/deployment/operations → whole-architecture validation**.

This order is a reasoning dependency. It does not require the final runtime to have one service per group or to deploy components in this sequence.

## Group 01 accepted architecture discipline

Later groups must preserve:

- verified public/vendor fact ≠ target-environment discovered fact ≠ organization requirement ≠ architecture assumption ≠ unresolved unknown;
- vendor/product name ≠ concrete capability instance;
- documented support ≠ target deployment presence/enablement/entitlement/permission/reachability/coverage;
- capability usability as proposition/service-class specific rather than one Boolean;
- capability verification as provenance-bearing and time-aware;
- unknown capability state as first-class;
- cloud/region/Geo/government deployment, version, plan/license, preview/feature flag and network/security context where material;
- optional source absence as bounded capability loss, not benign default;
- semantic/evidence/security/degraded-state rules as hard architecture constraints;
- decision-specific quality tradeoffs with no universal architecture score;
- explicit decision reversibility and assumption/unknown register;
- SC-01–SC-06 service classes instead of one freshness SLA;
- GAP-009-01–GAP-009-40 ownership/treatment through Phase 010 exits.

## Group 02 accepted architecture discipline

Later groups must also preserve:

- Delta Lake canonical structured persistence with deployment-bound managed/external realization;
- selective, data-minimized cloud-object payload retention rather than universal raw copying;
- framework evidence identity distinct from source-local identity and physical storage location;
- source ownership/authority after copy;
- event/effective, source-available, collection/persistence, correction/supersession and communication time separation;
- late evidence as late for prior knowledge cuts;
- non-rewriting semantic journals independent of physical compaction;
- common derivation and parser/normalizer provenance;
- graph/search/vector/serving stores as derived/rebuildable projections;
- Delta time travel not being the product replay model;
- storage retention ≠ retained resolution/detail ≠ reporting relevance;
- lifecycle tiering, dependency pinning, legal/audit holds, safe aggregation, archive/restore and provenance-stub semantics;
- exact basis/communication/control evidence protected from lossy downsampling for its promised horizon;
- no indefinite detailed accumulation as a default merely because storage can grow.

## Group 03 accepted architecture discipline

Later groups must also preserve:

- canonical tenant-scoped Entity/Principal IDs distinct from vendor-local identities;
- source identity bindings as evidence-bearing, revisioned and conflict-capable;
- rename continuity distinct from delete/recreate/incarnation;
- human/group/service/workload identity and acting-on-behalf-of relationships kept distinct;
- historical membership based on historical evidence rather than current group state;
- Monitoring Scope as organization-owned expected coverage, not discoverability/access;
- scope selectors/materializations retaining unknown membership and bounded denominator semantics;
- Assertion Authority as structured target/context/time rules independent from evidence sufficiency and permission;
- explicit authority precedence/co-authority/fallback with no hidden rule ordering;
- vendor role/ownership/responsibility/permission as source evidence, not automatic DMTZ authority;
- Capability Authorization as principal/action/subject/context/time/detail specific;
- no universal deny-wins/allow-wins authorization precedence;
- actual authorization decision ≠ replay-derived authorization ≠ enforcement/action;
- service processing permission ≠ requester visibility;
- disclosure of conclusion/context/limitation/basis/provenance/detail/export independently authorized;
- exact/coarse/redacted/opaque/withheld projection with epistemic monotonicity;
- hidden basis existence/count/type/path/provenance treated as potentially sensitive;
- retained/archived/provenance-stub material not automatically disclosable;
- tenant/residency policy limiting identity/governance metadata and evidence movement;
- canonical policy state in Group 02 persistence with caches/indexes as derived projections.

## Group 04 accepted architecture discipline

Later groups must also preserve:

- source adapters bound to exact deployment-verified capability instances and revisioned surfaces/plans;
- reconciliation as the completeness/recovery foundation, with stream/webhook/incremental/export paths as source-specific accelerators;
- acquisition-run/attempt identity and durable request/page/partition/window provenance;
- source cursor/checkpoint state as source-bound operational state, never truth;
- checkpoint advancement only after corresponding evidence/provenance commit;
- overlap/redelivery/retries as idempotent and common-derived where they represent one source event;
- Monitoring Scope expected population independent from connector discoverability;
- pagination/partition/window completion explicit rather than inferred from HTTP success;
- request/response/source identifiers retained where permitted for troubleshooting/provenance;
- source envelope/raw representation distinct from normalized evidence;
- versioned parser/normalizer and non-rewriting reparsing semantics;
- additive schema evolution tolerated while breaking drift becomes explicit integration state;
- malformed/unsupported payloads quarantined rather than silently discarded when coverage can be affected;
- source publication lag distinct from event/effective time and collection/persistence lag;
- service-class-specific acquisition cadence rather than one polling interval;
- authentication, permission, observer-relative not-found, quota, source outage, reachability, lag, checkpoint, pagination, schema, parser, persistence, coverage and freshness as separable integration-health dimensions;
- no universal integration-health score;
- collection coverage manifests used before strong negative reasoning;
- source-native retention expiry distinct from product-retained evidence;
- optional-source absence as proposition-bound degradation, not benign default;
- acquisition cost/volume observable without weakening required evidence coverage.

## Architecture choices still intentionally open after Group 04

Groups 01–04 deliberately selected no final:

- universal event bus or queue technology;
- final workflow/orchestration/worker runtime;
- source-adapter SDK implementation language/framework;
- external IAM/IdP product;
- external policy-engine product or runtime packaging;
- policy authoring UI/API/Git workflow;
- graph database/product;
- search/vector product;
- cache/materialized-serving technology;
- credential/secrets implementation;
- LLM/retrieval/embedding/reranking/template architecture;
- Gate/Safeguard implementation;
- UI/API/service topology;
- deployment topology;
- observability stack;
- final backup/archive/lifecycle automation vendor;
- final cost-control implementation.

These choices must be justified by accepted contracts and deployment facts rather than selected by familiarity.

## Durable architecture rejection rules

Reject an architecture if it requires any of the following shortcuts:

- source availability treated as Assertion Authority;
- public vendor documentation treated as proof of tenant capability;
- retained/copied evidence treated as newly authoritative or independent;
- names or timestamp proximity used as exact entity/deployment/run joins;
- vendor role/ownership/responsibility treated as automatic DMTZ Assertion Authority;
- source discoverability or technical access treated as Monitoring Scope;
- unknown scope membership treated as exclusion;
- current membership/permission projected backward as historical authorization;
- service-principal access inherited by end users;
- authorization treated as enforcement/action occurrence;
- replay-derived authorization presented as an actual retained decision;
- retention/archive state treated as disclosure permission;
- redaction/generalization that strengthens, broadens or hides a material limitation;
- hidden basis counts/provenance leaked by convenience;
- checkpoint advancement before durable evidence persistence;
- webhook/stream silence treated as complete no-event evidence;
- partial pagination/partitions treated as complete coverage;
- 401/403/observer-relative 404/throttle/outage treated as domain absence;
- source publication lag ignored for current negatives;
- schema/parser failure silently dropping evidence;
- current integration recovery rewriting a prior evidence gap;
- current state projected backward as historical state;
- missing/degraded telemetry converted into negative truth;
- Delta transaction-log history used as the sole long-horizon product replay model;
- physical compaction/downsampling silently rewriting semantic history;
- retained old history automatically flooding routine reporting;
- age alone treated as irrelevance or deletion justification;
- Baseline, Expectation, Observation and Assessment flattened together;
- Lineage traversal treated as exposure, Impact, or causality;
- control configuration/request treated as effective enforcement;
- reconstructed history labeled as authentic retained communication;
- loss of proposition/source/basis/acquisition provenance;
- one global confidence/health/Impact/control/replay/architecture/relevance/authorization/integration-health score;
- unsupported capabilities hidden behind planned future instrumentation.

## Phase 010 exit direction

Phase 010 should exit only when the architecture can demonstrate, through scenario replay and explicit traceability, that accepted semantics are technically realizable under deployment-verified environment/cost/latency/retention/security constraints and that all material residual gaps are resolved, reduced, intentionally scoped, or carried forward explicitly.

**Group 05 — Runtime Provenance, Health, Lineage & Impact Evidence Architecture is next.**
