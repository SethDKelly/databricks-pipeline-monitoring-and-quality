# EXPL-013 — Material Answer Statement Proposition Identity

**Status:** Accepted — Phase 008 Group 02

## Requirement

Treat each material answer statement as a bounded proposition independent of its rendered wording.

A statement identity preserves, when material:

- source-owned conclusion/predicate;
- resolved subject/entity;
- applicable environment/version/run/consumer/population/profile/path/control scope;
- event/effective-time point or window;
- knowledge-cut/current-retrospective perspective;
- source truth owner or explicit derived-statement classification.

Two sentences with different wording may represent the same answer proposition. Identical wording may represent different propositions when subject, scope or temporal perspective differs.

## Invariants

- rendered prose ≠ proposition identity;
- answer statement ≠ independent source truth;
- summary/detail rewording does not create a new substantive proposition when the proposition remains unchanged;
- materially changed scope, predicate, polarity or temporal perspective creates a different statement proposition.

## Example

`Pipeline C is late` for the current production cycle and `Pipeline C was late at 10:00 as known at 10:05` are not the same material statement even if a UI renders both as `C was late`.
