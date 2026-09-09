# Phase 010 Group 09 — Frozen MVP Topology

**Status:** ACCEPTED — implementation handoff boundary

This MVP topology realizes the behavioral MVP defined in `docs/foundation/008_mvp_boundary.md`. It is intentionally smaller than the full enterprise extension architecture while preserving every accepted truth/evidence/authority/time boundary.

## MVP objective preserved

The initial implementation must prove that DMTZ can turn a fragmented Databricks pipeline ecosystem into evidence-grounded, historically aware, Lineage-aware explanations of health, planned/realized change, investigation/causal context and downstream consequence for engineering and business users.

## Required MVP logical components

### 1. Environment capability inventory

Minimum:

- one or more target Databricks account/workspace capability instances;
- GitHub repository/Actions/deployment capability instances used by representative pipelines;
- cloud/region/Unity Catalog/system-table/API/permission facts required by enabled features;
- revisioned discovery result and unknown/unsupported state.

### 2. Databricks + GitHub acquisition adapters

Minimum source family:

- Databricks Jobs/tasks/runs and relevant workspace/account/system-table/source surfaces;
- Unity Catalog/object/Lineage/query/audit/measurement surfaces where enabled and proposition-relevant;
- Git repository revision evidence;
- GitHub Actions/workflow/deployment evidence for representative deployment flows.

Collection is reconciliation-first. Incremental/API/webhook acceleration is optional per source.

### 3. Canonical Delta evidence/governance plane

Minimum canonical records include:

- evidence/provenance/time identity;
- Entity/Principal/source identity bindings;
- Monitoring Scope;
- Assertion Authority rules needed for MVP propositions;
- Capability Authorization/disclosure rules needed for MVP users;
- Change Intent/Deployment/runtime associations;
- run implementation/input/output evidence at the precision supported by the representative proof scenarios;
- measurement/Assessment history;
- typed temporal Lineage;
- Investigation/lead/Causal Claim state;
- downstream encounter/exposure/effect/consequence evidence for representative consumers;
- Explanation snapshot/basis records where the MVP demonstrates historical communication replay.

### 4. High-value measurement/evaluation worker

Minimum health dimensions align with the existing MVP boundary:

- freshness/staleness;
- row quantity/volume;
- null/completeness;
- uniqueness where relevant;
- schema/structural state;
- selected domain checks;
- join/match/reconciliation behavior for A+B→C scenarios.

Expectation and Baseline remain independent; successful execution remains independent from output quality.

### 5. Runtime provenance and Lineage materialization

Provide enough exact/partial implementation, input/output and typed temporal topology evidence for the accepted MVP proof scenarios. Missing exact bundle/multi-input/consumer-version facets remain unknown unless the MVP deliberately adds attestation/instrumentation.

### 6. Deterministic Investigation/reasoning/replay core

Minimum:

- exact retrieval by canonical identity/proposition/time/scope;
- deterministic evidence/coverage/authority evaluation;
- Investigation and competing Causal Claim state;
- typed graph-compatible traversal using Delta-backed node/edge projections;
- historical availability-by-K replay for at least the representative correction scenario;
- Statement IR / Answer IR with basis and limitations.

No mandatory LLM or specialized graph database.

### 7. Authorization-aware serving API

Minimum:

- human/application authentication integrated with target identity capability;
- canonical Principal binding;
- current requester Capability Authorization/disclosure;
- bounded query/investigation/replay/`inspectBasis` operations;
- response epistemic envelope;
- deterministic rendering path;
- UI/API consumers never receive unrestricted canonical/admin-table access.

### 8. Initial UI / business-engineering experience

The UI may be a separate implementation workstream, but it must preserve:

- evidence-consistent business/engineering views;
- unknown/partial/conflicting/restricted state;
- distinction among reachability, exposure, effect and consequence;
- source/basis inspection subject to current disclosure;
- historical `what was known then` vs current retrospective explanation.

### 9. Basic operational plane

Minimum:

- source/integration health dimensions;
- canonical persistence health;
- serving/reasoning health;
- source/publication/acquisition watermarks;
- quota/rate state where observable;
- service-class operational metrics;
- basic cost attribution for ingestion/query/storage;
- backup/restore procedure for canonical records within the MVP promise.

## MVP active-control boundary

Execution Gate and Propagation Safeguard **are not required to satisfy the initial passive-monitoring MVP exit test**. The original MVP explicitly excludes autonomous remediation/rollback and write-back/remediation workflows, and Group 07 preserves active control as opt-in.

The MVP codebase should preserve clean interfaces for future SC-06 control components, but a deployment can complete the passive MVP without installing a Gate/Safeguard enforcement adapter.

If an MVP pilot chooses to demonstrate a Gate or Safeguard, it must implement the full accepted state/evidence semantics for that bounded path rather than a simplified `blocked` Boolean.

## MVP optional integrations

Not required for the initial MVP:

- Collibra;
- Immuta;
- external incident/financial/business consequence systems beyond a representative bounded source if needed for a proof scenario;
- broad external BI/application display telemetry;
- LLM/model rendering;
- semantic/vector search;
- specialized graph database;
- active-control enforcement;
- multi-region DR;
- enterprise-scale archive.

Their absence must not be represented as benign truth for propositions that would depend on them.

## MVP deployment shape

A valid minimal deployment can consist of:

1. Databricks-hosted/governed canonical Delta storage;
2. Databricks jobs/workflows or another verified worker runtime for acquisition/evaluation/reasoning;
3. a stateless API/service façade using separate workload identity;
4. a UI consuming the API;
5. GitHub/Databricks source credentials through short-lived federation where supported or a governed secret facility otherwise;
6. an observability/logging sink and backup/archive mechanism appropriate to the pilot promise.

The exact application framework/container/queue/cache/observability products remain implementation ADRs.

## MVP acceptance mapping

The implementation must demonstrate the foundation scenarios A–K, including stale upstream, join degradation, successful run/poor quality, deployment-correlated change without causal overclaim, planned structural transition, unintended violation, unregistered change, reachability vs exposure, multiple contributors, historical knowledge correction and policy-aware business explanation.

The architecture is acceptable only if those scenarios can be answered without special-case semantic shortcuts in the UI.
