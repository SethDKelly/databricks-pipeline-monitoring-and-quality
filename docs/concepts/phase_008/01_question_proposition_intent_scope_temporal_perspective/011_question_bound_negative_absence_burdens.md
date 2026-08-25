# EXPL-011 — Question-Bound Negative & Absence Burdens

**Status:** Accepted — Phase 008 Group 01

## Requirement

A negative-form question does not reduce the REF evidence burden required for a negative answer.

Examples of strong negatives include:

- no run occurred;
- no qualifying output existed;
- no consumer was exposed;
- no downstream effect/consequence occurred;
- no applicable path existed;
- no registered intent existed within a declared registration scope;
- no Gate/Safeguard enforcement occurred;
- the change was not planned;
- the control did not cause an effect.

Each negative requires the opportunity/coverage/scope semantics owned by the relevant source concept/refinement.

## Distinctions

Preserve:

- `not observed` ≠ `did not occur`;
- `not known by cutoff` ≠ historical absence;
- `no matching registered intent known` ≠ proven unplanned;
- `one safe path` ≠ no exposure;
- `no complaint` ≠ no consequence;
- `no run telemetry` ≠ no run;
- `no control telemetry` ≠ not enforced;
- `not authorized to view` ≠ nonexistent.

## Explanation behavior

Prefer a narrower statement such as `no exposure was established from the covered paths` or `exposure remains unknown` over a broad unsupported negative.
