# REF-006 — Temporal Coordinates and Evidence Availability

**Status:** Accepted — Phase 004 Group 02

## Purpose

Refine the time coordinates needed to reason honestly about when an event occurred, when evidence existed at a source, when the monitoring framework could use it, and when a derived conclusion was produced.

## Rule

Temporal reasoning distinguishes, where material:

- **event/effective time** — when the real-world condition/event/state applied;
- **source observation/production time** — when an evidence-producing system created or recorded its source fact;
- **source availability time** — when that source fact became queryable/obtainable from the source under the relevant integration contract;
- **collection/retrieval time** — when the monitoring framework fetched/received the evidence;
- **recorded/knowledge time** — when the evidence entered the framework's usable reasoning boundary;
- **evaluation time** — when an Assessment, Causal Claim status, Impact conclusion, gate-readiness result, Explanation, or other derived interpretation was actually produced;
- **correction/supersession time** — when a source or owning concept recorded a correction/supersession.

Not every evidence item must materialize every timestamp when the distinction is immaterial, but the model must not collapse coordinates whose difference changes historical truth or operational interpretation.

## Key boundaries

- source availability ≠ framework knowledge;
- framework knowledge ≠ derived evaluation;
- event time ≠ source production time ≠ ingestion time;
- later collection does not change the event/effective time of the fact;
- a current query of an old source fact gives the framework current knowledge unless retained evidence proves the framework knew it earlier;
- a source timestamp alone does not prove the framework had access to that evidence at that timestamp.

## Evidence-latency implication

The intervals between event time, source availability, framework knowledge, and evaluation time are themselves observable operational properties when evidence exists. They may later support monitoring-product latency objectives, but this refinement does not set SLAs or architecture.

## Example

A Databricks run finishes at 07:04. The run record becomes queryable at 07:04:05, the monitoring framework receives it at 07:04:09, and an execution-success validation is produced at 07:04:10. A Metric View refresh used for deeper quality Assessment may not become available until 07:08. These are different temporal facts; the early execution result does not wait for the later quality evidence.

## Non-goals

- choosing polling, streaming, event-bus, or storage technology;
- setting latency budgets;
- asserting that all sources expose source-availability timestamps;
- turning evidence latency into pipeline-health failure without an explicit Expectation.
