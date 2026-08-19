# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Current state

**Phase 002 — Concept Specifications is complete.** All five groups and 20 retained concepts are accepted.

The next planned work is **Phase 003 — Concept Synchronizations and Ecosystem Scenarios**, which has not yet started.

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
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — phased path; Phase 003 is next.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved decisions that must not be silently chosen.
12. [`concepts/README.md`](concepts/README.md) — accepted 20-concept catalog.
13. [`concepts/concept_template.md`](concepts/concept_template.md) — concept specification shape.
14. [`concepts/phase_002/README.md`](concepts/phase_002/README.md) — completed Phase 002 review, exit gate, and synchronization candidates for Phase 003.
15. [`reference/glossary.md`](reference/glossary.md) — canonical vocabulary.
16. [`decisions/README.md`](decisions/README.md) — durable decision history.

## Document statuses

- **Foundation** — accepted project principle/product boundary.
- **Accepted** — reviewed concept/decision currently in force.
- **Candidate** — plausible choice requiring review.
- **Deferred** — intentionally postponed.
- **Open** — unresolved; never treat as decided.
- **Rejected** — explicitly not selected, with rationale retained.

## Directories

### `foundation/`
Accepted product foundation and the roadmap toward technical design.

### `concepts/`
Concept Design specifications and, in Phase 003, detailed synchronizations/scenarios. Concepts describe functionality, not implementation modules.

### `planning/`
Earlier thematic discovery notes. They remain useful inputs, but accepted foundation/concept/decision documents take precedence when wording conflicts.

### `reference/`
Canonical shared vocabulary/reference material.

### `decisions/`
Explicit decisions, reversals, and unresolved choices. Major design choices must not exist only in chat history.

## Documentation discipline

- Prefer one canonical definition over subtly different duplicates.
- Preserve historical decision rationale; supersede/correct rather than silently rewrite meaning.
- Label implementation ideas as candidates until technical architecture approves them.
- Keep examples synthetic; no real PII, PHI, credentials, secrets, or production values.
- Preserve uncertainty and authorization limitations explicitly.
