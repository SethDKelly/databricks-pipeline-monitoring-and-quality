# Phase 007 Group 03 — Prospective Blast Radius & Change-Aware Review

**Status:** Review complete — accepted

## Goal

Refine prospective downstream reasoning from a proposed Change using then-relevant Lineage without confusing candidate reachability or review need with actual exposure, Impact, predicted defect or causality.

## Group result

Group 03 accepts **OPS-021–OPS-033** and retains the existing concepts. No new concept is required.

The central functional view is a **derived prospective review profile** built from:

**exact Change Intent revision/component → effective Lineage at the review cut + explicit planned topology delta → question-bound candidate/relevance analysis → scoped Phase 006 review surfaces → authority/coverage limitations**.

The proposed topology is evaluated through a scenario overlay; it never becomes Lineage merely because it is useful for analysis.

## Accepted OPS contracts

1. [`OPS-021 — Prospective Review Proposition, Change Component & Evaluation Cut`](021_prospective_review_proposition_change_component_evaluation_cut.md)
2. [`OPS-022 — Prospective Scenario Topology: Effective State + Planned Delta`](022_prospective_scenario_topology_effective_planned_delta.md)
3. [`OPS-023 — Prospective Candidate Discovery & Path Basis`](023_prospective_candidate_discovery_path_basis.md)
4. [`OPS-024 — Semantic Scope Narrowing & Candidate Relevance`](024_semantic_scope_narrowing_candidate_relevance.md)
5. [`OPS-025 — Prospective Structural / Interface Compatibility Review`](025_prospective_structural_interface_compatibility_review.md)
6. [`OPS-026 — Metric, Profile, Expectation & Baseline Review Surface`](026_metric_profile_expectation_baseline_review_surface.md)
7. [`OPS-027 — Transformation & Reconciliation Change Review`](027_transformation_reconciliation_change_review.md)
8. [`OPS-028 — Readiness & Control-Assumption Review`](028_readiness_control_assumption_review.md)
9. [`OPS-029 — Review Relevance, Obligation, Approval & Control Separation`](029_review_relevance_obligation_approval_control_separation.md)
10. [`OPS-030 — Criticality, Priority, Risk Language & No Universal Score`](030_criticality_priority_risk_language_no_universal_score.md)
11. [`OPS-031 — Candidate Coverage, Completeness & Restricted/Conflicting Topology`](031_candidate_coverage_completeness_restricted_conflicting_topology.md)
12. [`OPS-032 — Partial Rollout, Mixed Prospective/Realized State & Historical Review`](032_partial_rollout_mixed_state_historical_review.md)
13. [`OPS-033 — Prospective Review Ownership & Group 04 Handoff`](033_cross_concept_ownership_group04_handoff.md)

## Prospective scenario topology

Group 03 does **not** create planned Lineage.

A review overlays explicit Change Intent topology deltas over the then-effective OPS-001–OPS-009 topology while preserving whether each relationship is effective or planned-only. Addition, removal and relationship/scope modification are all representable.

A planned removal does not make a current consumer disappear from blast radius. The consumer becomes a **path-loss/change candidate** because the dependency being removed is itself the proposed change.

## Candidate/relevance model

Impact continues to own candidate/reachability truth. Prospective candidate bases include:

- effective-path candidate;
- planned-added-path candidate;
- path-loss/change candidate;
- indeterminate candidate where topology/relevance is insufficient, conflicting or restricted.

Candidate relevance is narrowed by field/key/population/transformation/interface/consumer/version semantics. Asset-level reachability cannot automatically answer a field-level question.

## Change-aware review surfaces

Group 03 maps prospective changes to the accepted Phase 006 semantics rather than inventing generic `risk`:

- structural/interface compatibility under HLTH-009–HLTH-018;
- metric/check/profile/Expectation/Baseline applicability and prospective comparability review;
- transformation-specific reconciliation under HLTH-041–HLTH-054;
- composite/readiness-suitability assumptions and AUTH-023 control-use context;
- existing Gate/Safeguard scope assumptions where a proposal changes the bound subject/interface/version.

Review is scoped. A key/grain change can require count/uniqueness/distribution/join review while leaving unrelated execution or freshness semantics intact.

A pre-deployment compatibility result is explicitly proposal-bound. If realized state differs, the prospective result remains historical evidence about the proposal and production requires a new realized Assessment.

## Review versus governance/control

Preserve:

**analytical review relevance ≠ governed review obligation ≠ review/approval action ≠ deployment/control decision ≠ enforcement**.

AUTH-020 and other accepted authority/policy contracts can establish who may decide metric/Baseline/structural applicability or whether a review is required. Group 03 cannot manufacture those obligations from topology or criticality.

Likewise, identifying a readiness/control assumption for review does not configure a Gate/Safeguard or create HOLD/ADMIT/release behavior.

## Criticality and risk language

Criticality, Classification, Semantic Definition, Responsibility Assignment and Policy Context may enrich review priority/context. They do not establish probability of failure, actual Impact or evidence strength.

No universal numeric/qualitative risk score, severity-weighted blast-radius score, path-count probability or shortest-path importance rule is accepted.

## Coverage and negative claims

A known candidate set can be useful while incomplete. The profile retains topology cut, semantic/depth scope, effective/planned path coverage, restrictions, conflicts and Monitoring Scope limitations.

`No downstream candidates` or `consumer X is not in blast radius` is a bounded negative conclusion requiring sufficient opportunity/path/relevance coverage. Failure to find a path is not enough.

## Partial rollout and history

Mixed rollout is slice-specific. Evidence from an active canary may legitimately inform review of remaining slices but cannot be projected as their realized outcome.

Historical review distinguishes actual retained pre-deployment review, reconstructed as-known-then review and current retrospective recomputation. Late Lineage/consumer discovery may expand today's retrospective profile without rewriting what the reviewer could see then.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **P03-01–P03-30** across field-level narrowing, planned additions/removals, incomplete/restricted/conflicting topology, consumer-specific compatibility, key/grain/reconciliation/reference review, criticality, governed review obligation, control assumptions, mixed rollout, overlapping intents and historical late discovery.

## Durable boundaries

- planned scenario topology ≠ effective Lineage;
- candidate ≠ exposure ≠ effect ≠ consequence ≠ cause;
- review trigger ≠ predicted defect;
- proposed compatibility ≠ realized compatibility;
- review relevance ≠ obligation ≠ approval ≠ control;
- planned Baseline break ≠ empirical non-comparability;
- reconciliation review ≠ reconciliation failure;
- readiness/control review ≠ readiness/control state;
- criticality/priority ≠ probability/Impact;
- incomplete topology ≠ no blast radius;
- active canary ≠ global realized outcome;
- retrospective review ≠ what was known during original review.

## Architecture boundary

Group 03 does not select graph traversal algorithms, static-analysis engines, CI gates, risk scoring, graph storage, UI visualization, source integrations or technical architecture.

## Group exit gate

**Satisfied.** OPS-021–OPS-033 and P03-01–P03-30 establish proposal-bound scenario topology, scoped candidate/relevance reasoning, Phase 006 review mapping, governance/control separation, criticality/risk discipline, coverage limits and mixed/historical review without a 25th concept.

**Next: Phase 007 Group 04 — Execution Reconstruction, Dependency Sequence & Version Use.**