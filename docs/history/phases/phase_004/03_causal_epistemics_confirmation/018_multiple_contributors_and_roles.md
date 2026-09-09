# REF-018 — Multiple Contributors and Qualitative Causal Roles

**Status:** Accepted — Phase 004 Group 03

## Purpose

Allow multiple causal claims to coexist with explicit qualitative roles without forcing one root cause or inventing unsupported percentage attribution.

## Role semantics

A claim may use a bounded qualitative role where evidence supports it, such as:

- **direct** — the claimed condition directly produced the defined outcome through the evidenced mechanism;
- **contributing** — the condition materially contributed but need not be sufficient or dominant by itself;
- **enabling** — the condition made another causal pathway possible without necessarily triggering the outcome alone;
- **triggering** — the condition initiated a causal sequence under the applicable mechanism;
- **preventing** — the condition/action prevented an otherwise plausible outcome;
- **primary** — the condition is comparatively dominant among material contributors under an explicit comparative basis;
- **unresolved role** — causal involvement may be supported while the exact role cannot yet be discriminated.

These labels are semantic roles, not universal ontology requirements; later domain refinement may narrow the vocabulary.

## Rules

- Multiple claims may be simultaneously supported or confirmed when they are causally compatible.
- Confirmation of one contributing claim does not automatically reject other contributors.
- The product never requires exactly one `root cause` to close an Investigation.
- `Primary` is a stronger comparative assertion and requires evidence comparing material contributors; it is not inferred from being first discovered, most severe, most upstream, or most recent.
- Qualitative contribution does not imply a numerical percentage of responsibility or effect.
- Percentage attribution requires a separate quantitative evidence/model standard if future scenarios demand it.
- Causal chains can be represented through explicit claim relationships/references as needed without creating a new concept in Group 03.
- A safeguard/gate may be a preventing cause for one outcome and a contributing cause for a different delay/non-delivery outcome; these are separate propositions.

## Example

B's reduced population and elevated join-key nulls may both contribute to C row loss. Neither must be called the sole root cause. If evidence only establishes both as contributors, the framework should not invent `60% B volume / 40% key quality` or call one primary.

## Non-goals

- quantitative attribution;
- blame/responsibility allocation;
- organizational accountability determination;
- forced root-cause ranking.
