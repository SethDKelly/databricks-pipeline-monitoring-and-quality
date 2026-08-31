# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

This file is the **sole living authority for repository phase progression**. Detailed group progress, architecture rationale, scenario reviews and exit conclusions belong in their phase-specific documents and are intentionally not duplicated here.

## Current state

- **Phase 002 — Concept Specifications: COMPLETE with four accepted post-exit addenda.** Current catalog: 24 concepts.
- **Phase 003 — Concept Synchronizations and Ecosystem Scenarios: COMPLETE.** SYN-001–SYN-035 accepted; E-01–E-22 pass.
- **Phase 004 — Evidence, Time, and Causality Refinement: COMPLETE.** REF-001–REF-030 accepted.
- **Phase 005 — Governance, Authority, Semantics, Policy, and Capability Refinement: COMPLETE.** AUTH-001–AUTH-053 final; G07-01–G07-26 pass.
- **Phase 006 — Health, Freshness, Quality, Metrics, and Result-Timing Refinement: COMPLETE.** Groups 01–07 accepted; HLTH-001–HLTH-066 final; H07-01–H07-36 pass.
- **Phase 007 — Lineage, Change, Investigation, Impact, Safeguard, and Execution-Control Refinement: COMPLETE.** Groups 01–09 accepted; OPS-001–OPS-123 final; L01-01–L01-18, C02-01–C02-24, P03-01–P03-30, X04-01–X04-32, I05-01–I05-34, IM06-01–IM06-36, SG07-01–SG07-36, GT08-01–GT08-36 and HR09-01–HR09-36 pass; Phase 007 exit review accepted.
- **Phase 008 — Business Questioning and Explanation: COMPLETE.** Groups 01–08 accepted; EXPL-001–EXPL-160 final; BQ01-01–BQ01-24, AS02-01–AS02-30, HCE03-01–HCE03-36, ICG04-01–ICG04-48, UNC05-01–UNC05-40, AUD06-01–AUD06-44, PMR07-01–PMR07-44 and HCX08-01–HCX08-48 pass; Phase 008 exit review accepted; no EXPL-161 required.
- **Phase 009 — Integration Contracts, Source Authority, and Evidence Availability: COMPLETE.** Groups 01–08 accepted; INTG-001–INTG-270 final; IC01-01–IC01-40, GOV02-01–GOV02-48, RTE03-01–RTE03-54, HME04-01–HME04-56, LIE05-01–LIE05-60, ICE06-01–ICE06-72, EBR07-01–EBR07-64 and XRC08-01–XRC08-64 pass; Phase 009 exit review accepted; no INTG-271 required.
- **Phase 010 — Technical Architecture: COMPLETE.** Groups 01–09 accepted; ARCH-001–ARCH-500 final; AFE01-01–AFE01-60, EPT02-01–EPT02-72, IAD03-01–IAD03-84, AHI04-01–AHI04-96, RHI05-01–RHI05-108, IRE06-01–IRE06-120, ACS07-01–ACS07-120, SSO08-01–SSO08-120 and ACV09-01–ACV09-120 pass; D-1263–D-1700 accepted; Phase 010 exit review accepted; no ARCH-501 required. **Later MVP implementation/validation planning is next.**

The current catalog contains **24 accepted concepts**: the original 20 plus **Propagation Safeguard**, **Capability Authorization**, **Execution Gate**, and **Assertion Authority**.

## Canonical reading order

### Foundation

1. [`../README.md`](../README.md) — project orientation; phase status here supersedes older status-only wording elsewhere.
2. [`foundation/001_product_definition.md`](foundation/001_product_definition.md) — product purpose.
3. [`foundation/002_actors_and_stakeholders.md`](foundation/002_actors_and_stakeholders.md) — actors and stakeholders.
4. [`foundation/003_terminology.md`](foundation/003_terminology.md) — foundational distinctions.
5. [`foundation/004_concept_design_method.md`](foundation/004_concept_design_method.md) — Concept Design method.
6. [`foundation/005_architectural_principles.md`](foundation/005_architectural_principles.md) — architectural constraints.
7. [`foundation/006_security_governance_and_policy_model.md`](foundation/006_security_governance_and_policy_model.md) — security/governance foundation.
8. [`foundation/007_ecosystem_lifecycles.md`](foundation/007_ecosystem_lifecycles.md) — functional lifecycles.
9. [`foundation/008_mvp_boundary.md`](foundation/008_mvp_boundary.md) — initial MVP boundary and proof scenarios.
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — durable phase ownership/sequence; this README remains live status authority.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — open questions.

