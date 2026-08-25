# OPS-084 — Historical Impact Replay, Correction & Restricted Projection

**Status:** Accepted — Phase 007 Group 06

## Purpose

Preserve bitemporal Impact history and authorization-safe downstream analysis as encounter/effect/consequence evidence arrives or changes.

## Contract

Historical Impact reconstruction preserves, where material:

- originating affected-state interval;
- candidate/path state effective at the relevant time;
- encounter opportunity and encounter event/interval;
- source evidence availability and framework knowledge time;
- effect/consequence event time and later discovery time;
- correction/supersession/re-evaluation history;
- audience authorization/disclosure projection.

Late query/refresh/cache/use evidence may change today's retrospective exposure or first-encounter result without rewriting what responders knew then.

Restricted consumer/path/use evidence may yield an authorized coarse result only when the underlying internal conclusion is actually supported. Redaction cannot strengthen `unknown` into `not exposed` or `exposed`.

## Invariants

- current retrospective Impact ≠ incident-time as-known Impact.
- late evidence ≠ evidence known then.
- restricted ≠ absent.
- safe projection ≠ stronger epistemic state.
- correction preserves prior knowledge/action history.
