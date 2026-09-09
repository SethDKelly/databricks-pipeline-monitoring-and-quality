# EXPL-017 — Answer-Bearing, Contextual & Limitation Statement Roles

**Status:** Accepted — Phase 008 Group 02

## Requirement

Allow an Explanation to distinguish presentation roles without creating new truth categories:

- **answer-bearing statement** — directly addresses a bounded question/subquestion;
- **context statement** — supplies meaning, scope, responsibility, timing or other relevant context needed to interpret answer-bearing statements;
- **limitation statement** — communicates evidence, ambiguity, authorization, coverage, temporal or interpretive constraints material to the answer.

The role is Explanation metadata. The underlying proposition retains its source concept and epistemic type.

## Examples

`Completeness failed` can be answer-bearing; `Data Platform is responsible` can be context; `consumer telemetry is incomplete` can be a limitation. Responsibility does not become evidence that completeness failed, and the limitation does not become proof that no consumer was exposed.

## Invariants

Context/limitation role ≠ source truth ownership. A limitation that materially bounds a conclusion cannot be silently omitted merely because it is not the headline answer.
