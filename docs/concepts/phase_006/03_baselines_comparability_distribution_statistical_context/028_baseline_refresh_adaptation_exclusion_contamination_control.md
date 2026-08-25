# HLTH-028 — Baseline Refresh, Adaptation, Exclusion & Contamination Control

**Status:** Accepted — Phase 006 Group 03

## Purpose

Keep adaptive/rolling Baselines descriptive and auditable without silently normalizing incidents or selecting reference data circularly.

## Contract

A Baseline refresh/adaptation rule defines, where material:

- eligible history/window progression;
- lag/holdout semantics for the current comparison target;
- inclusion/exclusion criteria and their provenance;
- treatment of known incident/change/transitional periods;
- derivation method/version;
- effective/knowledge time of the refreshed Baseline;
- supersession relationship to earlier Baseline versions.

## Invariants

- A current Observation must not silently redefine the reference used to judge itself.
- `Looks anomalous` alone is not a sufficient reason to exclude an Observation from history; that would make the Baseline self-validating.
- Known incident, test, incomplete-load, transition, or other excluded periods require an explicit reference-population basis and retained provenance.
- Repeated abnormal behavior may become historically typical under a legitimate descriptive Baseline; this still does not make it normatively acceptable.
- Rolling/adaptive refresh must preserve earlier Baseline versions and Assessments.
- A realized regime break should usually segment the affected reference rather than be gradually absorbed as if continuity were proven.
- Group 03 does not choose automatic anomaly-learning or change-point algorithms.

## Example

A five-day completeness incident should not automatically drag a rolling completeness Baseline toward the incident simply because those five values are recent. Whether that period belongs to future descriptive history follows the explicit reference-population rule, while any normative completeness Expectation remains independent.