# HLTH-017 — Structural Change Impact on Metric/Profile/Baseline Applicability

**Status:** Accepted — Phase 006 Group 02

## Purpose

Define how structural change triggers a bounded review of measurement semantics without automatically invalidating every historical metric or silently preserving measurements whose meaning changed.

## Contract

A structural change may affect one or more of:

- metric definition applicability;
- metric-profile selection/review status;
- field/path identity and measurement binding;
- denominator/population/grain semantics;
- key/uniqueness expectations;
- null/completeness metrics;
- distribution/quantile comparability;
- row-count/volume interpretation;
- join/referential/reconciliation relationships;
- freshness/current-cycle measures;
- business-semantic measures;
- Baseline eligibility/comparability review.

## Invariants

- Structural change triggers **scoped applicability review**, not a universal reset.
- Unaffected metrics may continue when their subject/definition/grain/window semantics remain stable.
- A field rename with supported identity continuity may preserve some metric identity while still requiring binding/version review.
- A type change can invalidate selected distribution/quantile metrics while leaving row count or freshness unchanged.
- A grain/key change commonly affects volume, uniqueness, join/reconciliation, population and distribution semantics but need not invalidate execution-duration or output-existence metrics.
- A new optional field does not automatically create routine metrics for that field.
- Governance under AUTH-020 may require review/suspension/retirement, but actual historical comparability remains Group 03 evidence/statistical semantics.
- Old Observations are preserved even when no longer eligible for current comparison.
- Structural incompatibility for one consumer does not globally invalidate producer-local metrics unrelated to that consumer.

## Example

Adding an optional `customer_segment` field may leave existing row-count/freshness Baselines untouched, while changing `account_id` grain to `account_id, business_date` requires review of row-count, uniqueness, distribution and join metrics tied to the former grain.