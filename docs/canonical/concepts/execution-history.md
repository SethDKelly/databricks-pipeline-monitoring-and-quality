# Execution History

**Canonical key:** `concept.execution_history`

**Kind:** CONCEPT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `concept.execution_history`

**Owns current question:** Which execution instances actually occurred and what lifecycle/run-specific state is evidenced for them?

**Stable IDs:** N/A

## Current semantics

Execution History owns execution identity/correlation, lifecycle events, attempts/retries/restarts/reruns/backfills, actual timing/outcome, parent/child and sequence evidence, run-specific implementation/input/output version bindings where established, provenance/knowledge time, coverage/conflict, and correction/reassembly history.

## Actions

- `recordState` — append an evidenced lifecycle event/state.
- `associateExecution` — assemble lower-level run/task evidence into a logical execution only with sufficient identity/correlation evidence.
- `associateImplementationState` — bind run-specific implementation state when evidenced.
- `associateInputVersion` — bind actual encountered/consumed input/version when evidenced.
- `associateOutputVersion` — bind produced/materialized output/version when evidenced.
- `correctState` — preserve correction/reassembly without rewriting history.
- `resolveAt` — reconstruct execution/lifecycle/ordering/version context with limitations.

## Invariants / boundaries

- Expected work/opportunity/Execution Gate state does not create an execution instance.
- Gate HOLD ≠ failed run; Gate ADMIT/override ≠ run occurred.
- Execution success ≠ output existence ≠ timely execution ≠ freshness ≠ data quality/readiness.
- Missing telemetry ≠ no run/no output/no consumption; negatives require bounded opportunity/coverage.
- Logical execution/retry/rerun/backfill continuity is evidence/source-semantics dependent, not name/time inference.
- Lineage/dependency order ≠ actual waiting/precedence/consumed-version proof.
- Active Deployment-at-time constrains context but does not universally prove run-specific implementation state.
- Latest upstream output is not automatically what downstream consumed.
- Event/effective and knowledge/record time remain separate; no universal reconstruction-confidence score is accepted.

## Ambiguity / evidence

Partial, duplicated/common-derived, conflicting, late, unavailable, clock-misaligned, or unauthorized run evidence remains explicit.

## Synchronizations / related canonical resources

Deployment supplies active-state context; Observation may record run/data facts; Expectation/Assessment own expected-work interpretation; Lineage owns topology; Execution Gate owns admission; Impact may consume exact encounter/version evidence; Causal Claim owns attribution.

## Non-goals

Schedules/expectations, gate decisions, health/readiness, Deployment truth, causality, or orchestration replacement.

## Provenance

- `docs/concepts/phase_002/04_history_lineage_change/execution_history.md`
- `docs/concepts/phase_007/04_execution_reconstruction_dependency_sequence/`
