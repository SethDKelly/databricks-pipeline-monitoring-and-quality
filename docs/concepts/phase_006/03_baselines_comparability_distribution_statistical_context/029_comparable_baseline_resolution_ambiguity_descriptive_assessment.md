# HLTH-029 — Comparable-Baseline Resolution, Ambiguity & Descriptive Assessment

**Status:** Accepted — Phase 006 Group 03

## Purpose

Define how one or more plausible Baselines support a current descriptive Assessment without introducing hidden precedence or normative health.

## Contract

For a current Observation, comparable-Baseline resolution considers the exact comparison target, context and reference eligibility. Outcomes can include:

- one sufficiently comparable Baseline;
- multiple Baselines whose distinct contexts are simultaneously relevant;
- ambiguous reference context where no accepted matching rule selects among candidates;
- conflicting reference/evidence state;
- insufficient reference;
- non-comparable;
- unavailable/unknown/not applicable.

A Baseline-based Assessment may report basis-specific results such as `within reference behavior`, `outside/atypical relative to reference`, `material shift observed`, or an unresolved state, provided the exact comparison semantics and limitations are retained.

## Invariants

- Newest, largest-history, narrowest, broadest, or numerically closest Baseline does not automatically win.
- Multiple legitimate Baselines can coexist without being contradictory when they describe different contexts.
- If two materially applicable Baselines imply different descriptive interpretations and no valid context rule resolves them, preserve ambiguity rather than selecting convenience.
- `Within Baseline` does not mean healthy/meets Expectation.
- `Outside Baseline` does not mean failed/degraded/unacceptable.
- Typical and normatively unacceptable may coexist; atypical and normatively acceptable may coexist.
- Group 04 will define normative threshold/margin/waiver Assessment semantics and how normative and descriptive results are presented together.

## Example

A month-end Tuesday may plausibly match both a month-end and weekday reference. If the Baseline definitions do not establish how those contexts compose, the product preserves reference ambiguity instead of silently using whichever Baseline produces a cleaner result.