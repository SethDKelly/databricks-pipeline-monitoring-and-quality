# 009 — Initial Roadmap

This roadmap delays implementation until product concepts, synchronizations, trust boundaries, evidence semantics, integration authority, health/metric semantics, and technical constraints are stable enough to guide architecture.

## Phase 001 — Product Foundation and Concept Discovery
**Status:** Complete.

## Phase 002 — Concept Specifications
**Status:** **Complete with three accepted post-exit addenda.**

The original five groups accepted 20 concepts. Phase 003 later added **Propagation Safeguard**, **Capability Authorization**, and **Execution Gate** after synchronization review exposed independent missing behavior. Current catalog: **23 concepts**.

## Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** **Complete — Groups 01–06 accepted; SYN-001–SYN-035 accepted; E-01–E-22 pass.**

Phase 003 defines end-to-end coordination for subject/governance context; planned change/reference transition; runtime timing/health/change; optional execution gating; safeguards; Investigation/causality; layered downstream Impact; Annotation; authorized analytical projection/Explanation; and bitemporal historical replay.

## Phase 004 — Evidence, Time, and Causality Refinement

**Status:** **COMPLETE — Groups 01–05 accepted; REF-001–REF-030 accepted.**

Phase 004 uses `REF-###` refinement contracts over accepted concepts/synchronizations. These are not new truth-owning concepts and do not extend the Phase 003 SYN sequence.

Accepted groups:

1. **Evidence Sufficiency, Coverage & Negative Evidence — REF-001–REF-005.** Proposition binding/evidence applicability, bounded coverage/opportunity-to-observe, negative/absence/exclusion evidence, corroboration/conflict/independence, conclusion-specific sufficiency.
2. **Event/Effective Time, Knowledge Cut & Correction — REF-006–REF-012.** Event/source-availability/framework-knowledge/evaluation time, exact `as-known` eligibility, negative epistemic claims, progressive analytical availability, late/corrected evidence classes, material reassessment/reopen behavior, actual-retained versus reconstructed historical state.
3. **Causal Epistemics, Confirmation & Multiple Contributors — REF-013–REF-020.** Causal proposition/status, multidimensional support/contradiction, bounded alternatives, claim-class confirmation profiles, evidence/authority separation, multiple contributors, qualitative roles, progressive RCA, post-confirmation challenge.
4. **Exposure, Consumption, Readiness & Control Evidence — REF-021–REF-030.** Encounter-bound exposure, non-exposure coverage, criterion-relative readiness, gate decision/enforcement/execution separation, safeguard enforcement/prevention, fallback evidence, control-effect causality and retrospective revision.
5. **Consolidation / Exit Review — accepted.** E-01–E-22 and all Phase 004 scenario checks pass under REF-001–REF-030. No additional Concept, synchronization, or REF contract is required.

### Progressive monitoring-result and RCA availability

Phase 004 establishes functional sequences rather than fixed SLAs:

**immediate operational validation → enriched health evaluation → investigative/RCA reasoning → retrospective/post-operations review**

Within RCA:

**candidate/proposed claim → early supported/weakened/unresolved evaluation → deeper investigative RCA → retrospective/confirmation review**

For controls/exposure:

**readiness/output facts → gate decision → enforcement evidence → execution/consumption evidence → negative/prevention/causal conclusions as coverage matures**.

The project should return the narrowest trustworthy result as soon as its evidence standard is satisfied. Faster job lifecycle evidence should not wait for slower Metric View/DQ/RCA evidence, while early results must not overstate health, causality, exposure, or control enforcement.

## Pre-Phase-005 metric-health handoff

Before Phase 005, the project accepted that **table/pipeline health is broader than successful execution** and that metric design needs explicit later treatment.

The handoff establishes:

- Phase 005 governs who may define/approve/revise/waive/retire/disclose metric profiles, Expectations, thresholds, margins/tolerance bands, and severity;
- Phase 006 defines actual metric families, per-asset metric profiles, statistical/Baseline/threshold semantics, metric bloat controls, technical/business health projections, and selective metric propagation/reconciliation;
- Phase 007 refines Lineage-aware metric propagation behavior and operational use;
- Phase 009 determines actual Databricks/Metric Views/DQX/source metric availability, cost, latency, and retention;
- Phase 010 selects precomputation/on-demand/fast-path architecture.

Metric selection should be purposeful rather than exhaustive: a small core plus critical-field/business, transformation-specific, and diagnostic/on-demand metrics. Metrics do not recursively propagate through Lineage by default; join/filter/aggregation/grain/business semantics determine valid relationships.

See `../concepts/phase_005/pre_phase_metric_health_handoff.md` and `../concepts/phase_006/README.md`.

## Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement

**Status:** **NEXT — delivery groups designed; not started.**

Planned review groups:

