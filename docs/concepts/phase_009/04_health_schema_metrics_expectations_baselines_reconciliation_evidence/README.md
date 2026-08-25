# Phase 009 Group 04 — Health, Schema, Metrics, Expectations, Baselines & Reconciliation Evidence

**Status:** Next — not started

## Goal

Map concrete measurement and metadata capabilities to the accepted Observation/Assessment/Expectation/Baseline/health model.

## Group 03 entry contract

Group 04 may consume accepted repository/run/task identities, execution timing, configured-versus-actual sequence distinctions, run-specific Git/implementation facets and input/output table/version bindings **only where INTG-051–INTG-083 establish them**.

Material Group 03 gaps remain explicit inputs: CI→Databricks association can require explicit correlation; bundle/workspace-source run commit identity can require attestation; composite implementation state is only partially natively bound; exact generic multi-input version consumption is unsupported out of the box; output-version evidence is conditional/per output; and historical precision differs across source windows.

Execution occurrence or success does **not** establish realized schema correctness, compatibility, data-quality success, metric validity, freshness/current-cycle status, Baseline comparability or health.

## Primary questions

- Which Databricks/Unity Catalog/system surfaces expose realized schema and structural history?
- Which surfaces can support compatibility assessment for exact consumers/interfaces rather than generic engine coercion?
- What DQX outputs are available, at what granularity/time/version, and what do they prove about Observation versus governed Expectation/Assessment?
- What Metric Views or query-derived metrics can support Observations and transformations without becoming blind status propagation?
- Where are governed Expectations defined and versioned, and how are warning/waiver/severity metadata sourced?
- What evidence can establish Baseline membership/comparability and historical reference windows?
- Which transformation/reconciliation results are directly available versus derived from multiple sources?
- How are freshness/currentness/current-cycle and exact-use suitability supported?
- How do Group 03 run/version gaps constrain exact health attribution to the implementation/input/output actually involved?
- What history, latency, retention and negative-evidence limits apply to missing metrics/checks/schema events?

## External-fact requirement

Verify current Databricks/Unity Catalog, DQX, Metric Views and any other evaluated measurement/check surfaces. Record exact source/version/edition/preview status, output grain, timing, history, permission, retention and provenance limitations.

## Boundary

Metric/check availability is not a governed normative requirement by itself. Baseline remains descriptive, Expectation normative, Observation evidential and Assessment interpretive. Run success and output existence remain separate from all of them.

## Handoff

Group 05 combines bounded source-state/health evidence with topology and consumer evidence without promoting reachability into Impact.
