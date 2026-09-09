# AUTH-018 — Threshold, Margin, Tolerance, and Severity Authority

**Status:** Accepted — Phase 005 Group 03

## Purpose

Resolve authoritative standing for normative thresholds, warning/failure boundaries, margins/tolerance bands, and severity declarations without conflating those rule layers or allowing Baseline behavior to become normative automatically.

## Contract

Authority may be independently resolved for:

- hard pass/fail criteria;
- warning versus failure boundaries;
- absolute/relative/asymmetric tolerance bands;
- severity or priority attached to a normative violation class;
- context-specific threshold variants;
- revision/retirement of those rules.

Different rule layers may have different authoritative holders when explicitly governed.

## Invariants

- Threshold authority does not determine how the metric is computed; metric semantics remain separate.
- A Baseline-derived range is descriptive unless explicitly adopted through an authoritative Expectation.
- Atypicality against Baseline does not become normative failure by severity labeling alone.
- Severity is not Impact. A `critical` violation class does not prove downstream exposure, business consequence, or cause.
- Business and technical thresholds can coexist when they apply to distinct dimensions, consumers, or contexts.
- If two authoritative rules target the same dimension/context/time and conflict, preserve normative conflict unless AUTH-001–AUTH-008 explicitly resolves it.
- `Worst wins`, `strictest wins`, `business wins`, and `technical wins` are not implicit precedence rules.
- Changing a threshold prospectively does not rewrite historical Assessments made against the earlier rule.
- Authority to set a threshold does not grant permission to waive it, alter the metric profile, configure a gate, or disclose restricted values unless separately authorized.

## Example

A technical team may own an early-warning freshness band while an external-reporting authority owns the hard delivery failure deadline. Both can apply without one silently replacing the other.