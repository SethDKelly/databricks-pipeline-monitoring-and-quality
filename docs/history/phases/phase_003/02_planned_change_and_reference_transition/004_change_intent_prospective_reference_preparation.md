# SYN-004 — Change Intent → Prospective Reference Preparation

**Status:** Accepted — Phase 003 Group 02

## Outcome

Allow a registered planned modification to prepare the monitoring references that may be needed after activation — an explicitly authorized prospective Expectation and/or a prospective Baseline comparability break — without treating anticipated behavior as normative truth or empirical history.

## Participating concepts and actions

- **Change Intent** — `resolvePlannedAt` (with `register`, `revise`, and `withdraw` occurring within the concept lifecycle).
- **Expectation** — `establish`, `revise`, `resolveApplicable`.
- **Baseline** — `registerProspectiveBreak`, `resolveComparable`.

## Trigger / initiating condition

A registered/revised Change Intent includes anticipated effects or monitoring implications that may alter future acceptable behavior and/or the comparability of an existing Baseline.

## Preconditions

- the intended target resolves to the correct Entity Identity/context;
- the relevant Change Intent is resolvable with provenance;
- any Expectation establishment/revision is performed by a source/actor authorized for that normative category;
- a Baseline exists only where a descriptive reference has actually been derived.

## Coordination semantics

1. Resolve the relevant Change Intent and its target/dimension/context.
2. Evaluate two **independent branches**:
   - **Expectation branch:** the intent may prompt review. If an authorized actor/source explicitly decides on post-change normative behavior, `Expectation.establish` or `Expectation.revise` records that criterion with provenance and prospective applicability semantics.
   - **Baseline branch:** if the intent predicts a structural comparability break, `Baseline.registerProspectiveBreak` records the pending break linked to the intent.
3. Do not require both branches to succeed. A valid prospective break may exist while the post-change Expectation remains unknown, and an authorized prospective Expectation may exist without an empirical Baseline.
4. Before realization, the pending Baseline break does not end current comparability merely because the intent was registered.
5. A prospective Expectation linked to activation does not apply to pre-change evidence. Its eventual boundary is established by SYN-006.
6. If an Expectation is explicitly established with applicability independent of this Change Intent, its own normative lifecycle governs; this synchronization does not override it.
7. `Change Intent.withdraw` prevents a still-pending intent-linked Baseline break from becoming effective through that intent. Withdrawal does not silently retire an independently authoritative Expectation.

This is semantic coordination, not a change-approval workflow or transaction.

## State and evidence effects

- Change Intent owns the planned modification, anticipated effects, and intent history.
- Expectation owns any normative criterion and its authority/effective history.
- Baseline owns the prospective comparability-break reference and existing descriptive reference history.
- The synchronization owns no combined “change policy” object.

## Ambiguity / failure propagation

- no registered intent → no planned-reference preparation is inferred;
- conflicting intents → preserve conflicting anticipated effects; do not guess a normative criterion;
- intent says “lower volume” but no authorized acceptable range exists → Expectation remains missing/unknown while the Baseline break may still be pending;
- no existing Baseline → there is nothing to break; do not manufacture one;
- unavailable/unauthorized intent detail may permit only an abstract indication that planned reference review exists;
- an unauthorized actor cannot turn an anticipated effect into an Expectation through synchronization.

## Temporal semantics

Preserve at least:

- intent registration/knowledge time;
- planned effective/activation context;
- Expectation assertion time and its prospective effective semantics;
- Baseline prospective-break registration time;
- later actual transition time, which remains unresolved in this synchronization.

Historical replay before realization shows the old Baseline still applicable where otherwise comparable and the new reference state as prospective/pending rather than active.

## Provenance / traceability

The product must trace why an Expectation review/revision or prospective Baseline break was considered, which Change Intent prompted it, who/what established any normative criterion, and which Baseline version is affected.

## Security / authorization

Planned filters, ranges, future population changes, schedules, and business rules can be sensitive. The synchronization operates only over authorized projections and does not broaden access because a related reference needs context.

## Invariants

- anticipated effect ≠ Expectation;
- planned value ≠ Baseline evidence;
- registering intent ≠ activating reference transition;
- prospective break ≠ current Baseline retirement;
- Expectation authority is independent from Change Intent authorship;
- one branch may remain unresolved while the other remains usable;
- withdrawal does not erase historical registration.

## Scenarios

**Filter prepared:** intent predicts lower C volume; old Baseline gets a pending break; authorized data owner creates a 13–15M post-change Expectation.

**No approved threshold:** intent predicts lower volume but no normative range is approved; pending Baseline break exists, Expectation remains unknown.

**Intent withdrawn:** planned filter is cancelled before activation; pending break never becomes effective from that intent.

**Restricted plan:** analyst can see that a future reference review exists without seeing sensitive filter details.

## Non-goals

Deployment realization, Observation collection, Assessment, Baseline derivation, causal attribution, change approval workflow, ticket/PR implementation.

## Deferred questions

Prospective Expectation lifecycle vocabulary and authority/source-precedence rules for change-driven normative revisions.
