# HLTH-059 — Severity, Criticality, Priority & Health-Truth Separation in Composition

**Status:** Accepted — Phase 006 Group 06

## Purpose

Prevent operational priority from becoming hidden evidence during health composition.

## Rules

- Severity, criticality, business importance, escalation priority, and health outcome remain separate dimensions.
- A low-severity required violation remains a health violation.
- A high-criticality component that currently `meets` remains met; criticality does not manufacture degradation.
- Criticality can govern which components belong in a profile, review cadence, escalation order, or presentation emphasis only through accepted governance rules.
- Severity does not determine which conflicting rule is true and does not override insufficient evidence.
- Weighted scores that multiply severity/criticality by component outcomes are not accepted as universal health truth.
- A summary may highlight a severe known violation prominently without implying that other unresolved components are known healthy.
- Impact remains separately evidenced; criticality/severity does not prove downstream consequence.

## Non-goal

This contract does not define incident-priority algorithms or alert-routing implementation.