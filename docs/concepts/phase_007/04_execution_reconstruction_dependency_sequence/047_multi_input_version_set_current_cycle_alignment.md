# OPS-047 — Multi-Input Version Set & Current-Cycle Alignment

**Status:** Accepted — Phase 007 Group 04

## Purpose

Represent the exact set of input versions a multi-input execution used without converting execution reconstruction itself into readiness/freshness Assessment.

## Contract

For each material input role, reconstruct the consumed input/version independently under OPS-039. The execution's **input-version set** is the collection of evidenced role bindings plus explicit unknown/conflicting/unavailable members.

A complete input-version set may support later reconciliation, freshness, readiness and Impact reasoning. It does not itself decide whether the set was acceptable/current.

A run can successfully consume:

- current A + current B;
- current A + stale B;
- old A + old B;
- mixed partitions/versions;
- an unresolved version for one input.

## Current-cycle boundary

`current-cycle`, `fresh`, `ready`, `expected version` and similar judgments remain Phase 006/REF-024 Assessment/readiness propositions. Execution History supplies the consumed-version evidence.

## Invariants

- multi-input run success ≠ all inputs current;
- one known input version ≠ complete input set;
- same calendar date/window ≠ same logical cycle;
- current active upstream deployment ≠ consumed upstream data version;
- version-set reconstruction ≠ health/readiness/cause.