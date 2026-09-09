# OPS-075 — Alternate Encounter Paths, Partial Path Coverage & Aggregation

**Status:** Accepted — Phase 007 Group 06

## Purpose

Handle consumers that can receive/use data through several publication, refresh, cache, API or other paths.

## Contract

Impact evaluates path-specific encounter propositions before making a consumer-wide exposure conclusion when multiple material paths exist.

- exposure through any qualifying path can establish consumer exposure to the bound state;
- path-specific non-exposure does not establish consumer-wide non-exposure while another material path remains unknown;
- safe-state use on one path can coexist with suspect-state exposure on another;
- path aggregation retains which path established the conclusion and which paths remain unresolved.

The material path set is bounded by historical Lineage/consumer semantics and REF coverage; it is not assumed globally complete.

## Invariants

- one safe path ≠ global non-exposure.
- one unknown alternate path can prevent a strong global negative.
- duplicate telemetry for the same path does not become independent path corroboration.
- path count is not impact severity/probability.
