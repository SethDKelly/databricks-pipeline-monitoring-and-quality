# OPS-064 — Restricted / Opaque Evidence & Localization

**Status:** Accepted — Phase 007 Group 05

## Purpose

Allow Investigation to remain useful across restricted topology/evidence without becoming an authorization bypass or inventing conclusions from hidden data.

## Contract

Where authorized, an Investigation may record that:

- a restricted/opaque upstream subject/path/evidence set is relevant;
- localization reaches an authorization boundary;
- undisclosed evidence supports/contradicts a linked proposition at a safe abstraction level;
- evidence availability/restriction prevents stronger localization or exclusion.

Internal truth, audience-visible projection and authorization remain separate under Phase 005.

An audience that cannot inspect evidence may receive a weaker safe statement such as `localization is limited by restricted upstream evidence`; it must not receive `no upstream issue found` merely because upstream detail is hidden.

## Invariants

- restricted ≠ absent.
- opaque evidence ≠ no evidence.
- Investigation visibility ≠ evidence visibility.
- disclosure cannot strengthen localization or causal status.
- aggregation/summary is not automatic declassification.
