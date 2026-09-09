# INTG-044 — Immuta Audit & Identity-History Boundary

**Status:** Accepted — Phase 009 Group 02

Immuta audit events can record policy changes, approvals, tags, group membership, attributes and governed query/access activity. They are useful for reconstructing authorization inputs and policy changes.

Immuta documents a 90-day default audit-log retention unless logs are exported. Historical effective authorization may also depend on upstream IAM and remote-platform state, so audit history alone is not universal authorization replay.
