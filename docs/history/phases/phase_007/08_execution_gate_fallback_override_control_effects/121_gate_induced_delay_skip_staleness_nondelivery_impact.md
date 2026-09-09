# OPS-121 — Gate-Induced Delay, Skipped Opportunity, Staleness & Non-Delivery Impact

**Status:** Accepted — Phase 007 Group 08

## Purpose

Expose operational consequences of admission control without turning them into Gate lifecycle state or hiding the protective intent.

## Potential downstream evidence

Depending on actual events, independently record/assess:

- wait/start delay;
- opportunity expiry/cancellation or skipped cycle;
- late completion or missed delivery;
- no current output because execution did not occur;
- continued consumer use of an older state;
- downstream freshness/currentness violation;
- analytical/business consequence where evidenced.

## Rules

- a valid enforced HOLD may coexist with an SLA/freshness violation;
- `Gate held` is not itself the Observation/Assessment of delay or business consequence;
- Gate HOLD does not prove an older state was consumed; Group 06 encounter evidence is still required;
- ADMIT/override does not prove a stale version was consumed; Group 04 version evidence remains required;
- control policy quality is not inferred from one adverse operational outcome;
- Impact/Causal Claim boundaries remain intact.