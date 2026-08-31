# 001-D — Minimal Canonical Delta Persistence & Historical Semantics

**Status:** Planned

## Goal

Prove the Delta-first canonical-history architecture with the minimum set of persisted records required for the first freshness question.

## Minimal persisted families

Implement only what the 001 slice needs, but design common envelopes for later expansion:

- canonical evidence/provenance records;
- source acquisition run/attempt/request/page records;
- entity reference/binding records sufficient for the pilot subject;
- freshness Expectation revisions;
- freshness Observations;
- freshness Assessments or their canonical evaluation record where Phase 010 specifies persistence;
- correction/supersession linkage;
- optional retained Statement/communication record only if the 001 demo explicitly promises retention.

Do not create a giant universal event table if the accepted ownership model calls for typed journals/tables.

## Historical semantics

Persist enough information to answer independently:

- what was effective at event time?;
- what source fact existed?;
- when did the framework retrieve/record it?;
- what was known by knowledge cut `K`?;
- what correction/supersession occurred later?;
- what is the current retrospective interpretation?

The implementation must not rely on `VERSION AS OF`/Delta time travel as the product's semantic definition of `known by K`.

## Non-rewriting pattern

Updates to material historical truth use append/link behavior:

```text
original record
   └── corrected/superseded by new record
```

Physical Delta maintenance (OPTIMIZE/compaction/schema migration) may rewrite files but may not erase semantic historical identity.

## Idempotency

Re-acquiring the same source record should not create duplicate semantic evidence. Record acquisition attempts separately from the canonical evidence identity.

## Schema evolution

Use source-controlled migrations/table definitions. Historical records retain enough schema/version metadata to be interpretable after code upgrades.

## Local/integration test strategy

- fast persistence tests may use a local compatible Delta/Spark test environment where practical;
- at least one integration path must run against the real development Databricks target by 001-G/H.

## Acceptance gates

Automated tests prove:

1. late evidence is excluded from an earlier knowledge cut;
2. correction does not erase the original record;
3. retrospective query can include the corrected evidence while historical query preserves prior knowledge;
4. duplicate acquisition is idempotent at canonical-evidence level;
5. unknown/unavailable evidence state can be represented without fake rows/zeros;
6. table migration does not change semantic IDs/history;
7. archive/restore full implementation is deferred, but persistence metadata does not block later lifecycle implementation.
