# HLTH-026 — Distribution, Quantile, Category-Share & Shape Reference Semantics

**Status:** Accepted — Phase 006 Group 03

## Purpose

Define descriptive comparison of distribution/shape behavior without requiring a universal drift score or treating every distribution change as a defect.

## Contract

A distribution Baseline may describe selected, purpose-driven characteristics such as:

- quantiles or bounded ranges;
- category/value shares;
- missing/present composition where the metric definition requires it;
- histogram/bin summaries under a stable definition;
- distribution-shape descriptors;
- other explicitly defined comparative summaries.

The comparison must retain the population, field semantics, units, bin/category definition, approximation method, and reference context needed to interpret the result.

## Invariants

- Quantiles are only meaningful for semantically ordered dimensions.
- Category emergence/disappearance is interpreted with reference coverage and population semantics; it is not automatically failure.
- Bin/category-definition changes can make historical summaries non-comparable.
- A shifted distribution is `different/atypical relative to reference` unless a normative Expectation separately establishes acceptability.
- Tail comparisons can require stronger sample/reference sufficiency than central summaries.
- The product does not require one universal divergence/drift statistic or score.
- Distribution summaries should remain purpose-driven under the Group 01 anti-bloat rule.

## Example

Transaction amount p95 may be meaningfully compared across comparable business days. Computing p95 over opaque UUIDs remains semantically inapplicable even if the engine supports it.