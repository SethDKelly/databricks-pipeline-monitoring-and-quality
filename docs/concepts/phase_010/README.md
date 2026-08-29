# Phase 010 — Technical Architecture

**Status:** IN PROGRESS — Groups 01–06 accepted; Group 07 next

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

Current accepted range: **ARCH-001–ARCH-350** from Groups 01–06.

## Logical groups

### Group 01 — Architecture Frame, Environment Discovery & Decision Criteria

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-001–ARCH-032**. **AFE01-01–AFE01-60 pass.** Decisions D-1269–D-1298 accepted.

Group 01 establishes the deployment-bound capability model, architecture fact classes, environment verification/unknown discipline, MVP/enterprise boundary, hard constraints, decision-specific quality tradeoffs, six service classes, ADR discipline and GAP-009 ownership.

Its central rule is:

**documented capability ≠ deployment presence ≠ licensed entitlement ≠ enablement ≠ authorization ≠ reachability ≠ observable coverage ≠ proposition-specific usability**.

Path: [`01_architecture_frame_environment_discovery_decision_criteria/README.md`](01_architecture_frame_environment_discovery_decision_criteria/README.md)

### Group 02 — Evidence, Provenance, Temporal & Persistence Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-033–ARCH-080**. **EPT02-01–EPT02-72 pass.** Decisions D-1299–D-1336 accepted.

Group 02 selects a Delta Lake-first canonical structured evidence plane, selective cloud-object payload retention, explicit multi-coordinate/bitemporal history, non-rewriting correction/supersession, common-derivation provenance and tiered retention/relevance lifecycle.

Its central persistence rule is:

**source-owned evidence → framework-retained identity/provenance/time → canonical non-rewriting journals → policy-bound lifecycle → derived rebuildable graph/search/serving projections**.

Storage retention, retained detail and reporting/retrieval relevance remain independent. Ordinary reference retention defaults keep roughly 120 days recent detail, roughly 400 days detailed replay and up to roughly 24 months approved trend aggregates, while exact multi-year evidence is pinned/retained only for explicit product, incident, recurrence, audit, security, legal or other governed need.

Path: [`02_evidence_provenance_temporal_persistence_architecture/README.md`](02_evidence_provenance_temporal_persistence_architecture/README.md)

### Group 03 — Identity, Scope, Authority, Authorization & Disclosure Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-081–ARCH-132**. **IAD03-01–IAD03-84 pass.** Decisions D-1337–D-1382 accepted.

Group 03 realizes tenant-scoped canonical Entity/Principal identity, evidence-bearing source identity bindings, organization-owned Monitoring Scope, Assertion Authority and Capability Authorization policy-as-data, current/historical authorization decision semantics, and disclosure-dimensional safe projection.

Its central governance chain is:

**source-local identity → canonical ecosystem identity → Monitoring Scope → Assertion Authority → Capability Authorization → current/historical authorization evaluation → authorized disclosure projection → independently evidenced enforcement/action**.

It preserves source-local IDs after mapping; unknown scope membership is not exclusion; vendor roles/ownership are not automatic Assertion Authority; authorization is not enforcement; service-principal processing permission is not requester access; actual authorization decision is not replay-derived authorization; and safe abstraction cannot strengthen truth.

Path: [`03_identity_scope_authority_authorization_disclosure_architecture/README.md`](03_identity_scope_authority_authorization_disclosure_architecture/README.md)

### Group 04 — Source Acquisition, Adapter, Synchronization & Integration-Health Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-133–ARCH-190**. **AHI04-01–AHI04-96 pass.** Decisions D-1383–D-1432 accepted.

Group 04 establishes reconciliation-first hybrid source acquisition, durable acquisition-run/surface/plan/checkpoint/page/window provenance, versioned normalization, explicit collection coverage, source publication/acquisition lag, quota/cost-aware scheduling and multidimensional integration health.

Its central acquisition chain is:

**verified capability + governed scope → revisioned acquisition plan → reconciliation-first hybrid collection → durable source/request/page/checkpoint provenance → versioned normalization → coverage + source lag + integration-health dimensions → canonical evidence publication**.

Streams/webhooks accelerate freshness but do not replace reconciliation where completeness matters. Empty/partial/degraded collection never becomes domain absence; integration recovery does not rewrite historical evidence gaps; no global integration-health score is accepted.

Path: [`04_source_acquisition_adapter_synchronization_integration_health_architecture/README.md`](04_source_acquisition_adapter_synchronization_integration_health_architecture/README.md)

