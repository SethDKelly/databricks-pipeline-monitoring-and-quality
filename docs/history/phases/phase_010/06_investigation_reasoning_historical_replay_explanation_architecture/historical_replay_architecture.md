# Historical Replay Architecture

## Coordinates

Replay binds at least:

- bounded proposition/question;
- event/effective interval;
- knowledge cut `K`;
- source/evidence availability coordinates;
- governing definition/authority revisions where relevant;
- current requester/purpose/delivery context for present disclosure.

Event before `K` does not imply evidence known by `K`.

## As-known-at-K

The replay engine filters canonical journals to evidence eligible by `K`, applies the rules/definitions relevant to the historical proposition, preserves then-known limitations and produces a reconstruction labeled as such.

Evidence arriving after `K` is excluded from the as-known result even if its event time is earlier.

## Current retrospective

A current retrospective view may include late evidence, corrections, supersessions and richer current context. It is a different perspective, not an update that rewrites the historical as-known result.

## Correction/supersession

Corrections can change current preferred interpretation while preserving the earlier record and the fact that earlier users acted on different evidence.

## Replay basis manifest

Every replay result records or can deterministically regenerate:

- evidence IDs included by `K`;
- late evidence excluded from that cut;
- source/acquisition coverage limitations;
- rule/definition revisions;
- missing/expired payloads;
- exact knowledge cut and query scope.

## Retention

Replay cannot promise what retention did not preserve. A provenance stub can prove that an evidence item existed and expired; it cannot recreate the exact payload or exact prior basis projection.

## Communication distinction

`historical source state` ≠ `as-known reconstructed Explanation` ≠ `authentic retained communication` ≠ `current retrospective Explanation`.

Historical replay relies on framework bitemporal journals, not Delta time travel as the product history contract.