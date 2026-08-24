# AUTH-031 — Restricted Derived Evidence and Inference-Leakage Constraints

**Status:** Accepted — Phase 005 Group 04

## Purpose

Prevent derived/aggregate monitoring evidence from being treated as inherently safe merely because it is not raw row data.

## Restricted derived classes

Potentially sensitive derived state can include:

- counts, null rates, distinct counts, quantiles, distributions, balances, thresholds, and Baselines;
- schema/field names, types, key roles, and compatibility failures;
- Lineage topology, hidden-node existence, consumer identity, and path structure;
- Classification, Policy Context, responsibility, authority-holder, and authorization-basis metadata;
- Causal Claim, Impact, exposure, business consequence, safeguard, gate, and operational-state details.

## Invariants

- Aggregation is not automatic declassification.
- A safe summary must be explicitly permitted for the requester/context.
- Combining individually permitted facts can still reveal a restricted fact; projection must account for material inference leakage where identifiable.
- Repeated queries or progressively narrower scopes must not be assumed safe merely because each answer is aggregate.
- Redaction of a name does not guarantee safety when surrounding metrics/topology make identity obvious.
- Restriction can apply to the authorization/authority basis itself.
- Group 04 defines capability and projection constraints; Group 06 later governs audience/disclosure policy and high-consequence communication review.
