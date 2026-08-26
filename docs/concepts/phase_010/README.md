# Phase 010 — Technical Architecture

**Status:** IN PROGRESS — Group 01 next

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

No ARCH contract is accepted by this phase-level grouping commit. Group 01 will establish the first accepted architecture range after review.

## Logical groups

### Group 01 — Architecture Frame, Environment Discovery & Decision Criteria

**Status:** Next — not started

Establish target-environment assumptions, architecture quality attributes, MVP versus enterprise-extension boundaries, service classes, capability discovery, decision criteria, ADR discipline, and explicit non-goals before selecting technical components.

Path: [`01_architecture_frame_environment_discovery_decision_criteria/README.md`](01_architecture_frame_environment_discovery_decision_criteria/README.md)

### Group 02 — Evidence, Provenance, Temporal & Persistence Architecture

**Status:** Planned

Select the durable representation and persistence strategy for evidence identity, provenance, source identity, bitemporal coordinates, correction/supersession, common derivation, historical reconstruction, retention, and durable statement-to-basis traceability.

### Group 03 — Identity, Scope, Authority, Authorization & Disclosure Architecture

**Status:** Planned

Realize ecosystem Entity Identity, Monitoring Scope, Assertion Authority, Capability Authorization, historical authorization, basis disclosure, and safe projection without collapsing those independent concerns.

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

## Architecture choices intentionally open at entry

Phase 010 begins without having selected:

- polling versus streaming versus hybrid ingestion;
- event bus or queue technology;
- relational, lakehouse, graph, search, object-store, or mixed persistence;
- graph database or graph-computation technology;
- source-adapter/SDK strategy;
- cache/materialized-view strategy;
- provenance/event schema;
- workflow/orchestration engine;
- credential/secrets implementation;
- LLM, retrieval, embedding, reranking, or template architecture;
- Explanation snapshot storage;
- redaction/policy engine;
- Gate/Safeguard implementation;
- UI/API/service topology;
- deployment topology;
- observability stack;
- cost-control implementation.

These choices must be justified by the accepted contracts and environment facts rather than selected by familiarity.

## Durable architecture rejection rules

Reject an architecture if it requires any of the following shortcuts:

- source availability treated as Assertion Authority;
- names or timestamp proximity used as exact entity/deployment/run joins;
- current state projected backward as historical state;
- missing/degraded telemetry converted into negative truth;
- Baseline, Expectation, Observation and Assessment flattened together;
- Lineage traversal treated as exposure, Impact, or causality;
- control configuration/request treated as effective enforcement;
- reconstructed history labeled as authentic retained communication;
- copied/retained source evidence promoted to newly authoritative or independent evidence;
- loss of proposition/source/basis provenance;
- disclosure/authorization boundaries removed for convenience;
- one global confidence/health/Impact/control/replay score;
- unsupported capabilities hidden behind planned future instrumentation.

## Phase 010 exit direction

Phase 010 should exit only when the architecture can demonstrate, through scenario replay and explicit traceability, that the accepted semantics are technically realizable under documented environment/cost/latency/retention constraints and that all material residual gaps are resolved, reduced, intentionally scoped, or carried forward explicitly.

**Group 01 — Architecture Frame, Environment Discovery & Decision Criteria is next.**
