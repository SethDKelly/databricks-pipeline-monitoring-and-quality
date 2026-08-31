# Implementation 003 — Source Acquisition, Capability & Evidence Reliability

**Status:** PLANNED

## Objective

Turn the 001 Databricks walking adapter into the production-shaped source acquisition plane for the MVP: Databricks + GitHub, capability discovery, reconciliation, cross-source correlation evidence, coverage, integration health and quota-aware operation.

## Entry gate

- 001 adapter/evidence/persistence contracts stable;
- 002 identity/governance interfaces available for source subject/principal mapping where needed;
- pilot Databricks/GitHub sources selected.

## Group plan

### 003-A — Deployment Capability Inventory

Implement startup/periodic discovery and versioned capability facts for exact target account/workspace/cloud/region/edition/API/system surfaces, permissions, retention/latency and optional features.

### 003-B — Adapter SDK / Source Contract

Generalize vendor-neutral adapter, checkpoint, coverage, raw-envelope/minimization, normalization and quarantine interfaces.

### 003-C — Databricks Acquisition Expansion

Implement the bounded Databricks surfaces needed for MVP runtime, metadata, execution, Lineage/measurement/audit evidence. Favor reconciliation/bulk/system surfaces plus selective incremental APIs according to capability and service class.

### 003-D — GitHub Acquisition Foundation

Implement repository/revision, workflow/run/attempt, deployment/environment/review evidence needed by the pilot. Prefer webhook/incremental accelerators plus reconciliation rather than unbounded polling.

### 003-E — Cross-System Correlation & Attestation

Implement durable repository/revision/deployment/Databricks-target/run association using explicit IDs/tokens/manifests/attestation where native linkage is insufficient.

No name/time proximity joins.

### 003-F — Coverage, Negative-Evidence & Integration Health

Implement proposition/source-specific coverage manifests and integration-health state sufficient to suppress or narrow strong negatives under permission, pagination, lag, outage, retention or schema failures.

### 003-G — Backfill, Replay, Checkpoint & Quota Behavior

Implement safe historical backfill/reconciliation, redelivery/idempotency, high-water marks, quota/rate budgets and cost-aware acquisition scheduling.

Cost/quota pressure may change schedule; it may not manufacture absence.

### 003-H — Consolidation / Exit

Run adapter fault injection plus real target integration tests and prove Databricks/GitHub evidence can be collected/replayed without semantic strengthening.

## Exit result

MVP source collection is trustworthy enough that downstream health/reasoning can distinguish:

- no source record with adequate coverage;
- source/integration unavailable;
- partial/incomplete evidence;
- unsupported/unlicensed capability;
- delayed evidence;
- actual bounded evidence absence.

## Deferred

Collibra, Immuta and specialized downstream consumer/application adapters belong to 009 unless the MVP pilot explicitly requires them.
