# INTG-124 — Lineage Entity Metadata & Consumer Identity

**Status:** Accepted — Phase 009 Group 05

Lineage entity metadata can identify Databricks jobs/runs, pipelines/updates, dashboards, SQL queries, notebooks, Genie spaces and alerts where captured. These IDs establish source-local consumer/execution identity only and must reconcile through Entity Identity where a broader consumer identity is needed.

Null entity metadata can accompany JDBC or other reads and must not be interpreted as no consumer.