### Group 05 — Runtime Provenance, Health, Lineage & Impact Evidence Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-191–ARCH-274**. **RHI05-01–RHI05-108 pass.** Decisions D-1433–D-1490 accepted.

Group 05 realizes exact/partial Change→deployment→activation→run correlation, run-specific implementation/input/output manifests, measurement/health provenance, typed historical Lineage, consumer encounter/cache/result state, exact-version exposure, downstream effect and consequence evidence.

Its central evidence chain is:

**source-owned runtime facts + selective attestation → exact/partial implementation/input/output manifests → measurements + governed Assessments → typed historical Lineage → actual encounter/version state → exposure → effect → consequence → Group 06 causal/reasoning handoff**.

Native source evidence is preferred; selective DMTZ deployment/runtime/consumer attestation fills explicit gaps where the deployment chooses to support stronger propositions. Missing exact bindings remain partial/unknown rather than inferred from current/latest state. Group 04 coverage/integration health constrains every strong operational/Impact negative.

Path: [`05_runtime_provenance_health_lineage_impact_evidence_architecture/README.md`](05_runtime_provenance_health_lineage_impact_evidence_architecture/README.md)

### Group 06 — Investigation, Reasoning, Historical Replay & Explanation Architecture

**Status:** COMPLETE / ACCEPTED

Accepted range: **ARCH-275–ARCH-350**. **IRE06-01–IRE06-120 pass.** Decisions D-1491–D-1544 accepted.

Group 06 realizes canonical Investigation/Causal Claim persistence, deterministic evidence-bound reasoning, Delta-backed rebuildable graph projections, exact-first retrieval, availability-by-K replay, Statement IR / Answer IR, independently authorized basis inspection, authentic Explanation snapshots and optional non-authoritative model assistance.

Its central reasoning chain is:

**bounded question / Investigation → exact retrieval + bounded derived graph → deterministic evidence/time/coverage/authority evaluation → lead/Causal Claim state → Statement IR / Answer IR → authorized basis projection → deterministic or optional model rendering → immutable retained communication where promised**.

Model, graph and semantic-search outputs remain derived. A model outage must not prevent a truthful basic answer when canonical evidence is available. Causal confirmation remains REF-017 + AUTH-034 gated, and reconstructed historical Explanation remains distinct from authentic retained communication.

Path: [`06_investigation_reasoning_historical_replay_explanation_architecture/README.md`](06_investigation_reasoning_historical_replay_explanation_architecture/README.md)

### Group 07 — Execution Gate, Propagation Safeguard & Active-Control Architecture

**Status:** Next — not started

Realize Execution Gate and Propagation Safeguard independently, including criterion/evidence suitability, readiness, decisions, delivery/acceptance, enforcement, actual execution, overrides/fallbacks, protected paths/cohorts, prevention evidence, release, and recovery.

Path: [`07_execution_gate_propagation_safeguard_active_control_architecture/README.md`](07_execution_gate_propagation_safeguard_active_control_architecture/README.md)

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

## Group 01 accepted architecture discipline

Later groups must preserve:

- verified public/vendor fact ≠ target-environment discovered fact ≠ organization requirement ≠ architecture assumption ≠ unresolved unknown;
- vendor/product name ≠ concrete capability instance;
- documented support ≠ target deployment presence/enablement/entitlement/permission/reachability/coverage;
- capability usability as proposition/service-class specific rather than one Boolean;
- capability verification as provenance-bearing and time-aware;
- unknown capability state as first-class;
- cloud/region/Geo/government deployment, version, plan/license, preview/feature flag and network/security context where material;
- optional source absence as bounded capability loss, not benign default;
- semantic/evidence/security/degraded-state rules as hard architecture constraints;
- decision-specific quality tradeoffs with no universal architecture score;
- explicit decision reversibility and assumption/unknown register;
- SC-01–SC-06 service classes instead of one freshness SLA;
- GAP-009-01–GAP-009-40 ownership/treatment through Phase 010 exits.

## Group 02 accepted architecture discipline

Later groups must also preserve:

- Delta Lake canonical structured persistence with deployment-bound managed/external realization;
- selective, data-minimized cloud-object payload retention rather than universal raw copying;
- framework evidence identity distinct from source-local identity and physical storage location;
- source ownership/authority after copy;
- event/effective, source-available, collection/persistence, correction/supersession and communication time separation;
- late evidence as late for prior knowledge cuts;
- non-rewriting semantic journals independent of physical compaction;
- common derivation and parser/normalizer provenance;
- graph/search/vector/serving stores as derived/rebuildable projections;
- Delta time travel not being the product replay model;
- storage retention ≠ retained resolution/detail ≠ reporting relevance;
- lifecycle tiering, dependency pinning, legal/audit holds, safe aggregation, archive/restore and provenance-stub semantics;
- exact basis/communication/control evidence protected from lossy downsampling for its promised horizon;
- no indefinite detailed accumulation as a default merely because storage can grow.

