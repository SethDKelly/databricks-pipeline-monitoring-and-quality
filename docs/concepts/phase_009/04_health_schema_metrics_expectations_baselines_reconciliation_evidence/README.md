# Phase 009 Group 04 — Health, Schema, Metrics, Expectations, Baselines & Reconciliation Evidence

**Status:** Not started

## Goal

Map concrete measurement and metadata capabilities to the accepted Observation/Assessment/Expectation/Baseline/health model.

## Primary questions

- Which Databricks/Unity Catalog/system surfaces expose realized schema and structural history?
- Which surfaces can support compatibility assessment for exact consumers/interfaces rather than generic engine coercion?
- What DQX outputs are available, at what granularity/time/version, and what do they prove about Observation versus governed Expectation/Assessment?
- What Metric Views or query-derived metrics can support Observations and transformations without becoming blind status propagation?
- Where are governed Expectations defined and versioned, and how are warning/waiver/severity metadata sourced?
- What evidence can establish Baseline membership/comparability and historical reference windows?
- Which transformation/reconciliation results are directly available versus derived from multiple sources?
- How are freshness/currentness/current-cycle and exact-use suitability supported?
- What history, latency, retention and negative-evidence limits apply to missing metrics/checks/schema events?

## Boundary

Metric/check availability is not a governed normative requirement by itself. Baseline remains descriptive, Expectation normative, Observation evidential and Assessment interpretive.

## Handoff

Group 05 combines bounded source-state/health evidence with topology and consumer evidence without promoting reachability into Impact.
