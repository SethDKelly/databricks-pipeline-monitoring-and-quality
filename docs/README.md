# Documentation Index

The `docs/` tree is the system of record for product and design decisions in this repository.

## Reading order

For the current Phase 002 work, read:

1. [`../README.md`](../README.md) — project orientation and product thesis.
2. [`foundation/001_product_definition.md`](foundation/001_product_definition.md) — product purpose, capabilities, goals, and non-goals.
3. [`foundation/002_actors_and_stakeholders.md`](foundation/002_actors_and_stakeholders.md) — human and system actors.
4. [`foundation/003_terminology.md`](foundation/003_terminology.md) — foundational vocabulary and distinctions.
5. [`foundation/004_concept_design_method.md`](foundation/004_concept_design_method.md) — mandatory Concept Design method.
6. [`foundation/005_architectural_principles.md`](foundation/005_architectural_principles.md) — principles that later architecture must satisfy.
7. [`foundation/006_security_governance_and_policy_model.md`](foundation/006_security_governance_and_policy_model.md) — security/privacy/governance model.
8. [`foundation/007_ecosystem_lifecycles.md`](foundation/007_ecosystem_lifecycles.md) — product lifecycles relevant to this domain.
9. [`foundation/008_mvp_boundary.md`](foundation/008_mvp_boundary.md) — initial MVP boundary.
10. [`foundation/009_initial_roadmap.md`](foundation/009_initial_roadmap.md) — phased path from product discovery to implementation.
11. [`foundation/010_open_questions.md`](foundation/010_open_questions.md) — unresolved decisions.
12. [`concepts/README.md`](concepts/README.md) — concept catalog and Phase 001 discovery seed.
13. [`concepts/concept_template.md`](concepts/concept_template.md) — required concept specification shape.
14. [`concepts/phase_002/README.md`](concepts/phase_002/README.md) — active grouped Phase 002 plan and review order.

## Document statuses

Documents should use these terms consistently:

- **Foundation** — currently accepted project principle or product boundary.
- **Candidate** — plausible design choice requiring discovery or review.
- **Deferred** — intentionally postponed to a later phase.
- **Open** — unresolved and should not be treated as decided.
- **Rejected** — considered and explicitly not selected; rationale should be retained.

## Directories

### `foundation/`

The product-level foundation. It should stay implementation-neutral until the project deliberately enters technical design.

### `concepts/`

Concept Design specifications and synchronizations. Concepts describe user-visible/system-visible functionality, not implementation modules.

### `planning/`

Earlier thematic discovery notes. They remain useful inputs, but if a planning note conflicts with an accepted foundation document, the foundation document is authoritative.

### `reference/`

Shared vocabulary and reference material.

### `decisions/`

Explicit decisions, reversals, and unresolved choices. Major design choices should not exist only in chat history.

## Documentation discipline

- Prefer one stable definition over repeated subtly different definitions.
- Link to authoritative terms rather than redefining them in every file.
- Label implementation ideas as candidates until a technical-design phase approves them.
- Keep example data synthetic; do not place real PII, PHI, credentials, secrets, or production data in documentation.
- Record uncertainty explicitly.