### Concept and refinement phases

12. [`concepts/README.md`](concepts/README.md) — accepted concept catalog and cross-cutting boundaries.
13. [`concepts/phase_003/README.md`](concepts/phase_003/README.md) — Phase 003 synchronization model.
14. [`concepts/phase_004/README.md`](concepts/phase_004/README.md) — Phase 004 evidence/time/causality refinement.
15. [`concepts/phase_005/README.md`](concepts/phase_005/README.md) — Phase 005 governance/authority refinement.
16. [`concepts/phase_005/07_consolidation_and_exit/phase_005_exit_review.md`](concepts/phase_005/07_consolidation_and_exit/phase_005_exit_review.md) — Phase 005 exit.
17. [`concepts/phase_006/README.md`](concepts/phase_006/README.md) — Phase 006 health/quality model.
18. [`concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md`](concepts/phase_006/07_consolidation_and_exit/phase_006_exit_review.md) — Phase 006 exit.
19. [`concepts/phase_007/README.md`](concepts/phase_007/README.md) — Phase 007 operational/Lineage/Impact/control refinement.
20. [`concepts/phase_007/09_historical_operational_replay_consolidation_exit/phase_007_exit_review.md`](concepts/phase_007/09_historical_operational_replay_consolidation_exit/phase_007_exit_review.md) — Phase 007 exit.
21. [`concepts/phase_008/README.md`](concepts/phase_008/README.md) — Phase 008 business questioning and Explanation.
22. [`concepts/phase_008/08_historical_comparative_explanation_consolidation_exit/phase_008_exit_review.md`](concepts/phase_008/08_historical_comparative_explanation_consolidation_exit/phase_008_exit_review.md) — Phase 008 exit.
23. [`concepts/phase_009/README.md`](concepts/phase_009/README.md) — Phase 009 integration contracts/source authority/evidence availability.
24. [`concepts/phase_009/08_cross_source_coverage_latency_retention_cost_consolidation_exit/phase_009_exit_review.md`](concepts/phase_009/08_cross_source_coverage_latency_retention_cost_consolidation_exit/phase_009_exit_review.md) — Phase 009 exit.
25. [`concepts/phase_009/08_cross_source_coverage_latency_retention_cost_consolidation_exit/residual_gap_register.md`](concepts/phase_009/08_cross_source_coverage_latency_retention_cost_consolidation_exit/residual_gap_register.md) — GAP-009-01–GAP-009-40 architecture input.
26. [`concepts/phase_009/08_cross_source_coverage_latency_retention_cost_consolidation_exit/phase_010_handoff.md`](concepts/phase_009/08_cross_source_coverage_latency_retention_cost_consolidation_exit/phase_010_handoff.md) — Phase 010 incoming architecture contract.

### Technical architecture

