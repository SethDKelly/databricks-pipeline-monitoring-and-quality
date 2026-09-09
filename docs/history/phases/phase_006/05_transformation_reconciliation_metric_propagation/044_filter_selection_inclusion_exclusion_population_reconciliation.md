# HLTH-044 — Filter Selection, Inclusion/Exclusion & Population Reconciliation

## Rule

Filter reconciliation binds the exact input population, predicate/version, eligible scope, output population, and any intentionally excluded populations.

For a pure row-filter transformation with stable grain and no other row-creating/removing behavior, useful reconciliation can include:

- eligible input count;
- included/output count;
- excluded count;
- exclusion rate under an explicit denominator;
- reason/category-specific exclusion counts where the predicate semantics support them.

## Invariants

- `input = output + excluded` is valid only for the explicitly bounded pure-filter semantics that justify it.
- A filter can intentionally lower row count without making the output unhealthy.
- Change Intent predicting a lower population does not make the resulting reduction acceptable; a normative rule remains separate.
- Filtering can materially change null rates, distributions, category shares, uniqueness and other metrics through selection effects; downstream values are not inherited from input values.
- A changed predicate/version can create a new reconciliation definition and Baseline regime.
- Missing evidence for the excluded population is not proof that no records were excluded.
- A filter-specific reconciliation violation is separate from downstream overall health and causal attribution.
