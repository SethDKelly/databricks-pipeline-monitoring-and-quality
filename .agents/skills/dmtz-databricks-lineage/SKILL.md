---
name: dmtz-databricks-lineage
description: Use reviewed Unity Catalog/system-table lineage guidance as DMTZ Lineage evidence without inferring encounter, exposure, Impact, causal confirmation, or business consequence from topology alone.
---

# DMTZ Databricks lineage

## Human-directed boundary

Read/query of live Unity Catalog/system tables requires task-authorized workspace access. Lineage evidence never grants authority to make causal or Impact claims beyond accepted DMTZ contracts.

## Workflow

1. Resolve the applicable INTG/OPS/ARCH Lineage and Impact contracts.
2. Read the reviewed `databricks-unity-catalog` and `databricks-dbsql` vendor skills when materialized.
3. Capture exact lineage identifiers, direction, granularity, event/observation time and known coverage limitations.
4. Keep Lineage distinct from consumer encounter/exposure.
5. Keep exposure distinct from downstream effect and business consequence.
6. Do not treat topology, dependency reachability or temporal correlation as cause.
7. When system-table coverage is missing, stale, retained-out or unauthorized, represent that limitation explicitly.
8. Add tests/scenarios that prove topology evidence cannot manufacture Impact or causal confirmation.

## Output expectations

Return lineage evidence with source/coverage/time limitations and explicit statement of which stronger propositions are not established.

## Stop conditions

Stop on causal/Impact inference unsupported by the accepted contracts, unresolved system-table coverage, or unauthorized workspace query.
