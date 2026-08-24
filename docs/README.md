# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is complete. Phase 004 — Evidence, Time, and Causality Refinement is active. Groups 01–03 are accepted; Group 04 — Exposure, Consumption, Readiness & Control Evidence is next.**

The original Phase 002 catalog contained 20 concepts. Three post-exit addenda are accepted:

1. **Propagation Safeguard**;
2. **Capability Authorization**;
3. **Execution Gate**.

The current catalog contains **23 accepted concepts**. Phase 003 contains accepted **SYN-001–SYN-035** and E-01–E-22 pass the Group 06 replay/consolidation review. Phase 004 contains accepted **REF-001–REF-020** through Groups 01–03.

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
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — roadmap/current phase, including progressive monitoring/RCA timing handoffs.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved choices, including concrete monitoring-result availability/latency targets and later authority/integration questions.
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
23. [`concepts/phase_004/02_event_time_knowledge_cut_and_correction/README.md`](concepts/phase_004/02_event_time_knowledge_cut_and_correction/README.md) — accepted Group 02 temporal evidence, progressive analytical availability, correction, and reconstruction framework.
24. [`concepts/phase_004/03_causal_epistemics_confirmation/README.md`](concepts/phase_004/03_causal_epistemics_confirmation/README.md) — accepted Group 03 causal epistemics/confirmation/multiple-contributor framework.
25. [`concepts/phase_004/04_exposure_consumption_readiness_control/README.md`](concepts/phase_004/04_exposure_consumption_readiness_control/README.md) — next Group 04 handoff; not started.
26. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
27. [`decisions/README.md`](decisions/README.md) — D-001–D-039.
28. [`decisions/phase_003_group_03_runtime_health_and_safeguard.md`](decisions/phase_003_group_03_runtime_health_and_safeguard.md) — D-040–D-046.
29. [`decisions/phase_003_group_04_lineage_investigation_causality.md`](decisions/phase_003_group_04_lineage_investigation_causality.md) — D-047–D-055.
30. [`decisions/pre_group_05_capability_authorization.md`](decisions/pre_group_05_capability_authorization.md) — D-056–D-060.
31. [`decisions/phase_003_group_05_impact_annotation_explanation.md`](decisions/phase_003_group_05_impact_annotation_explanation.md) — D-061–D-070.
32. [`decisions/pre_group_06_execution_gating.md`](decisions/pre_group_06_execution_gating.md) — D-071–D-078.
33. [`decisions/phase_003_group_06_historical_replay_and_exit.md`](decisions/phase_003_group_06_historical_replay_and_exit.md) — D-079–D-088.
34. [`decisions/phase_004_group_01_evidence_sufficiency_and_coverage.md`](decisions/phase_004_group_01_evidence_sufficiency_and_coverage.md) — D-089–D-097.
35. [`decisions/phase_004_group_02_time_knowledge_correction.md`](decisions/phase_004_group_02_time_knowledge_correction.md) — D-098–D-110.
36. [`decisions/phase_004_group_03_causal_epistemics_confirmation.md`](decisions/phase_004_group_03_causal_epistemics_confirmation.md) — D-111–D-123.

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
- **Event/effective time, source availability, framework knowledge time, and derived evaluation time remain distinct.**
- Source availability does not imply framework knowledge; current retrieval of an old source fact does not backdate knowledge.
- `Known by`, `learned after`, `not recorded by`, `not known by`, and `not available by` have different evidence standards.
- Monitoring/reasoning results may mature progressively from immediate operational validation through enriched health, RCA, and post-operations review.
- A faster narrow result must not be promoted into broader health/causal truth while slower evidence is pending.
- Concrete monitoring-result latency objectives remain deferred to Phases 006/009/010/011.
- Late evidence, source correction, independent conflict, reinterpretation, and later authority resolution remain distinct.
- Dependent reevaluation is basis/materiality driven; closed Investigations can become review/reopen candidates without automatic reopening.
- Actual historical state requires evidence it existed then; otherwise replay is reconstructed.
- Causal Claim status vocabulary is `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`.
- `Rejected` requires sufficient contradiction/exclusion evidence; it is not synonymous with no support or lower rank.
- `Confirmed` is a separate claim-specific confirmation gate, not `strongly supported` or `leading hypothesis`.
- Confirmation requires an explicit profile/standard, evidence across required dimensions, material contradiction/alternative review, sufficient negative-evidence coverage where relied upon, resolved confirmation authority/capability, and provenance-bearing confirmation action.
- Phase 004 does not assign confirmation authority; neither a human title nor automated process can self-authorize confirmation.
- Multiple compatible causal contributors can coexist; never force one root cause.
- `Primary` is a comparative causal-role claim and requires comparative evidence; qualitative roles never imply percentage attribution.
- RCA may mature progressively; speed or duration never upgrades causal status by itself.
- Confirmed claims remain challengeable by materially new evidence while historical confirmation remains reconstructable.
- Evidence sufficiency does not grant disclosure or production-control authority.
- Monitoring Scope, Responsibility Assignment, Policy Context, and Capability Authorization remain distinct.
- Raw-data read, metadata/health analysis, Lineage/RCA, job-operation, safeguard-control, gate-control/override, and causal-confirmation capabilities remain distinct.
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
- Do not select IAM, graph, event/temporal/ledger, quarantine, scheduler/orchestration, causal algorithm/LLM, workflow, or service architecture prematurely.
