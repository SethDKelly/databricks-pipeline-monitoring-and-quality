# REF-028 — Prevented Exposure Evidence Standard

**Status:** Accepted — Phase 004 Group 04

## Purpose

Define the evidence required to say an enforced safeguard **prevented exposure** rather than merely coexisted with non-exposure.

## Minimum prevented-exposure conditions

The determination requires all material elements below:

1. a sufficiently bound affected state/version/window and downstream consumer;
2. historical reachability/encounter path showing the consumer could receive the affected state through the protected boundary;
3. sufficient evidence that the safeguard was actually enforced at that boundary for the relevant interval;
4. a relevant consumption/refresh/use opportunity or other evidence that makes the safeguard materially operative rather than incidental;
5. sufficient negative consumption/version coverage showing the affected state did not reach the consumer through the protected route;
6. sufficient coverage of material alternate routes, or an explicit limitation if alternate-path coverage is incomplete.

## Rules

- `Safeguard active + consumer not exposed` is not automatically `safeguard prevented exposure` when no relevant encounter opportunity existed or another independent reason explains non-exposure.
- If the safeguard directly controls the only applicable route and blocks the relevant encounter opportunity, the prevention proposition may be strongly evidenced as a deterministic control effect under the applicable causal/Impact semantics.
- If alternate paths remain possible or the control's materiality is uncertain, retain `not exposed with safeguard active` or unresolved prevention rather than overstating cause.
- Prevented exposure is always scoped to the affected state/version and bounded consumer/path/time context.
- Blocking the affected version does not establish freshness or healthy delivery; an earlier stale state may still be served.
- Proposed or activation-unknown safeguards cannot establish prevented exposure.

## Causal boundary

The accepted Impact/SYN-028 prevented-exposure result is a narrowly scoped control-effect determination. Broader claims that the safeguard caused business delay, prevented a business outcome, or produced another consequence remain Causal Claims and use REF-013–REF-020.

## Non-goals

- general counterfactual simulation;
- assuming every non-exposed consumer was protected by the safeguard;
- health determination;
- business-consequence causality.
