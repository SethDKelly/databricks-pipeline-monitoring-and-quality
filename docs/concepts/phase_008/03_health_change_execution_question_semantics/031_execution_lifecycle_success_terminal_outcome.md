# EXPL-031 — Execution Lifecycle, Success & Terminal Outcome Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Did it succeed?`, `is it still running?`, `did it fail?`, and `was it cancelled?` are lifecycle/terminal propositions over an established execution, not synonyms for execution occurrence.

## Rules

- start/progress/terminal evidence may mature independently;
- a known start with missing terminal evidence remains partial rather than automatically running/failed/cancelled;
- platform/source terminal semantics remain authoritative for the bounded execution proposition;
- later successful retry/rerun does not rewrite an earlier failed attempt;
- `success` does not imply qualifying output, freshness, health, readiness, or downstream use.

Explanation must preserve attempt/logical-execution level when material.