# OPS-094 — No-Opportunity / Incidental Safeguard Non-Prevention

**Status:** Accepted — Phase 007 Group 07

## Purpose

Prevent a safeguard from receiving causal credit merely because a consumer happened not to encounter suspect state while the safeguard was active.

## Contract

When Group 06 establishes `no relevant encounter opportunity`, or another independent condition fully explains non-encounter, the safeguard may still have been validly active/enforced but the prevented-exposure proposition is not established from that interval alone.

Examples include:

- consumer had no scheduled/use opportunity;
- consumer was independently offline;
- safe state was already pinned for unrelated reasons;
- an upstream failure prevented production before the protected boundary became material.

## Invariants

- active protection can be operationally valid without having prevented an actual opportunity.
- no opportunity ≠ safeguard failure.
- no opportunity ≠ prevented exposure.
- counterfactual speculation is not substituted for evidence.
