# Phase 009 — Integration Contracts, Source Authority, and Evidence Availability

**Status:** IN PROGRESS — Group 01 accepted; INTG-001–INTG-022 accepted; Group 02 next

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

Accepted range so far: **INTG-001–INTG-022**.

## Logical delivery grouping

Phase 009 is reviewed in eight dependency-ordered groups. The groups are organized around **evidence responsibilities and reasoning dependencies**, not vendor ownership.

### Group 01 — Integration Contract Vocabulary, Source Roles & Capability Matrix
**Status:** **Accepted — INTG-001–INTG-022; IC01-01–IC01-40 pass.**

Defines exact source-surface identity/version context; proposition binding; evidence roles; authority/relevance/sufficiency/authorization separation; identity and association joins; temporal coordinates; grain/context; positive and negative evidence; coverage; availability/latency; retention/replay; correction/backfill/mutation; duplicate/common derivation; conflict/fallback; support-gap taxonomy; quota/cost; and integration observability.

No new concept is required. Integration support remains proposition/source-set/context bound rather than a vendor-wide score.

See [`01_integration_contract_vocabulary_source_roles_capability_matrix/README.md`](01_integration_contract_vocabulary_source_roles_capability_matrix/README.md).

### Group 02 — Identity, Scope, Semantics, Governance, Authority & Authorization Sources
**Status:** **Next — not started.**

Apply INTG-001–INTG-022 to Entity Identity, Monitoring Scope, Semantic Definition, Responsibility Assignment, Classification, Policy Context, Assertion Authority and Capability Authorization. Evaluate identity reconciliation, metadata-category authority, conflicting assertions, current/historical applicability, disclosure rules and source-specific gaps.

Likely source families include Unity Catalog, Collibra, Immuta, repository/configuration metadata and organizational identity/IAM surfaces, but source roles must be established from current evidence rather than assumed from product names.

See [`02_identity_scope_governance_authority_authorization_sources/README.md`](02_identity_scope_governance_authority_authorization_sources/README.md).

### Group 03 — Change Intent, Deployment, Execution, Version & Runtime Evidence
**Status:** Not started.

Map evidence for Change Intent, repository revision, workflow/deployment attempt and activation, execution opportunity/run/attempt/lifecycle, run-specific implementation/input/output version, dependency sequencing, retry/rerun/backfill and timing.

Likely source families include Git/GitHub, GitHub Actions, Databricks Jobs/Workflows and runtime/system telemetry. The group must prove cross-system associations instead of inferring them from names or timestamps.

See [`03_change_deployment_execution_version_runtime_evidence/README.md`](03_change_deployment_execution_version_runtime_evidence/README.md).

### Group 04 — Health, Schema, Metrics, Expectations, Baselines & Reconciliation Evidence
**Status:** Not started.

Map source support for structural observations, schema compatibility evidence, metric observations, DQ results, Expectation outcomes, Baseline/comparability evidence, transformation reconciliation, composite health inputs, freshness/currentness and exact-use evidence suitability.

Likely source families include Databricks metadata/system surfaces, DQX, Metric Views and other query/measurement outputs. Availability of a metric/check does not automatically make it the governed Expectation, Baseline, or authoritative health result.

See [`04_health_schema_metrics_expectations_baselines_reconciliation_evidence/README.md`](04_health_schema_metrics_expectations_baselines_reconciliation_evidence/README.md).

### Group 05 — Lineage, Consumer Use, Exposure, Effect & Impact Evidence
**Status:** Not started.

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