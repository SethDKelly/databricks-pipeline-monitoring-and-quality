# OPS-035 — Execution Opportunity, Expected Work, Gate State & Actual Instance Separation

**Status:** Accepted — Phase 007 Group 04

## Purpose

Prevent scheduled/expected/gated work from being rewritten as an execution that never actually started.

## Contract

Keep these propositions separate:

1. **execution opportunity** — a schedule/event/manual/control context created an opportunity for work to start;
2. **expected work** — an applicable Expectation says qualifying execution/output should occur under stated conditions;
3. **gate/control state** — a Gate may HOLD/ADMIT/override that opportunity;
4. **actual execution instance** — independent runtime evidence establishes that execution actually existed/started.

An opportunity can exist without an Expectation. An Expectation can apply without the scheduler emitting a visible opportunity. A gate can admit an opportunity that never starts. A held opportunity is not a failed run.

## Negative behavior

If expected work does not occur, absence is established through REF-002/REF-003 coverage plus Observation/Assessment semantics. Execution History must not synthesize a phantom cancelled/failed run merely to represent a missed expectation.

## Invariants

- expected ≠ scheduled/opportunity;
- opportunity ≠ admitted;
- admitted/overridden ≠ started;
- held ≠ execution failure;
- missed expected work ≠ fabricated execution;
- passive monitoring creates no execution opportunity or control state by itself.