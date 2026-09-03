---
name: dmtz-databricks-runtime-provenance
description: Apply Databricks Jobs/Pipelines runtime guidance to DMTZ provenance without using names, timestamps, execution success, or deployment proximity as identity, freshness, health, or causality proxies.
---

# DMTZ Databricks runtime provenance

## Human-directed boundary

Remote Jobs/Pipelines reads or runs require the corresponding authorized task. Vendor operational identifiers are evidence inputs, not canonical DMTZ identity by default.

## Workflow

1. Resolve active runtime-provenance and correlation contracts before adapter work.
2. Use reviewed `databricks-jobs`, `databricks-pipelines`, `databricks-dabs` and `databricks-core` guidance when materialized.
3. Preserve stable Databricks job/run/task/pipeline/update/deployment identifiers and source provenance.
4. Establish canonical associations only through accepted stable IDs, explicit correlation or attestation—not names or timestamp proximity.
5. Keep execution success distinct from timely run, freshness, structural compatibility and data quality.
6. Preserve partial run/task evidence and unknown correlation states.
7. Treat deployment correlation as correlation unless causal confirmation requirements are independently satisfied.
8. Test duplicate names, delayed telemetry, retries and partial task evidence.

## Output expectations

Provide exact source identifiers/correlation basis plus limitations; never summarize ambiguous correlation as confirmed identity or cause.

## Stop conditions

Stop when only name/time proximity supports the association, telemetry is incomplete but a definitive claim is requested, or remote execution/deployment is not explicitly authorized.
