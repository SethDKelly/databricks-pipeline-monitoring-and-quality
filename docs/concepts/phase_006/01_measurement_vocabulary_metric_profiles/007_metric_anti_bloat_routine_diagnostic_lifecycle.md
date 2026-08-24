# HLTH-007 — Metric Anti-Bloat, Routine/Diagnostic Use & Lifecycle Principle

**Status:** Accepted — Phase 006 Group 01

## Purpose

Constrain routine metric/check growth so the monitoring product remains interpretable, operationally useful and economically reasonable instead of becoming an indiscriminate statistics catalog.

## Inclusion test

A metric/check should have an identifiable reason to exist in a governed profile. Relevant considerations include:

- semantic applicability;
- monitored failure mode or business/operational question;
- likely actionability or investigative value;
- interpretability to intended users;
- redundancy/duplication with other measures;
- expected volatility/noise characteristics;
- functional cost/latency sensitivity;
- required evaluation frequency/horizon;
- retention value;
- governance owner and retirement/review path.

These considerations constrain selection but do not replace AUTH-017 authority.

## Anti-bloat rules

- Do not automatically calculate null rate, distinct count, min/max, mean, standard deviation, quantiles and cardinality for every column.
- Do not calculate a statistic merely because Databricks, DQX, Metric Views or another future source exposes it cheaply.
- Prefer a small stable routine core plus targeted critical/business/transformation checks.
- Keep richer exploratory statistics diagnostic/on-demand when routine value is weak.
- Avoid retaining multiple mathematically redundant forms unless they serve materially different uses or evidence needs.
- A metric useful during one Investigation does not automatically become permanent monitoring state.
- A newly added field does not automatically inherit the metric set of neighboring fields.
- A high-criticality asset can justify more careful review but does not automatically justify every available metric.
- Metric profile retirement/suspension preserves historical Observations and rationale.

## Routine versus diagnostic

Routine health should answer recurring operational/business questions with a bounded, interpretable signal set.

Diagnostic/on-demand measurement may be broader and more expensive because it is invoked to answer a specific Investigation question. Diagnostic output remains evidence-bound and may later justify a governed profile change, but escalation is explicit rather than automatic.

## Non-goals

This contract does not set compute budgets, sampling strategies, caching, retention infrastructure or a maximum metric count. Those require later source/architecture analysis.
