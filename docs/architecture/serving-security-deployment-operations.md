# Serving, Security, Deployment, Observability & Cost Architecture

**Canonical key:** `architecture.serving_security_deployment_operations`

**Kind:** TECHNICAL ARCHITECTURE CONTRACT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration records:** `stable_family.ARCH`, `architecture.serving_security_deployment_operations`

**Stable IDs:** ARCH-421–ARCH-500

**Stable ID index:** `ARCH-421`, `ARCH-422`, `ARCH-423`, `ARCH-424`, `ARCH-425`, `ARCH-426`, `ARCH-427`, `ARCH-428`, `ARCH-429`, `ARCH-430`, `ARCH-431`, `ARCH-432`, `ARCH-433`, `ARCH-434`, `ARCH-435`, `ARCH-436`, `ARCH-437`, `ARCH-438`, `ARCH-439`, `ARCH-440`, `ARCH-441`, `ARCH-442`, `ARCH-443`, `ARCH-444`, `ARCH-445`, `ARCH-446`, `ARCH-447`, `ARCH-448`, `ARCH-449`, `ARCH-450`, `ARCH-451`, `ARCH-452`, `ARCH-453`, `ARCH-454`, `ARCH-455`, `ARCH-456`, `ARCH-457`, `ARCH-458`, `ARCH-459`, `ARCH-460`, `ARCH-461`, `ARCH-462`, `ARCH-463`, `ARCH-464`, `ARCH-465`, `ARCH-466`, `ARCH-467`, `ARCH-468`, `ARCH-469`, `ARCH-470`, `ARCH-471`, `ARCH-472`, `ARCH-473`, `ARCH-474`, `ARCH-475`, `ARCH-476`, `ARCH-477`, `ARCH-478`, `ARCH-479`, `ARCH-480`, `ARCH-481`, `ARCH-482`, `ARCH-483`, `ARCH-484`, `ARCH-485`, `ARCH-486`, `ARCH-487`, `ARCH-488`, `ARCH-489`, `ARCH-490`, `ARCH-491`, `ARCH-492`, `ARCH-493`, `ARCH-494`, `ARCH-495`, `ARCH-496`, `ARCH-497`, `ARCH-498`, `ARCH-499`, `ARCH-500`

**Owns current question after cutover:** How is the accepted DMTZ architecture packaged into serving, security, deployment, observability/SLO, capacity/quota, cost and resilience boundaries without making runtime convenience into truth or authority?

## Canonical contract

The serving chain is:

**authenticated request → canonical Principal/request context → current Capability Authorization + disclosure → exact retrieval / deterministic reasoning → Statement/Answer IR → authorized projection → response epistemic envelope → retained communication where promised**.

Historical replay and basis inspection remain separately governed paths.

## Logical topology

The reference MVP is **Databricks-centered canonical evidence with portable stateless service/edge components**:

- Delta-first canonical journals/policies remain the durable evidence/governance plane;
- acquisition/normalization/measurement/reasoning workers may use verified Databricks-native or portable runtime;
- a thin stateless API façade serves UI/integration callers through authorization-aware projections;
- graph/search/vector/cache/read stores remain rebuildable projections;
- externally reachable protection/pre-start control adapters may execute outside Databricks where required;
- SC-06 active-control capacity/failure domains are isolated from optional model/heavy interactive load according to the deployment profile.

This is a logical architecture, not a mandate for a particular container platform, queue, API gateway or secrets product.

## Security and serving

Authentication does not establish Capability Authorization or Assertion Authority. Human and workload identities bind to canonical Principals; separate least-privilege workload identities are preferred. Short-lived federated/OAuth/OIDC credentials are preferred where verified support and policy allow them.

Secret values remain outside canonical evidence and routine telemetry. Material callbacks require authentication/integrity verification and replay protection. Tenant/residency applies to canonical data, projections, caches and operational telemetry.

UI/API callers do not receive unrestricted raw canonical/system-table access. Serving stores and caches bind projection revision, canonical/source watermark, tenant, material authorization/disclosure context and applicability horizon. Cache presence or page completeness cannot create freshness, completeness or authority.

## Observability and service levels

Operational health is multidimensional across acquisition/integration, canonical persistence, projections, serving, reasoning/replay, optional model/search, archive/restore and active control. No global platform/integration/control score is accepted.

SLOs bind SC-01–SC-06. Numeric objectives are deployment ADRs after source lag, quota, workload and product promises are measured. SLO breach is operational state, not monitored-domain health.

Capacity treats bursty reconciliation, interactive/replay and control work separately. Bounded priority/backpressure protects required work while optional model/enrichment can degrade first.

Quota exhaustion degrades freshness/coverage; it never becomes a negative domain fact.

## Cost, backup, DR and residency

Acquisition, processing/query/reasoning, storage/retention/archive, search/model and active-control use is attributable where measurable by deployment, tenant, source, service class and component. Budget policy cannot silently shrink required Monitoring Scope, evidence coverage, retention promises or control safety.

Canonical journals/policy revisions and promised retained Explanation/control/basis records receive deployment-specific retention, backup, RPO/RTO and residency protection. Derived stores are rebuildable. Restore provenance and unrecovered gaps remain explicit; current recovery does not rewrite earlier missing evidence.

## Optional integrations and deployment variability

Collibra, Immuta, external BI/application telemetry, incident/business sources and model/search providers remain capability-gated. Their absence narrows only dependent propositions/features. No substitute truth or benign default is fabricated.

Startup and periodic capability verification keeps operational topology bound to actual deployment facts.

## Technology boundary

No final application framework, API gateway, queue/event bus, workflow engine, secret manager, external IdP, observability backend, cache product, container/serverless platform, cloud networking product or deployment automation product is mandated by this architecture contract.

## Provenance

- `docs/concepts/phase_010/08_serving_security_deployment_observability_cost_architecture/README.md`
- atomic ARCH-421–ARCH-500 files under that Phase 010 group
- Phase 010 decisions D-1603–D-1662 and SSO08-01–SSO08-120 review evidence
