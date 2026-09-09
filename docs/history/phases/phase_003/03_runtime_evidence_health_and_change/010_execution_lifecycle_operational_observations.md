# SYN-010 — Execution Lifecycle → Operational Timing Observations

**Status:** Accepted — Phase 003 Group 03

## Outcome

Turn execution lifecycle evidence into provenance-bearing operational facts such as start time, completion time, duration, queue/wait interval, and other measurable timing properties without interpreting whether they are acceptable.

## Participating concepts and actions

- **Execution History** — `resolveAt`.
- **Observation** — `record`, `correct`, `retrieve`.

## Trigger / initiating condition

Execution state arrives or operational timing is requested for a run/pipeline.

## Preconditions

The execution and required source timestamps/coverage are sufficiently established for the fact being derived.

## Coordination semantics

- Record start/completion/outcome facts with source/effective times.
- Derive run duration only when compatible start/completion evidence exists.
- Derive queue/wait/processing intervals only when their defining timestamps are available and semantically comparable.
- Record actual cadence/inter-run intervals from execution evidence; do not infer an expected cadence here.
- Preserve source-specific timing semantics when they cannot be safely normalized.
- Missing completion/start evidence yields insufficient timing evidence, not zero duration.

## State and evidence effects

Execution History owns lifecycle state; Observation owns measured/derived timing facts and their derivation provenance.

## Ambiguity / failure propagation

Clock inconsistencies, partial task evidence, retries, overlapping runs, missing timestamps, or ambiguous logical-run assembly remain limitations. A source outage does not become a zero-length or missed run.

## Temporal semantics

Actual run timestamps are event times. Observation collection/derivation time remains distinct. Late-arriving run completion can create a later duration Observation without changing when the run occurred.

## Provenance / traceability

Derived duration retains the execution/timestamp evidence used to calculate it.

## Security / authorization

Operational timing can expose business schedules and infrastructure behavior; safe abstraction may expose `running unusually long` later without exact restricted timing details.

## Invariants

- execution duration is an Observation, not an Assessment;
- long runtime is not automatically degradation;
- successful completion is not timely completion;
- runtime timing is distinct from output data freshness;
- missing telemetry is not observed absence.

## Scenarios

A job normally runs 20 minutes but takes 55; a run is still in progress; a retry overlaps; completion arrives late; task timing is visible while logical-run duration remains unresolved.

## Non-goals

Defining runtime SLOs, Baseline algorithms, anomaly thresholds, or causal explanation.
