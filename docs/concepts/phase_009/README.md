# Phase 009 — Integration Contracts, Source Authority, and Evidence Availability

**Status:** IN PROGRESS — Groups 01–07 accepted; INTG-001–INTG-238 accepted; IC01-01–IC01-40, GOV02-01–GOV02-48, RTE03-01–RTE03-54, HME04-01–HME04-56, LIE05-01–LIE05-60, ICE06-01–ICE06-72 and EBR07-01–EBR07-64 pass; Group 08 next

## Goal

Map the accepted functional requirements from Phases 002–008 to concrete evidence/source capabilities without weakening those requirements to match whichever integration happens to be easiest to query.

Phase 009 must determine, proposition by proposition:

- which source surface can provide relevant evidence;
- what that source is authoritative, assertive, observational, contextual, or merely available for;
- how source identities join to accepted Entity Identity and other bounded subjects;
- which event/effective and recorded/knowledge timestamps exist and what they mean;
- what positive and negative conclusions the source can actually support;
- what population/path/opportunity coverage is observable;
- latency, retention, correction/backfill, mutability and historical replay limits;
- authorization, disclosure and basis-inspection constraints;
- rate, quota, cost and operational-observability characteristics;
- where requirements are only partially supported, unsupported, unknown, or require another source.

An integration gap is a product/integration finding. It is **not** permission to rewrite `unknown` as `no`, availability as authority, reachability as exposure, execution success as output/currentness/health, or control configuration as enforcement.

## Refinement namespace

Phase 009 uses **`INTG-###`** integration-contract refinements.

`INTG-###` describes the functional contract between accepted product semantics and actual source capabilities. It does not define adapter classes, service boundaries, event schemas, storage tables, polling architecture, credentials, SDK selection, or deployment topology.

Accepted range so far: **INTG-001–INTG-238**.

## Logical delivery grouping

Phase 009 is reviewed in eight dependency-ordered groups. The groups are organized around **evidence responsibilities and reasoning dependencies**, not vendor ownership.

### Group 01 — Integration Contract Vocabulary, Source Roles & Capability Matrix
**Status:** **Accepted — INTG-001–INTG-022; IC01-01–IC01-40 pass.**

Defines exact source-surface identity/version context; proposition binding; evidence roles; authority/relevance/sufficiency/authorization separation; identity and association joins; temporal coordinates; grain/context; positive and negative evidence; coverage; availability/latency; retention/replay; correction/backfill/mutation; duplicate/common derivation; conflict/fallback; support-gap taxonomy; quota/cost; and integration observability.

No new concept is required. Integration support remains proposition/source-set/context bound rather than a vendor-wide score.

See [`01_integration_contract_vocabulary_source_roles_capability_matrix/README.md`](01_integration_contract_vocabulary_source_roles_capability_matrix/README.md).

### Group 02 — Identity, Scope, Semantics, Governance, Authority & Authorization Sources
**Status:** **Accepted — INTG-023–INTG-050; GOV02-01–GOV02-48 pass.**

Applies INTG-001–INTG-022 to Entity Identity, Monitoring Scope, Semantic Definition, Responsibility Assignment, Classification, Policy Context, Assertion Authority and Capability Authorization across Unity Catalog/Databricks, Collibra, Immuta, GitHub/repository governance and upstream IAM projections.

It preserves source-local identity versus ecosystem identity; facet/type/scheme-specific governance authority; current versus historical governance; observer-relative metadata; optional-source degradation; and composed authorization across multiple enforcement planes.

Accepted gaps include no out-of-box Monitoring Scope registry, no automatic Assertion Authority registry, explicit cross-system Entity Identity crosswalk requirements, retention/configuration limits for long-horizon replay, environment-specific upstream IAM, and population-specific Immuta + Unity Catalog authorization composition.

See [`02_identity_scope_governance_authority_authorization_sources/README.md`](02_identity_scope_governance_authority_authorization_sources/README.md), [`02_identity_scope_governance_authority_authorization_sources/source_capability_matrix.md`](02_identity_scope_governance_authority_authorization_sources/source_capability_matrix.md), and [`02_identity_scope_governance_authority_authorization_sources/external_source_review.md`](02_identity_scope_governance_authority_authorization_sources/external_source_review.md).

