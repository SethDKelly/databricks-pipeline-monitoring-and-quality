# INTG-100 — Metric-View Query Observation & Grain

**Status:** Accepted — Phase 009 Group 04

A metric-view query can produce metric Observations at the requested fields/filters/parameter/window context under the active metric definition and source state.

The returned value must retain definition identity, evaluation/query time, grouping/filter context and source-version limitations. A measure name/value without this binding is insufficient for HLTH-001/004 provenance.
