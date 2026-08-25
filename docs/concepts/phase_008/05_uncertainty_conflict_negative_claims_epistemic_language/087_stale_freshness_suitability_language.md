# EXPL-087 — Stale / Freshness / Suitability Language

**Status:** Accepted — Phase 008 Group 05

## Requirement

When evidence/result is stale for an exact use, communicate the suitability limitation without rewriting the underlying historical result.

A previously `meets` Assessment can remain the prior Assessment while being unsuitable for a current readiness use. A recent recomputation over old evidence can still be stale.

`Stale` is not automatically `violates`, `unavailable`, `unknown` or `unsafe`.