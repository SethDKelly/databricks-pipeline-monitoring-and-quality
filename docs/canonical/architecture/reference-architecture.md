# DMTZ Frozen Target / Reference Architecture

**Canonical key:** `architecture.reference_architecture`

**Kind:** REFERENCE TECHNICAL ARCHITECTURE

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `architecture.reference_architecture`

**Stable-ID coverage:** composes ARCH-001–ARCH-500; it does not create ARCH-501.

**Owns current question after cutover:** What is the frozen end-to-end DMTZ target architecture and which planes own evidence, policy, reasoning, serving, controls and operations?

## Architecture thesis

DMTZ is a **Databricks-centered, evidence-first monitoring and reasoning framework** whose canonical structured history is Delta-first, whose user-facing/API paths are authorization-aware projections, and whose optional active controls are independent from passive truth.

The planes below describe logical ownership and failure boundaries; they do not require one service/container per plane.

## Plane 0 — Deployment capability and configuration facts

Discover exact account/workspace/cloud/region/Geo/edition/version/feature/permission/reachability facts; retain target capability revisions and limitations; and drive feature/service-class eligibility and optional-integration degradation.

Public/vendor documentation proves possible capability, not target deployment capability.

## Plane 1 — Source acquisition and normalization

Own Databricks, GitHub and optional-source adapters; reconciliation-first collection with incremental/stream/webhook accelerators; durable acquisition/request/page/window/partition/checkpoint provenance; minimized source capture; versioned normalization/quarantine; publication-lag/quota/integration-health telemetry; and coverage manifests for proposition-specific negative reasoning.

**Source acquisition transports evidence; it does not create authority or canonical domain truth by convenience.**

## Plane 2 — Canonical evidence, identity, governance and history

Use Delta Lake structured journals/tables as the preferred durable realization, with Unity Catalog managed tables/volumes only when verified and appropriate and governed external Delta/object storage where portability requires it.

Canonical framework-owned state includes retained evidence identity/provenance/time; Entity/Principal identity and source bindings; Monitoring Scope/materialization history; Assertion Authority; Capability Authorization/disclosure state and material decisions; Change Intent/Deployment/runtime and implementation/input/output manifests; measurements/Assessments and accepted derived propositions; Lineage; encounter/exposure/effect/consequence evidence; Investigation/lead/Causal Claim lifecycle; retained Explanation communication where promised; and Gate/Safeguard decision/enforcement evidence when active control is deployed.

Physical storage maintenance may change form without rewriting semantic history.

## Plane 3 — Deterministic evaluation, reasoning and derived projections

Own measurement/Expectation/Baseline/Assessment evaluation; run/output/version association and health derivation; typed Lineage/Impact evaluation; deterministic negative-coverage and authority/evidence rules; Investigation reasoning; Causal Claim state; historical availability-by-K replay; Statement IR / Answer IR; and rebuildable graph/search/vector/read projections.

Graph/search/vector/model systems may accelerate recall or presentation but do not own evidence, authority, causal confirmation or completeness.

## Plane 4 — Serving and experience

Authenticate callers; bind canonical Principal/request context; evaluate current Capability Authorization/disclosure; invoke exact retrieval/reasoning/replay/basis operations; project safe Statement/Answer IR; expose epistemic envelope, watermarks and limitations; render deterministic and optional model-assisted explanations; and retain authentic communication evidence where required.

The preferred application boundary is a thin/stateless service/API façade. UI clients do not receive unrestricted canonical/system-table access. Caches/materialized serving stores are authorization-context-aware derived projections with explicit watermarks and applicability horizons.

## Plane 5 — Optional active control

Execution Gate and Propagation Safeguard are independent opt-in capabilities over passive monitoring.

Gate:

**opportunity → criterion evidence suitability → readiness → normal/override/fallback decision → issuance → delivery/acceptance → enforcement → actual execution/non-execution**.

Safeguard:

**protected state/path/cohort → proposal/authorization/request → enforcement → exposure opportunity + alternate-path coverage → REF-028 prevention → release/expiry → independent recovery**.

Active control uses exact accepted proposition identities and deterministic policy. Search/model output cannot issue control decisions. SC-06 resource/latency/failure domains are protected from optional heavy work as required by the deployment profile.

## Plane 6 — Operations, security, resilience and economics

Cross-cutting responsibilities include workload identity/credential lifecycle; network/egress/callback controls; audit and sensitive telemetry minimization; multidimensional platform/integration/reasoning/control observability; SC-01–SC-06 SLOs; capacity/priority/backpressure/quota ledgers; cost attribution/budget policy; retention/archive/restore/backup/DR/residency; and startup/periodic capability verification.

Operational health is never automatically monitored-domain health.

## Primary end-to-end flow

**deployment-verified capability + Monitoring Scope → revisioned acquisition plan → source evidence + acquisition provenance/coverage → canonical identity/time/governance persistence → exact runtime/measurement/Lineage/encounter evidence → deterministic proposition evaluation → Investigation/replay/Statement IR → current authorized projection → UI/API/retained communication**.

Optional active control branches from accepted evidence/proposition state and rejoins only as independently evidenced decision/enforcement/execution/prevention history.

## Truth and ownership rules

1. Source-owned facts retain source authority and limitations after copying.
2. Framework-owned organization policy/workflow state is canonical only for its accepted DMTZ proposition family.
3. Derived graph/search/vector/cache/read models are rebuildable.
4. Renderer/model prose is not canonical proposition state.
5. UI/session/application stores are not parallel truth databases.
6. Current source/config/policy state never backfills historical state.
7. Retained prior communication is distinct from reconstructed historical Explanation.
8. Authorization is distinct from evidence sufficiency, Assertion Authority and enforcement/action.

## Frozen MVP boundary

The initial implementation is Databricks/GitHub-centered and proves passive monitoring/health/quality, provenance, typed temporal Lineage, Investigation/Causal Claim reasoning, representative Impact, historical replay and evidence-grounded authorization-aware Explanation.

Collibra, Immuta, LLM/model rendering, semantic/vector retrieval, a dedicated graph database, active-control enforcement, universal external BI/business-consequence telemetry and enterprise multi-region archive/DR are not mandatory MVP dependencies. Optional capabilities must preserve the accepted bounded semantics if enabled.

## Technology intentionally not frozen

The architecture does not mandate one application/API framework, container/serverless platform, queue/event bus/orchestrator, secret manager, external IdP, policy engine, observability backend, cache, specialized graph system, vector/search provider, model/provider/agent framework, UI framework, infrastructure-as-code tool or deployment automation product.

Those are implementation ADRs driven by target deployment facts and measurable workload needs; they may not alter the frozen semantic/ownership boundaries.

## Frozen result

ARCH-001–ARCH-500 and this reference architecture are sufficient to implement DMTZ without inventing new truth, authority, time, evidence, causal, Impact, Explanation or control semantics. **No ARCH-501 is required.**

## Provenance

- `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md`
- `docs/concepts/phase_010/09_architecture_consolidation_validation_exit/README.md`
- Phase 010 consolidation decisions D-1663–D-1700 and ACV09-01–ACV09-120 review evidence
