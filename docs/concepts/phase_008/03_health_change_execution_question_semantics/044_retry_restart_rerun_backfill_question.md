# EXPL-044 — Retry, Restart, Rerun & Backfill Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

Questions about repeated execution preserve source-specific continuity semantics for attempt, retry, restart/resume, rerun and backfill.

## Rules

- these terms are not universal synonyms;
- one logical execution may have multiple attempts where source semantics establish continuity;
- a rerun/backfill may be a separate execution even when it uses the same job definition;
- later successful repeated activity does not rewrite earlier failure;
- backfill success does not automatically establish current-cycle freshness/currentness;
- answer scope must identify whether it refers to attempt, logical execution, cycle or historical data interval.