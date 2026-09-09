# INTG-141 — Exact Table-Version Consumption Gap

**Status:** Accepted — Phase 009 Group 05

Evaluated generic lineage/query-history surfaces do not universally expose the exact Delta/table version read by every query or consumer.

Object-level read evidence can therefore be `encounter established; encountered-state/version unresolved`. Exact suspect-version exposure is conditional on explicit time-travel/version parameters, retained statement semantics, run-specific input evidence, snapshot identity or equivalent attestation.
