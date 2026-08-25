# HLTH-066 — Historical Composite Health, Suitability & Readiness Replay

**Status:** Accepted — Phase 006 Group 06

## Purpose

Preserve historical health and readiness reasoning against the exact component/profile/evidence state that existed at the relevant event and knowledge cut.

## Historical binding

Retain where material:

- composite profile/version and use/consumer context;
- component Assessment versions and applicable/not-applicable roles;
- warning, waiver, severity and unresolved qualifiers;
- Baseline/Expectation/reconciliation versions used by those components;
- evidence event/window/current-cycle identities and availability;
- result freshness/suitability rule/version;
- readiness criterion/opportunity where evaluated;
- event/effective time, framework knowledge time and derived evaluation time.

## Rules

- Current composite profiles, thresholds, Baselines, freshness rules, or current-cycle mappings are never projected backward automatically.
- Historical `healthy/degraded/indeterminate/...` results remain distinguishable from a present reconstruction of what was knowable then.
- Later evidence may produce a retrospective composite or readiness reassessment without rewriting what the framework actually concluded then.
- Historical readiness-suitability does not prove a historical gate decision, enforcement or execution; those remain separately evidenced.
- A later rule that would make an old result stale today does not make it retrospectively stale unless that rule applied then.
- Current requester authorization/disclosure still governs whether historical component detail can be shown now.

## Invariant

Historical replay preserves both the state of the world and the state of the framework's knowledge/rules at the relevant time.