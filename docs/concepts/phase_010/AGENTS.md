# Phase 010 AGENTS.md — Technical Architecture Discipline

## Scope

This directory owns Phase 010 technical architecture. It may select concrete architecture only where the accepted Phase 002–009 contracts and verified environment facts justify the choice.

## Mandatory incoming authorities

Before accepting an `ARCH-###` contract, preserve and consult:

- Phase 003 SYN-001–SYN-035;
- Phase 004 REF-001–REF-030;
- Phase 005 AUTH-001–AUTH-053;
- Phase 006 HLTH-001–HLTH-066;
- Phase 007 OPS-001–OPS-123;
- Phase 008 EXPL-001–EXPL-160;
- Phase 009 INTG-001–INTG-270;
- Phase 009 Group 08 consolidated capability matrix;
- Phase 009 residual gap register GAP-009-01–GAP-009-40;
- Phase 009 `phase_010_handoff.md`;
- Phase 010 Group 01 ARCH-001–ARCH-032;
- Phase 010 Group 02 ARCH-033–ARCH-080;
- Phase 010 Group 03 ARCH-081–ARCH-132;
- Phase 010 Group 04 ARCH-133–ARCH-190;
- Phase 010 Group 05 ARCH-191–ARCH-274;
- Phase 010 Group 06 ARCH-275–ARCH-350;
- Phase 010 Group 07 ARCH-351–ARCH-420.

Earlier functional/integration semantics remain authoritative. Architecture may realize them; it may not simplify them away.

## Namespace

Use **ARCH-###** for durable technical architecture contracts.

An ARCH contract should state at least:

1. architecture proposition/decision;
2. accepted semantic requirements it realizes;
3. environment/source assumptions;
4. alternatives considered where material;
5. consequences/tradeoffs;
6. failure/degradation behavior;
7. historical/security/disclosure implications where applicable;
8. verification/acceptance evidence;
9. residual gaps or later-group dependencies.

Do not use ARCH contracts to redefine a product concept, source fact, authority rule, evidence threshold, health proposition, causal status, Impact layer, or Explanation semantic.

## Review sequence

Review Phase 010 in this order:

1. Architecture Frame, Environment Discovery & Decision Criteria — **accepted**;
2. Evidence, Provenance, Temporal & Persistence Architecture — **accepted**;
3. Identity, Scope, Authority, Authorization & Disclosure Architecture — **accepted**;
4. Source Acquisition, Adapter, Synchronization & Integration-Health Architecture — **accepted**;
5. Runtime Provenance, Health, Lineage & Impact Evidence Architecture — **accepted**;
6. Investigation, Reasoning, Historical Replay & Explanation Architecture — **accepted**;
7. Execution Gate, Propagation Safeguard & Active-Control Architecture — **accepted**;
8. Serving, Security, Deployment, Observability & Cost Architecture — **next**;
9. Architecture Consolidation, Validation & Phase 010 Exit.

This is a design dependency order, not a mandate for runtime service boundaries.

## Group 01 accepted discipline

ARCH-001–ARCH-032 and AFE01-01–AFE01-60 are accepted.

Later architecture work must preserve:

- `verified_public_vendor_fact` ≠ `target_environment_fact` ≠ organization requirement/policy ≠ architecture assumption ≠ unknown/unverified;
- documented vendor capability ≠ deployment presence ≠ enablement ≠ entitlement ≠ permission ≠ reachability ≠ observable coverage ≠ proposition-specific usability;
- capability identity bound to deployment model/cloud/region/Geo/account/workspace/edition/version/surface where material;
- capability facts as provenance-bearing, revisioned and time-aware;
- unknown deployment facts as unknown rather than guessed support/absence;
- proposition/service-class usability rather than one vendor-wide availability flag;
- optional Collibra/Immuta absence as bounded degradation rather than hidden hard dependency;
- explicit MVP/enterprise capability boundaries;
- architecture hard constraints before optimization;
- decision-specific tradeoffs with no universal architecture score;
- explicit reversibility and assumption/unknown register;
- SC-01 through SC-06 service classes;
- GAP-009-01–GAP-009-40 ownership/treatment.

A public vendor document can justify a public capability statement. It cannot alone justify an architecture assumption that a particular enterprise deployment exposes that capability.

## Group 02 accepted discipline

ARCH-033–ARCH-080 and EPT02-01–EPT02-72 are accepted.

