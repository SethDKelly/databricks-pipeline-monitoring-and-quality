# OPS-098 — Expiry, Scheduled End & Effective End of Protection

**Status:** Accepted — Phase 007 Group 07

## Purpose

Keep configured expiry semantics separate from evidence that protection actually ceased.

## Contract

Distinguish:

- scheduled expiry/review deadline;
- authorization expiry where applicable;
- control/runtime effective expiry;
- observed persistence beyond scheduled expiry;
- unknown/conflicting expiry enforcement.

If the control semantics deterministically expire protection and evidence sufficiently establishes those semantics were operative, effective expiry may be established accordingly. Otherwise scheduled time alone is not runtime proof.

## Invariants

- scheduled expiry ≠ effective release by clock assumption alone.
- expiry ≠ healthy/current output.
- expiry before concern resolution can create renewed exposure opportunity but does not itself establish exposure.
- unknown expiry state remains unknown.
