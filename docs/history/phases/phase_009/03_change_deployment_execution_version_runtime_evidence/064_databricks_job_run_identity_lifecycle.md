# INTG-064 — Databricks Job Run Identity & Lifecycle

**Status:** Accepted — Phase 009 Group 03

Databricks Jobs Runs APIs and Lakeflow run timeline tables can establish job/run identity, trigger/run type, timing and source-owned lifecycle/result fields within their documented coverage.

`run_id` identifies an actual execution record; it is not inferred from schedule opportunity. Lifecycle evidence can still be partial or unavailable when source/history coverage is insufficient.
