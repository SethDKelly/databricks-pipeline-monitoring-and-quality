# EXPL-046 — Expected Work, Opportunity & Missing-Run Negative Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Why didn't it run?`, `was the scheduled run skipped?`, or `did no execution happen?` first separates expected work/opportunity from actual execution and only then evaluates any strong negative.

## Rules

- expected work ≠ execution opportunity ≠ Gate decision ≠ execution;
- absence of an execution record is not `no run` without adequate opportunity/coverage;
- Gate HOLD can explain admission state but HOLD ≠ failed execution;
- opportunity expiry/cancellation can coexist with no execution without creating a failed run;
- telemetry outage/unavailability remains a limitation;
- causal `why` attribution requires Causal Claim semantics and is handed to Group 04.