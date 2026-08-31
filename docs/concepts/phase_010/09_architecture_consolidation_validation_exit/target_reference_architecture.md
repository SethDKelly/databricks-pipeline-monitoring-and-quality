# Phase 010 Group 09 — Frozen Target / Reference Architecture

**Status:** ACCEPTED — Phase 010 reference architecture

## Architecture thesis

DMTZ is a **Databricks-centered, evidence-first monitoring and reasoning framework** whose canonical structured history is Delta-first, whose user-facing/API paths are authorization-aware projections, and whose optional active controls are independent from passive truth.

The final architecture is organized into logical planes. These planes are ownership and failure-boundary descriptions, not a requirement to deploy one service/container per plane.

## Plane 0 — Deployment capability and configuration facts

Purpose:

- discover exact account/workspace/cloud/region/Geo/edition/version/feature/permission/reachability facts;
- retain target capability revisions and known limitations;
- drive feature/service-class eligibility and optional-integration degradation.

Inputs include verified target-environment facts and organization requirements/policies. Public vendor documentation is evidence about possible capability, not proof that the target deployment exposes it.

## Plane 1 — Source acquisition and normalization

Responsibilities:

- Databricks, GitHub and optional-source adapters;
- reconciliation-first collection with stream/webhook/incremental accelerators where useful;
- durable acquisition-run/attempt, request/page/window/partition/checkpoint provenance;
- source envelope/raw capture where justified by minimization policy;
- versioned normalization and quarantine;
- publication lag, quota and multidimensional integration-health telemetry;
- coverage manifests for proposition-specific negative reasoning.

Rule:

**source acquisition transports evidence; it does not create authority or canonical domain truth by convenience.**

## Plane 2 — Canonical evidence, identity, governance and history

Preferred realization:

- Delta Lake structured journals/tables;
- Unity Catalog managed tables/volumes when verified/appropriate;
- governed external Delta/object storage as portability realization where needed.

Canonical framework-owned state includes evidence IDs/provenance/time coordinates; Entity and Principal identity/bindings; Monitoring Scope/materialization history; Assertion Authority rules; Capability Authorization/disclosure policy and material decisions; Change Intent/Deployment/runtime evidence and implementation/input/output manifests; measurements/Assessments and accepted derived proposition records; Lineage evidence; encounter/exposure/effect/consequence evidence; Investigation/lead/Causal Claim lifecycle; retained Explanation communication where promised; and Gate/Safeguard decision/enforcement/control evidence when active controls are deployed.

Physical compaction, clustering, table maintenance, archive/restore or migration may change storage form without rewriting semantic history.

## Plane 3 — Deterministic evaluation, reasoning and derived projections

Responsibilities include measurement/Expectation/Baseline/Assessment evaluation; run/output/version association and health derivation; exact typed Lineage/Impact evaluation; deterministic negative-coverage and authority/evidence rules; Investigation reasoning plans/runs; Causal Claim status evaluation; historical availability-by-K replay; Statement IR / Answer IR composition; and rebuildable graph/search/vector/read projections.

Graph/search/vector/model systems may accelerate recall or presentation but do not own evidence, authority, causal confirmation or completeness.

## Plane 4 — Serving and experience

Responsibilities:

- authenticate human/application callers;
- bind canonical Principal/request context;
- evaluate current requester Capability Authorization/disclosure;
- invoke exact retrieval/reasoning/replay/basis operations;
- project safe Statement/Answer IR;
- expose epistemic envelope, watermarks and limitations;
- render deterministic explanations and optionally model-assisted prose;
- retain authentic communication evidence where product/audit policy requires it.

The preferred application boundary is a thin/stateless service/API façade. UI clients do not receive unrestricted raw canonical/system-table access.

Caches/materialized serving stores are authorization-context-aware derived projections with explicit canonical/source watermarks and applicability horizons.

## Plane 5 — Optional active control

Execution Gate and Propagation Safeguard are independent opt-in capabilities over passive monitoring.

The Gate chain remains:

**opportunity → criterion evidence suitability → readiness → normal/override/fallback decision → issuance → delivery/acceptance → enforcement → actual execution/non-execution**.

The Safeguard chain remains:

**protected state/path/cohort → proposal/authorization/request → enforcement → exposure opportunity + alternate-path coverage → REF-028 prevention → release/expiry → independent recovery**.

Active control uses exact accepted proposition identities and deterministic policy. Search/model output cannot issue control decisions. SC-06 latency/resource/failure domains are protected from optional heavy workloads to the degree required by the deployment profile.

## Plane 6 — Operations, security, resilience and economics

Cross-cutting responsibilities include workload identity and credential lifecycle; network/egress/callback controls; audit and sensitive telemetry minimization; multidimensional platform/integration/reasoning/control observability; SC-01–SC-06 SLOs; capacity, priority, backpressure and quota ledgers; cost attribution and budget policy; retention/archive/restore/backup/DR/residency controls; and startup/periodic capability verification.

Operational health is never automatically monitored-domain health.

## Primary end-to-end evidence flow

**deployment-verified capability + Monitoring Scope → revisioned acquisition plan → source evidence + acquisition provenance/coverage → canonical identity/time/governance persistence → exact runtime/measurement/Lineage/encounter evidence → deterministic proposition evaluation → Investigation/replay/Statement IR → current authorized projection → UI/API/retained communication**.

Optional active control branches from accepted evidence/proposition state and rejoins only as independently evidenced decision/enforcement/execution/prevention history.

## Truth / ownership rules

1. Source-owned facts retain their source authority/limitations after copying.
2. Framework-owned organization policy/workflow state is canonical only for its accepted DMTZ proposition family.
3. Derived graphs/search/vector/caches/read models are rebuildable.
4. Renderer/model prose is not canonical proposition state.
5. UI session/application stores are not parallel truth databases.
6. Current source/config/policy state never backfills historical state.
7. Retained prior communication is distinct from reconstructed historical Explanation.
8. Authorization is distinct from evidence sufficiency, Assertion Authority and enforcement/action.

## Technology intentionally not frozen by Phase 010

The architecture does not require one universal API/application framework, container/serverless hosting product, event bus/queue/orchestrator, secret manager, external IdP, observability vendor, cache product, specialized graph database, vector/search provider, LLM/provider/agent framework, or infrastructure-as-code/deployment automation product.

Those selections are implementation ADRs driven by target deployment facts and measurable workload needs. Their adoption may not alter the frozen semantic/ownership boundaries above.

## Frozen result

The reference architecture is sufficiently concrete to implement without inventing new truth, authority, time, evidence, causal, Impact, Explanation or control semantics.
