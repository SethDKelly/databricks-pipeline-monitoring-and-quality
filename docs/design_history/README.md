# DMTZ Design History

**Role:** PROVENANCE / RATIONALE / HISTORICAL DESIGN RECORD

This directory defines the logical design-history layer introduced by the Canonical Knowledge & Documentation Authority Retrofit.

CKR deliberately does **not** bulk-move the existing phase corpus during CKR-A. Existing paths remain stable while their semantic records are progressively promoted into `docs/canonical/`.

## Existing design-history sources

The logical design-history layer includes, as applicable:

- `docs/concepts/phase_002/` through `docs/concepts/phase_010/`;
- `docs/decisions/`;
- phase scenario reviews and validation matrices;
- phase/group exit reviews;
- handoff documents and residual-gap registers;
- historical concept wording after concept cutover;
- foundation/planning records whose purpose is historical sequence rather than current truth.

During migration some files inside those paths still remain **legacy current owners** for records not yet canonicalized. Their role changes per record only at atomic cutover.

## Current-truth rule

Once an ownership-inventory record is `canonicalized`, the canonical owner under `docs/canonical/` answers current semantic questions. The historical source remains useful for:

- why a boundary was chosen;
- alternatives considered or rejected;
- when a refinement entered the design;
- scenario evidence and design validation;
- historical status-at-time-of-writing;
- explicit semantic-change review.

Design history should not be traversed merely to reconstruct a current definition that already has a canonical owner.

## Preservation rule

Historical documents are not rewritten to pretend the final design was known at the time they were authored.

A later CKR group may add a compact banner/index reference to a historical file after cutover, but should otherwise preserve the accepted-at-the-time narrative.

## Physical relocation

Moving all phase files beneath `docs/design_history/` is **not required** for CKR success and is intentionally deferred unless a later group demonstrates enough value to justify link churn.

Logical authority separation is the goal; filesystem aesthetics are secondary.
