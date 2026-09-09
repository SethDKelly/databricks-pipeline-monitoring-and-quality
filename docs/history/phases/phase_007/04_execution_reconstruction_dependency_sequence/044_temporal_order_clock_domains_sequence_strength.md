# OPS-044 — Temporal Ordering, Clock Domains & Sequence Strength

**Status:** Accepted — Phase 007 Group 04

## Purpose

Prevent false precision when reconstructing execution order from timestamps produced by different clocks/sources.

## Contract

Preserve distinct ordering evidence:

- explicit source sequence/order relationship;
- source-local event ordering;
- parent/child or orchestration ordering;
- timestamp ordering within a sufficiently comparable clock domain;
- bounded cross-source order with known timing/clock limitations;
- indeterminate order.

Exact wall-clock timestamps are not always necessary to establish order when explicit sequence relationships exist. Conversely, numerically ordered timestamps from unsynchronized/uncertain clocks may be insufficient to establish a close cross-source ordering.

## First/last claims

Claims such as `first run after activation`, `last run before rollback`, or `first downstream execution after upstream completion` require adequate ordering evidence for both boundaries. A coarse time window may yield several candidate runs rather than one selected by convenience.

## Invariants

- timestamp precision ≠ ordering certainty;
- arrival/knowledge order ≠ event order;
- numerically later timestamp ≠ guaranteed later event across incompatible clocks;
- explicit sequence can be stronger than wall-clock comparison for the bounded proposition;
- order ≠ dependency/consumption/cause.