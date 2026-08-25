# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

- **Phase 002 — Concept Specifications: COMPLETE with four accepted post-exit addenda.** Current catalog: 24 concepts.
- **Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE.** SYN-001–SYN-035 accepted; E-01–E-22 pass.
- **Phase 004 — Evidence, Time, and Causality Refinement: COMPLETE.** REF-001–REF-030 accepted.
- **Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement: COMPLETE.** AUTH-001–AUTH-053 final; G07-01–G07-26 pass.
- **Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement: COMPLETE.** Groups 01–07 accepted; HLTH-001–HLTH-066 final; H07-01–H07-36 pass.
- **Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement: NEXT — not started.**

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
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — initial roadmap and later-phase ownership; use current phase docs for authoritative status.
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
24. [`concepts/phase_006/07_consolidation_and_exit/README.md`](concepts/phase_006/07_consolidation_and_exit/README.md) — accepted Group 07 / Phase 006 exit status.
25. [`concepts/phase_006/07_consolidation_and_exit/consolidation_scenario_matrix.md`](concepts/phase_006/07_consolidation_and_exit/consolidation_scenario_matrix.md) — H07-01–H07-36.
26. [`concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md`](concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md) — canonical Phase 006 exit review.
27. [`concepts/phase_007/README.md`](concepts/phase_007/README.md) — next-phase handoff; Phase 007 has not started.
28. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
29. [`reference/authority_vocabulary.md`](reference/authority_vocabulary.md) — authority vocabulary.
30. [`decisions/README.md`](decisions/README.md) — durable decision history/index.
31. [`decisions/phase_006_group_07_consolidation_and_exit.md`](decisions/phase_006_group_07_consolidation_and_exit.md) — D-383–D-405.

## Phase 006 exit summary

Phase 006 establishes the final functional health chain:

**definition/applicability → Observation → structural/comparability context → component Assessment → transformation reconciliation → composite Assessment → freshness/maturity → exact-use suitability → readiness**, with gate decision/enforcement/execution remaining separate.

It preserves:

- structural compatibility ≠ statistical comparability;
- Baseline typicality ≠ normative health;
- warning/severity/waiver ≠ criterion truth;
- Lineage ≠ metric/status propagation or causality;
- composite health as profile/use/context bound rather than a universal score;
- evaluation recency ≠ evidence freshness;
- evidence maturity by sufficiency, not elapsed time;
- suitability as exact-use and outcome-neutral;
- AUTH-023 eligibility ≠ evidence suitability;
- passive monitoring as non-blocking for ungated production;
- non-rewriting historical health/readiness replay.

## Documentation discipline

- Concepts/synchronizations/refinements remain implementation-neutral.
- `REF-###` defines evidence/time/causal/control standards; `AUTH-###` defines authority/governance/capability/disclosure standards; `HLTH-###` defines health/metric/schema/statistical/reconciliation/composite/timing standards.
- Preserve historical rationale; add/supersede rather than silently rewrite.
- Synchronization/refinement order never becomes source authority or causation.
- Evidence sufficiency is conclusion-relative; missing/restricted/unavailable evidence is not a negative fact.
- Baseline remains descriptive; Expectation remains normative.
- Metric/reconciliation/composite semantics do not blindly propagate through Lineage.
- Audience simplification cannot strengthen underlying status.
- Passive monitoring remains non-blocking/out-of-band by default; Execution Gate remains explicit opt-in active control.
- Phase 007 must consume HLTH-001–HLTH-066 rather than reopen health semantics by convenience.
- Keep examples synthetic; no real PII/PHI/secrets/production values.
