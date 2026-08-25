# OPS-045 — Execution / Output / Consumption Negative Claims & Coverage

**Status:** Accepted — Phase 007 Group 04

## Purpose

Apply Phase 004 negative-evidence discipline to claims that operational activity or outputs did not occur.

## Contract

Strong negative propositions include, among others:

- no qualifying execution occurred;
- no execution started;
- no terminal event occurred by a boundary;
- no qualifying output/version was produced;
- no input/version was consumed;
- no retry/restart occurred.

Such claims require proposition-specific opportunity-to-observe and sufficient bounded coverage under REF-002/REF-003/REF-005. Relevant dimensions can include subject/target, event family, time window, run class, source coverage, output/interface, version/partition, retry/backfill behavior and authorization.

## Vocabulary discipline

Prefer precise weaker statements where coverage is insufficient, such as:

- `no qualifying execution observed in available telemetry`;
- `output existence unknown`;
- `no consumption evidence available`.

Do not translate these into `did not run`, `produced nothing`, or `did not consume`.

## Invariants

- scheduler omission ≠ no execution;
- telemetry outage ≠ no execution;
- no terminal event ≠ run still running unless other evidence supports that;
- no output event ≠ no output;
- no version-use record ≠ non-consumption;
- restricted evidence ≠ negative evidence.