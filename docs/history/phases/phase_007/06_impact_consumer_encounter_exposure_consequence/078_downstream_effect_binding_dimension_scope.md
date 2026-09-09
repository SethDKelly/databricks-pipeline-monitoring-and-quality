# OPS-078 — Downstream Effect Binding & Dimension Scope

**Status:** Accepted — Phase 007 Group 06

## Purpose

Keep downstream effect evidence separate from exposure while consuming Phase 006 Observation/Assessment/Change truth precisely.

## Contract

A downstream-effect association binds:

- consumer/downstream subject and exact use/population/interface context;
- effect dimension such as execution, freshness, completeness, validity, volume, schema, metric/result, availability or delivery;
- source Observation/Assessment/Change evidence and its basis;
- event/effective time and knowledge cut;
- whether exposure to the originating state is exposed/not-exposed/unknown independently.

Effect evidence remains owned by its source concept; Impact owns only its relevance to the downstream picture.

## Invariants

- exposed ≠ effect.
- effect ≠ origin-caused effect.
- healthy/unchanged on one monitored dimension ≠ no effect on all dimensions.
- unknown exposure does not erase independently established downstream effect.
- effect timing may differ from first encounter timing.