Later architecture work must preserve:

- framework-owned Delta Lake canonical structured evidence/provenance journals;
- Unity Catalog managed tables/volumes as preferred conditional deployment realizations, not universal requirements;
- external Delta/governed object storage as valid portability realization;
- selective data-minimized payload capture rather than wholesale raw copying;
- durable framework evidence IDs independent of source-local IDs/physical paths;
- source authority/limitations after retention/copy;
- proposition/basis and common-derivation links;
- event/effective, availability/knowledge, collection/persistence, correction/supersession and communication time separation;
- late evidence excluded from earlier K;
- append/supersede/correct semantic history despite physical file optimization;
- parser/normalizer revision provenance;
- Delta transaction-log time travel not being the product replay contract;
- graph/search/vector/serving stores as derived/rebuildable;
- storage retention, retained detail/resolution and reporting relevance as separate dimensions;
- lifecycle states for recent, warm, summary-eligible, cold/pinned, provenance-stub and expired material;
- configurable reference retention rather than a universal TTL;
- dependency pinning/holds and exact-basis non-lossy retention;
- safe trend aggregation only when future exact-evidence promises permit it;
- archive/restore/purge provenance and cost observability;
- security/residency sharding without unauthorized duplication.

Do not solve performance/cost by silently making retained evidence less exact than the product promise or by allowing old retained history to flood every report.

## Group 03 accepted discipline

ARCH-081–ARCH-132 and IAD03-01–IAD03-84 are accepted.

Later architecture work must preserve:

- tenant-scoped canonical Entity and Principal identities distinct from vendor-local identities;
- source identity bindings as evidence-bearing, revisioned and conflict-capable;
- rename continuity distinct from delete/recreate/incarnation;
- human, group, service-principal, application/workload and acting-on-behalf-of relationships kept distinct;
- current group/role membership not projected backward as historical membership;
- upstream IdP provenance retained where known without making synchronized vendor state silently authoritative;
- organization-owned Monitoring Scope rather than inference from discoverability/access;
- scope selectors and materializations retaining revision, input coverage, explicit exclusions and unresolved membership;
- unknown scope membership not converted into exclusion or a smaller negative-claim denominator;
- Monitoring Scope independent from Capability Authorization;
- Assertion Authority as structured, versioned policy-as-data with exact facet/proposition/subject/context/time targets;
- authority precedence, co-authority and fallback as explicit rule data rather than hidden engine ordering;
- co-authoritative conflict retained until an authorized resolver applies;
- vendor role/title/ownership/responsibility/permission as source evidence, never automatic DMTZ Assertion Authority;
- causal confirmation authority eligibility distinct from REF-017 evidence sufficiency and AUTH-034 confirmation;
- Capability Authorization as exact principal/action/subject/context/time/detail state;
- granular action vocabulary rather than one generic `access` Boolean;
- `allowed`, `denied`, `conditional`, `unknown`, `conflicting` and `unavailable` preserved;
- membership/inheritance composition explicit and source/rule scoped;
- no universal deny-wins, allow-wins, direct-user-wins, role-wins or latest-wins authorization rule;
- actual authorization-decision record distinct from replay-derived historical evaluation;
- authorization distinct from request, enforcement, action occurrence and outcome;
- service-principal/internal processing authorization distinct from requester visibility;
- least-privilege workload identity as source-acquisition posture where supported;
- delegation/break-glass bounded, expiring/revocable and auditable;
- disclosure bound to requester/audience/purpose/delivery/onward-use context;
- conclusion, material context, limitation, basis identity, provenance, exact detail and export/publish independently authorizable;
- exact/coarse/redacted/opaque/withheld projections as detail states, not epistemic-strength states;
- safe abstraction epistemically monotone: no strengthening, scope broadening, subject merging or material-limitation erasure;
- `inspectBasis` itemwise while internal statement-to-basis traceability remains complete;
- hidden basis existence/count/type/source/path/timestamp/provenance/redaction metadata potentially sensitive;
- mosaic/differencing/repeated-query leakage considered by disclosure policy;
- retained/cold/archived/provenance-stub material not automatically disclosable;
- current authorization distinct from historical authorization and prior visibility;
- tenant/residency boundaries limiting governance metadata/evidence movement;
- canonical identity/policy state in Group 02 structured persistence with caches/indexes as derived/rebuildable projections.

