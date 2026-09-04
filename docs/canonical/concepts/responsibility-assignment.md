# Responsibility Assignment

**Canonical key:** `concept.responsibility_assignment`

**Kind:** CONCEPT

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `concept.responsibility_assignment`

**Owns current question:** Who bears a named responsibility for an identified subject, context, and time?

**Stable IDs:** N/A

## Current semantics

Responsibility Assignment records subject, responsible party, responsibility type/scope, effective interval, provenance, Assertion Authority context, revisions/transfers/endings, and conflicts. Technical ownership, business accountability, stewardship, security/privacy, operational/on-call, and platform responsibility remain independently resolvable.

## Actions

- `assign` — record a named responsibility.
- `transfer` — prospectively replace an assignee while preserving history.
- `end` — terminate an assignment without inventing a successor.
- `resolveAt` — return assignments, unknown, explicitly unassigned, conflicting, unauthorized, or unavailable.

## Invariants / boundaries

- Responsibility ≠ Assertion Authority ≠ Capability Authorization.
- A responsible party is not automatically authoritative for semantics, Classification, Policy Context, Expectations, metrics, schema rules, or controls.
- Missing assignment evidence is `unknown`; `unassigned` requires an explicit authoritative assertion.
- No responsibility inheritance is implicit from repository/container/domain/pipeline/Lineage relationships.
- Repository activity, source ownership, creator identity, or on-call membership may be evidence but do not manufacture authoritative responsibility.
- Current assignments do not overwrite historical assignments.

## Ambiguity / evidence

Co-authoritative conflicting assignments remain conflict. Safe disclosure may expose team-level/opaque contacts instead of restricted individuals.

## Synchronizations / related canonical resources

Entity Identity supplies subject; Assertion Authority determines standing; Investigation/Impact use contacts for follow-up; Explanation may expose authorized responsibility context.

## Non-goals

Access grants, semantic/classification/policy truth, universal authority, ticket assignment, or inferred ownership from activity/topology.

## Provenance

- `docs/concepts/phase_002/02_semantics_governance_policy/responsibility_assignment.md`
- `docs/concepts/phase_005/02_semantic_responsibility_classification_policy_criticality_governance/`
