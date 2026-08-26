# Phase 010 — Technical Architecture

**Status:** IN PROGRESS — Groups 01–02 accepted; Group 03 next

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

Current accepted range: **ARCH-001–ARCH-080** from Groups 01–02.

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

**Status:** Next — not started

Realize ecosystem Entity Identity, Monitoring Scope, Assertion Authority, Capability Authorization, historical authorization, basis disclosure, and safe projection without collapsing those independent concerns.

Path: [`03_identity_scope_authority_authorization_disclosure_architecture/README.md`](03_identity_scope_authority_authorization_disclosure_architecture/README.md)

### Group 04 — Source Acquisition, Adapter, Synchronization & Integration-Health Architecture

**Status:** Planned

Design source capability discovery, adapters/connectors, polling/streaming/hybrid acquisition, checkpoints, pagination, retries, quotas, source lag, schema drift, integration health, and graceful degradation.

### Group 05 — Runtime Provenance, Health, Lineage & Impact Evidence Architecture

**Status:** Planned

Realize Git/change/deployment/run/implementation/input/output correlations, health measurement provenance, reconciliation, topology, consumer encounter, cache/copy paths, exposure, downstream effect, and consequence evidence.

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

The public/reference persistence architecture can be physically sharded by tenant/residency/security boundary and must remain deployable without assuming every Databricks feature is available in every enterprise environment.

## Architecture choices still intentionally open after Group 02

Groups 01–02 deliberately selected no final:

- polling versus streaming versus hybrid ingestion;
- event bus or queue technology;
- source-adapter/SDK strategy;
- graph database/product;
- search/vector product;
- cache/materialized-serving technology;
- workflow/orchestration engine;
- credential/secrets implementation;
- LLM/retrieval/embedding/reranking/template architecture;
- redaction/policy engine;
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
- loss of proposition/source/basis provenance;
- disclosure/authorization boundaries removed for convenience;
- one global confidence/health/Impact/control/replay/architecture/relevance score;
- unsupported capabilities hidden behind planned future instrumentation.

## Phase 010 exit direction

Phase 010 should exit only when the architecture can demonstrate, through scenario replay and explicit traceability, that accepted semantics are technically realizable under deployment-verified environment/cost/latency/retention constraints and that all material residual gaps are resolved, reduced, intentionally scoped, or carried forward explicitly.

**Group 03 — Identity, Scope, Authority, Authorization & Disclosure Architecture is next.**
