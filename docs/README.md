# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

- **Phase 002 — Concept Specifications: COMPLETE with four accepted post-exit addenda.** Current catalog: 24 concepts.
- **Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE.** SYN-001–SYN-035 accepted; E-01–E-22 pass.
- **Phase 004 — Evidence, Time, and Causality Refinement: COMPLETE.** REF-001–REF-030 accepted.
- **Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement: COMPLETE.** AUTH-001–AUTH-053 final; G07-01–G07-26 pass.
- **Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement: COMPLETE.** Groups 01–07 accepted; HLTH-001–HLTH-066 final; H07-01–H07-36 pass.
- **Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement: IN PROGRESS.** Groups 01–02 accepted; OPS-001–OPS-020 accepted; L01-01–L01-18 and C02-01–C02-24 pass; Group 03 next.

The current catalog contains **24 accepted concepts**: the original 20 plus **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**.

## Reading order

1. [`../README.md`](../README.md) — project orientation; older status-only wording is superseded by canonical phase status where necessary.
2. [`foundation/001_product_definition.md`](foundation/001_product_definition.md) — product purpose.
3. [`foundation/002_actors_and_stakeholders.md`](foundation/002_actors_and_stakeholders.md) — actors.
4. [`foundation/003_terminology.md`](foundation/003_terminology.md) — foundational distinctions.
5. [`foundation/004_concept_design_method.md`](foundation/004_concept_design_method.md) — Concept Design method.
6. [`foundation/005_architectural_principles.md`](foundation/005_architectural_principles.md) — architectural constraints.
7. [`foundation/006_security_governance_and_policy_model.md`](foundation/006_security_governance_and_policy_model.md) — security/governance foundation.
8. [`foundation/007_ecosystem_lifecycles.md`](foundation/007_ecosystem_lifecycles.md) — functional lifecycles.
9. [`foundation/008_mvp_boundary.md`](foundation/008_mvp_boundary.md) — MVP boundary.
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — phase ownership/sequence; use this current-state section for live status.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved choices.
12. [`concepts/README.md`](concepts/README.md) — accepted concept catalog and cross-cutting boundaries.
13. [`concepts/phase_003/README.md`](concepts/phase_003/README.md) — completed synchronization phase.
14. [`concepts/phase_004/README.md`](concepts/phase_004/README.md) — completed evidence/time/causality refinement.
15. [`concepts/phase_005/README.md`](concepts/phase_005/README.md) — completed authority/governance/capability/disclosure refinement.
16. [`concepts/phase_005/07_consolidation_and_exit/phase_005_exit_review.md`](concepts/phase_005/07_consolidation_and_exit/phase_005_exit_review.md) — Phase 005 exit.
17. [`concepts/phase_006/README.md`](concepts/phase_006/README.md) — completed Phase 006 health model.
18. [`concepts/phase_006/01_measurement_vocabulary_metric_profiles/README.md`](concepts/phase_006/01_measurement_vocabulary_metric_profiles/README.md) — HLTH-001–HLTH-008.
19. [`concepts/phase_006/02_structural_schema_ddl_compatibility/README.md`](concepts/phase_006/02_structural_schema_ddl_compatibility/README.md) — HLTH-009–HLTH-018.
20. [`concepts/phase_006/03_baselines_comparability_distribution_statistical_context/README.md`](concepts/phase_006/03_baselines_comparability_distribution_statistical_context/README.md) — HLTH-019–HLTH-029.
21. [`concepts/phase_006/04_expectations_thresholds_margins_waivers_assessment/README.md`](concepts/phase_006/04_expectations_thresholds_margins_waivers_assessment/README.md) — HLTH-030–HLTH-040.
22. [`concepts/phase_006/05_transformation_reconciliation_metric_propagation/README.md`](concepts/phase_006/05_transformation_reconciliation_metric_propagation/README.md) — HLTH-041–HLTH-054.
23. [`concepts/phase_006/06_composite_health_readiness_timing/README.md`](concepts/phase_006/06_composite_health_readiness_timing/README.md) — HLTH-055–HLTH-066.
24. [`concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md`](concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md) — canonical Phase 006 exit review.
25. [`concepts/phase_007/README.md`](concepts/phase_007/README.md) — current Phase 007 plan and progress.
26. [`concepts/phase_007/01_lineage_relationship_taxonomy_historical_topology/README.md`](concepts/phase_007/01_lineage_relationship_taxonomy_historical_topology/README.md) — accepted Group 01 / OPS-001–OPS-009.
27. [`concepts/phase_007/01_lineage_relationship_taxonomy_historical_topology/scenario_review.md`](concepts/phase_007/01_lineage_relationship_taxonomy_historical_topology/scenario_review.md) — L01-01–L01-18.
28. [`concepts/phase_007/02_change_intent_deployment_realized_change/README.md`](concepts/phase_007/02_change_intent_deployment_realized_change/README.md) — accepted Group 02 / OPS-010–OPS-020.
29. [`concepts/phase_007/02_change_intent_deployment_realized_change/scenario_review.md`](concepts/phase_007/02_change_intent_deployment_realized_change/scenario_review.md) — C02-01–C02-24.
30. [`concepts/phase_007/03_prospective_blast_radius_change_aware_review/README.md`](concepts/phase_007/03_prospective_blast_radius_change_aware_review/README.md) — next Phase 007 group.
31. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
32. [`reference/authority_vocabulary.md`](reference/authority_vocabulary.md) — authority vocabulary.
33. [`decisions/README.md`](decisions/README.md) — durable decision history/index.
34. [`decisions/phase_006_group_07_consolidation_and_exit.md`](decisions/phase_006_group_07_consolidation_and_exit.md) — D-383–D-405.
35. [`decisions/phase_007_group_01_lineage_topology.md`](decisions/phase_007_group_01_lineage_topology.md) — D-406–D-421.
36. [`decisions/phase_007_group_02_change_realization.md`](decisions/phase_007_group_02_change_realization.md) — D-422–D-440.

