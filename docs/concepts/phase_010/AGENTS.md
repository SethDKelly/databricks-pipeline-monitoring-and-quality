# Phase 010 AGENTS.md — Frozen Technical Architecture Discipline

## Status

Phase 010 is **COMPLETE / ACCEPTED**.

- Groups 01–09 accepted.
- ARCH-001–ARCH-500 final.
- ACV09-01–ACV09-120 pass.
- No ARCH-501 required.

Do not add or change a Phase 010 architecture contract merely to accommodate an implementation convenience. Reopening Phase 010 requires an explicit architecture reason and must preserve the earlier accepted functional/integration model unless that model is separately and deliberately reopened.

## Mandatory authorities

Implementation/design work that consumes Phase 010 must preserve:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- INTG-001–INTG-270;
- ARCH-001–ARCH-500;
- Phase 009 GAP-009-01–GAP-009-40 dispositions;
- Phase 010 Group 09 exit/handoff artifacts.

Use [`README.md`](README.md) and [`09_architecture_consolidation_validation_exit/phase_010_exit_review.md`](09_architecture_consolidation_validation_exit/phase_010_exit_review.md) as the architecture summary/exit, and follow individual group READMEs/contracts for detailed requirements.

## Frozen architecture sequence

1. Architecture frame/environment discovery — accepted.
2. Evidence/provenance/time/persistence — accepted.
3. Identity/scope/authority/authorization/disclosure — accepted.
4. Acquisition/adapters/integration health — accepted.
5. Runtime provenance/health/Lineage/Impact — accepted.
6. Investigation/reasoning/replay/Explanation — accepted.
7. Gate/Safeguard active control — accepted.
8. Serving/security/deployment/observability/cost — accepted.
9. Consolidation/validation/exit — accepted.

The sequence is a reasoning dependency, not a mandate for one runtime service per group.

## Core frozen rules

### Environment capability

- verified public/vendor fact ≠ target-environment fact ≠ organization requirement ≠ architecture assumption ≠ unknown;
- documented capability ≠ deployment presence/entitlement/enablement/permission/reachability/coverage/usable proposition support;
- cloud/region/Geo/account/workspace/edition/version/preview/feature state is material where relevant;
- optional-source absence is explicit capability degradation, not benign truth.

### Canonical evidence and time

- Delta-first canonical structured evidence/governance persistence is frozen;
- selective/minimized payload retention, not universal raw copying;
- source authority/limitations survive copying;
- event/effective, availability/knowledge, collection/persistence, correction/supersession and communication time remain distinct;
- corrections/supersessions are non-rewriting;
- Delta transaction-log time travel is not the product replay model;
- graph/search/vector/cache/read stores remain derived/rebuildable;
- retention/detail/relevance are independent; exact promised basis/control/communication evidence cannot be downsampled before its governed horizon.

### Identity, scope and governance

- canonical Entity/Principal identities remain distinct from source-local identities;
- names and timestamp proximity are not exact identity/correlation evidence;
- Monitoring Scope is organization-owned, not discoverability/access;
- Assertion Authority is proposition/facet/context/time-specific policy-as-data;
- Capability Authorization is action/subject/context/time/detail specific;
- service/workload processing permission ≠ requester visibility;
- current authorization/membership is not historical authorization/membership;
- conclusion/context/limitation/basis/provenance/detail/export may require independent disclosure permission;
- hidden basis existence/count/type/path/provenance can itself be sensitive.

### Acquisition and integration health

- reconciliation-first hybrid acquisition is the completeness/recovery foundation;
- stream/webhook/incremental paths are source-specific accelerators;
- request/page/window/partition/checkpoint/parser/coverage provenance is durable;
- checkpoint advancement follows durable evidence publication;
- partial pagination, 401/403/observer-relative 404, throttle, outage, publication lag, schema/parser failure and retention expiry do not become domain absence;
- integration health remains multidimensional; no global integration score.

### Runtime, health, Lineage and Impact

- Git/CI/deployment/activation/run remain distinct evidence stages;
- run-specific implementation/input/output state must not be inferred from current/latest state;
- missing manifest facets remain unknown/partial;
- Observation, Baseline, Expectation and Assessment remain distinct;
- successful run does not prove output existence/currentness/health;
- Lineage reachability is not consumption/encounter/exposure/effect/consequence/cause;
- exposure/effect/consequence require their own evidence;
- broad negatives require bounded population/path/outcome and sufficient coverage.

