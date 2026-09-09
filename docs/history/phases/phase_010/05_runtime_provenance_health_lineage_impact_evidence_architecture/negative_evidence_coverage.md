# Operational / Impact Negative-Evidence Coverage

## Principle

Strong negatives require a known denominator/opportunity and known observation coverage.

## `no run`

Requires expected run/opportunity population, source-native execution coverage, acquisition health and source publication-lag compatibility.

## `no output`

Requires expected output(s), write/output telemetry coverage and healthy relevant acquisition. Run failure/success is insufficient.

## `no measurement / no violation`

Requires expected applicable measurement/check population plus evaluation coverage. Missing rule/scan/integration does not count as pass.

## `no dependency`

Requires bounded topology scope and sufficient Lineage/source coverage. Databricks documents lineage as incomplete, so absence of a lineage event cannot be a universal negative.

## `not exposed`

Requires bounded consumers/paths/opportunities plus sufficient encounter and exact-version/state coverage for the interval.

## `no effect / no consequence`

Requires bounded effect/consequence population and adequate outcome telemetry. A safe/no-exposure path may reduce opportunity but does not generally prove every downstream outcome proposition.

## Acquisition dependency

Every negative-evidence evaluation consumes Group 04:

- expected Monitoring Scope/materialization
- page/partition/window completion
- integration health
- source publication lag
- retention reachability
- parser/schema state

A recovered connector does not retroactively repair an uncovered historical interval.