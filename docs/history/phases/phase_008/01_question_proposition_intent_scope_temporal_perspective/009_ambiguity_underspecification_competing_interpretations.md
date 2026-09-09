# EXPL-009 — Ambiguity, Underspecification & Competing Interpretations

**Status:** Accepted — Phase 008 Group 01

## Requirement

Preserve material ambiguity in the question contract rather than hiding it behind an apparently precise answer.

Common ambiguity sources include:

- unresolved subject identity;
- missing environment/version/run/consumer context;
- ambiguous temporal phrases;
- shorthand such as `healthy`, `okay`, `safe`, `affected`, `blocked`, `planned`, `owner` or `why`;
- multiple plausible health profiles or business uses;
- multiple candidate causal propositions;
- broad scope unsupported by available evidence.

## Response behavior

Where ambiguity is material, the framework may:

- state that the requested proposition is underspecified;
- provide several explicitly bounded interpretations when each is useful and supportable;
- answer the unambiguous portion and mark the remainder unresolved;
- use contextual defaults only when they are declared/established for the request context rather than silently invented.

## Anti-pattern

Do not map `Is C okay?` to one universal health score. Resolve the intended use/profile/dimension if available or present the material distinct health propositions.
