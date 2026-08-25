# OPS-040 — Produced Output / Version Binding & Qualification

**Status:** Accepted — Phase 007 Group 04

## Purpose

Separate execution lifecycle outcome from evidence that an execution produced a particular material output/version.

## Contract

An output proposition binds, where applicable:

- producing execution/attempt;
- produced Entity Identity/interface;
- output/data/version identity;
- partition/window/population;
- production/materialization/commit/publication timing where those meanings differ;
- provenance/evidence basis;
- knowledge/correction time;
- completeness/qualification limitations.

A terminally successful execution does not automatically prove a qualifying output exists. Conversely, a failed/cancelled/partial execution may have produced material intermediate or committed output that must not be erased merely because the terminal outcome was unsuccessful.

## Qualifying output

`Output exists` is weaker than criterion-specific propositions such as:

- committed/materialized output exists;
- publication became available;
- current-cycle output exists;
- output has the expected version;
- output is fresh/healthy/ready.

Those stronger propositions consume their owning semantics rather than being inferred from output existence.

## Invariants

- run success ≠ output existence;
- output existence ≠ publication availability;
- output existence ≠ current-cycle/fresh/healthy/ready;
- failed run ≠ no output;
- no output is a negative claim requiring OPS-045 coverage.