### Group 03 — Change Intent, Deployment, Execution, Version & Runtime Evidence
**Status:** **Accepted — INTG-051–INTG-083; RTE03-01–RTE03-54 pass.**

Applies the accepted source contract to Git/GitHub revision/change records, GitHub Actions workflow/attempt/deployment evidence, Databricks job/task/pipeline configuration and runtime history, bundle/direct-Git provenance, retries/repairs, actual sequence and Delta/input/output version evidence.

It establishes strong local evidence for Git revisions, workflow/run identity, Databricks execution lifecycle and direct remote-Git `used_commit`; explicit correlation requirements for CI→Databricks joins; an out-of-box run-commit gap for bundle/workspace-source execution; conditional per-output Delta version binding; and an explicit unsupported-out-of-box generic multi-input version-consumption gap.

See [`03_change_deployment_execution_version_runtime_evidence/README.md`](03_change_deployment_execution_version_runtime_evidence/README.md), [`03_change_deployment_execution_version_runtime_evidence/source_capability_matrix.md`](03_change_deployment_execution_version_runtime_evidence/source_capability_matrix.md), and [`03_change_deployment_execution_version_runtime_evidence/external_source_review.md`](03_change_deployment_execution_version_runtime_evidence/external_source_review.md).

### Group 04 — Health, Schema, Metrics, Expectations, Baselines & Reconciliation Evidence
**Status:** **Accepted — INTG-084–INTG-119; HME04-01–HME04-56 pass.**

Maps Unity Catalog/table structural evidence, DQX, Lakeflow expectations/event logs, Metric Views, data profiling, anomaly-detection/data-quality monitoring, Baseline/reference evidence, reconciliation, freshness/current-cycle and result-timing surfaces to the accepted Phase 006 health model.

It preserves realized schema ≠ consumer compatibility; constraint declaration ≠ empirical integrity; rule/check availability ≠ governed Expectation; metric/profile/drift availability ≠ Baseline/health authority; vendor anomaly/table-health/root-cause/impact labels ≠ DMTZ composite-health/Causal Claim/Impact truth; and exact current-cycle health as conditional where Group 03 input-version evidence is absent.

Accepted gaps include consumer-specific compatibility contracts, explicit DQX/metric-definition versioning and authority, event-time freshness evidence, exact measurement→run/output binding where current/latest state is insufficient, generic multi-input current-cycle instrumentation, and source-specific historical replay/negative-evidence coverage.

See [`04_health_schema_metrics_expectations_baselines_reconciliation_evidence/README.md`](04_health_schema_metrics_expectations_baselines_reconciliation_evidence/README.md), [`04_health_schema_metrics_expectations_baselines_reconciliation_evidence/source_capability_matrix.md`](04_health_schema_metrics_expectations_baselines_reconciliation_evidence/source_capability_matrix.md), and [`04_health_schema_metrics_expectations_baselines_reconciliation_evidence/external_source_review.md`](04_health_schema_metrics_expectations_baselines_reconciliation_evidence/external_source_review.md).

### Group 05 — Lineage, Consumer Use, Exposure, Effect & Impact Evidence
**Status:** **Accepted — INTG-120–INTG-153; LIE05-01–LIE05-60 pass.**

Maps Unity Catalog table/column lineage, SQL/query-history reads, dashboard/audit/query-result activity, caching, refresh/snapshot delivery, external-client context and bounded effect/consequence evidence to the accepted Lineage/Impact ladder.

It preserves captured lineage event ≠ permanent relationship; topology ≠ actual encounter; dashboard access ≠ dataset execution/result receipt; cached-state encounter ≠ fresh source read; platform query ≠ external report view/business reliance; object read ≠ exact affected-version exposure; and exposure ≠ downstream effect ≠ consequence ≠ causal attribution.

Accepted gaps include incomplete lineage capture, rename/path identity reconciliation, generic exact table-version consumption, exact dashboard-cache state, external BI/application view/use telemetry, business consequence evidence, heterogeneous historical retention and coverage-intensive non-exposure/no-effect/no-consequence negatives.