## Group 03 accepted architecture discipline

Later groups must also preserve:

- canonical tenant-scoped Entity/Principal IDs distinct from vendor-local identities;
- source identity bindings as evidence-bearing, revisioned and conflict-capable;
- rename continuity distinct from delete/recreate/incarnation;
- human/group/service/workload identity and acting-on-behalf-of relationships kept distinct;
- historical membership based on historical evidence rather than current group state;
- Monitoring Scope as organization-owned expected coverage, not discoverability/access;
- scope selectors/materializations retaining unknown membership and bounded denominator semantics;
- Assertion Authority as structured target/context/time rules independent from evidence sufficiency and permission;
- explicit authority precedence/co-authority/fallback with no hidden rule ordering;
- vendor role/ownership/responsibility/permission as source evidence, not automatic DMTZ authority;
- Capability Authorization as principal/action/subject/context/time/detail specific;
- no universal deny-wins/allow-wins authorization precedence;
- actual authorization decision ≠ replay-derived authorization ≠ enforcement/action;
- service processing permission ≠ requester visibility;
- disclosure of conclusion/context/limitation/basis/provenance/detail/export independently authorized;
- exact/coarse/redacted/opaque/withheld projection with epistemic monotonicity;
- hidden basis existence/count/type/path/provenance treated as potentially sensitive;
- retained/archived/provenance-stub material not automatically disclosable;
- tenant/residency policy limiting identity/governance metadata and evidence movement;
- canonical policy state in Group 02 persistence with caches/indexes as derived projections.

## Group 04 accepted architecture discipline

Later groups must also preserve:

- source adapters bound to exact deployment-verified capability instances and revisioned surfaces/plans;
- reconciliation as the completeness/recovery foundation, with stream/webhook/incremental/export paths as source-specific accelerators;
- acquisition-run/attempt identity and durable request/page/partition/window provenance;
- source cursor/checkpoint state as source-bound operational state, never truth;
- checkpoint advancement only after corresponding evidence/provenance commit;
- overlap/redelivery/retries as idempotent and common-derived where they represent one source event;
- Monitoring Scope expected population independent from connector discoverability;
- pagination/partition/window completion explicit rather than inferred from HTTP success;
- request/response/source identifiers retained where permitted for troubleshooting/provenance;
- source envelope/raw representation distinct from normalized evidence;
- versioned parser/normalizer and non-rewriting reparsing semantics;
- additive schema evolution tolerated while breaking drift becomes explicit integration state;
- malformed/unsupported payloads quarantined rather than silently discarded when coverage can be affected;
- source publication lag distinct from event/effective time and collection/persistence lag;
- service-class-specific acquisition cadence rather than one polling interval;
- authentication, permission, observer-relative not-found, quota, source outage, reachability, lag, checkpoint, pagination, schema, parser, persistence, coverage and freshness as separable integration-health dimensions;
- no universal integration-health score;
- collection coverage manifests used before strong negative reasoning;
- source-native retention expiry distinct from product-retained evidence;
- optional-source absence as proposition-bound degradation, not benign default;
- acquisition cost/volume observable without weakening required evidence coverage.

## Group 05 accepted architecture discipline

Later groups must also preserve:

