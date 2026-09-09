# HLTH-048 — Null, Default, Cast & Derived-Value Transformation Semantics

## Rule

Null/completeness and value-quality relationships across transformations are not inherited automatically. Reconciliation must model how the exact transformation can preserve, introduce, remove, replace, or reinterpret values.

Relevant transformation behavior can include:

- outer-join null introduction;
- filter-driven removal of null-bearing rows;
- default/coalesce replacement;
- cast/parse failure to null or sentinel value;
- conditional derivation;
- source-field fallback precedence;
- value mapping/standardization.

## Invariants

- Downstream null rate is not a copy of upstream null rate.
- Lower downstream null rate can result from filtering/defaulting and does not by itself prove improved source completeness.
- Replacing null with a sentinel can satisfy physical non-nullness while violating a separate validity/business-semantic criterion.
- Outer joins can legitimately introduce nulls on the non-matched side; acceptability depends on the join/output contract.
- Cast success/failure and default behavior must be observed or otherwise sufficiently evidenced; transformation intent alone is insufficient.
- Derived-value reconciliation can identify where value loss/replacement occurred without asserting root cause for a broader incident.
