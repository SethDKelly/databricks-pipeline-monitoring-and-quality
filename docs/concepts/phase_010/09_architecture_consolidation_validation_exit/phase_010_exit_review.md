# Phase 010 Exit Review — Technical Architecture

**Status:** ACCEPTED — PHASE 010 COMPLETE

## Exit result

Phase 010 exits successfully with:

- **ARCH-001–ARCH-500 final**;
- Group 01 **AFE01-01–AFE01-60 PASS**;
- Group 02 **EPT02-01–EPT02-72 PASS**;
- Group 03 **IAD03-01–IAD03-84 PASS**;
- Group 04 **AHI04-01–AHI04-96 PASS**;
- Group 05 **RHI05-01–RHI05-108 PASS**;
- Group 06 **IRE06-01–IRE06-120 PASS**;
- Group 07 **ACS07-01–ACS07-120 PASS**;
- Group 08 **SSO08-01–SSO08-120 PASS**;
- Group 09 **ACV09-01–ACV09-120 PASS**;
- **D-1263–D-1700 accepted** across Phase 010 architecture/exit work;
- all **GAP-009-01–GAP-009-40** classified with explicit architecture/deployment/implementation disposition;
- accepted concept catalog remains unchanged;
- **no ARCH-501 is required**.

Design scenario `PASS` remains architecture validation, not a claim that production code/integration tests already exist.

## What Phase 010 establishes

Phase 010 converts the completed functional/integration model into a technically realizable target architecture without making a vendor runtime, UI cache, graph, model, source table or control adapter the new truth model.

The frozen reference architecture is:

**deployment-verified capability + organization policy → reconciliation-first acquisition → Delta-first canonical evidence/identity/governance history → exact runtime/measurement/Lineage/encounter evidence → deterministic evaluation/reasoning/replay → Statement IR / Answer IR → current authorized serving projection → UI/API/retained communication**, with **Execution Gate and Propagation Safeguard as independent optional active-control branches**.

## Frozen target architecture

### Canonical data/evidence plane

- Delta-first canonical structured persistence;
- selective/minimized evidence payload retention;
- durable evidence identity independent from source-local IDs/paths;
- explicit event/effective, availability/knowledge, collection/persistence, correction/supersession and communication time;
- non-rewriting history through correction/supersession;
- governed retention/pin/archive/restore lifecycle;
- Unity Catalog managed tables/volumes as preferred conditional Databricks realization, with governed external Delta/object storage remaining portable where needed.

### Identity and governance plane

- canonical tenant-scoped Entity/Principal identity;
- source identity binding/incarnation history;
- organization-owned Monitoring Scope;
- proposition/facet/context/time-specific Assertion Authority;
- exact Capability Authorization and disclosure policy;
- current and historical authorization separated;
- requester permission separated from internal service/workload permission;
- no hidden universal allow/deny/role precedence.

### Acquisition/integration plane

- deployment-bound capability instances;
- reconciliation-first hybrid acquisition;
- durable run/attempt/request/page/window/checkpoint provenance;
- checkpoint advancement only after durable evidence publication;
- versioned parser/normalizer and quarantine;
- multidimensional integration health and coverage manifests;
- quota-aware Databricks/GitHub collection;
- optional integrations capability-gated rather than assumed.

### Runtime/health/Lineage/Impact plane

- exact/partial Change→Deployment→run association;
- run-specific implementation/input/output manifests;
- measurement/Expectation/Baseline/Assessment provenance;
- typed temporal Lineage;
- consumer encounter/cache/result/version evidence;
- exposure/effect/consequence separated;
- no transitive Impact or broad negative without coverage.

### Investigation/reasoning/replay/Explanation plane

- canonical Investigation/lead/Causal Claim history;
- deterministic-first evidence/coverage/authority evaluation;
- Delta-backed derived graph projection and exact-first retrieval;
- semantic/vector/model functions limited to candidate/assistance roles;
- `confirmed` causality remains REF-017 + AUTH-034 gated;
- availability-by-K replay from canonical bitemporal state;
- Statement IR / Answer IR before rendering;
- itemwise `inspectBasis` authorization;
- authentic retained communication distinct from reconstruction;
- deterministic render fallback independent from model availability.

### Active-control plane

- active control remains opt-in over passive monitoring;
- Gate and Safeguard remain independent;
- opportunity-specific deterministic criteria/readiness/decision state;
- decision/delivery/acceptance/enforcement/execution separated;
- override/fallback/degradation explicit as policy-as-data;
- path/cohort-specific Safeguard enforcement;
- REF-028 prevention requiring opportunity/enforcement/alternate-path evidence;
- current policy cannot backfill historical control action;
- model/search/graph outputs cannot issue decisions;
- SC-06 capacity/failure-domain protection where deployed.

### Serving/security/operations plane

- thin/stateless authorization-aware service façade preferred;
- UI has no unrestricted raw canonical/system-table access;
- derived read/cache/search stores retain revision/watermark/context and are rebuildable;
- separate human/workload identities and least privilege;
- short-lived federation preferred where verified;
- secrets excluded from canonical evidence/routine telemetry;
- authenticated/replay-protected callbacks;
- tenant/residency controls extend to derived stores, telemetry and archive;
- platform/integration/reasoning/control observability remains multidimensional;
- SC-01–SC-06 SLOs instead of one global SLA;
- cost attribution/budget cannot weaken evidence/control promises;
- backup/DR preserves non-rewriting history and explicit restore gaps.

