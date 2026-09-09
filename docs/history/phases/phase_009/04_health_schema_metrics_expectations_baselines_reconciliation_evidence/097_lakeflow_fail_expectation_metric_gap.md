# INTG-097 — Lakeflow Fail-Expectation Metric Gap

**Status:** Accepted — Phase 009 Group 04

Databricks documents that fail-update expectations can stop an update without recording the same tracking metrics available for warn/drop expectations.

A failed update can therefore evidence an expectation violation while detailed pass/fail population metrics remain unavailable. Missing metrics must not be interpreted as zero failing records or a clean result.
