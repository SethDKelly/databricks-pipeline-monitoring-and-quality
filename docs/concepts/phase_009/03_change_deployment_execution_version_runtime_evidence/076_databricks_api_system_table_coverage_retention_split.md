# INTG-076 — Databricks API / System-Table Coverage & Retention Split

**Status:** Accepted — Phase 009 Group 03

Jobs UI/API run history and Lakeflow system tables have materially different documented history windows and run-type/source coverage. The Runs API is useful for detailed recent records such as attempts/repairs/Git snapshots, while system tables provide longer account operational history.

Historical support is therefore source-set and time-window specific. A recent exact result cannot be assumed reconstructible for the whole 365-day system-table window unless the required fields exist there or were independently retained.
