# OPS-068 — Encounter Opportunity, Availability, Publication & Actual Encounter

**Status:** Accepted — Phase 007 Group 06

## Purpose

Separate conditions that make encounter possible from evidence that encounter actually occurred.

## Contract

Preserve the following propositions independently:

1. **encounter opportunity** — a qualifying refresh/run/query/use opportunity existed;
2. **state availability** — a producer/intermediary state was available to the relevant boundary;
3. **publication/serving** — a state was actually published/served through a boundary;
4. **actual encounter** — the consumer used/read/materialized/consumed the state under the bound encounter mode.

A publication may exist with no consumer opportunity. A consumer opportunity may occur while a safe prior state is served. A suspect state may be served but never actually used by the end consumer.

## Invariants

- available ≠ published/served.
- published/served ≠ actually encountered when the proposition is downstream use.
- opportunity ≠ encounter.
- downstream activity after publication ≠ suspect-state encounter without binding evidence.
- no opportunity may support a bounded non-exposure result only when the opportunity/path coverage is itself sufficiently established.