## Cross-group contradiction review

`cross_group_consistency_matrix.md` passes. The principal potential tensions were explicitly reconciled:

- Databricks-centered reference topology does not override environment discovery;
- serving/caches cannot become canonical truth;
- cost/retention optimization cannot erase promised replay basis;
- service identities cannot leak their privilege to requesters;
- current authorization cannot rewrite historical authorization/truth;
- graph traversal cannot manufacture exposure/cause;
- model assistance cannot replace deterministic status/authority rules;
- active-control latency cannot collapse decision/enforcement/execution semantics;
- control deployment remains optional for passive MVP.

No contradiction requires a new ARCH contract.

## Phase 009 gap disposition

All GAP-009-01–40 have architecture dispositions. Important limitations are intentionally retained rather than overclaimed:

- complete native historical Lineage is not universally guaranteed;
- exact bundle/workspace-source commit and multi-input consumption can require instrumentation/attestation;
- exact external consumer-version/use and business consequence evidence is source/environment specific;
- broad multi-hop negative Impact coverage can remain expensive/partial;
- there is no universal single Safeguard mechanism across every delivery path;
- authentic historical communication/projection only exists where it was retained;
- Collibra/Immuta operational capability remains tenant/contract specific;
- numeric SLO/capacity/RPO/RTO/cost values remain target-deployment ADRs.

These are not hidden behind weaker semantics.

## MVP freeze

The initial MVP is **passive monitoring/reasoning/replay focused** and Databricks/GitHub-centered.

Required:

- capability discovery;
- source acquisition/reconciliation;
- canonical Delta evidence/governance state;
- identity/scope/authority/authorization;
- core health/data-quality observations/evaluations;
- run/deployment/Lineage provenance;
- representative downstream encounter/Impact evidence;
- deterministic Investigation/Causal Claim/replay/Explanation;
- authorization-aware API/UI;
- basic multidimensional observability/cost/backup.

Not mandatory for the initial MVP:

- Collibra;
- Immuta;
- LLM/model rendering;
- semantic/vector retrieval;
- dedicated graph database;
- Execution Gate/Safeguard enforcement;
- universal external BI/business consequence integration;
- enterprise multi-region archive/DR.

If an optional capability is deployed, it must implement the accepted semantics for its bounded use rather than a simplified substitute.

## Build-versus-integrate conclusion

DMTZ builds the semantic machinery that vendors cannot safely define implicitly:

- canonical evidence/time/identity contracts;
- scope/authority/authorization/disclosure semantics;
- acquisition coverage/reconciliation semantics;
- deterministic status/negative/causal rules;
- Investigation/Causal Claim/replay;
- Statement IR / Answer IR;
- Gate/Safeguard state machines.

It integrates commodity/source infrastructure such as Delta/Unity Catalog storage/governance capabilities, Databricks/GitHub APIs, enterprise identity/secrets, schedulers/queues, observability, backup/archive and optional search/model/graph technologies.

## External capability revalidation

Current 2026-08-31 public Databricks/GitHub documentation remains compatible with the architecture:

- system tables remain Unity Catalog-governed and source/surface specific in retention/latency;
- system-table data is sensitive and should be governed rather than exposed directly;
- Databricks workload OAuth federation remains a recommended automated-auth pattern where supported;
- GitHub environment protection remains a viable pre-run control for the exact protected job.

Target deployments must still be discovered independently.

## Remaining implementation decisions

`unresolved_implementation_decisions.md` records concrete choices intentionally deferred: language/framework, API gateway, worker/orchestrator/queue, physical schemas/optimization, secret/IdP/policy engine, cache, graph/search/model products, UI framework, observability, exact SLO/capacity values, optional enterprise integrations, active-control adapters, DR/IaC and executable test harness.

Those are implementation selections, not missing Phase 010 semantics.

## Phase 010 exit gate evaluation

The exit gate passes because:

1. accepted Phase 002–009 semantics are technically realizable under the reference architecture;
2. source limitations remain visible and proposition-specific;
3. runtime truth ownership is explicit through the store ownership map;
4. all architecture groups compose without unresolved contradiction;
5. all Phase 009 residual gaps have explicit disposition;
6. MVP and enterprise boundaries are frozen;
7. security/trust boundaries are explicit;
8. failure/degradation behavior preserves supported sibling propositions and avoids false negatives/positives;
9. observability/SLO/cost/DR constraints are architecture-defined without inventing universal numeric claims;
10. active control remains safe/independent/optional;
11. implementation has an explicit unresolved-decision register rather than hidden assumptions;
12. implementation can begin without inventing missing truth/evidence/authority/control/Explanation semantics.

## Final conclusion

**Phase 010 — Technical Architecture is COMPLETE.**

**Final Phase 010 range: ARCH-001–ARCH-500. No ARCH-501 is required.**

The durable roadmap now proceeds to **later MVP implementation/validation planning**, which should convert this architecture into implementation phases, executable contract tests, deployment-specific ADR values and measurable MVP acceptance criteria. The roadmap does not currently assign a numbered Phase 011, so this exit does not invent one.
