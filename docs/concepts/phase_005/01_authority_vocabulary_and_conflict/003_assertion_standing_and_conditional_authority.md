# AUTH-003 — Assertion Standing and Conditional Authority

**Status:** Accepted — Phase 005 Group 01

## Purpose

Define common standing semantics for source/actor assertions without turning source presence into authority.

## Standing vocabulary

An applicable source/actor may resolve as:

- **authoritative** — assertions may establish authoritative state for the bound target under the applicable rule;
- **advisory** — assertions may enrich, warn, challenge, or provide context but cannot displace authoritative state;
- **explicitly non-authoritative** — the applicable rule explicitly excludes the holder from authoritative standing for the target;
- **conditional** — standing depends on explicit evidenced conditions, such as environment, purpose, or an accepted fallback condition;
- **unknown** — no sufficient applicable authority rule is known;
- **conflicting** — applicable authority rules disagree about standing/conditions.

## Contract

Standing is resolved independently for each authority target. A holder can be authoritative for one facet and advisory for another.

Conditional authority does not activate merely because the condition would be convenient. The condition must be established from applicable evidence/state under the accepted rule.

## Invariants

- Advisory assertions remain provenance-bearing and may still be useful to Investigation/Explanation where authorized.
- Advisory agreement does not become authoritative consensus.
- Explicitly non-authoritative does not mean an assertion is deleted or necessarily false; it means it cannot establish authoritative state for that target.
- Unknown authority does not promote the most available source.
- Conditional standing must preserve the condition/basis used to resolve it.
- Standing is historical and can change prospectively without rewriting earlier authority.
