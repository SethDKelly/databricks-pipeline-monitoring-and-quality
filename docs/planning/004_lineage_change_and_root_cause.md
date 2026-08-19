# 004 — Lineage, Change Attribution, and Root-Cause Reasoning

## Goal

Turn lineage from a static dependency map into an evidence structure for answering “where did this change come from?” and “what does it affect?”

## Root-cause stance

The system should help narrow causes, not manufacture certainty.

A useful explanation should be able to separate:

- observed facts;
- correlated events;
- plausible causes;
- eliminated causes;
- unresolved uncertainty;
- confirmed cause when confirmation exists.

## Canonical example: join-driven volume change

Assume:

`Table C = Table A JOIN Table B`

Historical state:

- A = 20M rows
- B = 10M rows
- C = 18M rows

Current state:

- C = 13M rows

A useful investigation should not stop at “C volume decreased.” It should inspect the relevant lineage and time window to determine whether:

- A lost rows;
- B lost rows;
- both changed;
- key uniqueness changed;
- nulls increased in join keys;
- key distributions shifted;
- match rate changed even when source volumes stayed stable;
- filters or transformation logic changed;
- a deployment changed join type or conditions;
- an upstream pipeline failed or became stale;
- one source contains the same row count but a materially different population.

The framework should support attribution at the level justified by available evidence.

## Temporal lineage

Root-cause analysis requires answering not just “what is upstream?” but “what was upstream, and what state was it in, at the time of the change?”

Useful temporal questions include:

- What changed immediately before the degradation began?
- Which upstream quality signal moved first?
- Which deployment was active for the first affected run?
- Did a dependency become stale before the downstream effect?
- Did multiple downstream datasets degrade after one shared upstream asset changed?

## Upstream reasoning

For a degraded asset, the system should help explore:

- direct inputs;
- upstream pipelines;
- upstream quality/freshness state;
- source volume and distribution changes;
- code/deployment changes;
- structural changes such as schema or key behavior;
- shared dependencies that might explain multiple symptoms.

## Downstream reasoning

For an affected or changing asset, the system should help identify:

- dependent tables/views;
- dependent pipelines;
- metrics and analytical products;
- reports/dashboards where available;
- business owners and consumers;
- downstream quality signals that have already moved;
- downstream assets that are likely exposed but not yet visibly degraded.

## Change attribution as a first-class capability

The framework should aim to answer forms of:

- “C lost 5M rows; 4.2M of that change is consistent with reduced matching population from B, while 0.8M remains unexplained.”
- “The first abnormal observation occurred in upstream pipeline X two runs before downstream table Y crossed its threshold.”
- “Three downstream datasets degraded after the same source table became stale.”

These examples are target reasoning patterns, not implementation commitments.

## Evidence chain

A root-cause explanation should be capable of referencing the evidence that supports it, potentially including:

- run history;
- freshness observations;
- quality observations;
- row/distribution metrics;
- lineage relationships;
- deployment history;
- code version;
- schema changes;
- ownership and semantic context;
- analyst or engineer annotations.
