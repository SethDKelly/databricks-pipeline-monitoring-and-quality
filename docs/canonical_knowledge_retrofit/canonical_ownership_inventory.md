# Canonical Ownership Inventory — Human View

The machine-readable authority ledger is [`canonical_ownership_inventory.json`](canonical_ownership_inventory.json). This page summarizes the accepted CKR result in the final normalized documentation topology; it is not a second independently maintained ownership registry.

## Current result

CKR-A–K and DPTN-A–G are complete/accepted. DPTN promoted accepted semantic owners to first-class paths and later retired the temporary compatibility namespace without changing meaning.

- all **34** record-level semantic entries remain `canonicalized`;
- all **24** accepted concepts have current owners under `docs/concepts/`;
- all eight stable-ID families remain `canonicalized`, covering **1,237** accepted IDs;
- the architecture inventory contains **nine canonicalized records**: eight ARCH range partitions covering ARCH-001–ARCH-500 plus the frozen reference architecture;
- all current targets carry `CANONICAL CURRENT AUTHORITY` markers and bounded provenance;
- Phase 001–010, decisions, scenario reviews, exit reviews, handoffs and completed DPTN evidence are preserved under `docs/history/` as provenance/rationale/history rather than alternate current authority;
- the inventory lifecycle marker remains `ckr_complete`.

## Stable-ID ownership

| Family | Accepted range | Current domain |
|---|---|---|
| SYN | SYN-001..SYN-035 | `docs/contracts/synchronization/` |
| REF | REF-001..REF-030 | `docs/contracts/evidence-time-causality/` |
| AUTH | AUTH-001..AUTH-053 | `docs/authority/` |
| HLTH | HLTH-001..HLTH-066 | `docs/contracts/health-quality-timing/` |
| OPS | OPS-001..OPS-123 | `docs/contracts/operations/` |
| EXPL | EXPL-001..EXPL-160 | `docs/experience/` |
| INTG | INTG-001..INTG-270 | `docs/contracts/integration/` |
| ARCH | ARCH-001..ARCH-500 | `docs/architecture/` |

Exact stable IDs resolve through `scripts/agentic/resolve_stable_id.py <ID>` to `owner_path::ID`. Historical occurrence discovery is separate through `--history` and never selects current ownership.

## Architecture inventory

The accepted CKR-I topology remains intentionally compact:

- eight range-owning architecture records partition ARCH-001–ARCH-500;
- one separately inventoried frozen reference architecture composes the end-to-end target without creating ARCH-501 or another stable-ID range.

## History preservation

The JSON ledger retains legacy `current_owner` paths as provenance pointers and current `target_owner`/`target_documents` as normalized first-class owners. Historical files are retrievable beneath `docs/history/`, but they do not compete with current targets.

The current history index is `docs/history/README.md`; the pre-DPTN design-history index is preserved at `docs/history/design-history/README.md`; the completed DPTN program is preserved at `docs/history/retrofits/dptn/`.

## Final topology

The temporary CKR-era compatibility namespace has been retired. Current semantic owners are only the ledger-selected first-class `docs/<family>/` resources. Generated `knowledge/` remains routing compatibility only, and the retired compatibility orientation is preserved under history for provenance.

## Critical inventory invariant

> **The JSON ledger selects current ownership; this summary, path presence, recency, search rank, generated OKF and historical provenance do not.**

At CKR exit all required semantic migration states were closed. DPTN exit changed only their physical/routing topology. Future semantic changes use normal governed change control rather than re-opening chronological phase authority.

**Implementation 001-A is NEXT / READY / NOT STARTED.** Its readiness follows documentation-topology exit; implementation still requires separate explicit human selection.
