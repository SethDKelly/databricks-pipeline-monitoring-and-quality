# OPS-057 — Execution, Version, Change & Temporal Localization

**Status:** Accepted — Phase 007 Group 05

## Purpose

Use OPS-010–OPS-020 and OPS-034–OPS-049 to localize around actual changes/executions without turning timing into causality.

## Contract

Investigation may compare:

- last evidenced unaffected versus first evidenced affected execution/output;
- exact consumed input-version sets across affected/unaffected runs;
- run-specific implementation-state differences;
- realized Change intervals;
- Deployment activation/rollback context;
- retries/restarts/reruns/backfills and their outcomes;
- actual sequence/waiting evidence.

Statements such as `first affected run after activation`, `only affected runs consumed B2`, or `deviation disappeared after rollback` are evidence-bearing localization/contrast facts. They may support or contradict a later Causal Claim but are not causal conclusions themselves.

Mixed/unknown version sets and ambiguous run ordering remain explicit.

## Invariants

- first post-change run ≠ caused by change.
- shared version among affected runs ≠ causal proof.
- rollback/retry recovery ≠ automatic confirmation.
- temporal precedence ≠ transmission/mechanism.
- unknown consumed version limits localization rather than being filled with latest/active state.
