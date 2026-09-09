# HLTH-047 — Union, Merge/Upsert, Source Contribution & Overlap Semantics

## Rule

Union/merge reconciliation must bind the exact combination semantics, source roles, key/overlap behavior, and output action classes.

For bag/append unions, valid relationships can include source contribution counts/rates and output population reconciliation when no additional filtering/deduplication occurs.

For distinct unions or merge/upsert behavior, reconciliation can distinguish overlapping keys, inserts, updates, unchanged matches, deletes/tombstones where applicable, and source-specific contributions.

## Invariants

- `rows(C) = rows(A) + rows(B)` is valid only for explicitly additive bag/append semantics with aligned scope and no hidden filtering/deduplication/overlap behavior.
- Distinct union counts are not additive when inputs overlap.
- Merge/upsert output population depends on existing target state and action classes; input row count is not a direct output-count invariant.
- Source contribution is not causal attribution and does not imply business ownership.
- Duplicate/overlap semantics require exact keys/grain and evidence.
- A source-specific local failure or waiver does not automatically transfer to the merged output.
- Contribution and merge-action evidence can support downstream reconciliation Assessments under explicit Expectations.
