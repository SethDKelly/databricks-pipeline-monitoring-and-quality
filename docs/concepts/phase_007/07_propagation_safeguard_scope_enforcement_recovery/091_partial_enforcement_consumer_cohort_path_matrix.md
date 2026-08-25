# OPS-091 — Partial Enforcement Across Consumers, Cohorts & Paths

**Status:** Accepted — Phase 007 Group 07

## Purpose

Make partial protection first-class instead of forcing a safeguard to be globally active or failed.

## Contract

Enforcement may resolve independently by:

- consumer;
- publication/consumption path;
- environment/region;
- cohort/population;
- version/state;
- interval/opportunity.

A bounded view may therefore contain enforced, not enforced, conflicting, indeterminate or unavailable members simultaneously.

## Invariants

- partial enforcement ≠ total safeguard failure.
- partial enforcement ≠ global protection.
- successful protection of one consumer cannot hide exposure of another.
- aggregate summaries must preserve material unprotected/unknown members.
- no universal enforcement percentage is required or accepted as a truth substitute.
