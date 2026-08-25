# HLTH-056 — Component Eligibility, Required/Optional Roles & Explicit Composition Logic

**Status:** Accepted — Phase 006 Group 06

## Purpose

Define which component Assessments participate in a composite and how they combine without relying on majority vote, weighted averaging, or hidden precedence.

## Rules

- A component participates only under an explicit composite profile/role that identifies whether it is required, optional, conditional, alternative, or informational.
- Applicability, profile inclusion, current availability, and current component outcome remain distinct.
- Required but unresolved components remain part of the composite obligation; they do not disappear because evidence is unavailable.
- `not applicable` removes a component only when the governing rule genuinely makes it non-applicable for the bound context; it is not equivalent to `meets`.
- AND, OR, conditional, fallback, quorum-like, or alternative-branch composition is valid only when explicitly part of the composite rule semantics.
- No default majority, arithmetic average, weighted score, `most components pass`, or `highest severity wins` rule is accepted.
- Optional/informational components can be surfaced without silently changing the normative composite result.
- A diagnostic/on-demand component can inform Investigation without becoming routine composite membership.

## Invariant

Composition logic must be explainable from the accepted profile/rule, not inferred from the observed results after the fact.