See [`05_lineage_consumer_use_exposure_impact_evidence/README.md`](05_lineage_consumer_use_exposure_impact_evidence/README.md), [`05_lineage_consumer_use_exposure_impact_evidence/source_capability_matrix.md`](05_lineage_consumer_use_exposure_impact_evidence/source_capability_matrix.md), and [`05_lineage_consumer_use_exposure_impact_evidence/external_source_review.md`](05_lineage_consumer_use_exposure_impact_evidence/external_source_review.md).

### Group 06 — Investigation, Causality, Safeguard, Gate & Control Evidence
**Status:** **Accepted — INTG-154–INTG-200; ICE06-01–ICE06-72 pass.**

Maps Databricks audit/runtime/control-flow evidence, GitHub environment/deployment protection, Immuta policy/query audit and environment-specific review/control sources to Investigation localization, Causal Claim evaluation, Propagation Safeguard enforcement/prevention and Execution Gate decision/enforcement semantics.

It preserves trigger/lead/localization ≠ cause; vendor/human/model assertion ≠ confirmed Causal Claim; policy/config/request ≠ effective enforcement; Safeguard enforcement ≠ REF-028 prevention; no-opportunity ≠ prevention credit; GitHub environment Gate ≠ uncorrelated Databricks Gate; Databricks cancellation ≠ pre-start HOLD; task condition ≠ DMTZ readiness/Gate without explicit mapping; HOLD/ADMIT ≠ execution outcome; and missing control telemetry ≠ fail-open/fail-closed.

Accepted gaps include no automatic causal-confirmation source, environment-specific Investigation/Annotation/authority records, path-specific Safeguard realization, Immuta registration/audit limits, cross-system GitHub→Databricks Gate correlation, explicit criterion/override/fallback/multi-Gate contracts and heterogeneous control-history retention.

See [`06_investigation_causality_safeguard_gate_control_evidence/README.md`](06_investigation_causality_safeguard_gate_control_evidence/README.md), [`06_investigation_causality_safeguard_gate_control_evidence/source_capability_matrix.md`](06_investigation_causality_safeguard_gate_control_evidence/source_capability_matrix.md), and [`06_investigation_causality_safeguard_gate_control_evidence/external_source_review.md`](06_investigation_causality_safeguard_gate_control_evidence/external_source_review.md).

### Group 07 — Explanation, Historical Replay, Basis Inspection & Disclosure Source Contracts
**Status:** **Accepted — INTG-201–INTG-238; EBR07-01–EBR07-64 pass.**

Maps Databricks/GitHub/Collibra/Immuta and accumulated Phase 009 source history to Phase 008 statement-to-basis traceability, as-known-at-cut replay, retained communication, current retrospective Explanation, `inspectBasis`, safe abstraction and current disclosure authorization.

It preserves source history ≠ as-known-at-cut Explanation ≠ actual retained communication ≠ current retrospective Explanation; event time ≠ availability by knowledge cut; notification delivery ≠ exact communication content; visible citation ≠ source access/disclosure permission; current requester authorization ≠ historical actor authorization; and more visible basis ≠ stronger truth.

Accepted gaps include heterogeneous/short vendor retention, incomplete availability-by-K evidence, no universal native retained-Explanation store, Databricks query-content blanking/truncation, mutable GitHub discussion history, configurable Collibra history, short Immuta SaaS audit retention, incomplete historical-authorization replay, sensitive basis metadata and exact prior `inspectBasis` presentation requiring independent retention.

See [`07_explanation_historical_replay_basis_disclosure_source_contracts/README.md`](07_explanation_historical_replay_basis_disclosure_source_contracts/README.md), [`07_explanation_historical_replay_basis_disclosure_source_contracts/source_capability_matrix.md`](07_explanation_historical_replay_basis_disclosure_source_contracts/source_capability_matrix.md), and [`07_explanation_historical_replay_basis_disclosure_source_contracts/external_source_review.md`](07_explanation_historical_replay_basis_disclosure_source_contracts/external_source_review.md).

### Group 08 — Cross-Source Coverage, Latency, Retention, Cost & Phase Consolidation / Exit
**Status:** **Next — not started.**

Compose the source contracts across all prior groups. Identify evidence gaps, conflicting/overlapping source roles, cross-source join risks, clock/time-cut limitations, coverage boundaries, latency/freshness envelopes, retention/replay/communication-retention feasibility, quotas/cost, integration observability and graceful degradation.

