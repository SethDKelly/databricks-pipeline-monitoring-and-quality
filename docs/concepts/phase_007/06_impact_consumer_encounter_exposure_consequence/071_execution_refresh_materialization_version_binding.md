# OPS-071 — Execution, Refresh & Materialization Version Binding

**Status:** Accepted — Phase 007 Group 06

## Purpose

Connect Group 04 execution/output reconstruction to Impact exposure without letting timing or latest-state assumptions substitute for consumed-version evidence.

## Contract

For execution/refresh/materialization consumers, exposure may consume OPS-039/040/047 evidence that binds:

- consuming execution/refresh/materialization identity;
- producer/intermediary entity and role;
- exact input/output state/version where supportable;
- partition/window/population/interface scope;
- encounter time;
- provenance and limitations.

If Group 04 establishes only that the consumer ran/refreshed, Impact must not infer which producer state was used.

## Invariants

- latest producer output ≠ consumed output.
- producer completion before consumer start ≠ version consumption.
- active Deployment ≠ consumer exposure.
- successful downstream execution ≠ affected-state encounter unless its input binding is established.
- Group 04 version ambiguity propagates into Impact rather than being resolved by convenience.
