# HLTH-030 — Normative Criterion Binding & Evaluation Basis

## Purpose

Define the functional identity of a normative health criterion before evaluation.

## Rule

A normative criterion binds, where material:

- subject and assessed dimension/property;
- exact metric/check/structural definition and version;
- applicable grain, population, window and consumer/context;
- comparator/operator and boundary semantics;
- units, denominator and directionality;
- effective interval and applicable Expectation version;
- any required reference basis such as an explicitly named Baseline/version or other governed reference;
- evidence-suitability requirements needed to support a conclusion.

`Expectation exists` is not equivalent to `Expectation can be evaluated now`. Assessment requires both an applicable criterion and sufficiently suitable current evidence.

A criterion may be absolute, relative, structural, categorical, temporal or another explicitly defined form without creating a new Threshold concept.

## Invariants

- Expectation owns the normative rule; Assessment owns the evaluation result.
- Metric/check extraction success does not establish criterion satisfaction.
- Missing criterion semantics are unresolved rather than guessed.
- A criterion never inherits its unit, denominator, direction, inclusivity or reference basis merely from a display label.
- Historical evaluation resolves the criterion version applicable at the evaluated time/knowledge cut.

## Non-goals

- choosing DQX/SQL/Metric View syntax;
- defining authority to establish the criterion;
- overall/composite health.