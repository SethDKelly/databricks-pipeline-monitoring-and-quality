# OPS-037 — Attempt, Retry, Restart, Rerun, Backfill & Execution Continuity

**Status:** Accepted — Phase 007 Group 04

## Purpose

Preserve operational continuity without flattening every repeated invocation into either one run or many unrelated runs.

## Contract

The framework distinguishes, when source semantics/evidence support it:

- **attempt** — one bounded attempt to execute work;
- **retry** — another attempt associated with the same logical execution under an explicit retry relationship;
- **restart/resume** — continuation/re-entry semantics only where the source establishes continuity/checkpoint/restart meaning;
- **rerun** — a later execution of similar logical work that may be a new execution even when it targets the same logical period;
- **backfill/reprocessing** — execution intentionally addressing an earlier logical/data period, still a distinct actual execution unless explicit continuity says otherwise.

Names and timestamps do not decide these classes by themselves.

## Outcome composition

Attempt outcomes remain distinct. `last attempt succeeded` does not automatically erase an earlier failed attempt. A logical execution may have an overall outcome only when the applicable orchestration/composition semantics justify one.

## Invariants

- retry ≠ duplicate telemetry;
- retry ≠ rerun by assumption;
- restart ≠ proof of same in-memory/runtime state;
- rerun/backfill does not overwrite the original execution;
- later success does not rewrite earlier failed attempt history;
- same logical data interval ≠ same execution identity.