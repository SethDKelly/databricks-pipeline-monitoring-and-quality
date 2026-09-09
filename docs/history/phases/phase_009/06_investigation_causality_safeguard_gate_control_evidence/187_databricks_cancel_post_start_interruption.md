# INTG-187 — Databricks Jobs Cancel as Post-Start Interruption

**Status:** Accepted — Phase 009 Group 06

A Databricks Jobs cancel request targets an already-created run/task and is asynchronous; request success does not mean termination was immediate or complete.

Cancel evidence can support interruption/control history but is not pre-start Execution Gate HOLD evidence.
