# INTG-101 — Metric-View Materialization & Freshness Boundary

**Status:** Accepted — Phase 009 Group 04

Metric-view materialization is an optimization path using managed materialized views and a Lakeflow pipeline; refresh schedule/availability can affect when precomputed state is updated.

Optimizer transparency does not eliminate exact-use freshness requirements. Query result correctness/freshness must be evaluated from documented query/materialization semantics rather than assuming the materialization schedule is a framework freshness SLA.
