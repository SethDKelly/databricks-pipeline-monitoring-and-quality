# Phase 010 Group 02 — Temporal & Provenance Model

## Core rule

Historical truth, historical knowledge and framework persistence are different coordinates.

A material retained record can carry the following independently where applicable:

| Coordinate | Meaning |
|---|---|
| `effective_from` / `effective_to` | when the represented state is asserted/evidenced to apply |
| `event_time` | when the source-described event occurred |
| `source_recorded_at` | when the source says it recorded the fact/event |
| `source_available_at` | earliest evidenced availability in the source, when knowable |
| `collected_at` | when the framework acquired the source material |
| `persisted_at` | when the framework durably persisted the occurrence |
| `superseded_at` / correction coordinate | when a later retained record changed current interpretation/state |
| `communicated_at` | when a retained Explanation/communication was actually released/sent, if applicable |

Not every source provides every coordinate. Missing coordinates remain unknown.

## Bitemporal reconstruction

For stateful propositions, historical queries use at least:

1. an **event/effective target**; and
2. a **knowledge/availability cutoff K**.

A fact can therefore be effective at time T but absent from an as-known-at-K reconstruction if the source/framework did not have evidence of it by K.

## Late evidence

Late evidence retains both the earlier event/effective time and later availability/collection time. It can change current retrospective conclusions while leaving prior as-known conclusions historically valid.

## Corrections and supersession

Correction creates a later linked record. Material earlier state is not overwritten. Current-state views select the applicable unsuperseded/corrected state according to explicit rules.

Correction linkage is not causality and does not imply the corrected source was malicious/erroneous beyond what the source evidence states.

## Source mutation and deletion

The framework distinguishes:

- source record existed and was retained;
- source record later changed;
- source record later became unavailable/deleted;
- framework payload expired while provenance remained;
- framework never captured the payload;
- source existence itself is unknown.

These states must not collapse.

## Normalization provenance

Normalized facts retain:

- evidence occurrence ID(s);
- parser/normalizer revision;
- normalized schema revision;
- derivation/common-source identity;
- processing time.

Re-running a newer normalizer can produce a new derived representation while preserving the original evidence occurrence and prior normalized history when material.

## Identity across physical movement

Archival, compaction, migration and restore retain durable evidence IDs. Object keys/paths may change as physical implementation, but manifest identity and integrity linkage survive.

## Knowledge-cut indexing

Group 02 requires temporal fields/indexability sufficient for Group 06 to answer `composeAt`/as-known queries. It does not yet choose the final query API or reasoning engine.
