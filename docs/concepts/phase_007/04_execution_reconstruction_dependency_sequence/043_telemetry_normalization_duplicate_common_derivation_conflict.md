# OPS-043 — Telemetry Normalization, Duplication, Common Derivation & Conflict

**Status:** Accepted — Phase 007 Group 04

## Purpose

Reconstruct execution facts from multiple telemetry feeds without double-counting duplicated/common-derived events as independent evidence.

## Contract

Material telemetry retains, where available:

- source/event identity;
- source semantic event type/state;
- execution/task identity context;
- source event time;
- source production/availability time;
- framework knowledge/collection time;
- derivation/common-root relationship;
- correction/supersession relationship;
- restriction/availability limitations.

Exact duplicates can be co-referenced without becoming extra corroboration. Two feeds derived from one underlying orchestrator event remain common-derived evidence under REF-004.

## Conflict

If applicable sources disagree about the same bounded execution proposition and accepted authority/evidence semantics do not resolve the disagreement, preserve conflict. `Latest event`, `majority`, or `more sources` is not a hidden conflict-resolution rule.

## Invariants

- duplicate event ≠ retry attempt;
- duplicate/common-derived telemetry ≠ independent corroboration;
- out-of-order arrival ≠ reversed event chronology;
- source count ≠ evidence strength;
- normalization must not erase source semantics needed to explain conflict.