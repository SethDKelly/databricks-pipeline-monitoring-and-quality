# EXPL-033 — Freshness, Currentness & Current-Cycle Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Is the data current?`, `is it fresh?`, and `did this cycle finish?` must bind the exact temporal/current-cycle proposition, reference opportunity, allowed age/window, and relevant output/version.

## Rules

- latest successful execution ≠ current-cycle completion;
- most recent output ≠ fresh/current output;
- fresh-for-one-use may be stale-for-another where the bounded rule differs;
- recent Assessment calculation over old evidence can remain stale for current use;
- stale/currentness state does not automatically imply broader quality/health state;
- current-cycle input alignment in a multi-input run is distinct from execution success.

No universal TTL is introduced.