- stable source run/task/attempt identities rather than name/time joins;
- Git/CI/deployment/activation/run as separately evidenced transitions;
- DMTZ correlation token/attestation as join evidence, not truth/authority;
- direct-Git `used_commit` as strong code evidence only within its exact supported source/task scope;
- bundle/workspace-source exact revision requiring deployment/content/run attestation where promised;
- current workspace/job configuration never back-projected as run-specific state;
- run implementation as a composite manifest with independent code/config/parameter/runtime/library/environment/external-config facets;
- missing implementation facets remaining partial rather than inherited from current state;
- exact input consumption requiring source/runtime/query evidence or approved attestation;
- table history/latest state not becoming arbitrary exact read-version evidence;
- multi-input completeness explicit and current-cycle alignment separately proven;
- output existence/version requiring write/transaction/attestation evidence rather than run status/timestamp proximity;
- measurement identity bound to exact target, definition/profile revision, window/grain and source/acquisition context;
- run/output/version-specific health requiring explicit attribution;
- event-time freshness distinct from commit/publication/ingestion/processing/acquisition lag;
- Baseline/anomaly/typicality remaining distinct from Expectation and Assessment;
- reconciliation mismatch not becoming causality;
- typed historical Lineage with source/acquisition evidence and capture limitations;
- missing Lineage under incomplete capture not becoming `no dependency`;
- Lineage reachability not becoming consumption/encounter/exposure/effect/cause;
- statement/query IDs used for encounter joins only where source semantics support them;
- direct and indirect Lineage retained distinctly;
- consumer encounter/use context distinct from resource availability;
- cache/materialization/result-state provenance independent from current upstream state;
- exact exposure requiring actual encounter plus affected-version/state evidence;
- multi-hop exposure evaluated hop-by-hop and alternate paths considered for global negatives;
- exposure, effect, consequence and Causal Claim kept distinct;
- vendor downstream-impact/RCA labels retained as bounded vendor Assessments rather than DMTZ realized Impact/cause;
- external BI/application use and business/customer/financial consequence remaining explicit optional telemetry/source integrations;
- Group 04 acquisition coverage/integration health constraining all strong operational/Impact negatives;
- derived operational graph/index remaining rebuildable projection rather than canonical truth.

## Group 06 accepted architecture discipline

Later groups must also preserve:

- canonical Investigation identity and non-rewriting scope/lifecycle history independent from external tickets/model sessions;
- Investigation leads/annotations remaining workflow/commentary state rather than source or causal truth;
- lead exclusion requiring proposition-specific contradiction/exclusion evidence and adequate coverage;
- human/rule/graph/search/model lead origin retained as provenance without truth/authority promotion;
- reasoning graph/search/vector stores as derived/rebuildable projections over canonical evidence;
- semantically typed graph edges with exact source/derivation provenance;
- bounded graph traversal and no causal/Impact ranking from distance, centrality, path count or recency;
- Delta node/edge projection as the MVP graph realization, with dedicated graph technology only for measured scale/latency needs;
- exact structured retrieval by canonical identity/proposition/time/scope before semantic candidate retrieval;
- semantic/vector similarity as candidate recall only, never truth/authority/evidence/completeness;
- tenant/residency/authorization/disclosure filtering before sensitive retrieval/model exposure;
- versioned reasoning plans/runs with rule/code/source-watermark/knowledge-cut/authorization provenance;
- deterministic accepted evidence/status/negative-coverage/authority rules where the functional contracts define them;
- cross-concept derived statements requiring explicit versioned derivation rules and exact input proposition IDs;
- Causal Claim persistence/status as canonical proposition state rather than model output;
- `confirmed` Causal Claim remaining REF-017 + AUTH-034 gated;
- rejected cause requiring contradiction/exclusion evidence, not absence of support;
- localization and counterfactual analysis remaining separate from realized causal truth;
- availability-by-K historical replay with late evidence excluded from earlier cuts;
- corrections/supersessions changing retrospective interpretation without rewriting prior as-known state;
- canonical bitemporal journals rather than Delta time travel/current graph/current policy as the replay model;
- reconstructed Explanation distinct from authentic retained communication;
- Statement IR / Answer IR carrying exact proposition/status/basis/limitations before rendering;
- partial sibling answers without a global completeness/confidence score;
- deterministic template rendering available without any LLM;
- renderer epistemic equivalence and output validation against Statement IR;
- `inspectBasis` separately authorized itemwise from conclusion visibility;
- authentic Explanation snapshots bound to content, Statement IDs, limitations, audience/purpose/delivery and communication time where promised;
- Explanation/model trace retention driven by explicit product/audit/value horizons rather than indefinite accumulation;
- provider-neutral model gateway with Databricks model/AI services as conditional deployment realization;
- model/prompt/template/tool immutable invocation identity rather than mutable alias history;
- models restricted to assistance roles and bounded tools; free-form output never becomes domain fact;
- model/provider agreement remaining common-derived rather than corroboration;
- model/vector/trace/prompt-registry outages degrading convenience/observability rather than source truth or basic answerability.

## Architecture choices still intentionally open after Group 06

Groups 01–06 deliberately selected no final:

