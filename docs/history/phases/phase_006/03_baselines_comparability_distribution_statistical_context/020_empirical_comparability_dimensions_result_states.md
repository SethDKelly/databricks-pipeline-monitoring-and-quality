# HLTH-020 — Empirical Comparability Dimensions & Result States

**Status:** Accepted — Phase 006 Group 03

## Purpose

Define when historical and current measurements are sufficiently alike in meaning and evidence context to support a descriptive comparison.

## Comparability dimensions

Evaluate as applicable:

- subject/entity identity continuity;
- metric/check definition/version continuity;
- unit, denominator, grain and population continuity;
- field/path/key and structural/interface continuity;
- operating mode/environment and consumer context;
- calendar/cadence/cohort context;
- measurement method, sampling and approximation semantics;
- evidence coverage and temporal alignment.

No universal numeric comparability score is introduced.

## Result vocabulary

A bounded comparison may resolve as:

- **directly comparable**;
- **comparable under an explicit normalization/transformation**;
- **non-comparable**;
- **insufficient reference**;
- **ambiguous reference context**;
- **conflicting evidence/reference**;
- **unavailable**;
- **unknown/unresolved**;
- **not applicable**.

## Invariants

- Same display name is insufficient for comparability.
- Structural compatibility is neither necessary nor sufficient for every historical metric comparison; the exact measurement semantics govern.
- Authority may approve use/review policy but cannot change an empirically non-comparable relationship into a comparable one.
- Comparability is conclusion-relative: two observations may be comparable for one derived comparison and not another.
- A limitation must not be compressed into `typical`, `atypical`, or `healthy`.

## Example

Execution-duration observations may remain directly comparable across a harmless additive schema change, while row-count observations may become non-comparable after the table grain changes.