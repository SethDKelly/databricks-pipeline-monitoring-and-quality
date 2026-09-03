---
name: dmtz-databricks-persistence
description: Apply Databricks Delta/pipeline/SQL guidance to DMTZ canonical persistence while preserving non-rewriting history, event-vs-knowledge time, correction history, and rebuildable projection boundaries.
---

# DMTZ Databricks persistence

## Human-directed boundary

Use within an explicitly selected persistence/schema task. Remote table/schema creation, deployment or data mutation is A3 unless explicitly authorized. Databricks storage behavior does not redefine DMTZ temporal semantics.

## Workflow

1. Resolve the accepted REF/SYN/ARCH persistence and temporal contracts first.
2. Read the reviewed vendor profile; use `databricks-pipelines`, `databricks-dbsql`, `databricks-dabs` and `databricks-unity-catalog` when materialized and relevant.
3. Keep canonical IDs distinct from source-local IDs.
4. Represent event/effective time separately from DMTZ knowledge/recorded time.
5. Preserve corrections/supersession without rewriting the prior as-known state.
6. Use Delta capabilities as implementation mechanisms; do not define historical/as-known replay solely as Delta time travel.
7. Keep graph/search/cache/read models rebuildable from canonical history.
8. Test late evidence and correction behavior at explicit knowledge cuts.

## Output expectations

Persistence realization must show how current and historical/as-known answers remain distinguishable and traceable.

## Stop conditions

Stop if the design would overwrite prior truth, collapse time dimensions, make a projection canonical, or require changing frozen temporal contracts for implementation convenience.
