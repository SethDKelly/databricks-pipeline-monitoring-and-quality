# Annotation

**Canonical key:** `concept.annotation`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.annotation`

**Owns current question:** What attributed human context/commentary was attached to a defined referent, and what is its revision/dispute/withdrawal state?

**Stable IDs:** N/A

## Current semantics

Annotation owns human-authored content/context, referent, author, recorded/effective/context time, visibility/sensitivity, revision history, and dispute/withdrawal state.

## Actions

- `add` — attach attributed human context.
- `revise` — preserve a traceable material revision.
- `withdraw` — end endorsement/applicability without deleting history.
- `dispute` — record contestation while retaining both statements.

## Invariants / boundaries

- Annotation is human context, not source Observation, Causal Claim confirmation, Change Intent, Expectation, Responsibility Assignment, Classification, Policy Context, or shadow evidence/authority store.
- Human title/role alone does not make note content universally authoritative.
- Annotation cannot mutate source evidence.
- When note content should become structured operational truth, the owning concept must record it separately with its own provenance/authority semantics.
- Revision/dispute/withdrawal are non-rewriting; absence of Annotation has no evidentiary meaning.

## Ambiguity / evidence

Annotations may be mistaken, stale, disputed, withdrawn, or contradicted; those states remain explicit.

## Synchronizations / related canonical resources

Investigation can collect notes; Causal Claim may cite them as attributed human context; Impact may reference business context; Explanation may surface them clearly labeled; structured assertions route to their respective concept owners.

## Non-goals

Causal confirmation, planned-change registration, normative criteria, source-evidence mutation, responsibility assignment, or universal authority resolution.

## Provenance

- `docs/concepts/phase_002/05_investigation_impact_explanation/annotation.md`
- `docs/concepts/phase_003/05_impact_annotation_and_explanation/`