The exit review must state which accepted product requirements are fully supportable, partially supportable, unsupported or still unknown with the evaluated integrations, without weakening source semantics. It must separately distinguish source reconstruction, as-known replay, authentic retained communication and current basis-disclosure support before handing concrete facts to Phase 010 technical architecture.

See [`08_cross_source_coverage_latency_retention_cost_consolidation_exit/README.md`](08_cross_source_coverage_latency_retention_cost_consolidation_exit/README.md).

## Accepted Group 01 integration-contract discipline

Every later source review uses the common matrix:

**source-surface identity/version → bounded proposition → evidence role → authority applicability → subject/join contract → temporal coordinates → grain/context → positive capability → negative/opportunity/coverage capability → availability/latency → retention/replay → mutation/correction → disclosure → derivation/independence → quota/cost → integration observability → support classification + residual gaps**.

Preserve:

- product/vendor name ≠ exact source surface;
- source availability ≠ relevance ≠ authority ≠ sufficiency ≠ authorization;
- source role ≠ standing;
- source-local identifier/name ≠ Entity Identity;
- timestamp proximity ≠ exact cross-system association;
- event/effective time ≠ recorded/knowledge/availability/retrieval time;
- aggregate/asset grain ≠ narrower proposition grain;
- positive-event support ≠ negative-evidence capability;
- no returned record ≠ absence without opportunity + sufficient coverage + source health;
- coverage for one mode/path/cohort ≠ global completeness;
- current-state availability ≠ historical replay capability;
- backfill/correction now ≠ knowledge available then;
- destructive mutation can make historical requirements unsupported;
- multiple endpoints ≠ independent corroboration when commonly derived;
- fallback availability ≠ inherited authority;
- source conflict ≠ hidden winner;
- quota/cost may constrain feasible coverage but cannot rewrite truth;
- integration failure ≠ monitored-product negative;
- `supported`, `partially supported`, `unsupported`, `unknown/not yet verified`, and `not applicable` are feasibility outcomes, not truth/confidence states;
- no vendor-wide support/completeness score is accepted.

## Accepted Group 02 source-contract discipline

Every later group must preserve:

- Unity Catalog object/principal identity ≠ ecosystem Entity Identity without cross-system mapping;
- Collibra UUID ≠ Unity Catalog/GitHub/Immuta identity without a governed crosswalk;
- GitHub repository/path identity ≠ data identity;
- external-IAM synchronization is a projection whose upstream source remains material;
- Collibra operating-model scope ≠ framework Monitoring Scope;
- semantic authority is facet-specific, responsibility authority is responsibility-type specific, and Classification authority is scheme/context specific;
- Unity Catalog comments, ownership, governed tags, Collibra responsibilities/tags/data classes, Immuta tags/policies and GitHub CODEOWNERS/rulesets retain their documented narrow meanings;
- no evaluated platform role automatically implements full Assertion Authority;
- Unity Catalog Information Schema is principal-filtered and does not provide universal absence evidence;
- current governance/permission state ≠ historical state;
- Databricks, Collibra, Immuta and GitHub history is retention/configuration bounded;
- effective Immuta + Unity Catalog authorization can be a composed, user-population-specific proposition;
- optional Collibra/Immuta absence creates explicit gaps rather than benign defaults;
- Group 02 source/governance mapping does not prove repository revision → deployment → run → version association.

## Accepted Group 03 runtime-source discipline

Every later group must preserve:

- Git commit SHA ≠ governed Change Intent unless an explicit Change Intent rule binds the change record;
- event-triggering SHA ≠ workflow-definition SHA;
- workflow run ≠ workflow attempt;
- GitHub Actions success ≠ Databricks activation;
- GitHub Deployment request/status ≠ target activation by default;
- CI→Databricks association requires explicit correlation/attestation evidence;
- current/active Databricks job config ≠ run-specific implementation state;
- direct remote-Git `git_snapshot.used_commit` can bind the code revision of the exact run when present;
- bundle/workspace-source run revision remains unsupported/conditional without immutable attestation;
- code commit ≠ entire composite implementation state;
- configured dependency ≠ actual precedence ≠ waiting ≠ consumption;
- retry ≠ repair ≠ rerun ≠ backfill;
- execution success ≠ output existence/version/currentness/health;
- Delta output-version association is per-output and conditional on explicit correlation;
- Delta `readVersion` ≠ a generic upstream input-version manifest;
- generic exact multi-input version consumption is unsupported out of the box and requires explicit evidence where needed;
- recent Jobs API detail ≠ longer Lakeflow system-table replay capability;
- no-run/no-output/no-consumption remain opportunity/coverage/source-health bound.

