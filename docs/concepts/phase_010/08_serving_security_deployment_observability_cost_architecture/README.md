# Phase 010 Group 08 — Serving, Security, Deployment, Observability & Cost Architecture

**Status:** COMPLETE / ACCEPTED

## Accepted result

- **ARCH-421–ARCH-500 accepted.**
- Cumulative Phase 010 architecture range: **ARCH-001–ARCH-500**.
- **SSO08-01–SSO08-120 pass.**
- **D-1603–D-1662 accepted.**
- No new product concept is required.

## Goal

Package ARCH-001–ARCH-420 into deployable serving, security, topology, observability/SLO, capacity/quota, cost and resilience boundaries without allowing runtime convenience to become truth, authority, evidence or control semantics.

## Selected serving chain

**authenticated request → canonical Principal/request context → current Capability Authorization + disclosure → exact retrieval / deterministic reasoning → Statement/Answer IR → authorized projection → response epistemic envelope → retained communication where promised**.

Historical replay and basis inspection remain dedicated governed paths.

## Selected logical topology

The MVP reference topology is **Databricks-centered canonical evidence + portable stateless service/edge components**:

- Delta-first canonical journals/policies remain the durable evidence/governance plane;
- reconciliation/normalization/measurement/reasoning workers may use Databricks-native or portable runtime according to verified deployment facts;
- a thin stateless API façade serves UI/integration callers through authorization-aware projections;
- derived graph/search/vector/cache/read stores remain rebuildable;
- externally reachable GitHub protection/Databricks pre-start control adapters may run outside Databricks when needed;
- SC-06 active-control capacity/failure domains are isolated from optional model/heavy interactive load.

This is a logical reference architecture, not a mandate for one container platform, queue, API gateway or secrets product.

## Security boundary

Authentication does not establish Capability Authorization or Assertion Authority. Human identities bind to canonical Principals; workloads use separate least-privilege identities where practical. Short-lived federated/OAuth/OIDC credentials are preferred where target capabilities support them.

Secret values are excluded from canonical evidence/routine telemetry. Material callbacks are authenticated/integrity-checked and replay-protected. Tenant/residency constraints cover canonical data, derived indexes/caches and operational telemetry.

For active control, authorization is opportunity/revision/horizon bound; revocation-sensitive or materially delayed irreversible enforcement is revalidated when policy requires it.

## Serving/cache boundary

UI callers do not receive unrestricted raw canonical/admin-table access. Serving stores/caches bind projection revision, canonical/source watermark, tenant and material authorization/disclosure context. A cache/page/index cannot create completeness, freshness or authority.

## Observability and SLOs

No global platform/integration/control score is accepted. Health remains multidimensional across acquisition/integration, canonical persistence, projections, serving, reasoning/replay, optional model/search, archive/restore and active control.

SLOs bind SC-01–SC-06. Numeric objectives are deployment ADRs after actual source publication lag, quota, workload and product promises are measured. An SLO breach is operational state, not monitored-domain health.

## Capacity and quota

Capacity plans bursty reconciliation, interactive/replay and control work separately. Bounded backpressure/priority protects required work while allowing optional model/enrichment work to degrade first.

Databricks acquisition prefers verified bulk/system-table/reconciliation/selective surfaces over naive per-object polling. GitHub uses scoped/incremental paths plus reconciliation and observed rate/secondary-limit state. Quota exhaustion degrades freshness/coverage; it never becomes a negative domain fact.

## Cost

Acquisition, processing/query/reasoning, storage/retention/archive, search/model and active-control usage is attributable where measurable by deployment/tenant/source/service-class/component dimensions. Budgets may drive explicit operational policy, but cannot silently shrink required Monitoring Scope, evidence coverage or control safety.

## Backup / DR / residency

Canonical journals/policy revisions and promised retained Explanation/control/basis records receive deployment-specific retention/RPO/RTO protection. Derived stores are rebuildable. Restore provenance and unrecovered gaps remain explicit; current recovery does not rewrite earlier missing evidence.

## Optional integrations

Collibra, Immuta, external BI/application telemetry, incident/business sources and model/search providers remain capability-gated. Their absence reduces only the propositions/features that depend on them and is reflected in coverage/availability; no replacement defaults are fabricated.

## Phase 009 gap treatment

- GAP-009-32 → service-class SLO model.
- GAP-009-33 → multidimensional integration/runtime observability.
- GAP-009-34 → Databricks quota-aware acquisition.
- GAP-009-35 → GitHub quota-aware acquisition.
- GAP-009-36 → optional deployment-verified Collibra capability.
- GAP-009-37 → optional deployment/contract-verified Immuta capability.
- GAP-009-38 → attributable ingestion/query/storage/model/control cost.
- GAP-009-39 → proposition-specific graceful optional-source degradation.
- GAP-009-40 → revisioned startup/periodic target capability inventory.

## Technology decisions intentionally not made

No final application framework, API gateway, queue/event bus, workflow engine, secrets vendor, external IdP, observability stack, cache product, container platform, cloud networking product or deployment automation product is mandated. Group 09 may freeze the MVP/enterprise implementation topology after whole-architecture replay.

## Group 09 handoff

Group 09 may now consolidate and replay **ARCH-001–ARCH-500**, resolve cross-group contradictions, freeze the target/reference architecture and ADR set, and produce the implementation handoff.
