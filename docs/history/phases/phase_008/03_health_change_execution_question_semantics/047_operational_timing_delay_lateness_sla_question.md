# EXPL-047 — Operational Timing, Delay, Lateness & SLA Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Was it late?`, `how long did it take?`, `did it miss the delivery window?`, and `what was delayed?` must bind the exact timing proposition and reference boundary.

## Rules

- execution duration ≠ start delay ≠ wait interval ≠ output delivery lateness ≠ freshness/currentness violation;
- expected/scheduled time and observed event time remain separate;
- a valid Gate/Safeguard action can coexist with a timing/freshness violation;
- late completion does not automatically establish stale consumer use or business consequence;
- temporal overlap with an outage/control/change does not establish causal attribution;
- no universal latency/SLA threshold is introduced by Explanation.