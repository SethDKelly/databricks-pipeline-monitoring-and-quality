# Phase 006 Agent Handoff

Applies to work under `docs/concepts/phase_006/` and complements the repository root `AGENTS.md` without replacing its accepted cross-phase rules.

## Current status

- Phase 006 is **ACTIVE**.
- Group 01 accepted: HLTH-001–HLTH-008; H01-01–H01-20 pass.
- Group 02 accepted: HLTH-009–HLTH-018; H02-01–H02-30 pass.
- Group 03 accepted: HLTH-019–HLTH-029; H03-01–H03-32 pass.
- Group 04 accepted: HLTH-030–HLTH-040; H04-01–H04-40 pass.
- Group 05 accepted: HLTH-041–HLTH-054; H05-01–H05-44 pass.
- **Group 06 — Composite Health, Readiness Suitability & Progressive Result Timing is next and has not started.**
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
- local Observation ≠ downstream-relevant context ≠ derived reconciliation Observation ≠ reconciliation Assessment;
- A+B→C does not imply generic row-count arithmetic or conservation;
- join match rate is directional and fan-out/cardinality is explicit;
- aggregation conservation is measure-specific; averages/ratios/quantiles/distinct counts are not generically composable;
- filter/dedupe/union/merge/null/default/value transformations create their own reconciliation semantics;
- output completion ≠ all required inputs current;
- multi-hop Lineage does not create transitive reconciliation formulas;
- reconciliation localization ≠ root cause;
- authority cannot manufacture evidence sufficiency or empirical comparability;
- passive monitoring remains non-blocking unless an explicitly governed active control later requires otherwise.

## Group 06 entry contract

Group 06 must compose existing local and reconciliation Assessments without erasing dimension state, conflict, unavailable/indeterminate evidence, warning/proximity, severity or waiver truth.

It must define functional result freshness/maturity and readiness suitability while preserving:

**health Assessment ≠ readiness Assessment ≠ gate decision ≠ enforcement ≠ actual execution**.

AUTH-023 high-consequence-use eligibility does not make a stale/unavailable/non-comparable/immature metric suitable for a particular control opportunity.

Do not introduce a universal numeric health/confidence score or majority/average roll-up that hides severe/conflicting/unknown child state.

## Architecture boundary

Do not select latency SLAs, caching/streaming architecture, DQX/Metric View computation placement, Spark/SQL implementation, scheduler/gate mechanism, storage, graph engine, or service topology during Group 06.

Do not begin Group 06 or a later group without explicit user direction.
