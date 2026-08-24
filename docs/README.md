# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is complete. Phase 004 — Evidence, Time, and Causality Refinement is complete. Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement is active: Group 01 is accepted with AUTH-001–AUTH-008; Group 02 is next.**

The original Phase 002 catalog contained 20 concepts. Four post-exit addenda are accepted:

1. **Propagation Safeguard**;
2. **Capability Authorization**;
3. **Execution Gate**;
4. **Assertion Authority** — discovered during Phase 005 Group 01.

The current catalog contains **24 accepted concepts**. Phase 003 contains accepted **SYN-001–SYN-035** and E-01–E-22 pass the Group 06 replay/consolidation review. Phase 004 contains accepted **REF-001–REF-030** and has exited. Phase 005 Group 01 contains accepted **AUTH-001–AUTH-008**.

## Reading order

1. [`../README.md`](../README.md) — project orientation/current state.
2. [`foundation/001_product_definition.md`](foundation/001_product_definition.md) — product purpose.
3. [`foundation/002_actors_and_stakeholders.md`](foundation/002_actors_and_stakeholders.md) — actors.
4. [`foundation/003_terminology.md`](foundation/003_terminology.md) — foundational distinctions.
5. [`foundation/004_concept_design_method.md`](foundation/004_concept_design_method.md) — Concept Design method.
6. [`foundation/005_architectural_principles.md`](foundation/005_architectural_principles.md) — architectural constraints, including non-blocking passive monitoring, optional active gating, and bitemporal/non-rewriting replay.
7. [`foundation/006_security_governance_and_policy_model.md`](foundation/006_security_governance_and_policy_model.md) — security/governance/authorization foundation.
8. [`foundation/007_ecosystem_lifecycles.md`](foundation/007_ecosystem_lifecycles.md) — functional lifecycles.
9. [`foundation/008_mvp_boundary.md`](foundation/008_mvp_boundary.md) — MVP boundary.
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — roadmap/current phase, including progressive monitoring/RCA/control timing and metric-health handoffs.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved choices, including category-specific authority, health timing, metric semantics, control policy, integration, and architecture questions.
12. [`concepts/README.md`](concepts/README.md) — 24-concept catalog.
13. [`concepts/phase_002/README.md`](concepts/phase_002/README.md) — original concept review + addenda history.
14. [`concepts/phase_002/addenda/`](concepts/phase_002/addenda/) — Propagation Safeguard, Capability Authorization, Execution Gate, and Assertion Authority.
15. [`concepts/phase_002/addenda/assertion_authority.md`](concepts/phase_002/addenda/assertion_authority.md) — accepted Assertion Authority concept.
16. [`concepts/phase_003/README.md`](concepts/phase_003/README.md) — completed synchronization phase state and E-01–E-22.
17. [`concepts/phase_003/03_runtime_evidence_health_and_change/032_dependency_readiness_execution_gate.md`](concepts/phase_003/03_runtime_evidence_health_and_change/032_dependency_readiness_execution_gate.md) — accepted optional execution-gating extension.
18. [`concepts/phase_003/05_impact_annotation_and_explanation/README.md`](concepts/phase_003/05_impact_annotation_and_explanation/README.md) — accepted downstream Impact/Annotation/Explanation synchronizations.
19. [`concepts/phase_003/06_historical_replay_and_consolidation/README.md`](concepts/phase_003/06_historical_replay_and_consolidation/README.md) — accepted historical replay/consolidation.
20. [`concepts/phase_003/06_historical_replay_and_consolidation/scenario_replay_matrix.md`](concepts/phase_003/06_historical_replay_and_consolidation/scenario_replay_matrix.md) — E-01–E-22 end-to-end replay matrix.
21. [`concepts/phase_003/06_historical_replay_and_consolidation/phase_003_exit_review.md`](concepts/phase_003/06_historical_replay_and_consolidation/phase_003_exit_review.md) — Phase 003 exit decision.
22. [`concepts/phase_004/README.md`](concepts/phase_004/README.md) — completed Phase 004 structure/status.
23. [`concepts/phase_004/01_evidence_sufficiency_and_coverage/README.md`](concepts/phase_004/01_evidence_sufficiency_and_coverage/README.md) — accepted evidence applicability/coverage/sufficiency framework.
24. [`concepts/phase_004/02_event_time_knowledge_cut_and_correction/README.md`](concepts/phase_004/02_event_time_knowledge_cut_and_correction/README.md) — accepted temporal evidence/progressive availability/correction framework.
25. [`concepts/phase_004/03_causal_epistemics_confirmation/README.md`](concepts/phase_004/03_causal_epistemics_confirmation/README.md) — accepted causal epistemics/confirmation/multiple-contributor framework.
26. [`concepts/phase_004/04_exposure_consumption_readiness_control/README.md`](concepts/phase_004/04_exposure_consumption_readiness_control/README.md) — accepted exposure/readiness/control evidence framework.
27. [`concepts/phase_004/05_consolidation_and_exit/phase_004_exit_review.md`](concepts/phase_004/05_consolidation_and_exit/phase_004_exit_review.md) — accepted Phase 004 exit review.
28. [`concepts/phase_005/README.md`](concepts/phase_005/README.md) — active Phase 005 structure/status.
29. [`concepts/phase_005/01_authority_vocabulary_and_conflict/README.md`](concepts/phase_005/01_authority_vocabulary_and_conflict/README.md) — accepted Group 01 Assertion Authority and AUTH-001–AUTH-008.
30. [`concepts/phase_005/01_authority_vocabulary_and_conflict/scenario_checks.md`](concepts/phase_005/01_authority_vocabulary_and_conflict/scenario_checks.md) — Group 01 authority/conflict stress checks.
31. [`concepts/phase_005/02_semantic_governance_authority/README.md`](concepts/phase_005/02_semantic_governance_authority/README.md) — next Group 02 handoff.
32. [`concepts/phase_005/pre_phase_metric_health_handoff.md`](concepts/phase_005/pre_phase_metric_health_handoff.md) — metric/health handoff.
33. [`concepts/phase_006/README.md`](concepts/phase_006/README.md) — future health/metrics phase handoff.
34. [`reference/glossary.md`](reference/glossary.md) — canonical broad vocabulary.
35. [`reference/authority_vocabulary.md`](reference/authority_vocabulary.md) — accepted Group 01 authority vocabulary reference.
36. [`decisions/README.md`](decisions/README.md) — foundational decision history.
37. [`decisions/phase_003_group_03_runtime_health_and_safeguard.md`](decisions/phase_003_group_03_runtime_health_and_safeguard.md) — D-040–D-046.
38. [`decisions/phase_003_group_04_lineage_investigation_causality.md`](decisions/phase_003_group_04_lineage_investigation_causality.md) — D-047–D-055.
39. [`decisions/pre_group_05_capability_authorization.md`](decisions/pre_group_05_capability_authorization.md) — D-056–D-060.
40. [`decisions/phase_003_group_05_impact_annotation_explanation.md`](decisions/phase_003_group_05_impact_annotation_explanation.md) — D-061–D-070.
41. [`decisions/pre_group_06_execution_gating.md`](decisions/pre_group_06_execution_gating.md) — D-071–D-078.
42. [`decisions/phase_003_group_06_historical_replay_and_exit.md`](decisions/phase_003_group_06_historical_replay_and_exit.md) — D-079–D-088.
43. [`decisions/phase_004_group_01_evidence_sufficiency_and_coverage.md`](decisions/phase_004_group_01_evidence_sufficiency_and_coverage.md) — D-089–D-097.
44. [`decisions/phase_004_group_02_time_knowledge_correction.md`](decisions/phase_004_group_02_time_knowledge_correction.md) — D-098–D-110.
45. [`decisions/phase_004_group_03_causal_epistemics_confirmation.md`](decisions/phase_004_group_03_causal_epistemics_confirmation.md) — D-111–D-123.
46. [`decisions/phase_004_group_04_exposure_readiness_control.md`](decisions/phase_004_group_04_exposure_readiness_control.md) — D-124–D-139.
47. [`decisions/phase_004_group_05_consolidation_and_exit.md`](decisions/phase_004_group_05_consolidation_and_exit.md) — D-140–D-152.
48. [`decisions/pre_phase_005_metric_health_and_grouping.md`](decisions/pre_phase_005_metric_health_and_grouping.md) — D-153–D-160.
49. [`decisions/phase_005_group_01_authority_vocabulary_conflict.md`](decisions/phase_005_group_01_authority_vocabulary_conflict.md) — D-161–D-172.

