# INTG-113 — Commit Freshness vs Event Freshness

**Status:** Accepted — Phase 009 Group 04

Databricks anomaly detection currently evaluates commit-based freshness; current documentation states event freshness from event-time/ingestion-latency analysis is not supported in the current anomaly-detection version.

Commit recency therefore cannot satisfy event-time freshness, source-latency or current-cycle propositions unless separate evidence establishes those semantics.
