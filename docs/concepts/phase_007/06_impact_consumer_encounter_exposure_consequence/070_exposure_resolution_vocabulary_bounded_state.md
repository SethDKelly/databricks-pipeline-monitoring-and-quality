# OPS-070 — Exposure Resolution Vocabulary & Bounded State

**Status:** Accepted — Phase 007 Group 06

## Purpose

Provide bounded exposure language without collapsing safe-state use, missing opportunity and evidence limitations into one boolean.

## Accepted vocabulary

For the exact exposure proposition, use the strongest justified result among:

- **exposed** — actual encounter with the bound affected/suspect state is sufficiently established;
- **not exposed** — sufficient bounded negative/path evidence establishes no encounter with that state;
- **safe/other-state encounter** — encounter occurred and a different non-affected state is sufficiently identified;
- **encountered-state unknown** — encounter occurred but the exact state/version cannot be resolved;
- **no relevant encounter opportunity** — sufficient evidence establishes no qualifying opportunity in the bounded window;
- **indeterminate** — evidence is insufficient/non-discriminating;
- **conflicting** — applicable evidence materially disagrees;
- **unavailable** — required evidence cannot currently be evaluated.

Authorization/redaction is handled separately; restricted evidence is not an epistemic synonym for `unavailable` unless it is actually unavailable to the evaluating process.

## Invariants

- `safe/other-state encounter` can support `not exposed to suspect V` but does not imply fresh/current/healthy.
- `no relevant encounter opportunity` is distinct from `opportunity occurred, no encounter`.
- `indeterminate` is not a reassuring negative.
- no universal exposure probability/confidence score is accepted.
