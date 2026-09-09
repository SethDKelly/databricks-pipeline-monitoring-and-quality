# HLTH-061 — Health Result Age, Evidence Freshness & Use-Specific Staleness

**Status:** Accepted — Phase 006 Group 06

## Purpose

Define freshness/age for health results without confusing evaluation recency with evidence recency or imposing one universal TTL.

## Distinct times

Preserve where material:

- Observation event/effective/window time;
- source availability time;
- framework recorded/knowledge time;
- Assessment evaluation time;
- newest/oldest required evidence time;
- intended operational/readiness-use opportunity time.

## Rules

- A recently recomputed Assessment over old evidence can still be stale for a current-cycle use.
- An older Assessment can remain usable when the exact use criterion explicitly permits its evidence age/context.
- `stale for use U` is a suitability conclusion, not automatically a normative health violation unless an applicable freshness Expectation is itself violated.
- Different uses may have different valid freshness requirements for the same result.
- Current-cycle identity/version alignment matters independently from wall-clock age.
- Cached/retained prior evidence is not silently treated as current simply because the latest query failed.
- No universal health-result TTL, staleness threshold, or source-age SLA is selected in Phase 006.
- Historical age/freshness evaluations retain the then-applicable use criterion/version.

## Invariant

Evaluation timestamp alone never proves current evidence.