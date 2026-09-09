# OPS-042 — Mid-Execution Activation, Rollback & Dynamic State

**Status:** Accepted — Phase 007 Group 04

## Purpose

Handle long-running or multi-stage executions that overlap implementation-state transitions without assuming the run switched—or did not switch—state globally.

## Contract

When activation/supersession/rollback occurs during an execution, reconstruction asks per material implementation facet:

- when was the facet bound for this run/task;
- is it launch/start-bound, task-bound, dynamically read, or otherwise governed by known runtime semantics;
- did lower-level tasks bind at different times/states;
- what direct evidence establishes the state actually used.

These are functional questions, not architecture selections.

A run spanning R1→R2 may remain on R1, use R2 for later tasks, dynamically observe selected configuration changes, or remain indeterminate. The Deployment timeline alone cannot decide.

Rollback during a run similarly does not prove the run reverted.

## Invariants

- activation during run ≠ automatic in-flight switch;
- rollback during run ≠ automatic in-flight reversion;
- one facet switching ≠ every facet switching;
- parent run version ≠ every child/task version by assumption;
- unresolved binding remains unresolved rather than choosing start-time or completion-time state by convenience.