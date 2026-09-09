# INTG-112 — Join / Fan-Out Metric-Semantics Boundary

**Status:** Accepted — Phase 009 Group 04

Metric Views and query-derived measurements can encode joins, but join-cardinality assumptions and optimizer hints are not empirical key-integrity or reconciliation proof.

Databricks metric-view `rely` cardinality assertions are not universally validated at runtime; incorrect assumptions can produce incorrect measures. DMTZ must retain independent cardinality/key/reconciliation evidence where material.
