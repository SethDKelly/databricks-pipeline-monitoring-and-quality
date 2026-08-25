# HLTH-025 — Approximation, Sampling & Measurement-Uncertainty Comparability

**Status:** Accepted — Phase 006 Group 03

## Purpose

Carry known measurement-method uncertainty into descriptive comparison rather than treating approximate or sampled values as exact facts.

## Contract

Where material, an Observation/Baseline records:

- exact versus approximate/sampled method class;
- method/definition version;
- sampling frame/rate or approximation parameters at an appropriate functional level;
- known error/uncertainty bounds or limitations when available;
- whether historical/current methods are sufficiently equivalent for the proposed comparison.

## Invariants

- Approximate values can be useful evidence; they are not automatically lower quality or unusable.
- Exact and approximate observations are not automatically interchangeable.
- A small observed difference inside material measurement uncertainty must not be presented as a precise historical shift.
- Changing approximation algorithms/parameters can create a definition/comparability break when it materially changes meaning/error behavior.
- Unknown uncertainty remains unknown rather than being treated as zero.
- Multiple copies of one approximate measurement do not narrow uncertainty through false corroboration.
- Group 03 does not define statistical confidence scores or a vendor-specific error model.

## Example

An approximate distinct count of 1.01M compared with a historical approximate reference around 1.00M may be descriptively indistinguishable if the method's material error range overlaps that difference. The product should preserve the limitation rather than assert a precise 1% increase.