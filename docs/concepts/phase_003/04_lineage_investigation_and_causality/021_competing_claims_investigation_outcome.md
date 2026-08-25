# SYN-021 — Competing Causal Claims → Epistemic Evolution and Investigation Outcome

**Status:** Accepted — Phase 003 Group 04

## Outcome

Allow an Investigation to retain multiple causal explanations, evolve their epistemic states as evidence changes, and close with an honest resolved, multi-contributor, unresolved, or no-actionable-conclusion outcome without forcing one root cause.

## Participating concepts and actions

- **Causal Claim** — `reviseStatus`, `support`, `contradict`, `confirm`, `reject`.
- **Investigation** — `linkClaim`, `refineScope`, `close`, `reopen`.

## Trigger / initiating condition

The Investigation has one or more Causal Claims with an evidence picture sufficient for review or a practical need to record the current inquiry outcome.

## Coordination semantics

1. Preserve each claim independently; competing claims are not forced into a zero-sum ranking.
2. `proposed`, `supported`, `weakened`, `rejected`, and `unresolved` remain available according to evidence/review semantics.
3. **`confirmed` is unavailable unless an explicit accepted evidence/authority standard exists and is satisfied.** In its absence, even strong automated reasoning must stop short of confirmation.
4. More than one claim may be supported or later confirmed as contributing causes.
5. A claim can be weakened while another gains support without deleting either history.
6. Investigation closure records the inquiry outcome for its purpose; closure does not upgrade any claim.
7. An Investigation may close `unresolved` when evidence cannot discriminate candidates, or `multi-causal` when several contributing explanations remain material.
8. An Investigation may close for operational action even when exact root cause is not confirmed, provided explanations preserve the claim statuses/uncertainty.
9. Material late evidence can reopen the Investigation and revise claims while preserving prior closure/status history.

## State and evidence effects

Causal Claim owns epistemic state; Investigation owns inquiry closure/history. Neither owns the other's truth.

## Ambiguity / failure propagation

Incomplete/unauthorized evidence may prevent confirmation or even rejection. The product must not promote a leading claim simply because investigation time is running out.

## Temporal semantics

Every claim status, closure, reopening, and later revision carries knowledge time; incident event time remains separate.

## Provenance / traceability

Closure points to the material claims/evidence state used at that time. High-consequence status changes retain reviewer/standard provenance where defined.

## Security / authorization

Different audiences may receive different allowed detail while the underlying claim status remains consistent.

## Invariants

- leading claim ≠ confirmed cause;
- Investigation closure ≠ Causal Claim confirmation;
- multiple contributors are valid;
- unresolved is valid;
- no evidence gap may be converted into certainty merely to close;
- later correction does not erase earlier knowledge state.

## Scenarios

B volume decline and join-key null increase remain two supported contributing claims. A Deployment claim is weakened because the effect predates activation. Restricted upstream evidence prevents discrimination, so the Investigation closes unresolved. Later authoritative evidence arrives and the Investigation reopens.

## Non-goals

Incident SLA policy, automatic confirmation authority, numeric confidence scoring, or quantitative percent attribution.

## Later refinement — Phase 007 Group 05

OPS-051/058/061–063 refine the synchronization without changing ownership:

- Investigation lead branches may exist before any Causal Claim is proposed;
- multiple simultaneous deviations do not automatically mean multiple causes;
- compatible contributors and mutually exclusive alternatives remain distinct;
- causal claim statuses remain Causal Claim truth and use the final REF-014 vocabulary `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, `confirmed`;
- Investigation closure uses operational inquiry dispositions and merely references linked claim states;
- the earlier `multi-causal` Investigation wording is a summary over independently established linked causal claims, not Investigation-owned causal truth;
- operational resolution/remediation can close an Investigation while causal state remains non-confirmed;
- material late evidence can reopen the Investigation and challenge claims without rewriting the earlier closure/status knowledge cut.

No ranking, vote, duration or closure rule may promote a claim. `confirmed` remains REF-017 + AUTH-034 gated.
