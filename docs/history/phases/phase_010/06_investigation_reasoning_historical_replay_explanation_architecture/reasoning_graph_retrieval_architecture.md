# Reasoning Graph and Retrieval Architecture

## Selection

The MVP uses Delta-backed **derived node and edge projection tables** rather than introducing a dedicated graph database.

The projection is rebuildable from canonical Group 02–05 records and retains canonical IDs, edge type, effective/history coordinates, derivation rule and evidence provenance.

## Logical node families

Examples include Entity, Principal where authorized, Change Intent, Deployment, Run/Task/Attempt, implementation/input/output manifest, Measurement, Assessment, Lineage edge, Encounter, Exposure, Effect, Consequence, Investigation, Lead, Causal Claim, Statement and Evidence.

## Edge rules

Edges are semantically typed. `lineage_to`, `consumed`, `produced`, `measured`, `encountered`, `exposed`, `effected`, `supports`, `contradicts`, `limits`, `derived_from` and temporal-precedence edges are not interchangeable.

Each edge carries a derivation/source reference. Convenience edges cannot silently strengthen source semantics.

## Traversal

Traversal requests bind:

- proposition family;
- starting canonical entity/event IDs;
- relationship types;
- event/effective interval and knowledge cut;
- maximum depth/path constraints;
- Monitoring Scope where relevant;
- authorization/disclosure context;
- required acquisition/path coverage.

A traversal can find candidates; it does not automatically produce an answer.

## Dedicated graph-engine threshold

A graph product is justified only if measured workload shows that Delta/SQL/Spark/application traversal cannot satisfy required service classes or operational complexity. Introduction of such a product does not move canonical truth out of the evidence plane.

## Retrieval layers

1. exact structured retrieval by canonical identity/proposition/time;
2. typed graph traversal;
3. optional lexical/full-text search;
4. optional semantic/vector search for candidate recall.

Semantic similarity is a retrieval heuristic, never an evidence status.

## Authorization

Sensitive corpus eligibility is determined before material is exposed to a semantic index/model path where metadata or embeddings could reveal restricted existence. Index partitions/filters and request-level authorization are deployment concerns, but post-hoc UI hiding alone is insufficient.

## Provenance and rebuild

Every derived index records source watermark, transformation/projection revision and, for vector indexes, embedding model/revision. Reindexing changes retrieval behavior but does not rewrite canonical evidence or historical Explanation snapshots.