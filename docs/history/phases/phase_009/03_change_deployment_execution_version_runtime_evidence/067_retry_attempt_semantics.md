# INTG-067 — Retry Attempt Semantics

**Status:** Accepted — Phase 009 Group 03

Databricks attempt fields such as `attempt_number` and `original_attempt_run_id` provide source-specific continuity between retries when present. GitHub Actions uses its own `run_id`/`run_attempt` semantics.

Attempts remain source-local until explicitly assembled into the framework's logical Execution History. A later successful attempt never rewrites a prior failed attempt.
