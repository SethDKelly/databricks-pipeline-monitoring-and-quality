# INTG-065 — Databricks Task Run & Parent/Child Execution Identity

**Status:** Accepted — Phase 009 Group 03

Task-run timelines and Runs API records can bind task execution to job runs and, where exposed, parent/source/root run relationships.

These explicit identifiers are stronger than time/name correlation for assembling multi-task or run-job-triggered executions. Fields introduced later in system-table history cannot be assumed present for older evidence.
