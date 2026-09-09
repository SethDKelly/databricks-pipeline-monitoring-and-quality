# HLTH-050 — Distribution, Quantile, Unit & Normalization Preservation Boundaries

## Rule

Distributional or normalized measurements may relate across a transformation only when the transformation semantics preserve or explicitly transform the relevant measure.

Examples of potentially valid relationships include:

- deterministic unit conversion with a known monotonic mapping;
- explicit rate normalization with stable numerator/denominator semantics;
- distribution comparison over a row-preserving value transform whose mapping is known;
- source/output category-share reconciliation where categories are preserved and population changes are explicitly modeled.

## Invariants

- Quantiles are not generally additive or composable across joins, unions, filters or aggregations.
- A filter/join can change a distribution through selection even when values themselves are unchanged.
- Unit conversion can transform a measurement without creating empirical comparability for unrelated population/grain changes.
- Normalization does not repair an invalid reconciliation definition or unknown denominator.
- Approximation/sampling limitations remain attached through valid transformed comparisons.
- Do not propagate generic `distribution drift` status through Lineage; derive a new bound reconciliation/comparison when semantics justify it.
