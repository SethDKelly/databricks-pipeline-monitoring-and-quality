---
name: dmtz-databricks-acquisition
description: Apply reviewed Databricks ingestion/pipeline guidance to DMTZ acquisition work without collapsing source availability, coverage, errors, source identity, or ingestion success into authoritative domain truth.
---

# DMTZ Databricks acquisition

## Human-directed boundary

Use only inside a human-selected acquisition task. Creating connections, pipelines, jobs, schedules, credentials, or running remote workloads is A3 unless explicitly authorized for the task.

Vendor skills are operational guidance, not DMTZ evidence/authority definitions.

## Workflow

1. Resolve active DMTZ acquisition contracts and implementation group first.
2. Read the reviewed vendor profile; when materialized, use `databricks-lakeflow-connect`, `databricks-pipelines`, `databricks-dabs`, `databricks-jobs`, and `databricks-unity-catalog` as relevant.
3. Preserve source-native IDs and provenance separately from canonical DMTZ identity.
4. Model connector/source denial, timeout, missing page, retention gap, schema failure, throttle, unsupported surface and partial coverage as acquisition/integration state—not observed negative truth.
5. Preserve source event/effective time, source availability time and DMTZ recorded/knowledge time where applicable.
6. Treat Lakeflow Connect/pipeline execution success as operational evidence only; it does not prove completeness, freshness, quality, health, authority or downstream effect.
7. Add the lowest-cost tests for failure/partial/unknown paths before claiming acquisition semantics are implemented.

## Output expectations

Produce acquisition code/config/evidence mapping that retains provenance, partiality, exact source identity and explicit limitations.

## Stop conditions

Stop on unresolved workspace/profile/credential authority, unsupported target capability, an attempted false-negative inference, or any need to weaken accepted REF/INTG/AUTH semantics.