## Accepted Group 04 health-source discipline

Every later group must preserve:

- current Unity Catalog schema metadata ≠ historical structure ≠ consumer-specific compatibility;
- principal-filtered schema metadata cannot support absence by non-return;
- declared PK/FK/key metadata ≠ empirical integrity unless independently observed/enforced for the exact proposition;
- DQX rule/check availability or generated origin ≠ governed Expectation authority;
- DQX criticality/action ≠ framework severity, waiver, Gate or control semantics;
- Lakeflow expectation definition/action ≠ normative result, and fail-update flows can have incomplete tracking metrics;
- Metric View YAML specification version ≠ organization metric-definition revision;
- Metric View availability/materialization ≠ profile membership, Expectation or freshness SLA;
- profiling metrics/drift ≠ Baseline membership ≠ normative violation;
- anomaly-detection learned freshness/completeness ≠ explicit SLA/Expectation by default;
- Databricks table-level `Healthy`/`Unhealthy` ≠ DMTZ universal/composite health without an explicit HLTH-055 profile mapping;
- vendor `root_cause_analysis` ≠ Causal Claim confirmation and vendor downstream-impact labels ≠ realized Impact;
- commit freshness ≠ event-time/ingestion-latency freshness;
- Baseline membership/regime/version remains explicit even when vendor historical models/baseline tables exist;
- measurement grain/window/slice/cohort remains proposition identity;
- run-specific health needs exact measurement→run/output binding rather than latest/current-state inference;
- reconciliation binds exact transformation/version/population/key/measure semantics rather than metric adjacency;
- exact multi-input current-cycle alignment inherits Group 03 input-version gaps;
- measurement/scan/refresh/availability/retrieval clocks remain distinct;
- historical health replay requires retained definitions plus results/source context;
- skipped/disabled/failed evaluation ≠ clean result;
- same-proposition health conflicts have no universal vendor precedence, while different health propositions may coexist.

## Accepted Group 05 lineage/consumer/Impact-source discipline

Every later group must preserve:

- captured lineage event ≠ permanent/effective relationship interval;
- lineage capture is incomplete and missing lineage cannot support global no-dependency/no-use conclusions;
- source-local lineage entity/path/name ≠ reconciled ecosystem consumer/table identity;
- `direct_access` ≠ relevance/exposure/causal strength;
- topology/availability/publication ≠ actual encounter;
- query execution ≠ source read unless the source association is established;
- lineage `statement_id` ↔ query history is strong association evidence where present;
- client application/query source ≠ external report view/business user identity;
- query-result-cache encounter ≠ fresh source read;
- dashboard access ≠ dataset query execution ≠ result receipt;
- dashboard cache can represent safe, affected or unresolved prior state and can be served without a new warehouse query;
- schedule configuration ≠ refresh execution; refresh execution ≠ human view;
- snapshot/subscription delivery ≠ reading/reliance;
- external BI/application platform read ≠ external report/application display/use;
- generic object-level read ≠ exact table/data-version consumption;
- exact suspect-state exposure requires state/version binding where the proposition is version-specific;
- query time/proximity ≠ consumed version;
- cache/copy/export/snapshot state can persist after source correction;
- multi-hop exposure is non-transitive;
- one safe path ≠ global non-exposure;
- exposure ≠ downstream effect ≠ consequence ≠ Causal Claim;
- dashboard/report view/delivery ≠ decision reliance;
- popularity/vendor downstream-impact context ≠ realized Impact/severity;
- historical Impact replay and strong non-exposure/no-effect/no-consequence remain source-set/coverage bound.

## Accepted Group 06 investigation/causal/control-source discipline

Every later group must preserve:

