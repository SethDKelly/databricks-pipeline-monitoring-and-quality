# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

**Phase 003 is active. Groups 01–04 are accepted. Group 05 — Downstream Impact, Annotation & Explanation is next and has not started.**

The original Phase 002 catalog contained 20 concepts. Two post-exit addenda are now accepted:

1. **Propagation Safeguard**;
2. **Capability Authorization**.

The current catalog contains **22 accepted concepts**.

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
15. [`concepts/phase_003/README.md`](concepts/phase_003/README.md) — synchronization phase state.
16. [`concepts/phase_003/05_impact_annotation_and_explanation/README.md`](concepts/phase_003/05_impact_annotation_and_explanation/README.md) — next Group 05 handoff; not started.
17. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
18. [`decisions/README.md`](decisions/README.md) — D-001–D-039.
19. [`decisions/phase_003_group_03_runtime_health_and_safeguard.md`](decisions/phase_003_group_03_runtime_health_and_safeguard.md) — D-040–D-046.
20. [`decisions/phase_003_group_04_lineage_investigation_causality.md`](decisions/phase_003_group_04_lineage_investigation_causality.md) — D-047–D-055.
21. [`decisions/pre_group_05_capability_authorization.md`](decisions/pre_group_05_capability_authorization.md) — D-056–D-060.

## Documentation discipline

- Concepts/synchronizations remain implementation-neutral.
- Preserve historical decision rationale; add/supersede rather than silently rewrite.
- Synchronization order never becomes source authority or causation.
- Monitoring Scope, Responsibility Assignment, Policy Context, and Capability Authorization remain distinct.
- Raw-data read, metadata/health analysis, Lineage/RCA, job-operation, and safeguard-control capabilities remain distinct.
- Denial of direct-data access must not automatically block independently authorized analytical evidence.
- Derived evidence is not automatically unrestricted; apply safe projection/redaction/opacity per capability.
- Restricted evidence is never retrieved merely to summarize it to an unauthorized user.
- Keep examples synthetic; no real PII/PHI/secrets/production values.
- Do not select IAM, graph, event/ledger, quarantine, LLM, workflow, or service architecture prematurely.