Group 03 selects the canonical record/rule semantics but no external policy engine, IAM/IdP product, policy authoring UI/API/Git workflow, secrets implementation or runtime service topology.

## Group 04 accepted discipline

ARCH-133–ARCH-190 and AHI04-01–AHI04-96 are accepted.

Later architecture work must preserve:

- adapters as acquisition mechanisms, never independent owners of canonical identity/scope/authority/domain truth;
- exact capability-instance + source-surface + acquisition-plan revision binding;
- reconciliation-first hybrid collection, with incremental/stream/webhook/export/on-demand paths as source-specific accelerators;
- durable acquisition run/attempt identity;
- checkpoint/cursor/window/page/partition provenance tied to the exact query/surface;
- overlap for ambiguous ordering/late publication with idempotent deduplication;
- pagination/partition completion explicitly evidenced rather than inferred from successful HTTP response;
- expected population from Monitoring Scope/materialization, not whatever the connector can currently list;
- source request IDs and safe request/response provenance where available;
- source envelope/raw capture separated from normalized evidence and governed by minimization;
- normalized evidence bound to parser/normalizer revision and acquisition provenance;
- API/webhook/stream/export representations of one event marked common-derived rather than independent corroboration;
- additive schema evolution tolerated; breaking drift and unsupported fields explicit;
- malformed/unsupported payloads quarantined where their omission can affect coverage;
- partial collection allowed to preserve usable evidence without claiming complete coverage;
- evidence publication only after required provenance is durably persisted;
- checkpoint advancement only after corresponding evidence/provenance commit;
- retry behavior based on error taxonomy, idempotency and vendor guidance;
- authentication, permission and observer-relative not-found distinct from source/domain absence;
- 429/quota state, Retry-After/reset handling and bounded backoff;
- source-selective queries/partitioning/conditional requests used to conserve quota without hiding omitted coverage;
- source publication lag separated from event time and observed acquisition/persistence lag;
- acquisition scheduling bound to SC-01–SC-06 rather than one universal frequency;
- multidimensional integration health across presence/authn/authz/reachability/quota/publication/checkpoint/pagination/schema/parser/persistence/coverage/freshness/retention;
- no universal integration-health score;
- collection coverage manifest required for strong-negative support;
- source retention expiry distinguished from product-retained evidence;
- optional-source absence treated as proposition-bound degradation;
- acquisition request/query/compute/transfer volume and cost-relevant telemetry attributable where measurable;
- current integration recovery non-rewriting with respect to historical evidence gaps.

Group 04 selects no universal event bus, queue product, orchestration engine, worker runtime, secret store, observability vendor, API gateway or deployment topology.

## Group 05 accepted discipline

ARCH-191–ARCH-274 and RHI05-01–RHI05-108 are accepted.

Later architecture work must preserve:

- run/task/retry/repair/backfill identities as distinct source-backed executions;
- immutable Git commit identity separate from mutable branch/tag labels;
- Change Intent, GitHub CI, GitHub Deployment, target deployment, activation and Databricks run as separate evidence stages;
- cross-system correlation ID/attestation as join evidence, not truth or authority;
- direct-Git Databricks `used_commit` as run-specific code evidence only for qualifying task/source scope;
- bundle/workspace/Git-folder exact revision unresolved unless deployment/content/run attestation establishes it;
- deployment manifest distinct from actual run execution and realized target state;
- run-specific implementation manifest across code/config/parameters/runtime/compute/libraries/environment/external-config facets;
- missing implementation facets preserved as partial rather than filled from current state;
- secret/config references minimized and disclosure-governed;
- exact input consumption bound to run/task/query evidence or approved attestation;
- table history/current/latest state not used as generic exact input-version evidence;
- file/object version/generation/digest and streaming offset/range semantics source-specific;
- multi-input manifest completeness explicit with sibling unknowns preserved;
- current-cycle alignment as an explicit cycle/window proposition;
- output existence/version based on exact production/write/transaction/attestation evidence;
- run success/failure distinct from output existence/non-existence/health;
- every measurement bound to exact target, definition/profile revision, window/grain, source and acquisition context;
- measurement→run/output/version attribution explicit rather than temporal convenience;
- commit freshness, event-time freshness, publication, ingestion, processing and acquisition lag kept separate;
- completeness/volume/schema/compatibility/expectation/baseline/reconciliation observations not flattened;
- Baseline/anomaly typicality distinct from normative Expectation/Assessment;
- reconciliation discrepancy distinct from cause;
- health conflict retained and no universal asset-health rollup;
- health strong negatives requiring applicable check/population and acquisition coverage;
- Lineage edges typed, temporal, source-provenanced and coverage-limited;
- source-documented incomplete Lineage preserved as incomplete rather than absence;
- rename/incarnation identity semantics inherited from Group 03;
- stable statement/query IDs used for source-supported encounter joins only;
- direct/indirect Lineage preserved distinctly;
- Lineage reachability never becoming actual consumption/exposure/effect/cause;
- consumer encounter identity/use context independent from availability/publication;
- query execution independent from human viewing/decision reliance;
- cache/materialization/result state separately versioned from upstream current state;
- exact affected-version exposure requiring encounter + version/state binding;
- multi-hop exposure evaluated hop-by-hop rather than transitively;
- alternate-path coverage required for global non-exposure;
- exposure, technical effect, analytical/decision effect, business/customer/financial consequence and Causal Claim separate;
- vendor downstream-impact/RCA/Criticality retained only as bounded source Assessments;
- external BI/application use and business consequence sources optional/environment-specific;
- `not exposed`, `no effect`, `no consequence` requiring exact population/path/outcome and Group 04 coverage;
- late/backfilled evidence changing current retrospective state without rewriting earlier K;
- derived operational graph as rebuildable projection over canonical journals.

