# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios is active.** Phase 002 is complete with all 20 retained concepts accepted.

**Phase 003 Group 01 — Subject, Scope & Governance Context is accepted. Group 02 — Planned Change & Reference Transition is next.**

## Reading order

1. [`../README.md`](../README.md) — project orientation and current design state.
2. [`foundation/001_product_definition.md`](foundation/001_product_definition.md) — product purpose/capabilities/non-goals.
3. [`foundation/002_actors_and_stakeholders.md`](foundation/002_actors_and_stakeholders.md) — human/system actors.
4. [`foundation/003_terminology.md`](foundation/003_terminology.md) — foundational vocabulary/distinctions.
5. [`foundation/004_concept_design_method.md`](foundation/004_concept_design_method.md) — mandatory Concept Design method.
6. [`foundation/005_architectural_principles.md`](foundation/005_architectural_principles.md) — constraints future architecture must preserve.
7. [`foundation/006_security_governance_and_policy_model.md`](foundation/006_security_governance_and_policy_model.md) — security/privacy/governance foundation.
8. [`foundation/007_ecosystem_lifecycles.md`](foundation/007_ecosystem_lifecycles.md) — functional lifecycles.
9. [`foundation/008_mvp_boundary.md`](foundation/008_mvp_boundary.md) — MVP proof boundary.
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — phased path and active Phase 003 position.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved decisions that must not be silently chosen.
12. [`concepts/README.md`](concepts/README.md) — accepted 20-concept catalog.
13. [`concepts/concept_template.md`](concepts/concept_template.md) — concept specification shape.
14. [`concepts/phase_002/README.md`](concepts/phase_002/README.md) — completed Phase 002 review/exit gate.
15. [`concepts/phase_003/README.md`](concepts/phase_003/README.md) — active synchronization groups, method, scenarios, and exit gate.
16. [`concepts/phase_003/synchronization_template.md`](concepts/phase_003/synchronization_template.md) — synchronization specification checklist.
17. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
18. [`decisions/README.md`](decisions/README.md) — durable decision history.

## Document statuses

- **Foundation** — accepted project principle/product boundary.
- **Accepted** — reviewed concept/synchronization/decision currently in force.
- **Candidate** — plausible choice requiring review.
- **Planned** — scheduled Phase 003 review group not yet reviewed.
- **Deferred** — intentionally postponed.
- **Open** — unresolved; never treat as decided.
- **Rejected** — explicitly not selected, with rationale retained.

## Directories

### `foundation/`
Accepted product foundation and roadmap toward technical design.

### `concepts/`
Accepted concept specifications plus active Phase 003 synchronization contracts/scenarios. Concepts and synchronizations describe functionality, not implementation modules/workflows.

### `planning/`
Earlier thematic discovery notes. Accepted foundation/concept/synchronization/decision documents take precedence when wording conflicts.

### `reference/`
Canonical shared vocabulary/reference material.

### `decisions/`
Explicit decisions, reversals, and unresolved choices. Major design choices must not exist only in chat history.

## Documentation discipline

- Prefer one canonical definition over subtly different duplicates.
- Preserve historical decision rationale; supersede/correct rather than silently rewrite meaning.
- Synchronization specifications must state trigger, participating concept actions, partial ordering, failure/ambiguity propagation, time/provenance, security, invariants, scenarios, and non-goals.
- Never turn synchronization ordering into source authority or causation.
- Label implementation ideas as candidates until technical architecture approves them.
- Keep examples synthetic; no real PII, PHI, credentials, secrets, or production values.
- Preserve uncertainty and authorization limitations explicitly.