### Investigation, causality, replay and Explanation

- Investigation identity is canonical and independent from alerts/tickets/chats/model sessions;
- leads/annotations/model suggestions do not create truth/authority;
- exact retrieval precedes semantic/vector candidate retrieval;
- graph distance/centrality/path count and semantic similarity do not create causal rank;
- Causal Claim `confirmed` remains REF-017 + AUTH-034 gated;
- lack of support is not rejection;
- historical replay uses canonical bitemporal/availability-by-K state, not current graph/config/policy;
- Statement IR / Answer IR carry proposition/status/basis/limitations before rendering;
- deterministic rendering remains available without a model;
- model output may rephrase but not strengthen scope/status or suppress material limitations;
- `inspectBasis` is independently authorized itemwise;
- authentic retained communication requires retained snapshot/content evidence and remains distinct from reconstruction.

### Active control

- active control is opt-in over passive monitoring;
- Gate and Safeguard remain independent state machines;
- criterion evidence suitability ≠ readiness ≠ decision ≠ delivery ≠ enforcement ≠ execution;
- HOLD ≠ failed run; ADMIT ≠ actual run;
- override/fallback/timeout/multi-Gate behavior is explicit organization policy;
- stale control decisions are rejected outside applicability horizon;
- GitHub environment protection is bounded to the exact protected GitHub opportunity unless cross-system correlation proves downstream mapping;
- Databricks cancellation after execution starts is interruption, not pre-start HOLD;
- Safeguard configuration/request ≠ effective path/cohort enforcement;
- REF-028 prevention requires exposure opportunity + enforcement + alternate-path evidence;
- release/expiry ≠ recovery/health;
- models/search/graph cannot issue active-control decisions.

### Serving, security, operations and cost

- preferred serving boundary is thin/stateless and authorization-aware;
- UI has no unrestricted raw canonical/system-table access;
- response caches/read models are context-keyed, watermarked, derived and rebuildable;
- authentication ≠ Capability Authorization ≠ Assertion Authority;
- separate least-privilege workload identities; short-lived federation preferred where verified;
- secrets remain outside canonical evidence/routine telemetry;
- material callbacks require authenticity/integrity and replay/idempotency controls;
- tenant/residency isolation applies to derived stores, telemetry, model packets and archive too;
- SC-01–SC-06 govern SLOs; numeric values are deployment ADRs after measurement;
- operational SLO/health is not monitored-domain health;
- quota exhaustion degrades freshness/coverage rather than producing negative truth;
- cost policy cannot silently shrink Monitoring Scope, skip required reconciliation, delete pinned basis or reuse stale control decisions;
- backup/DR/restore preserves non-rewriting history and exposes unrecovered gaps.

## Frozen MVP boundary

Initial MVP is Databricks/GitHub-centered passive monitoring/reasoning/replay and does not require Collibra, Immuta, LLM/model rendering, semantic/vector retrieval, a specialized graph database or active-control enforcement.

If an optional/enterprise capability is enabled, its full accepted bounded semantics apply.

See:

- [`09_architecture_consolidation_validation_exit/mvp_topology.md`](09_architecture_consolidation_validation_exit/mvp_topology.md)
- [`09_architecture_consolidation_validation_exit/enterprise_extension_topology.md`](09_architecture_consolidation_validation_exit/enterprise_extension_topology.md)

## Implementation-decision boundary

Concrete language/framework/API gateway/queue/orchestrator/secret store/IdP/policy engine/cache/observability/graph/search/model/UI/IaC selections are intentionally deferred. They may be chosen without reopening architecture only if they satisfy the frozen contracts.

See [`09_architecture_consolidation_validation_exit/unresolved_implementation_decisions.md`](09_architecture_consolidation_validation_exit/unresolved_implementation_decisions.md).

## Reopening trigger

Reopen Phase 010 only when a required product capability cannot be technically realized within ARCH-001–ARCH-500 despite reasonable implementation alternatives, or when a deliberate product/functional contract change invalidates an architecture assumption.

Performance preference, team familiarity, vendor convenience or desire for a simpler schema is not by itself a valid reason to weaken a frozen architecture boundary.
