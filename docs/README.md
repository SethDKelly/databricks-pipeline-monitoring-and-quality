# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

**Phase 003 is active. Groups 01–05 are accepted. Group 06 — Historical Replay & Phase 003 Consolidation is next.**

The original Phase 002 catalog contained 20 concepts. Two post-exit addenda are accepted:

1. **Propagation Safeguard**;
2. **Capability Authorization**.

The current catalog contains **22 accepted concepts**. Phase 003 now contains accepted SYN-001–SYN-031.

## Reading order

1. [`../README.md`](../README.md) — project orientation/current state.
2. [`foundation/001_product_definition.md`](foundation/001_product_definition.md) — product purpose.
3. [`foundation/002_actors_and_stakeholders.md`](foundation/002_actors_and_stakeholders.md) — actors.
4. [`foundation/003_terminology.md`](foundation/003_terminology.md) — foundational distinctions.
5. [`foundation/004_concept_design_method.md`](foundation/004_concept_design_method.md) — Concept Design method.
6. [`foundation/005_architectural_principles.md`](foundation/005_architectural_principles.md) — architectural constraints.
7. [`foundation/006_security_governance_and_policy_model.md`](foundation/006_security_governance_and_policy_model.md) — security/governance/authorization foundation.
8. [`foundation/007_ecosystem_lifecycles.md`](foundation/007_ecosystem_lifecycles.md) — functional lifecycles.
9. [`foundation/008_mvp_boundary.md`](foundation/008_mvp_boundary.md) — MVP boundary.
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — roadmap/current phase.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved choices.
12. [`concepts/README.md`](concepts/README.md) — 22-concept catalog.
13. [`concepts/phase_002/README.md`](concepts/phase_002/README.md) — original concept review + addenda history.
14. [`concepts/phase_002/addenda/`](concepts/phase_002/addenda/) — Propagation Safeguard and Capability Authorization.
15. [`concepts/phase_003/README.md`](concepts/phase_003/README.md) — synchronization phase state and E-01–E-20.
16. [`concepts/phase_003/05_impact_annotation_and_explanation/README.md`](concepts/phase_003/05_impact_annotation_and_explanation/README.md) — accepted Group 05 downstream Impact/Annotation/Explanation synchronizations.
17. [`concepts/phase_003/06_historical_replay_and_consolidation/README.md`](concepts/phase_003/06_historical_replay_and_consolidation/README.md) — next Group 06 consolidation handoff.
18. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
19. [`decisions/README.md`](decisions/README.md) — D-001–D-039.
20. [`decisions/phase_003_group_03_runtime_health_and_safeguard.md`](decisions/phase_003_group_03_runtime_health_and_safeguard.md) — D-040–D-046.
21. [`decisions/phase_003_group_04_lineage_investigation_causality.md`](decisions/phase_003_group_04_lineage_investigation_causality.md) — D-047–D-055.
22. [`decisions/pre_group_05_capability_authorization.md`](decisions/pre_group_05_capability_authorization.md) — D-056–D-060.
23. [`decisions/phase_003_group_05_impact_annotation_explanation.md`](decisions/phase_003_group_05_impact_annotation_explanation.md) — D-061–D-070.

## Documentation discipline

- Concepts/synchronizations remain implementation-neutral.
- Preserve historical decision rationale; add/supersede rather than silently rewrite.
- Synchronization order never becomes source authority or causation.
- Monitoring Scope, Responsibility Assignment, Policy Context, and Capability Authorization remain distinct.
- Raw-data read, metadata/health analysis, Lineage/RCA, job-operation, and safeguard-control capabilities remain distinct.
- Denial of direct-data access must not automatically block independently authorized analytical evidence.
- Derived evidence is not automatically unrestricted; apply safe projection/redaction/opacity per capability.
- Restricted evidence is never retrieved merely to summarize it to an unauthorized user.
- Impact candidate/reachability, exposure, downstream effect, consequence, and causal attribution remain distinct.
- `Not exposed` requires sufficient negative evidence; missing telemetry never becomes non-exposure.
- Criticality/policy sensitivity can affect priority/handling but not manufacture actual Impact or compliance consequence.
- Prevented exposure requires active/enforced safeguard evidence plus sufficient negative-consumption coverage.
- Annotation remains attributed human context, not hidden structured truth.
- Explanation consumes only authorized projected evidence and preserves statement-to-basis/epistemic/redaction context.
- Historical authorization can be reconstructed but cannot bypass current requester authorization.
- Keep examples synthetic; no real PII/PHI/secrets/production values.
- Do not select IAM, graph, event/ledger, quarantine, LLM, workflow, or service architecture prematurely.
