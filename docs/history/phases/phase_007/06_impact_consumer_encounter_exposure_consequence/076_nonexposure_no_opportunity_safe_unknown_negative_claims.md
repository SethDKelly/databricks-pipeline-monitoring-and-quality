# OPS-076 — Non-Exposure, No Opportunity, Safe-State & Unknown Negative Claims

**Status:** Accepted — Phase 007 Group 06

## Purpose

Specialize REF-023 using Groups 01 and 04 so strong downstream negatives cannot be manufactured from telemetry gaps.

## Contract

`Not exposed to affected state V during W` requires sufficient evidence for the relevant opportunity, encounter modes and material alternate paths.

Useful weaker/distinct findings include:

- no relevant encounter opportunity established;
- opportunity occurred but no qualifying encounter occurred;
- safe/other state was encountered;
- encounter occurred but state/version is unknown;
- path/consumer telemetry is missing, conflicting, unavailable or restricted;
- only some material paths have been excluded.

`No refresh/query/use observed` is not itself a strong negative unless the source had adequate opportunity-to-observe and coverage.

## Invariants

- missing telemetry ≠ no encounter.
- no reported consumer issue ≠ not exposed.
- not exposed to V ≠ no activity.
- not exposed to V ≠ fresh/current/healthy.
- negative conclusions remain scope/time/path/version specific.
