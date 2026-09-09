# Phase 010 Technical Architecture Handoff from Phase 009

**Status:** Accepted handoff input — Phase 009 complete

This document is an architecture **input contract**, not an architecture proposal. Phase 010 owns technical design choices.

## Stable incoming semantics

Phase 010 inherits the complete accepted ranges:

- SYN-001–SYN-035;
- REF-001–REF-030;
- AUTH-001–AUTH-053;
- HLTH-001–HLTH-066;
- OPS-001–OPS-123;
- EXPL-001–EXPL-160;
- **INTG-001–INTG-270**.

Architecture must preserve every durable boundary established by those ranges.

## Required architecture problem set

### 1. Source capability discovery

Architecture needs a way to represent which exact source surfaces/versions/editions are enabled and usable in a target environment, including permissions, retention, latency, rate limits, coverage and feature/preview status.

Do not model `Databricks`, `GitHub`, `Collibra` or `Immuta` as one Boolean integration capability.

### 2. Identity and association

Realize durable mappings for:

- ecosystem Entity Identity across source-local IDs;
- repository revision / Change Intent / deployment / target activation / run association;
- consumer identities and material path identities;
- source evidence identity that survives rename/recreation where required.

Names and timestamp proximity remain invalid substitutes.

### 3. Governance truth sources

Realize explicit governed sources for at least:

- Monitoring Scope;
- Assertion Authority;
- organization-specific semantic/responsibility/classification rules where vendor facets are not sufficient;
- Capability Authorization composition/disclosure rules.

These may reuse vendor systems but their exact authority mapping must be explicit.

### 4. Runtime and version provenance

Provide the mechanism needed to preserve run-specific:

- code/revision evidence;
- job/task/config/parameter/runtime/library facets where material;
- output versions;
- exact input versions when a product question requires them.

Bundle/workspace-source execution and generic multi-input workloads need explicit attestation/instrumentation if exact provenance is a requirement.

### 5. Health and measurement provenance

Ensure every retained measurement/check/metric/reconciliation result can retain the exact subject, grain/window/slice, definition/rule/Baseline revision, run/output/input association where applicable, production/evaluation/availability time and source limitations needed by HLTH/EXPL semantics.

### 6. Lineage, consumer and Impact evidence

Support explicit differentiation among:

- effective/candidate topology;
- publication/availability;
- actual read/encounter;
- cache/copy/export/application path;
- exact state/version exposure;
- downstream effect;
- technical/analytical/business consequence.

Architecture must not create transitive exposure from graph traversal.

### 7. Investigation and causality

Retain investigation lead/localization provenance, statement-relative evidence and Causal Claim proposition/status/history without promoting model/human/vendor output by origin.

A durable case/annotation realization may be chosen, but `confirmed` remains REF-017 + AUTH-034 gated.

### 8. Gate and Safeguard realization

If active controls are implemented, preserve independent lifecycle/evidence for:

- criterion/evidence suitability/readiness;
- Gate HOLD/ADMIT/override/fallback decision;
- delivery/acceptance/enforcement;
- actual execution;
- Safeguard protected state/path/cohort;
- proposal/authorization/request/enforcement;
- encounter opportunity and REF-028 prevention;
- release/reopening/recovery.

Architecture must not merge Execution Gate and Propagation Safeguard.

### 9. Historical time and knowledge

Preserve the time coordinates necessary for accepted replay:

- event/effective time;
- source-recorded/first-available time when obtainable/needed;
- correction/supersession timing;
- retrieval/extraction timing;
- requested knowledge cutoff K;
- actual communication time.

Late evidence must remain late for earlier K.

### 10. Durable provenance and retention

Determine which source-owned evidence must be retained beyond vendor-native horizons to support intended enterprise replay. The retention mechanism is an architecture choice, but it must preserve source identity, original semantics, common derivation, correction/supersession, availability timing and authorization constraints.

Do not treat copied evidence as newly authoritative or independent.

### 11. Explanation communication retention

Where the product promises proof of actual prior Explanation content, architecture must retain authentic communication/snapshot identity, exact proposition statements, limitations, audience/context, basis/projection metadata and communication time as required.

