# HLTH-053 — Historical Transformation Version, Rule Binding & Reassessment

## Rule

Historical reconciliation binds the transformation/version, time-valid Lineage relationship, reconciliation definition, input/output versions, current-cycle context, and evidence/reference versions applicable at the relevant event/effective and knowledge times.

## Invariants

- Current transformation logic is never projected backward onto historical runs.
- Change Intent can describe a prospective reconciliation change but does not activate it before realized evidence supports the new transformation/version.
- A changed join/filter/dedupe/aggregation/merge/value rule can create a new reconciliation-definition version and may segment Baseline/comparability history.
- Later-discovered Lineage, corrected metrics or corrected transformation metadata can justify a new retrospective reconciliation Assessment while preserving the earlier historical Assessment.
- Historical replay distinguishes the rule actually used/known then from a current reconstructed analysis using later evidence.
- A prior reconciliation result is not silently rewritten when code or Expectations change.
