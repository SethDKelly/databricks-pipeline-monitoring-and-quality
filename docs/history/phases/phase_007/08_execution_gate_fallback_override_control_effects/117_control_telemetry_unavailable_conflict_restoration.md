# OPS-117 — Control Telemetry Unavailability, Conflict & Restoration

**Status:** Accepted — Phase 007 Group 08

## Purpose

Apply REF-029 to Gate-specific degradation and later control restoration without inventing production behavior.

## Distinct states

Preserve where material:

- readiness evidence unknown/unavailable/conflicting;
- Gate decision unknown/unavailable/conflicting;
- decision delivery unknown;
- enforcement unknown/contradicted;
- control integration degraded/unavailable;
- configured fallback known;
- actual fallback application known/unknown;
- control integration restored.

## Rules

- a downstream run during control degradation does not by itself prove fail-open or fallback admission;
- no downstream run does not prove fail-closed or successful hold;
- restored control telemetry/availability does not automatically ADMIT, HOLD or reevaluate an opportunity;
- late telemetry may change retrospective enforcement understanding while preserving actual historical decisions/executions;
- passive/ungated production availability remains independent from Gate-control degradation.