# Phase 006 Agent Handoff

Applies to work under `docs/concepts/phase_006/` and complements the repository root `AGENTS.md` without replacing its accepted cross-phase rules.

## Current status

- Phase 006 is **ACTIVE**.
- Group 01 accepted: HLTH-001–HLTH-008; H01-01–H01-20 pass.
- Group 02 accepted: HLTH-009–HLTH-018; H02-01–H02-30 pass.
- Group 03 accepted: HLTH-019–HLTH-029; H03-01–H03-32 pass.
- Group 04 accepted: HLTH-030–HLTH-040; H04-01–H04-40 pass.
- Group 05 accepted: HLTH-041–HLTH-054; H05-01–H05-44 pass.
- Group 06 accepted: HLTH-055–HLTH-066; H06-01–H06-44 pass.
- **Group 07 — Consolidation / Exit Review is next and has not started.**
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
- reconciliation localization ≠ root cause;
- component Assessment ≠ composite health Assessment;
- composite health ≠ readiness suitability ≠ readiness result ≠ gate decision ≠ enforcement ≠ actual execution;
- evaluation recency ≠ evidence freshness/current-cycle validity;
- result freshness/maturity is exact-use specific; no universal TTL;
- a suitable violation can support `not ready`; a stale `meets` result can be unsuitable;
- AUTH-023 eligibility ≠ current evidence freshness/comparability/availability/maturity ≠ control authority;
- narrow trustworthy results do not wait for slower unrelated evidence;
- elapsed time never upgrades result maturity;
- passive monitoring remains non-blocking unless an explicitly governed active control requires otherwise;
- authority cannot manufacture evidence sufficiency or empirical comparability.

## Group 07 entry contract

Replay Groups 01–06 end-to-end. Do not add a new Concept or HLTH contract merely for summary convenience. Add one only if a genuine independent truth owner or unresolved semantic gap is exposed by consolidation.

Verify especially:

- composite health is profile/use/context bound and dimension-preserving;
- required violation + unresolved component remains degraded with unresolved qualifier rather than becoming clean or unknown-only;
- `healthy` requires positive resolution of all applicable required predicates under the accepted profile logic;
- warnings, waivers, severity, conflict, unavailability and Baseline typicality remain separate;
- consumer-specific composites differ only because their bound propositions/profiles differ;
- recent recomputation does not make stale evidence current;
- progressive horizons preserve narrow early results while broader health matures;
- readiness suitability is outcome-neutral and exact-opportunity bound;
- AUTH-023 eligibility plus evidence suitability still does not create a gate decision or enforcement;
- historical composite/suitability/readiness replay is non-rewriting.

## Architecture boundary

Do not select latency SLAs, caching/streaming architecture, DQX/Metric View computation placement, Spark/SQL implementation, scheduler/gate mechanism, storage, graph engine, or service topology during Group 07 merely to close Phase 006.

Do not begin Group 07 or a later phase without explicit user direction.