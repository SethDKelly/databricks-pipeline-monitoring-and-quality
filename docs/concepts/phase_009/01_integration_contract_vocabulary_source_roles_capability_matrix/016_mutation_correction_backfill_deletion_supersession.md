# INTG-016 — Mutation, Correction, Backfill, Deletion & Supersession

Contracts describe whether records are immutable, mutable in place, versioned, corrected through explicit events, backfilled later, deleted with/without tombstones, or superseded through identifiable history.

Late/backfilled evidence must preserve when it became available if it is to support knowledge-cut reasoning.

A correction may improve current retrospective interpretation without rewriting what was available earlier.

If mutation destroys prior state or recorded-time evidence, the affected historical/replay requirement is partial or unsupported rather than reconstructed by assumption.