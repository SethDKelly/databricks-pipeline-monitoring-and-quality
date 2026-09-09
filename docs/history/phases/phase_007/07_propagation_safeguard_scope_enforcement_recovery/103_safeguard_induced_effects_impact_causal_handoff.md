# OPS-103 — Safeguard-Induced Effects, Impact & Causal Handoff

**Status:** Accepted — Phase 007 Group 07

## Purpose

Keep the protection control separate from operational effects and from causal assertions about those effects.

## Contract

Safeguard activity can coexist with independently evidenced:

- delayed publication/refresh;
- stale safe-state serving;
- non-delivery/unavailability;
- missed timing/readiness criterion;
- workload/consumer behavior changes;
- technical, analytical or business consequence.

Those facts remain Observation/Assessment/Execution History/Impact state. If asserting that safeguard enforcement caused/contributed to/prevented an outcome, create/evaluate the appropriate Causal Claim under OPS-060/082 and REF-013–REF-020, except the narrowly scoped prevented-exposure determination governed by REF-028/OPS-093.

## Invariants

- safeguard active ≠ safeguard caused delay.
- protection success ≠ consequence absence.
- delayed/non-delivered output ≠ defective safeguard design by default.
- causal attribution cannot outrun enforcement evidence.
