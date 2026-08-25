# OPS-077 — Repeated Encounter, First Exposure & Exposure Interval

**Status:** Accepted — Phase 007 Group 06

## Purpose

Represent repeated consumer encounters without collapsing them into one permanent exposed/not-exposed flag.

## Contract

Impact may record distinct encounter events or bounded intervals for the same consumer/state proposition, including:

- first sufficiently established affected-state encounter;
- repeated affected-state encounters;
- safe-state intervals before/after exposure;
- transition from unknown/safe state to affected state;
- cessation of affected-state encounter after supersession/recovery where evidenced.

`First exposure` is bounded by available opportunity/path/version evidence and may change retrospectively when late evidence arrives.

## Invariants

- exposed once ≠ exposed forever.
- later safe-state use does not erase earlier exposure.
- first observed encounter ≠ earliest true encounter absent sufficient historical coverage.
- exposure interval ≠ downstream effect interval by default.
