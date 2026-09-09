# OPS-036 — Logical Execution Assembly, Parent/Child & Multi-Job Association

**Status:** Accepted — Phase 007 Group 04

## Purpose

Allow one logical pipeline execution to be reconstructed from lower-level jobs/tasks/runs without assuming one platform job equals one logical execution.

## Contract

Association of lower-level evidence into a logical execution requires applicable identity/context evidence such as, where available:

- explicit parent/root execution identity;
- invocation/correlation context;
- target/environment;
- logical pipeline/version context;
- bounded time/context relationship;
- explicit dependency/orchestration references;
- other provenance-bearing linkage.

Temporal overlap, naming similarity or repository membership alone is insufficient.

## Partial assembly

A reconstruction may legitimately contain:

- one established root with some unresolved children;
- several established lower-level executions with no sufficiently evidenced common logical parent;
- competing possible assemblies;
- restricted child identities;
- later correction that reassigns a child while preserving the earlier as-known assembly.

## Invariants

- one logical pipeline ≠ one job/task by assumption;
- one job/task definition may participate in many execution instances;
- overlapping executions must not be merged merely because their windows overlap;
- child success/failure does not automatically define logical-execution outcome absent explicit composition semantics;
- assembly confidence is expressed through REF evidence/limitations, not a universal score.