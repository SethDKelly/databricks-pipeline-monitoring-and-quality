# Group 04 — Checkpoint, Pagination & Recovery Model

## Checkpoint families

A source can use one or more checkpoint forms:

- opaque cursor/page token;
- source sequence/version;
- event/update timestamp + tie-break identity;
- source Delta/stream version;
- export batch/file identity;
- webhook delivery position only where source semantics justify it;
- explicit window end plus overlap policy.

The checkpoint record must bind the exact source surface and query shape.

## Advancement

A checkpoint advances only after the corresponding evidence and required provenance are durable.

If persistence fails after source retrieval, the retry re-fetches or resumes conservatively rather than skipping the material.

## Overlap

Timestamp/window collectors normally need an explicit overlap strategy when late publication/order ambiguity is possible. Overlap records are deduplicated by source identity/common derivation.

## Pagination

A paginated acquisition is complete only when the source-specific completion condition is satisfied.

Examples include:

- no next link/token under a valid response contract;
- known final page reached;
- partition/window set fully enumerated;
- source-specific terminal cursor state.

A missing token caused by a failed/ambiguous response is not a normal terminal page.

## Recovery states

- `complete` — objective fully acquired under its declared coverage contract;
- `partial` — some evidence acquired but one or more declared segments failed/unresolved;
- `failed` — objective did not produce usable bounded coverage;
- `stalled` — repeated progress failure or source backlog not advancing;
- `checkpoint_invalid` — source rejected or invalidated continuation state;
- `retention_gap` — source can no longer serve required history;
- `unknown` — source/client state insufficient to classify.

These are acquisition states, not domain states.

## Backfill after gap

Where the source supports historical re-enumeration, invalid checkpoints trigger a bounded reconciliation/backfill. If the source retention window has already closed, the gap remains explicit and product-retained evidence is used only where it independently exists.
