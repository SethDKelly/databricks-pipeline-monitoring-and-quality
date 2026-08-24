# Phase 006 Group 02 — Structural / Schema / DDL Compatibility

**Status:** Next — not yet started

## Goal

Define functional structural/schema health and consumer-specific compatibility without selecting whether validation runs in GitHub Actions, Unity Catalog/Databricks, DQX, or the monitoring application.

## Accepted handoff from Group 01

- structural/schema is one canonical metric/check family, but observed structure is not automatically compatibility Assessment;
- every structural Observation must remain bound to subject/schema version/window/context;
- `column exists`, observed type/nullability/nesting and similar facts are Observation;
- normative compatibility depends on applicable structural Expectations governed by AUTH-019;
- profile selection/applicability/support/availability remain separate;
- structural change can trigger later metric/Baseline applicability review without globally invalidating every metric.

## Review scope

- required versus optional fields;
- add/drop/rename semantics;
- type widening/narrowing and precision/scale;
- nullability/default/generated-value changes;
- nested structure evolution;
- key/identifier-role and grain changes;
- declared schema-contract/version compatibility;
- consumer-specific compatibility by transformation/export/report/application use;
- planned versus realized structural change;
- structural checks that can be observed before deployment versus only after activation, without choosing validation placement;
- scoped consequences for metric definition/profile/Baseline applicability.

## Boundaries

Do not treat every schema change as breaking. Do not infer rename identity from drop/add alone. Do not let declared schema meaning prove realized structure or key uniqueness. Do not choose validation architecture.

**Group 02 has not started.**
