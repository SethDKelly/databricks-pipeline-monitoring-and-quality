# REF-009 — Progressive Evidence Availability and Analytical Maturity

**Status:** Accepted — Phase 004 Group 02

## Purpose

Allow monitoring and reasoning results to become available progressively as different evidence classes arrive, without forcing fast conclusions to wait for slower enrichment and without presenting early partial knowledge as complete.

## Principle

The framework should produce the **narrowest trustworthy result as soon as the evidence required for that result is known**, subject to the applicable evidence standard and authorization. Later-arriving evidence may enrich, qualify, contradict, or supersede the current retrospective interpretation.

A broader conclusion must not be emitted early merely because a narrower fast-path conclusion is available.

## Functional analytical horizons

The project recognizes provisional functional horizons without yet setting concrete latency targets:

1. **Immediate operational validation** — evidence such as run started/completed/succeeded/failed, queue/duration facts, obvious dependency state, or directly available output existence.
2. **Enriched health evaluation** — additional quality/freshness/Metric View/DQ evidence, comparable Baseline context, or richer semantic/governance context becomes available.
3. **Investigative / RCA reasoning** — historical Lineage, change/deployment evidence, competing hypotheses, consumption evidence, and analyst research are assembled and evaluated.
4. **Retrospective / post-operations review** — late/corrected evidence, complete incident windows, downstream consequence evidence, and historical comparison may produce a more mature retrospective result.

These are reasoning/evidence-availability horizons, not fixed services, jobs, UI screens, SLAs, or architecture tiers.

## Rules

- a fast operational result does not wait for slower Metric View, downstream-consumption, or RCA evidence unless that slower evidence is required by the specific conclusion or control decision;
- an early answer carries its knowledge cutoff, evidence limitations, and conclusion scope;
- later enrichment creates a later knowledge/evaluation state rather than silently editing what was known earlier;
- `job succeeded` must not be displayed as `pipeline healthy` merely because deeper health evidence is not yet available;
- `health evidence pending` is preferable to assuming healthy or failed;
- high-consequence decisions such as gate admission, safeguard activation/release, or causal confirmation may require evidence unavailable to a fast path and cannot bypass their standard for latency convenience;
- availability targets for these horizons must not make passive monitoring a production critical-path dependency for ungated jobs.

## Timing handoff

Later phases must turn this functional model into explicit product/technical objectives:

- **Phase 006** — define which health/quality outputs belong to which analytical horizon and what freshness/latency expectations they need;
- **Phase 009** — map Databricks, Metric Views, DQX, GitHub, governance, consumption, and other sources to evidence availability/collection characteristics;
- **Phase 010** — select asynchronous/streaming/polling/cache/compute architecture and performance budgets while preserving passive-monitoring non-interference;
- **Phase 011** — convert accepted latency objectives into MVP acceptance criteria.

## Example

At 07:04 the framework can establish that Job C succeeded. At 07:05 it can establish that the expected output exists and is fresh. At 07:08 a Metric View provides completeness evidence showing a violation. At 07:15 Lineage/change evidence supports an RCA hypothesis. The next morning late downstream usage evidence changes the retrospective Impact.

Each result is valid only for its own proposition and knowledge cut. The 07:04 success statement remains historically valid; it never implied that quality was healthy.

## Non-goals

- selecting fixed latency numbers;
- defining service boundaries;
- requiring every health metric to be real-time;
- delaying production to improve monitoring completeness;
- allowing a low-latency shortcut to weaken a high-consequence evidence standard.