## Phase 006 exit summary

Phase 006 establishes the final functional health chain:

**definition/applicability → Observation → structural/comparability context → component Assessment → transformation reconciliation → composite Assessment → freshness/maturity → exact-use suitability → readiness**, with gate decision/enforcement/execution remaining separate.

It preserves structural compatibility ≠ statistical comparability; Baseline typicality ≠ normative health; warning/severity/waiver ≠ criterion truth; Lineage ≠ metric/status propagation or causality; composite health as profile/use/context bound rather than a universal score; evaluation recency ≠ evidence freshness; evidence maturity by sufficiency, not elapsed time; exact-use suitability; AUTH-023 eligibility ≠ evidence suitability; passive monitoring as non-blocking for ungated production; and non-rewriting historical health/readiness replay.

## Phase 007 accepted progress

### Group 01 — operational Lineage

Group 01 establishes:

**bounded relationship proposition → minimum semantic family → field/key/population/consumer/version scope → effective/historical interval → REF-based relationship evidence → authority-aware resolution → question-bound traversal relevance → bounded completeness**,

while actual execution/encounter/Impact/control/cause remain separate.

Accepted range: **OPS-001–OPS-009**.

### Group 02 — Change Intent / Deployment / realized Change

Group 02 establishes:

**exact intent revision/component → evidence-backed Deployment association → attempt/outcome → target/facet activation → active-state interval → evidence-established realized Change → derived intent-to-realization comparison**.

It explicitly rejects a universal deployment/version identity or realization score; keeps partial rollout slice-specific; separates `not evidenced` from strong `not realized`; distinguishes missing registration from proven unplanned change; and makes rollback/reversion non-rewriting and non-transitive to downstream state.

Accepted range: **OPS-010–OPS-020**. No new concept was required.

## Documentation discipline

- Concepts/synchronizations/refinements remain implementation-neutral.
- `REF-###` defines evidence/time/causal/control standards; `AUTH-###` defines authority/governance/capability/disclosure standards; `HLTH-###` defines health/metric/schema/statistical/reconciliation/composite/timing standards; `OPS-###` defines Phase 007 operational/topology/change/impact/control refinements.
- Preserve historical rationale; add/supersede rather than silently rewrite.
- Synchronization/refinement order never becomes source authority or causation.
- Evidence sufficiency is conclusion-relative; missing/restricted/unavailable evidence is not a negative fact.
- Baseline remains descriptive; Expectation remains normative.
- Metric/reconciliation/composite semantics do not blindly propagate through Lineage.
- Lineage reachability does not imply relevance, encounter, Impact or causality.
- Deployment activation does not imply intended/downstream effect or execution version use.
- Intent conformance does not imply health/cause.
- Audience simplification cannot strengthen underlying status.
- Passive monitoring remains non-blocking/out-of-band by default; Execution Gate remains explicit opt-in active control.
- Phase 007 must consume HLTH-001–HLTH-066 rather than reopen health semantics by convenience.
- Keep examples synthetic; no real PII/PHI/secrets/production values.
