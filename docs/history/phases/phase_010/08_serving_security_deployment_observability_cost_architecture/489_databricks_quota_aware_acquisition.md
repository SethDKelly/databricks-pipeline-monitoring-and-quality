# ARCH-489 — Databricks Quota-Aware Acquisition

**Status:** Accepted

Databricks acquisition favors deployment-verified bulk/system-table/reconciliation surfaces, selective queries, incremental checkpoints and bounded on-demand API calls appropriate to each proposition instead of naive per-object high-frequency polling.

Exact endpoint limits remain capability-instance/environment facts.