Group 05 selects canonical record/attestation interfaces but no graph product, runtime-attestation SDK language, tracing vendor, external BI telemetry vendor, incident/business system, event bus, serving topology or LLM stack.

## Group 06 accepted discipline

ARCH-275–ARCH-350 and IRE06-01–IRE06-120 are accepted.

Later architecture work must preserve:

- canonical Investigation identity independent from alerts/tickets/chats/model sessions;
- non-rewriting Investigation scope/lifecycle/reopen history;
- leads as inquiry state with human/rule/graph/search/model generation provenance but no automatic truth or authority;
- lead exclusion requiring proposition-specific contradiction/exclusion evidence and adequate coverage;
- annotations as commentary unless separately evidenced;
- reasoning graph/search/vector state as derived/rebuildable projection over canonical journals;
- semantically typed graph edges with exact canonical/derivation provenance;
- bounded graph traversal and graph distance/centrality/path count not becoming causal or Impact rank;
- Delta node/edge projection as the MVP graph realization, with specialized graph technology only for measured later needs;
- exact structured retrieval before semantic/vector candidate retrieval;
- semantic similarity as candidate recall only;
- tenant/residency/authorization/disclosure filtering before sensitive retrieval/model exposure where metadata itself can leak;
- versioned Reasoning Plan/Run identity with rules, source watermarks, knowledge cut and authorization context;
- deterministic versioned evidence/status/negative-coverage/authority evaluation where accepted contracts define it;
- explicit derivation rules for cross-concept statements; prose adjacency never a semantic join;
- canonical Causal Claim persistence using the accepted six-state vocabulary;
- `confirmed` remaining REF-017 + AUTH-034 gated and `rejected` requiring contradiction/exclusion evidence;
- localization/counterfactual analysis remaining distinct from realized causal truth;
- historical replay bound to event/effective window plus availability-by-K;
- late evidence excluded from earlier as-known cuts and corrections/supersessions non-rewriting;
- canonical bitemporal journals rather than Delta time travel/current graph/current policy as replay truth;
- expired/missing basis constraining replay rather than being reconstructed from provenance stubs;
- reconstructed historical Explanation distinct from authentic retained communication;
- Statement IR and Answer IR carrying exact proposition/status/basis/material limitations before rendering;
- sibling partial answers without global confidence/completeness scores;
- deterministic template rendering available without model service;
- model/UI/API/template renderers epistemically equivalent and validated against Statement IR;
- `inspectBasis` separately authorized itemwise, with reference visibility/resolvability/payload availability/permission distinct;
- authentic retained Explanation snapshots for promised communication replay;
- composition/approval/release/delivery/read/reliance evidence kept distinct;
- snapshot/basis/model-trace retention governed by explicit product/audit/value horizon rather than indefinite accumulation;
- provider-neutral model invocation, with Databricks AI/model facilities only conditional deployment realizations;
- immutable model/prompt/template/tool identity for each invocation;
- model roles limited to interpretation/lead/candidate/rendering assistance and bounded tools;
- free-form model output never becoming domain fact;
- model/provider agreement not becoming independent corroboration;
- semantic index/model/MLflow/Prompt Registry failure degrading convenience/observability rather than source truth or basic answerability.

