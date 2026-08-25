# EXPL-006 — Current, Historical & Retrospective Question Semantics

**Status:** Accepted — Phase 008 Group 01

## Requirement

Distinguish at least three common temporal request modes:

1. **current-state question** — asks what applies/what is known now for the current relevant context;
2. **as-known-at-cut historical question** — asks what could legitimately be concluded for historical event/window `T` using evidence available by cut `K`;
3. **current retrospective question about the past** — asks what is concluded now about historical event/window `T` using later permitted evidence.

## Default discipline

A past event-time target with no explicit knowledge cut must not be silently presented as `what the team knew then`. Treat it as a present retrospective interpretation unless surrounding request context unambiguously supplies the earlier cut.

If the distinction materially changes the answer, Explanation should make the perspective explicit.

## Boundaries

- current retrospective truth ≠ contemporaneous knowledge;
- retained historical Explanation ≠ current source truth;
- historical actor authorization ≠ current requester disclosure authorization;
- later correction ≠ evidence known earlier.
