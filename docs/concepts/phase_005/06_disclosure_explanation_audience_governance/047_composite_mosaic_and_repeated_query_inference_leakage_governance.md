# AUTH-047 — Composite, Mosaic, and Repeated-Query Inference-Leakage Governance

**Status:** Accepted — Phase 005 Group 06

## Purpose
Prevent disclosure from being judged safe only item-by-item when combinations of allowed facts, repeated queries, differencing, or narrowing can reveal a restricted fact.

## Contract
Disclosure review may consider material inference from:
- combinations of metric/threshold/schema/topology facts;
- exact counts, path lengths, timing, and unique categories;
- repeated queries over overlapping populations/windows;
- differencing between broader and narrower results;
- current answers combined with previously disclosed retained information;
- authority, approver, control, or incident metadata that indirectly identifies restricted subjects.

## Invariants
- Individually permitted facts do not guarantee the composite disclosure is safe.
- Aggregation, rounding, or redaction does not automatically eliminate inference risk.
- Repeated-query risk is a disclosure-governance concern even when each individual answer is aggregate.
- When a material leakage path is identifiable, the product may reduce detail, broaden abstraction, omit existence, or refuse the composite disclosure according to authorized policy.
- Leakage protection must not fabricate contradictory facts or false absence.
- Group 06 does not select privacy-budget, differential-privacy, query-throttling, or policy-engine technology.
