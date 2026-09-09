# HLTH-021 — Baseline Classes, Fixed/Rolling Reference & Version Semantics

**Status:** Accepted — Phase 006 Group 03

## Purpose

Define common functional Baseline classes without selecting a statistical algorithm.

## Functional classes

A Baseline may be defined as, for example:

- **fixed/reference-period** — a bounded historical period remains the reference until explicitly superseded;
- **rolling/adaptive** — the eligible reference window advances under an explicit membership/refresh rule;
- **seasonal/cadence-stratified** — comparison uses a matching calendar/cycle context;
- **cohort-segmented** — comparison uses a declared population/cohort context;
- **post-change/new-regime** — evidence accumulated after a material realized break forms a distinct reference regime.

These classes can compose; e.g. a rolling weekday Baseline for a particular cohort.

## Invariants

- Baseline class identifies reference semantics, not algorithm implementation.
- Rolling does not mean silently mutable. Material refresh produces a versioned derivation context and preserves earlier Assessments.
- Fixed does not mean universally permanent; realized change can make it non-comparable.
- A post-change Baseline is derived from post-change evidence, not the intended post-change target.
- One subject may legitimately have multiple Baselines for different contexts.
- `Most recent Baseline` is not an automatic resolution rule when multiple contexts match.

## Example

C may have a fixed month-end reference and a rolling ordinary-weekday reference. A month-end Tuesday is not automatically compared to the rolling weekday reference merely because that Baseline was refreshed yesterday.