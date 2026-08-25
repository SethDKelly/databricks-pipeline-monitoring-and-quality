# HLTH-027 — Explicit Normalization & Transformed Comparison Semantics

**Status:** Accepted — Phase 006 Group 03

## Purpose

Allow legitimate comparisons across changing scale or context through explicit derived normalization without pretending the raw measurements are directly comparable.

## Contract

A normalized/transformed comparison requires:

- an explicit transformation/normalization definition and version;
- identified source Observations and denominator/reference variables;
- stable semantic meaning of numerator, denominator, grain and units;
- evidence that the transformation addresses the material difference relevant to the comparison;
- provenance linking the transformed Observation/reference back to raw evidence;
- limitations where normalization does not remove other comparability breaks.

Examples can include rates per eligible entity, per-million measures, duration per processed unit, or currency/unit normalization when semantically justified.

## Invariants

- Normalization creates a defined derived comparison basis; it does not make raw observations identical in meaning.
- An ad-hoc rescaling chosen after seeing an outlier is not automatically a valid comparison rule.
- Changing denominator semantics creates a new derived-metric definition/version.
- A valid normalized comparison can coexist with `raw values non-comparable`.
- Normalization cannot repair unrelated grain, identity, structural, cohort, or measurement-method breaks.
- The normalized result remains descriptive unless an Expectation separately makes it normative.

## Example

Raw error counts rise because eligible volume doubles. If `errors per million eligible records` has stable numerator/denominator semantics, that rate may remain comparable even though raw error counts should not be compared as if population size were unchanged.