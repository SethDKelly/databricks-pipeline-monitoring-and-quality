# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is complete. Phase 004 — Evidence, Time, and Causality Refinement is active. Group 01 — Evidence Sufficiency, Coverage & Negative Evidence is accepted; Group 02 — Event/Effective Time, Knowledge Cut & Correction is next.**

The original Phase 002 catalog contained 20 concepts. Three post-exit addenda are accepted:

1. **Propagation Safeguard**;
2. **Capability Authorization**;
3. **Execution Gate**.

The current catalog contains **23 accepted concepts**. Phase 003 contains accepted **SYN-001–SYN-035** and E-01–E-22 pass the Group 06 replay/consolidation review. Phase 004 Group 01 contains accepted **REF-001–REF-005**.

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
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — roadmap/current phase.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved choices.
12. [`concepts/README.md`](concepts/README.md) — 23-concept catalog.
13. [`concepts/phase_002/README.md`](concepts/phase_002/README.md) — original concept review + addenda history.
14. [`concepts/phase_002/addenda/`](concepts/phase_002/addenda/) — Propagation Safeguard, Capability Authorization, and Execution Gate.
15. [`concepts/phase_003/README.md`](concepts/phase_003/README.md) — completed synchronization phase state and E-01–E-22.
16. [`concepts/phase_003/03_runtime_evidence_health_and_change/032_dependency_readiness_execution_gate.md`](concepts/phase_003/03_runtime_evidence_health_and_change/032_dependency_readiness_execution_gate.md) — accepted optional execution-gating extension.
17. [`concepts/phase_003/05_impact_annotation_and_explanation/README.md`](concepts/phase_003/05_impact_annotation_and_explanation/README.md) — accepted Group 05 downstream Impact/Annotation/Explanation synchronizations.
18. [`concepts/phase_003/06_historical_replay_and_consolidation/README.md`](concepts/phase_003/06_historical_replay_and_consolidation/README.md) — accepted Group 06 historical replay/consolidation.
19. [`concepts/phase_003/06_historical_replay_and_consolidation/scenario_replay_matrix.md`](concepts/phase_003/06_historical_replay_and_consolidation/scenario_replay_matrix.md) — E-01–E-22 end-to-end replay matrix.
20. [`concepts/phase_003/06_historical_replay_and_consolidation/phase_003_exit_review.md`](concepts/phase_003/06_historical_replay_and_consolidation/phase_003_exit_review.md) — Phase 003 exit decision and Phase 004 handoff.
21. [`concepts/phase_004/README.md`](concepts/phase_004/README.md) — active Phase 004 structure/status.
22. [`concepts/phase_004/01_evidence_sufficiency_and_coverage/README.md`](concepts/phase_004/01_evidence_sufficiency_and_coverage/README.md) — accepted Group 01 evidence applicability/coverage/sufficiency framework.
23. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
24. [`decisions/README.md`](decisions/README.md) — D-001–D-039.
25. [`decisions/phase_003_group_03_runtime_health_and_safeguard.md`](decisions/phase_003_group_03_runtime_health_and_safeguard.md) — D-040–D-046.
26. [`decisions/phase_003_group_04_lineage_investigation_causality.md`](decisions/phase_003_group_04_lineage_investigation_causality.md) — D-047–D-055.
27. [`decisions/pre_group_05_capability_authorization.md`](decisions/pre_group_05_capability_authorization.md) — D-056–D-060.
28. [`decisions/phase_003_group_05_impact_annotation_explanation.md`](decisions/phase_003_group_05_impact_annotation_explanation.md) — D-061–D-070.
29. [`decisions/pre_group_06_execution_gating.md`](decisions/pre_group_06_execution_gating.md) — D-071–D-078.
30. [`decisions/phase_003_group_06_historical_replay_and_exit.md`](decisions/phase_003_group_06_historical_replay_and_exit.md) — D-079–D-088.
31. [`decisions/phase_004_group_01_evidence_sufficiency_and_coverage.md`](decisions/phase_004_group_01_evidence_sufficiency_and_coverage.md) — D-089–D-097.

## Documentation discipline

- Concepts/synchronizations/refinements remain implementation-neutral.
- Phase 004 `REF-###` artifacts define standards over accepted concepts/synchronizations and are not new truth owners.
- Preserve historical decision rationale; add/supersede rather than silently rewrite.
- Synchronization/refinement order never becomes source authority or causation.
- **Evidence sufficiency is conclusion-relative**; bind the target proposition before evaluating adequacy.
- Evidence applicability, bounded coverage, corroboration/conflict, and conclusion sufficiency remain separate.
- Coverage is always scoped to an explicit observation universe/window; never imply global completeness.
- Negative/absence/exclusion conclusions require an adequate opportunity to observe and sufficient bounded coverage.
- Missing telemetry, failed/unavailable queries, restricted evidence, out-of-scope evidence, or unresolved identity/version state are not negative facts.
- Duplicated/common-source telemetry is not independent corroboration merely because it appears in multiple systems.
- Applicable conflicts remain explicit unless an accepted authority rule resolves them; do not use majority vote/source count/synchronization order as hidden authority.
- Do not invent a universal evidence trust/confidence score.
- Evidence sufficiency does not grant disclosure or production-control authority.
- Monitoring Scope, Responsibility Assignment, Policy Context, and Capability Authorization remain distinct.
- Raw-data read, metadata/health analysis, Lineage/RCA, job-operation, safeguard-control, and gate-control/override capabilities remain distinct.
- Denial of direct-data access must not automatically block independently authorized analytical evidence.
- Derived evidence is not automatically unrestricted; apply safe projection/redaction/opacity per capability.
- Restricted evidence is never retrieved merely to summarize it to an unauthorized user.
- **Passive monitoring is non-blocking/out-of-band by default**; monitoring degradation must not delay ungated production jobs.
- Baseline monitoring should prefer framework deployment independent of production ETL repositories/GitHub Actions when platform metadata is sufficient.
- **Execution Gate is explicit opt-in active control**, not an automatic effect of Lineage, schedules, or readiness Assessment.
- Execution Gate start/admission control remains separate from Execution History and Propagation Safeguard output/consumption control.
- `held` is not execution failure; `admitted` is not actual run occurrence; `override` is not readiness.
- Missing gate/readiness evidence is not automatically ready; fallback/timeout/override semantics must be explicit.
- Gate-induced delay remains observable/assessable/Impact evidence.
- Impact candidate/reachability, exposure, downstream effect, consequence, and causal attribution remain distinct.
- `Not exposed` requires sufficient negative evidence; missing telemetry never becomes non-exposure.
- Criticality/policy sensitivity can affect priority/handling but not manufacture actual Impact or compliance consequence.
- Prevented exposure requires active/enforced safeguard evidence plus sufficient negative-consumption coverage.
- Annotation remains attributed human context, not hidden structured truth.
- Explanation consumes only authorized projected evidence and preserves statement-to-basis/epistemic/redaction/control/temporal context.
- **Historical replay uses event/effective time + recorded/knowledge cutoff.**
- Current topology/reference/governance/authorization/control state is not silently projected backward.
- Later evidence can revise retrospective conclusions without rewriting what was known then.
- Actual historical Assessment/claim/control/Explanation is distinct from replay-derived reconstruction.
- Actual gate/safeguard action is not counterfactually replaced by what later evidence suggests should have happened.
- Historical authorization/control state can be reconstructed but cannot bypass current requester authorization.
- Keep examples synthetic; no real PII/PHI/secrets/production values.
- Do not select IAM, graph, event/temporal/ledger, quarantine, scheduler/orchestration, LLM, workflow, or service architecture prematurely.