1. **Authority Vocabulary, Source Assertions & Conflict Resolution** — common authority scope, authoritative/advisory/correction/supersession/conflict semantics.
2. **Semantic, Responsibility, Classification, Policy & Criticality Governance** — category-specific descriptive/governance authority.
3. **Normative Health, Metric & Threshold Governance** — who may define/approve metric profiles, Expectations, thresholds, margins, severity, waivers, and high-consequence metric use; does not define metric statistical semantics.
4. **Capability Authorization & Restricted Analytical Visibility** — canonical capability vocabulary, conditional/current/historical authorization, restricted-data analytical projection.
5. **High-Consequence Action, Control & Causal-Confirmation Authority** — causal confirmation, job operations, safeguards, Execution Gates, override/delegation/separation-of-duties semantics.
6. **Disclosure, Explanation & Audience Governance** — authorized technical/business disclosure, opacity, inference leakage, high-consequence communication review.
7. **Consolidation / Exit Review** — compose authority/governance semantics without stealing evidence truth or selecting IAM/technical architecture.

Phase 005 may determine who/what is permitted to confirm, configure, operate, disclose, define normative metric state, or resolve authoritative assertions. It must **not** weaken or redefine Phase 004 evidence meanings, define Phase 006 metric/statistical behavior, or select IAM implementation.

## Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement

**Status:** Future — not started.

Phase 006 explicitly owns the detailed health/metric model, including:

- metric-family taxonomy;
- per-table/pipeline metric profiles;
- core versus critical-field versus transformation-specific versus business-critical versus diagnostic/on-demand metrics;
- output/load, volume, freshness, completeness, uniqueness, validity, schema, distribution/quantile, relational/join/reconciliation, and business-semantic metric families as applicable;
- metric-bloat control and lifecycle/retirement principles;
- hard thresholds, warning/failure margins, absolute/relative/asymmetric tolerance bands, Baseline-derived ranges, seasonality/cohort behavior, low-volume/sample-size uncertainty, and structural-change comparability;
- Assessment/composite-health semantics without hiding dimension disagreement;
- selective transformation-aware metric propagation/reconciliation across pipelines;
- technical versus business health projections over the same truth;
- Databricks Metric Views/DQX semantic fit;
- functional availability expectations for immediate operational metrics, near-real-time core health, enriched DQ/distribution health, diagnostic/RCA metrics, and post-ops metrics.

Phase 006 must not blindly calculate every possible metric, recursively copy every upstream statistic downstream, or make useful monitoring metrics synchronous production dependencies by default.

## Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement

Refine Lineage taxonomy/historical topology evidence, Change Intent realization, execution reconstruction, Investigation lifecycle, prospective/actual Impact, consumer/version encounter patterns, consequence categories, **Lineage-aware health/metric propagation and transformation-reconciliation behavior**, safeguard placement/release, Execution Gate classes, timeout/fallback/escalation/override/recovery policy, and control-induced operational effects. Preserve Phase 004 evidence burdens and Phase 006 metric meanings.

## Phase 008 — Business Questioning and Explanation

Define question types, audience-specific Explanation structures, visible evidence citations, Authorized Analytical Projection/redaction, layered Impact/control state, contemporaneous/retrospective/comparison views, reconstructed-versus-actual historical Explanation labeling, uncertainty communication, deterministic versus generative behavior, progressive result maturity communication, and technical-versus-business metric/health presentation.

## Phase 009 — Integration Contracts, Source Authority, and Evidence Availability

Determine required facts and actual evidence support for Databricks, Git repositories, GitHub Actions, DQX, Metric Views, Collibra, Immuta, downstream consumption/version evidence, Change Intent, safeguard/gate enforcement, authorization sources, causal evidence inputs, and **accepted health/metric profiles**.

Characterize **source production/availability time, collection latency, retention, query cost/availability, metric computation cost, and control-enforcement observability** needed to satisfy accepted evidence/timing semantics. Preserve the objective that baseline monitoring be independently deployed and avoid production repository/GitHub Actions changes where platform metadata is sufficient.

## Phase 010 — Technical Architecture

Only now select implementation architecture. Evaluate evidence/history storage; graph-compatible Lineage; temporal/ledger history; ingestion/synchronization; Capability Authorization realization; Databricks deployment model; out-of-band passive monitoring; optional dependency-gating control-plane realization/availability/fallback; safeguard/quarantine realization; metric precomputation/on-demand evaluation strategy; Explanation interface; testing/observability; causal reasoning implementation; and **fast-path versus asynchronous/deeper analysis architecture and performance budgets**.

A key architecture criterion remains that **ungated production jobs must not depend on monitoring-framework availability**. Explicitly gated paths may require deliberate production-critical control availability under accepted policies.

## Phase 011 — MVP Implementation Planning

Convert accepted architecture into implementation phases, interfaces, test strategy, onboarding/migration strategy, acceptance criteria, and concrete availability/latency targets for selected MVP monitoring-result, metric/health, RCA, exposure, and control classes.

## Phase 012 — MVP Implementation

Implement minimum vertical slices required to prove the accepted MVP scenarios.

## Roadmap rule

A later phase may reveal a flaw in an earlier concept, synchronization, or refinement. Reopen/revise it explicitly with rationale rather than preserving a bad boundary merely to maintain sequence.