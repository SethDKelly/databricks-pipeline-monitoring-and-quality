# INTG-060 — Databricks Job Definition & SCD2 Configuration Identity

**Status:** Accepted — Phase 009 Group 03

Databricks Lakeflow Jobs system tables can identify job definitions by workspace/job and retain slowly-changing job/task configuration history within documented history boundaries.

Configuration effective at a time constrains possible execution state but does not itself prove an execution occurred or every implementation/configuration facet a run actually used.
