# Phase 010 Group 02 — Persistence Technology ADR

**Decision:** Accepted

## Decision

Use a **Delta Lake-first canonical structured persistence plane**, plus cloud-object payload storage for selectively retained large/opaque artifacts. Treat graph/search/vector/serving stores as optional derived projections.

## Hard requirements

Any option must preserve:

- durable evidence/proposition/basis identity;
- source ownership/authority after copy;
- bitemporal and multi-coordinate history;
- non-rewriting correction/supersession;
- common derivation;
- selective retention/downsampling without semantic loss;
- long-running analytical/history scale;
- security/residency partitioning;
- deployment variability;
- graceful degraded operation;
- rebuildable reasoning/index projections.

## Alternatives considered

### A. Delta Lake-first — **selected**

Strengths:

- natural fit with Spark/Databricks monitoring workloads;
- scalable history and trend analytics;
- ACID structured persistence;
- open table format with cloud-object backing;
- supports append/journal patterns and schema evolution;
- avoids making a separate always-on database mandatory for the MVP;
- can use managed or external deployment patterns depending capability/policy.

Tradeoffs:

- interactive point lookup/graph traversal may later need derived indexes/caches;
- Delta transaction-log time travel cannot be treated as the product replay retention contract;
- managed-table optimizations/lifecycle vary by deployment.

### B. PostgreSQL/relational canonical store — rejected as sole canonical store

Strengths: strong transactional semantics, mature indexing, convenient small relational state.

Reasons not selected as sole canonical plane: introduces a separate capacity/operations tier for high-volume evidence/history and becomes less natural for Spark-scale trend/replay workloads. A relational serving/control store may still be added later if a bounded use case justifies it.

### C. Graph database as canonical store — rejected

Strengths: traversal ergonomics.

Reasons not selected: relationship traversal is only one view of the model; a graph-first system risks making graph reachability appear authoritative and duplicates high-volume temporal evidence. Graph projections remain allowed/rebuildable.

### D. Search/vector database as canonical store — rejected

Search/ranking indexes are excellent derived retrieval accelerators but unsuitable as the durable truth/provenance ledger. Ranking also must not become truth/evidence strength.

### E. Vendor-native history only — rejected

Fails long-horizon replay, availability-by-K, retained communication and durable-basis requirements because vendor retention/configuration varies and expires.

### F. Event broker/event-sourcing platform as primary durable store — not selected for Group 02

Streaming/event infrastructure may later improve acquisition latency, but an event broker is not required to preserve the canonical historical model and would add an unnecessary MVP infrastructure dependency before Group 04 chooses acquisition architecture.

## Deployment realization

- Prefer Unity Catalog managed Delta tables when the concrete deployment verifies them and policy permits.
- Use external Delta tables over governed organization-controlled object storage where managed lifecycle is unavailable/inappropriate.
- Use Unity Catalog volumes for non-tabular payloads only when verified; otherwise use an equivalently governed cloud-object location.
- Do not require preview/beta FILE features or runtime-specific VARIANT support for canonical portability.

## Reversibility

The choice is moderately hard to reverse because canonical historical storage is foundational. Risk is reduced by using open Delta tables, stable logical IDs, explicit schemas and keeping derived graph/search/serving stores non-canonical.

## Deferred decisions

Group 02 does not select ingestion polling/streaming, orchestration, graph product, search/vector product, API serving database, cache technology, backup vendor or final cloud storage lifecycle configuration.
