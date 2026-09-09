# HLTH-042 — Join Eligibility, Match/Unmatched Population & Directionality

## Rule

Join reconciliation begins from explicitly bound eligible input populations and join semantics rather than generic row counts.

A join reconciliation can distinguish, as applicable:

- eligible left/right records;
- records with usable/non-usable join keys;
- left records matched at least once;
- right records matched at least once;
- left-unmatched and right-unmatched populations;
- matched pair/relationship count;
- output population after the exact join type and any co-located predicates.

Match rates are directional. `left matched %` and `right matched %` are different measures with different denominators.

## Invariants

- `rows(A) + rows(B) = rows(C)` is not a generic join invariant.
- Inner/left/right/full/semi/anti and other join semantics can imply different relationships.
- Eligibility filters, null/invalid keys, temporal predicates, and consumer grain are part of the reconciliation definition.
- One side being fully matched does not imply the other side is fully matched.
- An unmatched population is an Observation/reconciliation result; whether it is acceptable requires an Expectation.
- A high upstream local null-rate or uniqueness violation can be relevant evidence but does not itself establish join mismatch.
- Join match evidence can localize a transformation discrepancy but does not establish causal attribution for a downstream incident.
