# INTG-230 — Databricks System-History Retention

**Status:** Accepted — Phase 009 Group 07

Databricks system-table history is evaluated per table: many material audit/query/lineage/job/alert surfaces currently retain about 365 days, while some surfaces have different or indefinite retention.

A generic `system` source label does not imply uniform replay horizon.