- Investigation trigger/lead/localization ≠ Causal Claim truth;
- first observed ≠ earliest evidenced change ≠ first reconciliation boundary ≠ first consumer effect ≠ root cause;
- lead exclusion requires proposition-specific negative/discriminating coverage;
- human review, GitHub issue/comment, vendor RCA or model output ≠ causal authority by origin;
- Causal Claim proposition identity binds cause/effect/role/scope/mechanism/time before evaluation;
- no evaluated vendor automatically owns `confirmed`; REF-017 + AUTH-034 remain mandatory;
- remediation/rollback/rerun contrast can support a claim without automatically confirming it;
- Databricks audit request/response ≠ asynchronous effective enforcement by default;
- current UC privilege/policy state ≠ historical enforcement;
- Immuta policy configuration ≠ query-time policy application;
- Immuta applied-policy/denial evidence is strong only for covered registered/instrumented scope;
- Safeguard proposal/authorization/request ≠ enforcement;
- Safeguard enforcement ≠ REF-028 prevented exposure;
- no encounter opportunity ≠ prevention credit;
- one denied/protected path ≠ global protection;
- Safeguard release/regrant ≠ health/currentness/recovery;
- Databricks Jobs cancel is asynchronous post-start interruption, not pre-start HOLD;
- no universal native output quarantine/hold capability is assumed;
- GitHub environment protection is a strong pre-start Gate only for the exact Actions job/deployment opportunity it protects;
- GitHub reviewer approval/rejection/bypass/wait/custom-rule results retain distinct source semantics;
- GitHub Gate ≠ Databricks Gate absent explicit Group 03 correlation;
- Databricks `Run if`/`If/else` becomes a DMTZ Gate only under explicit criterion/opportunity mapping;
- criterion identity/evidence suitability/readiness/decision/delivery/acceptance/enforcement/execution remain distinct;
- start during unsuperseded HOLD contradicts full HOLD enforcement;
- no start alone ≠ successful HOLD;
- ADMIT ≠ execution;
- override/fallback/timeout/escalation retain separate semantics;
- multiple Gates/Safeguards have no hidden universal precedence;
- missing/conflicting control telemetry ≠ fail-open/fail-closed/success/failure;
- broader control-effect attribution remains Causal Claim work except the bounded REF-028 prevention determination.

## Accepted Group 07 Explanation/replay/basis-source discipline

Every later group must preserve:

- material statement identity retains exact source proposition/basis identity independently of rendered wording;
- source-local names/URLs/display labels are not stable historical identity where rename/recreate/mutation matters;
- event/effective time, source availability/recorded time, knowledge cut, retrieval time and communication time remain distinct;
- event-before-K ≠ known-by-K;
- late evidence/corrections do not enter an earlier knowledge cut;
- source correction may change current retrospective Explanation without invalidating historically correct unknown/partial states;
- current source state/latest surviving record ≠ complete historical source state;
- retention expiry, deletion, truncation, CMK blanking or disabled history remain explicit limitations;
- historical source state ≠ as-known-at-cut Explanation ≠ actual retained communication ≠ current retrospective Explanation;
- delivery status ≠ exact retained message content ≠ reading/reliance;
- reconstruction ≠ authentic prior communication even when wording would match;
- missing retained communication remains missing;
- statement identity can persist across refresh only while proposition-defining scope/time is materially stable;
- basis enrichment ≠ confidence/status strengthening;
- source outages/lag/permission failures are basis-availability limitations rather than domain negatives;
- partial answerability remains proposition/subquestion bound;
- internal basis inspectability remains mandatory even where requester-visible basis is restricted;
- visible reference/citation ≠ source accessibility ≠ basis-disclosure permission;
- current requester authorization governs present disclosure of historical basis;
- historical actor authorization and current disclosure are independent;
- conclusion/context/limitation/basis/provenance/detail may have separate disclosure rules;
- safe abstraction/redaction remains epistemically monotone;
- basis existence/count/type/source class/timestamps/redaction markers may themselves be sensitive;
- query text/parameters/errors and actor/consumer identities are sensitive basis facets;
- filtered/permission-scoped history is observer-relative and cannot support absence by non-return;
- Databricks `system` tables have heterogeneous retention and no universal indefinite replay promise;
- Databricks query text/error/parameter inspectability is conditional on encryption/truncation behavior;
- Databricks alert evaluation/delivery history does not retain exact Explanation content by implication;
- GitHub audit history is retention-bound and streamed duplicates are not independent evidence;
- GitHub comment edit history is mutable/edit-capped and revision content can be deleted;
- Collibra history is facet/configuration/permission specific;
- Immuta audit requires verified long-term export for replay beyond native SaaS retention;
- exact prior `inspectBasis` presentation requires independently retained prior projection/communication evidence;
- comparative Explanation sides independently bind source coverage/retention before a delta is asserted.