Group 06 selects deterministic reasoning, Statement/Answer IR and the Delta graph-projection MVP, but no final LLM/provider, embedding model, agent framework, dedicated graph product, orchestration runtime, UI/API topology, secrets implementation or active-control technology.

## Group 07 accepted discipline

ARCH-351–ARCH-420 and ACS07-01–ACS07-120 are accepted.

Later architecture work must preserve:

- active control as opt-in and separable from passive monitoring/RCA;
- Gate and Safeguard independent state machines;
- deployment-verified control capability instances;
- immutable control/profile/criterion revisions and exact control-opportunity identities;
- criteria bound to exact accepted proposition/Assessment identities;
- evidence suitability, readiness, decision, issuance, delivery, acceptance, enforcement and execution kept separate;
- HOLD not becoming failed execution/non-execution by wording; ADMIT not becoming run occurrence;
- override authorization/decision/expiry explicit while preserving underlying readiness;
- fallback policy, trigger, decision and enforcement explicit; timeout/escalation separate;
- multi-Gate composition/precedence explicit with no hidden implementation-order rule;
- concurrency/idempotency/stale-decision handling bound to opportunity/decision identity;
- control decisions bound to actual knowledge cut and basis manifest;
- GitHub environment protection treated as pre-start only for the exact protected GitHub job/deployment opportunity;
- GitHub custom protection rule use conditional on target plan/deployment capability;
- GitHub Gate → Databricks execution requiring Group 05 durable correlation;
- Databricks external trigger broker requiring governance of alternate/bypass trigger paths;
- Databricks `If/else`/`Run if` becoming DMTZ Gate only through explicit criterion/opportunity mapping;
- Databricks cancellation represented as asynchronous post-start interruption, not pre-start HOLD;
- degraded control dependencies following explicit Gate/Safeguard policy rather than implicit fail-open/fail-closed;
- model/search/graph recommendations never becoming control decisions;
- Safeguard profiles binding exact protected state/version, surface/path/cohort and interval;
- Safeguard proposal, authorization, request, attempt and effective enforcement distinct;
- partial enforcement remaining path/cohort specific;
- alternate-path inventory and actual exposure opportunity required for broad prevention evaluation;
- no opportunity → no prevention credit;
- `not exposed` distinct from `prevented by Safeguard`;
- REF-028 prevention conclusion-specific and not a universal control-effectiveness score;
- safe stale serving distinct from freshness/currentness/health;
- configured expiry, effective expiry, release request, effective release and recovery separate;
- overlapping controls retaining independent evidence and no hidden causal credit;
- broader control-effect attribution remaining Causal Claim work beyond narrow REF-028 prevention;
- actual historical control decision/enforcement distinct from replay reconstruction/current retrospective/counterfactual preferred action;
- control/audit retention following explicit product/audit/value horizons rather than indefinite trace accumulation.

Group 07 selects canonical Gate/Safeguard state/evidence architecture and bounded GitHub/Databricks adapter patterns, but no final control runtime, external policy engine, queue/event bus, workflow engine, secrets product, serving topology, deployment topology or observability vendor.

## Group 08 discipline

Group 08 must package serving, security, deployment, observability and cost over ARCH-001–ARCH-420.

It must not:

- collapse canonical evidence with caches/search/serving projections;
- make UI/API convenience determine truth or disclosure scope;
- merge internal service authorization with requester authorization;
- hide connector/reasoning/control-path degradation behind one health score;
- place an LLM/model in the mandatory truth or active-control path when deterministic evidence/rules suffice;
- relax evidence, negative-coverage, retention, disclosure or control decision TTL requirements for latency/cost;
- make active-control availability a prerequisite for passive monitoring;
- treat a control-service HTTP success as effective external enforcement;
- treat deployment topology boundaries as permission to merge Gate and Safeguard semantics.

## Cross-group invariants

Preserve all accepted durable boundaries, especially:

