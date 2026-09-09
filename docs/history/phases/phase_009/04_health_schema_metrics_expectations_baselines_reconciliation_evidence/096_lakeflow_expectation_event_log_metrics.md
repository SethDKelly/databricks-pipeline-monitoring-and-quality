# INTG-096 — Lakeflow Expectation Event-Log Metrics

**Status:** Accepted — Phase 009 Group 04

Lakeflow pipeline event logs expose flow/update identity and, for qualifying expectations, passed_records, failed_records and dropped_records metrics.

These are strong source-local Observations for the exact flow/update/rule population when present. They do not independently establish governed rule meaning, complete historical coverage, business severity or composite health.
