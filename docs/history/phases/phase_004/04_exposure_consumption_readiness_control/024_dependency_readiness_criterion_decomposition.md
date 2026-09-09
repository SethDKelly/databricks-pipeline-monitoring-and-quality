# REF-024 — Dependency Readiness Criterion Decomposition

**Status:** Accepted — Phase 004 Group 04

## Purpose

Define readiness as satisfaction of an explicit downstream prerequisite criterion rather than a vague global statement that an upstream pipeline is `ready` or `healthy`.

## Bound readiness proposition

A readiness evaluation identifies:

- the Execution Gate/downstream execution opportunity or other readiness context;
- the prerequisite subject(s);
- the applicable criterion/profile/version;
- the required event/window/current-cycle context;
- the required evidence cut and evaluation time.

## Criterion dimensions

A readiness criterion may require one or more explicit predicates, such as:

- qualifying upstream execution completion;
- qualifying output existence;
- expected output identity/version;
- current-cycle/currentness evidence;
- freshness relative to an applicable requirement;
- publication/availability through a required boundary;
- a named quality/Assessment condition **only when the gate criterion explicitly requires it**;
- another accepted prerequisite condition.

These dimensions are not universally required and are not interchangeable.

## Rules

- `Upstream job succeeded` proves only the execution proposition it actually evidences; it is not global readiness.
- If a required predicate is sufficiently evidenced false, the criterion is not satisfied.
- If a required predicate cannot be resolved because evidence is unknown/conflicting/unavailable, readiness remains unknown/conflicting/unavailable unless the criterion itself defines another logical result. A control fallback may act on that uncertainty but does not convert it into `ready`.
- Satisfying a readiness criterion does not imply every upstream quality/health dimension is healthy.
- A criterion that requires only execution completion may legitimately resolve ready while later Metric View/DQ evidence remains pending; that does not promote the broader health state.
- Criterion changes are time/version aware and are not projected backward into historical decisions.

## Authorization

An analyst may be allowed to see `prerequisite ready/not ready/unknown` while some predicate details remain restricted. The internal evidence standard still must be satisfied.

## Non-goals

- deciding which gate criteria are appropriate for each pipeline;
- defining final freshness/quality thresholds;
- choosing scheduler/orchestrator implementation;
- creating one universal readiness formula.
