# INTG-115 — Result Timing, Scan / Refresh & Availability

**Status:** Accepted — Phase 009 Group 04

DQX workflow schedules, pipeline expectation events, Metric View materialization refreshes, data-profiling refreshes and anomaly-detection intelligent scans have different production/evaluation/availability clocks.

Result freshness is exact-use and source-specific. A newer retrieval timestamp, latest dashboard state or last scan does not prove the underlying evidence is fresh enough for the requested use.