- universal event bus or queue technology;
- final workflow/orchestration/worker runtime;
- source-adapter SDK implementation language/framework;
- runtime-attestation SDK implementation language/framework;
- external IAM/IdP product;
- external policy-engine product or runtime packaging;
- policy authoring UI/API/Git workflow;
- dedicated graph database/product beyond the accepted Delta-projection MVP and optional measured later extension;
- final search/vector product or embedding model/provider;
- cache/materialized-serving technology;
- external BI/application telemetry vendor;
- incident/business consequence source product;
- credential/secrets implementation;
- final LLM/model/provider or agent framework;
- Gate/Safeguard implementation;
- UI/API/service topology;
- deployment topology;
- final observability stack;
- final backup/archive/lifecycle automation vendor;
- final cost-control implementation.

These choices must be justified by accepted contracts and deployment facts rather than selected by familiarity.

## Durable architecture rejection rules

Reject an architecture if it requires any of the following shortcuts:

- source availability treated as Assertion Authority;
- public vendor documentation treated as proof of tenant capability;
- retained/copied evidence treated as newly authoritative or independent;
- names or timestamp proximity used as exact entity/deployment/run/input/output joins;
- Git branch/tag/current workspace state treated as historical executed revision without exact evidence;
- successful CI/deployment status treated as target activation/run execution;
- deployment manifest treated as proof every later run executed unchanged content;
- current job/config/library/environment state projected backward as run-specific implementation state;
- latest/current input state used as exact consumed version;
- run success/failure used as output existence/non-existence proof;
- output write timestamp proximity used as exact run-version correlation;
- source discoverability or technical access treated as Monitoring Scope;
- unknown scope membership treated as exclusion;
- current membership/permission projected backward as historical authorization;
- service-principal access inherited by end users;
- authorization treated as enforcement/action occurrence;
- replay-derived authorization presented as an actual retained decision;
- retention/archive state treated as disclosure permission;
- redaction/generalization that strengthens, broadens or hides a material limitation;
- hidden basis counts/provenance leaked by convenience;
- checkpoint advancement before durable evidence persistence;
- webhook/stream silence treated as complete no-event evidence;
- partial pagination/partitions treated as complete coverage;
- 401/403/observer-relative 404/throttle/outage treated as domain absence;
- source publication lag ignored for current negatives;
- schema/parser failure silently dropping evidence;
- current integration recovery rewriting a prior evidence gap;
- measurement label/source availability treated as normative health authority;
- Baseline/anomaly/Expectation/Assessment flattened together;
- Lineage traversal treated as consumption, exposure, Impact, or causality;
- query/read activity automatically treated as human viewing or decision reliance;
- cached/materialized state assumed equal to current upstream state;
- multi-hop exposure propagated transitively;
- one safe path treated as global non-exposure;
- vendor downstream-impact/RCA or Criticality treated as realized Impact/cause;
- exposure treated as effect/consequence, or consequence treated as cause;
- missing external consumer/consequence telemetry converted into no impact;
- an LLM/agent/model treated as a source of domain truth or Assertion Authority;
- model confidence/probability treated as DMTZ evidence strength;
- agreement across model runs/providers treated as independent corroboration;
- graph distance/centrality/path count or semantic similarity treated as causal ranking;
- a graph/search/vector index treated as the only historical truth store;
- semantic retrieval allowed to bypass tenant/disclosure restrictions;
- free-form model output accepted directly as domain fact;
- current evidence/policy/source state projected backward into an as-known knowledge cut;
- reconstructed Explanation labeled as authentic retained communication;
- Statement-to-basis links lost during rendering or model transformation;
- summary/model prose that strengthens status, broadens scope or suppresses material limitations;
- `inspectBasis` permission inherited from conclusion visibility;
- model/vector availability made a prerequisite for truthful basic answers;
- indefinite retention of every reasoning/model trace merely because it was produced;
- current state projected backward as historical state;
- missing/degraded telemetry converted into negative truth;
- Delta transaction-log history used as the sole long-horizon product replay model;
- physical compaction/downsampling silently rewriting semantic history;
- retained old history automatically flooding routine reporting;
- age alone treated as irrelevance or deletion justification;
- control configuration/request treated as effective enforcement;
- loss of proposition/source/basis/acquisition/runtime/measurement/Lineage/reasoning provenance;
- one global confidence/health/Impact/control/replay/architecture/relevance/authorization/integration-health score;
- unsupported capabilities hidden behind planned future instrumentation.

## Phase 010 exit direction

Phase 010 should exit only when the architecture can demonstrate, through scenario replay and explicit traceability, that accepted semantics are technically realizable under deployment-verified environment/cost/latency/retention/security constraints and that all material residual gaps are resolved, reduced, intentionally scoped, or carried forward explicitly.

**Group 07 — Execution Gate, Propagation Safeguard & Active-Control Architecture is next.**