## Documentation discipline

- Concepts/synchronizations/refinements remain implementation-neutral.
- Phase 004 `REF-###` artifacts define evidence/time/causal/control standards; Phase 005 `AUTH-###` artifacts define authority/governance standards.
- Preserve historical decision rationale; add/supersede rather than silently rewrite.
- Synchronization/refinement order never becomes source authority or causation.
- Evidence sufficiency is conclusion-relative; evidence applicability, coverage, corroboration/conflict, and sufficiency remain separate.
- Negative/absence/exclusion conclusions require an adequate opportunity to observe and sufficient bounded coverage.
- Missing telemetry, failed/unavailable queries, restricted evidence, out-of-scope evidence, or unresolved identity/version state are not negative facts.
- Duplicated/common-source telemetry is not independent corroboration merely because it appears in multiple systems.
- Event/effective time, source availability, framework knowledge time, and derived evaluation time remain distinct.
- Monitoring/reasoning results may mature progressively without evidence-status inflation.
- Causal Claim status remains explicit; confirmed is separate from supported/leading and requires independent confirmation authority.
- Exposure/readiness/gate/safeguard evidence layers remain separate.
- **Assertion Authority is target/category/facet/context/time scoped.** No source/vendor is globally authoritative by default.
- Preserve source assertions regardless of authority standing.
- Authoritative standing is not factual infallibility, evidence sufficiency, Capability Authorization, Responsibility Assignment, policy applicability, or enforcement proof.
- Source count, majority, recency alone, ingestion order, availability, repository ownership, admin/title/responsibility, and apparent specificity are not hidden precedence.
- Co-authoritative disagreements remain authoritative conflict unless an explicit accepted resolver applies.
- Authority-rule conflict remains conflict unless an accepted governing rule resolves it.
- Conditional/fallback authority requires an explicit rule plus evidence that its activation condition holds.
- Historical authority uses effective time + knowledge time; later corrections do not rewrite what was known then.
- Capability Authorization remains distinct from Assertion Authority, Responsibility Assignment, Policy Context, Classification, and Monitoring Scope.
- Passive monitoring remains non-blocking/out-of-band by default; monitoring degradation must not delay ungated production jobs.
- Execution Gate remains explicit opt-in control and separate from Propagation Safeguard.
- Phase 006 owns detailed metric taxonomy/statistics/propagation; Phase 005 Group 03 only governs who may define/approve normative metric state.
- Keep examples synthetic; no real PII/PHI/secrets/production values.
- Do not select IAM, authority-rule engine, graph/event/temporal store, quarantine, scheduler/orchestration, causal algorithm/LLM, metric engine/storage, workflow, or service architecture prematurely.