## Why this order

1. **Contract vocabulary first** — every source must be evaluated using the same proposition/authority/time/coverage vocabulary before vendor facts can be compared.
2. **Identity/governance before operational joins** — later evidence is unsafe if source identities, metadata authority and disclosure constraints cannot be resolved.
3. **Runtime/version before health and Impact** — run-specific execution/version evidence is required to interpret many measurements and downstream consumption claims correctly.
4. **Health before downstream inference** — Impact and investigation need bounded source-state/Assessment evidence rather than generic asset status.
5. **Lineage/consumer evidence before causal/control conclusions** — candidate paths must be separated from actual encounter/exposure/effect.
6. **Control evidence after operational/Impact evidence** — Gate/Safeguard effectiveness cannot be assessed from configuration alone.
7. **Explanation/history after source contracts** — basis inspection and historical replay must consume known source capabilities and retention limits.
8. **Cross-source consolidation last** — feasibility, cost and architecture handoff only become meaningful after source-specific contracts are known.

## Permanent Phase 009 boundaries

Preserve throughout the phase:

- source availability ≠ source authority;
- source authority ≠ evidence sufficiency;
- evidence sufficiency ≠ authorization;
- integration accessibility ≠ permission to disclose;
- source precedence is proposition/category/context specific, never synchronization-order based;
- source-local identifier ≠ Entity Identity without reconciliation evidence;
- timestamp proximity ≠ association or causality;
- source event time ≠ recorded/knowledge time unless the source semantics establish both;
- event timestamp ≠ historical knowledge availability;
- current source state ≠ historical state;
- late/corrected evidence must not be backfilled into earlier knowledge cuts;
- missing telemetry ≠ negative fact;
- negative conclusions retain proposition-specific opportunity/coverage burdens;
- duplicate/common-derived integrations ≠ independent corroboration;
- Lineage ≠ actual consumer use/exposure;
- observed read ≠ exact affected-version exposure absent state/version evidence;
- dashboard/report access ≠ dataset execution/result receipt/business reliance;
- safe cache/copy path ≠ global non-exposure;
- exposure ≠ effect ≠ consequence ≠ cause;
- deployment/workflow success ≠ activation/realized Change/run-specific version by convenience;
- run success ≠ output existence/currentness/health;
- check/metric availability ≠ governed Expectation/Baseline/Assessment authority;
- Investigation/localization ≠ Causal Claim status;
- control configuration/request/decision ≠ enforcement/effect;
- Safeguard enforcement ≠ prevented exposure without exact opportunity/path evidence;
- Gate HOLD/ADMIT ≠ execution outcome;
- retained source history ≠ as-known Explanation ≠ actual retained communication;
- delivery evidence ≠ exact communication content;
- reconstructed historical Explanation ≠ actual historical communication;
- current requester disclosure ≠ historical actor authorization;
- citation/reference ≠ inspectBasis permission;
- more visible basis ≠ more true/more supported;
- restricted ≠ unavailable/absent;
- unsupported integration capability is an explicit result, not a reason to weaken product semantics;
- no integration adapter, service, storage, event, polling, streaming, agent, LLM, snapshot-store or deployment architecture is selected in Phase 009.

## Phase 010 handoff target

Phase 010 should receive a concrete, evidence-backed matrix of source capabilities and gaps, including identity/join contracts, authority applicability, temporal semantics, coverage, latency, retention, historical availability timing, retained-communication requirements, basis inspectability, disclosure constraints, cost/quota and observability. Architecture may then choose how to ingest, persist, archive, reconcile and serve those capabilities without rediscovering or changing the functional contracts.