27. [`concepts/phase_010/README.md`](concepts/phase_010/README.md) — completed Phase 010 architecture index.
28. [`concepts/phase_010/01_architecture_frame_environment_discovery_decision_criteria/README.md`](concepts/phase_010/01_architecture_frame_environment_discovery_decision_criteria/README.md) — ARCH-001–ARCH-032.
29. [`concepts/phase_010/02_evidence_provenance_temporal_persistence_architecture/README.md`](concepts/phase_010/02_evidence_provenance_temporal_persistence_architecture/README.md) — ARCH-033–ARCH-080.
30. [`concepts/phase_010/03_identity_scope_authority_authorization_disclosure_architecture/README.md`](concepts/phase_010/03_identity_scope_authority_authorization_disclosure_architecture/README.md) — ARCH-081–ARCH-132.
31. [`concepts/phase_010/04_source_acquisition_adapter_synchronization_integration_health_architecture/README.md`](concepts/phase_010/04_source_acquisition_adapter_synchronization_integration_health_architecture/README.md) — ARCH-133–ARCH-190.
32. [`concepts/phase_010/05_runtime_provenance_health_lineage_impact_evidence_architecture/README.md`](concepts/phase_010/05_runtime_provenance_health_lineage_impact_evidence_architecture/README.md) — ARCH-191–ARCH-274.
33. [`concepts/phase_010/06_investigation_reasoning_historical_replay_explanation_architecture/README.md`](concepts/phase_010/06_investigation_reasoning_historical_replay_explanation_architecture/README.md) — ARCH-275–ARCH-350.
34. [`concepts/phase_010/07_execution_gate_propagation_safeguard_active_control_architecture/README.md`](concepts/phase_010/07_execution_gate_propagation_safeguard_active_control_architecture/README.md) — ARCH-351–ARCH-420.
35. [`concepts/phase_010/08_serving_security_deployment_observability_cost_architecture/README.md`](concepts/phase_010/08_serving_security_deployment_observability_cost_architecture/README.md) — ARCH-421–ARCH-500.
36. [`concepts/phase_010/09_architecture_consolidation_validation_exit/README.md`](concepts/phase_010/09_architecture_consolidation_validation_exit/README.md) — Group 09 consolidation and Phase 010 exit.
37. [`concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md`](concepts/phase_010/09_architecture_consolidation_validation_exit/target_reference_architecture.md) — frozen target/reference architecture.
38. [`concepts/phase_010/09_architecture_consolidation_validation_exit/mvp_topology.md`](concepts/phase_010/09_architecture_consolidation_validation_exit/mvp_topology.md) — frozen MVP topology.
39. [`concepts/phase_010/09_architecture_consolidation_validation_exit/scenario_replay_matrix.md`](concepts/phase_010/09_architecture_consolidation_validation_exit/scenario_replay_matrix.md) — ACV09-01–ACV09-120.
40. [`concepts/phase_010/09_architecture_consolidation_validation_exit/phase_010_exit_review.md`](concepts/phase_010/09_architecture_consolidation_validation_exit/phase_010_exit_review.md) — canonical Phase 010 exit review.
41. [`concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md`](concepts/phase_010/09_architecture_consolidation_validation_exit/implementation_handoff.md) — later MVP implementation/validation handoff.

### Reference and decision history

42. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
43. [`reference/authority_vocabulary.md`](reference/authority_vocabulary.md) — authority vocabulary.
44. [`decisions/README.md`](decisions/README.md) — durable decision history.
45. [`decisions/phase_010_group_09_architecture_consolidation_exit.md`](decisions/phase_010_group_09_architecture_consolidation_exit.md) — D-1663–D-1700 and Phase 010 closure.

## Documentation authority discipline

- Current repository phase progression is maintained **only** in `## Current state` above.
- `docs/phase_status.md` is generated from those phase lines by `scripts/check_docs_consistency.py --render` and must match exactly.
- The roadmap owns durable phase sequence, not live status.
- Phase-specific READMEs may state their own group/phase-local status.
- Historical files may preserve status-at-time-of-writing when clearly historical.
- Living indexes/guidance should reference this current-state section rather than duplicate a separately maintained current/next declaration.
- Detailed scenario/result/rationale text belongs in phase-specific documents rather than this index.

## Cross-cutting documentation discipline

- Concepts/refinements remain distinct from architecture and implementation.
- Synchronization order is never authority or causality.
- Evidence sufficiency is conclusion-relative; missing/restricted/unavailable evidence is not negative truth.
- Baseline is descriptive; Expectation is normative.
- Lineage reachability is not encounter/exposure/Impact/causality.
- Investigation/lead/localization is not causal confirmation.
- Assertion Authority, Capability Authorization, evidence sufficiency and enforcement remain independent.
- Current state is not projected backward into historical state.
- Retained authentic communication is distinct from reconstruction.
- Derived graph/search/vector/cache/model/UI state is not canonical truth.
- Gate configuration/readiness/decision/delivery/enforcement/execution remain distinct.
- Safeguard configuration/enforcement/prevention/release/recovery remain distinct.
- One global confidence/health/Impact/control/integration/architecture score is not accepted.

For full semantics and architecture constraints, follow the phase-specific contract/exit documents above rather than relying on this index as a substitute.
