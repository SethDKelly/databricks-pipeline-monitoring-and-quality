# INTG-068 — Repair, Restart, Rerun & Backfill Continuity

**Status:** Accepted — Phase 009 Group 03

Databricks repair history, retries, independently triggered reruns, run-job children and backfill activity preserve their source meanings. GitHub Actions re-run semantics are different again.

The framework must not normalize all repeated execution into `retry`. Logical continuity is established from source identities/relationships and the accepted OPS-037 semantics.
