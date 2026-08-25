# Phase 009 — Integration Contracts, Source Authority, and Evidence Availability

**Status:** IN PROGRESS — Groups 01–04 accepted; INTG-001–INTG-119 accepted; IC01-01–IC01-40, GOV02-01–GOV02-48, RTE03-01–RTE03-54 and HME04-01–HME04-56 pass; Group 05 next

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

Accepted range so far: **INTG-001–INTG-119**.

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
**Status:** **Next — not started.**

Map effective Lineage/topology, prospective path evidence, actual publication/availability, consumer encounter/use, run/query/version consumption, exposure, downstream effect and technical/analytical/business consequence evidence.

The group must characterize path/population coverage explicitly. Lineage reachability alone cannot satisfy encounter/exposure/Impact requirements, and missing downstream telemetry cannot become non-exposure.

See [`05_lineage_consumer_use_exposure_impact_evidence/README.md`](05_lineage_consumer_use_exposure_impact_evidence/README.md).

### Group 06 — Investigation, Causality, Safeguard, Gate & Control Evidence
**Status:** Not started.

Map source support for Investigation leads/localization, discriminating evidence, Causal Claim support/contradiction, Propagation Safeguard proposal/authorization/request/enforcement/release, Execution Gate readiness/decision/delivery/enforcement and actual control effects.

Control configuration or intended action is not enforcement. Broader prevention/delay/harm attribution remains evidence- and authority-gated Causal Claim work.

See [`06_investigation_causality_safeguard_gate_control_evidence/README.md`](06_investigation_causality_safeguard_gate_control_evidence/README.md).

### Group 07 — Explanation, Historical Replay, Basis Inspection & Disclosure Source Contracts
**Status:** Not started.

Map what is required to compose current/as-known/retrospective Explanation, retain or reconstruct historical views, inspect statement basis, preserve source provenance, apply current disclosure authorization and distinguish actual retained communication from present reconstruction.

This group evaluates source/history/disclosure capability only. It does not select an LLM, retrieval engine, snapshot store, citation UI or Explanation-delivery architecture.

See [`07_explanation_historical_replay_basis_disclosure_source_contracts/README.md`](07_explanation_historical_replay_basis_disclosure_source_contracts/README.md).

### Group 08 — Cross-Source Coverage, Latency, Retention, Cost & Phase Consolidation / Exit
**Status:** Not started.

Compose the source contracts across all prior groups. Identify evidence gaps, conflicting/overlapping source roles, cross-source join risks, clock/time-cut limitations, coverage boundaries, latency/freshness envelopes, retention/replay feasibility, quotas/cost, integration observability and graceful degradation.

The exit review must state which accepted product requirements are fully supportable, partially supportable, unsupported or still unknown with the evaluated integrations, without weakening source semantics. It then hands concrete integration facts to Phase 010 technical architecture.

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
- current source state ≠ historical state;
- late/corrected evidence must not be backfilled into earlier knowledge cuts;
- missing telemetry ≠ negative fact;
- negative conclusions retain proposition-specific opportunity/coverage burdens;
- duplicate/common-derived integrations ≠ independent corroboration;
- Lineage ≠ actual consumer use/exposure;
- deployment/workflow success ≠ activation/realized Change/run-specific version by convenience;
- run success ≠ output existence/currentness/health;
- check/metric availability ≠ governed Expectation/Baseline/Assessment authority;
- control configuration/request/decision ≠ enforcement/effect;
- restricted ≠ unavailable/absent;
- retained source history ≠ exact retained Explanation communication;
- unsupported integration capability is an explicit result, not a reason to weaken product semantics;
- no integration adapter, service, storage, event, polling, streaming, agent, LLM or deployment architecture is selected in Phase 009.

## Phase 010 handoff target

Phase 010 should receive a concrete, evidence-backed matrix of source capabilities and gaps, including identity/join contracts, authority applicability, temporal semantics, coverage, latency, retention, disclosure constraints, cost/quota and observability. Architecture may then choose how to ingest, persist, reconcile and serve those capabilities without rediscovering or changing the functional contracts.
