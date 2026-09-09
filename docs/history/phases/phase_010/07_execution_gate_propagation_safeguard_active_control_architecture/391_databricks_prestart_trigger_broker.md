# ARCH-391 — Databricks Pre-Start Trigger Broker

**Status:** Accepted

For externally triggered jobs, a DMTZ-authorized trigger broker may evaluate a Gate before calling `run-now`/submit APIs, using stable idempotency/correlation tokens.

This is a DMTZ-owned enforcement point and requires bypass-path governance; it is not inferred from Databricks job configuration.
