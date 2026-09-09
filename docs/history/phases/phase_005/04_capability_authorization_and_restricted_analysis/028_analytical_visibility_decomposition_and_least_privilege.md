# AUTH-028 — Analytical Visibility Decomposition and Least Privilege

**Status:** Accepted — Phase 005 Group 04

## Purpose

Make useful monitoring/RCA access possible without treating an asset as simply `visible` or `hidden` and without requiring direct row access for every analytical task.

## Decomposed visibility

A requester may independently be permitted to view, for example:

- raw rows or samples;
- sensitive fields/values;
- technical schema/field names;
- semantic/governance summaries;
- exact metric/Observation values;
- Assessment/health status without the exact value;
- exact Expectations/thresholds/margins;
- Baseline details;
- Lineage node identity versus opaque dependency/path existence;
- Investigation state and RCA evidence;
- Causal Claim status versus restricted causal basis;
- Impact/exposure/consequence detail;
- gate/safeguard state;
- authority/authorization basis details;
- Explanation/report output.

## Invariants

- Raw-data denial does not automatically deny approved derived health/RCA visibility.
- Derived-health permission does not automatically expose raw values, thresholds, schemas, Baselines, or every underlying Observation.
- Permission to see a violation does not necessarily include permission to see the sensitive threshold or offending value.
- Permission to traverse Lineage can be narrower than permission to identify every node/edge.
- Investigation participation may proceed over partial/opaque evidence and must retain the visibility limitation.
- Metadata, counts, thresholds, schemas, topology, policy labels, control state, and derived metrics can themselves be sensitive.
- Least privilege is capability/detail specific; it is not a blanket `metadata is safe` assumption.
