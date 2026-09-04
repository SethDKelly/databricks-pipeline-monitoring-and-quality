# Monitoring Scope

**Canonical key:** `concept.monitoring_scope`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.monitoring_scope`

**Owns current question:** Which identified entities are within DMTZ monitoring responsibility for a given effective time?

**Stable IDs:** N/A

## Current semantics

Monitoring Scope records provenance-bearing inclusion or exclusion assertions for an Entity Identity. State includes participation disposition, effective time, source/actor and authority context, optional reason, correction/supersession history, and unresolved conflict. A missing assertion resolves to `unknown`; it is not an exclusion.

## Actions

- `include` — assert monitoring responsibility prospectively/effectively.
- `exclude` — assert intentional exclusion without erasing known evidence or relationships.
- `resolveAt` — return included, excluded, unknown, conflicting, unauthorized, or unavailable for the relevant time.

## Invariants / boundaries

- Monitoring Scope is monitoring responsibility, not ecosystem existence, data access, Capability Authorization, Assertion Authority, or implementation topology.
- Scope applies only to identified entities; unresolved identity is never guessed.
- A known entity may be excluded or have unknown scope.
- Scope never propagates implicitly through Lineage, repository membership, containment, or pipeline boundaries.
- Inclusion does not guarantee evidence exists, is fresh, healthy, complete, or visible.
- Exclusion does not erase historical evidence or authorized contextual reasoning.
- Scope changes are time-aware and non-rewriting.

## Ambiguity / evidence

Conflicting assertions remain explicit until applicable authority resolves them. A restricted boundary may be exposed opaquely without disclosing the entity identity or exclusion reason.

## Synchronizations / related canonical resources

Entity Identity supplies the referent. Observation may use scope as evidence-coverage context; Lineage can cross scope boundaries; Investigation and Explanation may expose incomplete monitoring coverage subject to authorization.

## Non-goals

Entity discovery, authorization, health definition, Lineage-edge scoping, telemetry guarantees, or modifying pipelines/assets.

## Provenance

- `docs/concepts/phase_002/01_scope_and_identity/monitoring_scope.md`
- `docs/concepts/phase_003/01_subject_scope_and_context/`
