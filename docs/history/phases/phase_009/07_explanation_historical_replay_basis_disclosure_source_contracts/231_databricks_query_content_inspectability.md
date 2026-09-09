# INTG-231 — Databricks Query-Content Inspectability

**Status:** Accepted — Phase 009 Group 07

`system.query.history` can expose statement identity/text/parameters and execution context for covered queries, but statement/error content can be blank under customer-managed-key configuration and long content/parameters can be truncated.

Exact historical query-content basis is therefore conditional rather than guaranteed.
