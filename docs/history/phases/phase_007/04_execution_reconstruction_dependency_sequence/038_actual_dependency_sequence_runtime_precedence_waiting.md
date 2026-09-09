# OPS-038 — Actual Dependency Sequence, Runtime Precedence & Waiting

**Status:** Accepted — Phase 007 Group 04

## Purpose

Separate intended dependency/schedule structure from what runtime evidence establishes actually happened.

## Contract

For two executions A and C, preserve distinct propositions such as:

- A is an effective `operational_dependency` of C under Lineage;
- A was expected/scheduled before C;
- A completed before C started;
- C was held/waiting for A under evidenced orchestration/control semantics;
- C started after a qualifying A condition became true;
- C consumed a specific A output/version under OPS-039.

None is a synonym for the others.

## Ordering evidence

Actual temporal precedence can be established through applicable source-local sequence/event evidence, compatible timestamps or explicit orchestration relationships. Cross-source timestamp comparison may remain indeterminate under OPS-044.

An actual ordering violation can be described where the relevant intended/required order is separately established, but sequence alone does not establish health or causality.

## Invariants

- Lineage dependency ≠ runtime wait;
- scheduled order ≠ actual order;
- `A ended before C started` ≠ `C waited for A`;
- actual order ≠ consumed-version proof;
- temporal precedence ≠ cause.