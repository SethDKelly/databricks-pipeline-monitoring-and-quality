# OPS-034 — Execution Proposition Identity & Lifecycle Event Binding

**Status:** Accepted — Phase 007 Group 04

## Purpose

Define an actual execution as an evidence-bound proposition rather than a schedule slot, job name, repository revision or inferred row in an operations timeline.

## Contract

A material execution proposition binds, where applicable:

- logical execution subject / Entity Identity;
- execution-instance identity or bounded identity evidence;
- lower-level run/job/task identity when present;
- target/environment/context;
- execution attempt identity when multiple attempts matter;
- source lifecycle event semantics;
- source event/effective time;
- framework knowledge/collection time;
- parent/child/orchestration context when evidenced;
- provenance, limitations, conflict and correction state.

An execution instance exists only when applicable evidence establishes that an actual execution/run instance existed. Schedule, readiness, gate, deployment and Lineage context can constrain interpretation but cannot create the instance.

## Lifecycle evidence

Start, running/progress, terminal-state and other lifecycle facts are independently evidentiary. A terminal event may be known while start is missing; a start may be known while completion remains unknown. The framework must not fabricate intermediate transitions merely to produce a complete-looking lifecycle.

Source-specific state may be normalized only when its semantic equivalence is established. Otherwise preserve the source state plus any bounded higher-level interpretation.

## Invariants

- schedule/opportunity ≠ execution instance;
- job/task identifier ≠ logical execution identity;
- observed start ≠ observed completion;
- terminal state ≠ output existence/health;
- missing lifecycle event ≠ negative event;
- current source state is not projected backward onto historical execution state.

## Handoff

OPS-035 separates execution opportunities from actual executions. OPS-036 defines evidence-based assembly of logical executions from lower-level runs/tasks.