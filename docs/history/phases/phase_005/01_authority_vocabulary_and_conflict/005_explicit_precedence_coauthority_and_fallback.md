# AUTH-005 — Explicit Precedence, Co-Authority, and Fallback

**Status:** Accepted — Phase 005 Group 01

## Purpose

Define how accepted authority rules may resolve among multiple eligible holders without inventing hidden precedence.

## Supported functional forms

An authority rule may explicitly establish, where needed:

- **sole authority** — one holder has authoritative standing for the bound target/context;
- **co-authority** — multiple holders have authoritative standing concurrently;
- **ordered precedence** — multiple holders are eligible but an explicit order decides which governs when several applicable assertions exist;
- **conditional/fallback authority** — a holder becomes authoritative only when explicit conditions are satisfied, such as evidenced unavailability of a primary authority for a bounded context.

These are functional semantics, not a requirement that every target use all forms.

## Invariants

- Majority, source count, ingestion order, record recency, repository ownership, administrator status, and apparent source quality are not precedence rules.
- Scope specificity is not automatically precedence. An explicit rule may define specific-over-broad behavior, but the framework does not invent it.
- Co-authoritative disagreement remains authoritative conflict unless another accepted rule resolves it.
- Ordered precedence resolves standing, not factual correctness; lower-precedence assertions remain provenance-bearing.
- Fallback requires both an explicit fallback rule and evidence that its activation condition holds.
- An unavailable primary authority does not automatically promote another available source.
- A fallback authority returning an assertion does not retroactively make that source primary outside the fallback condition.
