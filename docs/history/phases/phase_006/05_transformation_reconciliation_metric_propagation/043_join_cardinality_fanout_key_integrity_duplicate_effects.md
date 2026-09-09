# HLTH-043 — Join Cardinality, Fan-Out, Key Integrity & Duplicate Effects

## Rule

Join reconciliation must preserve relationship cardinality and multiplicity rather than treating output row count as a direct proxy for input completeness.

Material measures can include:

- expected versus observed key cardinality shape;
- matches-per-left-key / matches-per-right-key;
- zero/one/many match populations;
- fan-out or amplification ratio under a defined denominator;
- duplicate-key contribution to matched pairs/output rows;
- unexpected many-to-many relationships where a one-to-one or one-to-many contract was expected.

## Invariants

- A many-to-many join can legitimately produce more output rows than either or both inputs.
- Duplicate keys can amplify output without any missing input rows.
- Declared key semantics do not prove observed uniqueness; key integrity requires evidence.
- Fan-out can be expected or unacceptable depending on an explicit transformation/consumer contract.
- One aggregate fan-out number must not hide materially distinct key populations where the reconciliation purpose requires distribution or outlier detail.
- Key/grain/schema changes can invalidate prior cardinality reconciliation definitions and require scoped revision rather than silent continuation.
- Fan-out observations can support Investigation and Causal Claim evidence but are not themselves causal confirmation.
