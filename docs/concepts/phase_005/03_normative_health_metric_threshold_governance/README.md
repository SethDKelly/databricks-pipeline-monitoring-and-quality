# Phase 005 Group 03 — Normative Health, Metric & Threshold Governance

**Status:** Next review group — not yet started

## Goal

Define who is permitted/authoritative to establish the normative health rules that Phase 006 will later refine semantically and statistically.

## Accepted handoff from Group 02

- Assertion Authority is the common authority truth owner and AUTH-001–AUTH-015 are accepted;
- Semantic Definition authority is facet-specific, including governed technical schema meaning, grain, field role, and key/identifier role;
- declared/governed schema meaning ≠ normative schema contract ≠ realized schema state;
- Responsibility Assignment, Classification/criticality, and Policy Context do not grant normative health authority;
- derived/inherited governance state does not automatically propagate authority or normative requirements;
- criticality may influence priority and policy but is not evidence of health failure;
- schema/DDL changes can require scoped metric/Baseline/Expectation review without automatically resetting all health context.

## Primary review questions

- authority to establish/revise Expectations by asset/dimension/context;
- authority to approve table/pipeline metric profiles or mark metrics business-critical;
- authority for thresholds, warning/failure margins, tolerance bands, severity, and exceptions/waivers;
- authority for **structural/schema Expectations and compatibility rules**, including required/optional columns, accepted type/nullability/key/grain conditions, allowed additive changes, and consumer-specific compatibility where appropriate;
- who may approve metric/Baseline applicability changes after schema/grain/key changes;
- metric/Expectation retirement and historical governance;
- technical versus business threshold/compatibility conflicts;
- authority required before a metric/schema Expectation can participate in an Execution Gate or other high-consequence control.

## Boundaries

This group decides **who may define/approve/revise/waive** normative health, metric, and schema-contract state. It does not define metric families, schema-compatibility algorithms, statistical calculations, Baseline behavior, metric propagation algorithms, overall-health aggregation, or Metric Views/DQX implementation; those belong to Phase 006/007/009/010.

Schema validation location remains unresolved: GitHub Actions, Databricks/Unity Catalog metadata checks, and an independent monitoring application are candidate integration points with different temporal roles, not decisions made in Group 03.

## Exit direction

Group 03 exits when normative health, metric, threshold, and structural/schema-setting authority can be resolved without stealing metric/statistical/schema-health meaning from Phase 006.
