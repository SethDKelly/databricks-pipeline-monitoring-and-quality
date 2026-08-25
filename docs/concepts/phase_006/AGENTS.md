# Phase 006 Agent Handoff

Applies to work under `docs/concepts/phase_006/` and complements the repository root `AGENTS.md` without replacing its accepted cross-phase rules.

## Current status

- Phase 006 is **ACTIVE**.
- Group 01 accepted: HLTH-001–HLTH-008; H01-01–H01-20 pass.
- Group 02 accepted: HLTH-009–HLTH-018; H02-01–H02-30 pass.
- Group 03 accepted: HLTH-019–HLTH-029; H03-01–H03-32 pass.
- Group 04 accepted: HLTH-030–HLTH-040; H04-01–H04-40 pass.
- **Group 05 — Transformation Reconciliation & Metric Propagation is next and has not started.**
- Accepted concept count remains 24; SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged.

## Permanent Phase 006 boundaries

Preserve:

- metric definition ≠ Observation ≠ Assessment;
- structural compatibility ≠ statistical comparability;
- Baseline typicality ≠ normative acceptability;
- criterion outcome ≠ warning/proximity ≠ severity/priority ≠ waiver/disposition;
- `violates + waived` ≠ `meets`;
- missing/uncertain evidence ≠ pass/fail;
- Lineage relation ≠ metric propagation ≠ status propagation ≠ causality;
- local metric/Assessment ≠ downstream reconciliation measurement/Assessment;
- authority cannot manufacture evidence sufficiency or empirical comparability;
- passive monitoring remains non-blocking unless an explicitly governed active control later requires otherwise.

## Group 05 entry contract

Group 05 must define transformation-aware relationships for joins, filters, aggregations, deduplication, unions/merges, null handling, current-cycle/freshness alignment, and other semantically justified relationships.

Do not recursively copy upstream row counts, null rates, quantiles, Baseline states, warnings, violations, severities or waivers downstream merely because Lineage exists.

A+B→C does not imply row-count conservation. A derived reconciliation Observation/Expectation/Assessment must state the exact transformation relationship, grain/population/denominator, current-cycle/version context, evidence provenance and limitations.

Do not convert upstream abnormality into causal attribution. Causal Claim remains separately governed by REF-013–REF-020.

## Architecture boundary

Do not select Spark implementation patterns, SQL/DQX/Metric View rule syntax, Unity Catalog placement, graph engine, storage, streaming, caching, orchestration or service topology during Group 05.

Do not begin Group 05 or a later group without explicit user direction.