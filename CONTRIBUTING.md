# Contributing

## Current phase and contribution scope

The canonical repository phase status is declared in [`docs/README.md#current-state`](docs/README.md#current-state).

This file intentionally does **not** duplicate the current or next phase number. Before contributing, read the canonical current-state section and the corresponding phase README under `docs/concepts/`.

Contributions must stay within the boundary of the currently active/planned phase. Do not advance architecture or implementation earlier than the canonical phase documents permit.

## Durable contribution rules

- preserve accepted Concept Design ownership and boundaries unless a concrete scenario requires an explicit reopening;
- refine documentation, scenarios, terminology, governance, evidence, health, Lineage, change, Investigation, Impact, safeguard, gate, or other semantics only within the current phase's declared scope;
- preserve historical rationale and use explicit supersession rather than silently rewriting accepted decisions;
- keep implementation choices out of functional-design phases unless the current phase explicitly authorizes technical selection;
- do not treat synchronization order, repository ownership, source availability, platform identity, or implementation convenience as authority or causation;
- record unresolved questions, rejected alternatives, and accepted decisions in the appropriate documentation/decision artifacts;
- run `python3 scripts/check_docs_consistency.py` when changing phase-status, roadmap, contributor, agent, or living index documentation.

## Design method

All functional design follows Daniel Jackson's Concept Design approach described in `docs/foundation/004_concept_design_method.md`.

Before proposing a concept, make sure it has a clear purpose and operational principle and is not merely a vendor feature or implementation component.

## Documentation authority

`docs/README.md#current-state` is the sole living declaration of repository phase progression. Phase-specific README files may describe their own internal group status. Historical documents may retain status-at-time-of-writing language when clearly labeled as historical.

Living indexes, contributor instructions, and current-state guidance should reference canonical phase status rather than maintain independent phase declarations.

## Security and examples

Never commit secrets, credentials, production data, or real PII/PHI. Use synthetic examples. Policy classifications should be described precisely and must not be presented as compliance certifications.