Retrospective reconstruction remains separately labeled.

### 12. Basis inspection and disclosure

Architecture must support the independent questions:

- can the system resolve the internal basis?;
- may this requester/audience/purpose/delivery context see the conclusion/context/limitation/basis/detail?;
- what safe exact/coarse/redacted/opaque projection is permitted?;
- does revealing existence/count/type/provenance itself create a disclosure issue?

Current disclosure changes cannot rewrite source truth or retained historical communication.

### 13. Integration health

Instrument source collection/query health sufficiently to distinguish:

- no record;
- permission denial;
- auth failure;
- throttling/rate exhaustion;
- timeout/outage;
- delayed publication;
- partial pagination;
- schema/API change;
- parser/transform failure;
- retention expiry;
- optional integration absent.

Negative conclusions must be suppressed/narrowed when their source coverage is degraded.

### 14. Latency and service classes

Define service expectations by question/use class rather than one universal freshness SLA. Examples include:

- near-current operational monitoring;
- periodic health/quality evaluation;
- slower investigative/RCA reasoning;
- historical/as-known replay;
- retained-communication/basis inspection.

Different source publication envelopes may legitimately serve different classes.

### 15. Quota and cost

Architecture must model source/API/query/storage/control costs and quota state. Material Phase 009 facts include:

- Databricks system tables currently incur query compute rather than separate table-use charges;
- Databricks REST/lineage limits are endpoint/scope specific;
- GitHub REST/audit/secondary limits constrain polling/query volume;
- GitHub Actions use/storage is plan/meter dependent if selected for future workflows;
- Collibra throttling/token/license/capacity is tenant-specific;
- Immuta exact API/licensing/export constraints require environment discovery.

Cost optimizations may change retrieval/retention strategy, not evidence burden.

### 16. Graceful degradation

Design capability-aware partial operation. If a source is unavailable, expired, restricted or not licensed:

- keep supported sibling statements;
- mark the affected proposition unsupported/unknown/unavailable as appropriate;
- do not invent benign defaults;
- do not silently fall back to a lower-authority source;
- do not emit strong negatives whose coverage is broken;
- preserve internal/visible limitations.

### 17. MVP versus enterprise extensions

Phase 009 accepts a bounded Databricks/GitHub-centered MVP as feasible. Architecture should make optional/advanced capabilities pluggable without making Collibra/Immuta universal prerequisites.

However, organization-owned Monitoring Scope, Assertion Authority, identity/correlation and any promised long-horizon provenance/Explanation retention are not optional merely because vendor products are optional—the exact product commitments determine whether those capabilities are required.

## Architecture choices still intentionally open

Phase 009 has **not** selected:

- polling versus streaming versus hybrid ingestion;
- event bus/queue technology;
- relational, lakehouse, graph, search or other persistence models;
- graph database or graph computation implementation;
- source adapter/SDK strategy;
- cache/materialized-view strategy;
- provenance/event schema;
- workflow/orchestration engine;
- credential/secrets design;
- LLM/retrieval/template architecture;
- Explanation snapshot store;
- redaction/policy engine;
- Gate/Safeguard technical realization;
- UI/API/service topology;
- deployment topology;
- observability stack;
- cost-control implementation.

Those decisions now belong in Phase 010 and should be evaluated against the Phase 009 capability matrix and gap register.

## Phase 010 acceptance direction

A Phase 010 architecture should be rejected if it can only appear simple by doing any of the following:

- treating source availability as authority;
- joining entities/deployments/runs by name/time convenience;
- projecting current state backward;
- turning missing telemetry into negative truth;
- flattening Baseline/Expectation/Observation/Assessment;
- treating Lineage as exposure or causality;
- treating control configuration as enforcement;
- treating reconstructed history as retained communication;
- losing statement-to-basis provenance;
- dropping disclosure/authorization boundaries;
- using one global confidence/health/Impact/control/replay score;
- hiding unsupported capabilities behind planned architecture.

The architecture is ready to begin because the functional semantics and integration facts are now stable enough to constrain technical tradeoffs rather than be rediscovered by implementation.
