# Canonical Ownership Inventory — Human View

The machine-readable authority ledger is [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json). This page summarizes the accepted CKR exit state; it is not a second independently maintained ownership registry.

## Final result

CKR-A–K are complete/accepted. The repository now has one current-truth layer selected by the machine-readable ownership inventory.

At CKR exit:

- all **34** record-level semantic entries are `canonicalized`;
- all **24** accepted concepts have canonical owners under `docs/canonical/concepts/`;
- all eight stable-ID families are `canonicalized`, covering **1,237** accepted IDs;
- the architecture inventory contains **nine canonicalized records**: eight ARCH range partitions covering ARCH-001–ARCH-500 plus the frozen reference architecture;
- all canonical targets carry `CANONICAL CURRENT AUTHORITY` markers and bounded provenance;
- Phase 001–010, decisions, scenario reviews, exit reviews and handoffs remain provenance/rationale/history rather than alternate current authority;
- the inventory lifecycle marker is `ckr_complete`.

## Stable-ID ownership

| Family | Accepted range | Canonical domain |
|---|---|---|
| SYN | SYN-001..SYN-035 | `docs/canonical/contracts/synchronization/` |
| REF | REF-001..REF-030 | `docs/canonical/contracts/evidence-time-causality/` |
| AUTH | AUTH-001..AUTH-053 | `docs/canonical/authority/` |
| HLTH | HLTH-001..HLTH-066 | `docs/canonical/contracts/health-quality-timing/` |
| OPS | OPS-001..OPS-123 | `docs/canonical/contracts/operations/` |
| EXPL | EXPL-001..EXPL-160 | `docs/canonical/experience/` |
| INTG | INTG-001..INTG-270 | `docs/canonical/contracts/integration/` |
| ARCH | ARCH-001..ARCH-500 | `docs/canonical/architecture/` |

Exact stable IDs resolve through `scripts/agentic/resolve_stable_id.py <ID>` to `owner_path::ID`. Historical occurrence discovery is separate through `--history` and never selects current ownership.

## Architecture inventory

The accepted CKR-I topology remains intentionally compact:

- eight range-owning architecture records partition ARCH-001–ARCH-500;
- one separately inventoried frozen reference architecture composes the end-to-end target without creating ARCH-501 or another stable-ID range.

## Design-history preservation

Legacy `current_owner` paths remain in the JSON ledger as provenance pointers. Their files remain retrievable for rationale/history, but after canonicalization they do not compete with the canonical `target_owner` for current truth.

`docs/design_history/README.md` is the logical history index. The phase corpus remains physically in place to avoid needless link churn.

## Critical inventory invariant

> **The JSON ledger selects current ownership; this summary, path presence, recency, search rank and historical provenance do not.**

At CKR exit all required semantic migration states are closed. Future canonical changes use normal governed change control rather than re-opening chronological phase authority.
