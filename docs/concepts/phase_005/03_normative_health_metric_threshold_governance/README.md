# Phase 005 Group 03 — Normative Health, Metric & Threshold Governance

**Status:** Planned — not yet started

## Goal

Define who is permitted/authoritative to establish the normative health rules that Phase 006 will later refine semantically and statistically.

## Primary review questions

- authority to establish/revise Expectations by asset/dimension/context;
- authority to approve table/pipeline metric profiles or mark metrics business-critical;
- authority for thresholds, warning/failure margins, tolerance bands, severity, and exceptions/waivers;
- metric/Expectation retirement and historical governance;
- technical versus business threshold conflicts;
- authority required before a metric/Expectation can participate in an Execution Gate or other high-consequence control.

## Boundaries

This group decides **who may define/approve/revise/waive** normative metric state. It does not define metric families, statistical calculations, Baseline behavior, metric propagation algorithms, overall-health aggregation, or Metric Views/DQX implementation; those belong to Phase 006/007/009/010.

## Exit direction

Group 03 exits when normative health and metric-setting authority can be resolved without stealing metric/statistical meaning from Phase 006.