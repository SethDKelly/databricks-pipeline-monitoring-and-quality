# HLTH-035 — Normative Assessment Result Vocabulary & Basis Separation

## Purpose

Define a minimal basis-specific normative result vocabulary without creating a universal health score.

## Rule

For one bound normative criterion, Assessment can express at least:

- **meets** — sufficient applicable evidence supports criterion satisfaction;
- **violates** — sufficient applicable evidence supports criterion violation;
- **indeterminate / insufficient evidence** — applicable criterion exists but evidence cannot support either conclusion;
- **conflicting** — applicable rule/evidence conflict prevents a resolved conclusion;
- **unavailable** — material evidence/reference/evaluation source is unavailable;
- **not applicable** — criterion does not apply to the bound subject/context/time.

Additional metadata can separately represent warning/proximity, waiver/disposition, severity/priority, descriptive Baseline comparison and authorization/disclosure limitations.

## Invariants

- `warning` is not the primary criterion outcome.
- `degraded` is not used as a substitute for a bound criterion result; broader dimension/composite semantics remain later work.
- `atypical` remains a Baseline-relative descriptive result, not a normative status.
- `unknown`, `unavailable`, `conflicting`, `insufficient evidence` and `not applicable` must not collapse to pass or fail.
- One criterion meeting does not imply subject-wide health.

## Non-goals

- overall health aggregation;
- severity taxonomy;
- UI color/status design.