- source availability ≠ Assertion Authority;
- Entity Identity ≠ source-local name equality;
- Monitoring Scope ≠ accessibility ≠ authorization;
- current state ≠ historical state;
- copied/retained evidence ≠ independent/newly authoritative evidence;
- missing/degraded integration telemetry ≠ source/domain negative truth;
- checkpoint progress ≠ source completeness/domain truth;
- HTTP/request success ≠ page/population/window completeness;
- webhook/stream silence ≠ no event;
- integration recovery ≠ historical gap erasure;
- Git/CI/deployment status ≠ target activation ≠ execution;
- run success ≠ output existence ≠ output health/currentness;
- active deployment/current config ≠ run-specific implementation state;
- current/latest input ≠ exact consumed input;
- Lineage read/dependency ≠ exact consumed version;
- measurement availability/vendor health label ≠ normative authority;
- storage retention ≠ reporting relevance;
- retained/archived evidence ≠ disclosure permission;
- payload expired ≠ source absent;
- graph/search/cache projection ≠ canonical truth;
- semantic similarity/model output ≠ source truth/evidence strength/causal status;
- current authorization ≠ historical authorization;
- actual authorization decision ≠ replay-derived authorization ≠ enforcement/action;
- service processing authorization ≠ requester visibility;
- Assertion Authority ≠ evidence sufficiency ≠ Capability Authorization;
- Baseline ≠ Expectation ≠ Observation ≠ Assessment;
- Lineage ≠ encounter ≠ exposure ≠ effect ≠ consequence ≠ causality;
- query execution ≠ human view ≠ decision reliance;
- Investigation/localization ≠ Causal Claim truth;
- historical as-known reconstruction ≠ retained authentic communication ≠ current retrospective interpretation;
- Statement IR ≠ prose wording;
- conclusion visibility ≠ inspectBasis permission;
- readiness ≠ Gate decision ≠ delivery ≠ enforcement ≠ execution;
- HOLD ≠ failed execution; ADMIT ≠ execution occurrence;
- override/fallback admission ≠ prerequisite readiness;
- Execution Gate ≠ Propagation Safeguard;
- Safeguard proposal/authorization/request ≠ enforcement;
- Safeguard enforcement ≠ REF-028 prevention;
- `not exposed` ≠ `prevented by Safeguard`;
- release/expiry ≠ health/currentness/recovery;
- internal basis traceability ≠ universal visible raw evidence;
- cost/quota optimization ≠ relaxed evidence burden;
- optional source/instrumentation/model/index/control absence ≠ benign default;
- architecture convenience ≠ semantic permission.

## Environment facts

Documented vendor defaults are architecture inputs, not tenant facts. Every later group must distinguish:

- verified public capability/default;
- target-environment discovered fact;
- organization policy/requirement;
- architecture assumption;
- unresolved unknown.

Do not silently promote a public default into a production tenant contract.

When capability is material, bind exact deployment model/cloud/region/Geo/account/workspace/tenant/edition/plan/version/license/release/enablement/permission/reachability/coverage/health dimensions as applicable.

## Decision quality

Prefer architecture decisions that are:

- traceable to accepted contracts/gaps;
- reversible where uncertainty remains high;
- explicit about capability loss and graceful degradation;
- observable in operation;
- secure by least privilege and disclosure-aware design;
- cost/quota aware without weakening truth/evidence semantics;
- testable through scenario replay;
- modular enough that optional integrations/derived stores do not become hidden canonical dependencies.

Material decisions must follow the accepted ADR rubric rather than relying on familiarity.

## Documentation discipline

- Keep Phase 010 architecture documentation under `docs/concepts/phase_010/` unless another repository authority explicitly owns the artifact.
- Preserve source references and architecture rationale.
- Prefer additive decisions/supersession over silent historical rewrite.
- Update canonical repository phase status only through `docs/README.md`; keep `docs/phase_status.md` synchronized.
- Do not claim `scripts/check_docs_consistency.py` ran unless it actually ran.
- Group exit reviews must state accepted ARCH range, scenario/validation results, unresolved architecture risks, and next-group entry conditions.

## Current state

**Phase 010 is IN PROGRESS. Groups 01–07 are accepted: ARCH-001–ARCH-420; AFE01-01–AFE01-60, EPT02-01–EPT02-72, IAD03-01–IAD03-84, AHI04-01–AHI04-96, RHI05-01–RHI05-108, IRE06-01–IRE06-120 and ACS07-01–ACS07-120 pass. Group 08 — Serving, Security, Deployment, Observability & Cost Architecture is next.**