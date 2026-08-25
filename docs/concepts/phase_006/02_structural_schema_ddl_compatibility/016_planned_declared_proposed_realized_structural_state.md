# HLTH-016 — Planned, Declared, Proposed & Realized Structural State

**Status:** Accepted — Phase 006 Group 02

## Purpose

Separate pre-change structural validation from proof of realized production state so proactive DDL checks can coexist with post-deployment monitoring without one masquerading as the other.

## Structural horizons

The framework may reason about distinct structural states:

1. **current realized structure** — what evidence shows is active now;
2. **declared/governed structure** — the currently authoritative technical/schema declaration;
3. **proposed/planned structure** — Change Intent or deployment candidate not yet realized;
4. **prospective compatibility result** — evaluation of a proposed transition against known consumer contracts;
5. **realized compatibility result** — evaluation after evidence establishes which structure/interface actually became active;
6. **retrospective structural interpretation** — later reconstruction/correction using historical evidence.

## Invariants

- Passing a pre-deployment structural check proves only the bounded proposed-state proposition evaluated with the evidence/contracts known at that time.
- A GitHub Actions validation success does not prove the deployment occurred or the production schema matches the candidate.
- A realized catalog/schema Observation does not prove the change was planned or approved.
- Prospective compatibility may be revised when previously unknown consumers/contracts or realized differences become known.
- Planned/declared effective time does not backdate framework knowledge or prove actual activation time.
- If realized structure differs from the validated proposal, the prospective validation result remains historical evidence but does not apply automatically to the realized state.
- Validation can legitimately occur at several horizons; this contract does not choose GitHub Actions, Unity Catalog/Databricks, DQX, or the monitoring application as the execution location.

## Example

CI validates a proposed rename with an explicit compatibility mapping and passes all known consumers. Deployment later partially applies and leaves both old and new fields. The CI result remains valid for the proposal it evaluated, but the realized schema requires a new Observation and compatibility Assessment.