# OPS-046 — Partial Execution Evidence, Terminal Resolution & Level Scope

**Status:** Accepted — Phase 007 Group 04

## Purpose

Keep incomplete lifecycle evidence honest and prevent lower-level task states from being silently promoted to whole-execution outcomes.

## Contract

Execution reconstruction may legitimately resolve as:

- established execution with partial lifecycle evidence;
- established start with terminal state unknown;
- terminal state established with start/time details incomplete;
- lower-level task/job states established while logical execution outcome is unresolved;
- conflicting terminal state;
- unavailable/restricted lifecycle detail;
- identity/assembly indeterminate.

`failed`, `cancelled`, `timed out`, `skipped`, `terminated`, `successful` or similar normalized outcomes are used only where their bounded semantics are supported. A source-specific state can remain source-specific if normalization would overstate meaning.

## Level discipline

Task/job/root logical execution outcomes remain separate. One child failure may or may not determine the root outcome depending on explicit orchestration semantics; a root success does not erase failed/retried child attempts.

## Invariants

- incomplete lifecycle ≠ failed;
- missing completion ≠ running indefinitely;
- child failure ≠ root failure by assumption;
- root success ≠ every child succeeded;
- terminal outcome ≠ output/health state.