# Phase 010 Group 02 — Persistence Reference Architecture

## Selected architecture

Group 02 selects a **lakehouse-first, framework-owned evidence persistence plane**.

Canonical structured state is stored in **Delta Lake tables**. Large or opaque retained payloads use a separately governed **cloud-object payload plane** referenced by durable manifests. Graph/search/vector/serving stores are derived projections and are not canonical truth stores.

This is the reference architecture. Exact catalog/storage realization is deployment-bound under ARCH-001–ARCH-032.

## Why this shape

The framework must retain high-volume time-series/operational evidence, bitemporal state, provenance links, history, long-running trends and replay data while remaining close to its Databricks/Spark execution environment. A lakehouse-first model provides scalable batch/stream-compatible structured persistence without requiring a separate always-on relational or graph database as the primary evidence ledger.

The architecture also keeps persistence semantics separate from a particular Databricks managed feature:

- Delta Lake is the structured storage contract.
- Unity Catalog managed tables are preferred where verified and policy-compatible.
- External Delta tables over organization-controlled object storage remain a supported realization.
- Unity Catalog volumes are preferred for non-tabular payloads where verified; direct governed object storage is the logical fallback.
- Preview/runtime-specific FILE or VARIANT capabilities are optimizations, not required semantics.

## Canonical logical store families

### 1. Evidence manifest journal

Stores one durable row per logical evidence occurrence, including at minimum:

- framework evidence ID;
- source system/capability-instance ID;
- source-local event/object/revision identifier or locator where available;
- source/provenance family and common-derivation identity;
- capture class;
- payload digest/reference where retained;
- event/effective coordinates;
- source-recorded/available coordinate where known;
- framework collection and persistence coordinates;
- sensitivity/minimization metadata;
- schema/parser/normalizer revision context;
- retention policy/state references;
- correction/supersession relationships;
- integration/acquisition context needed to understand limitations.

The manifest is the framework system of record for **what evidence it retained/observed and when**, not the authority for the source proposition itself.

### 2. Normalized source-fact journals

Typed source-fact families derive from evidence manifests and retain the exact evidence and parser/normalizer provenance that produced them.

They use append/supersede/correct semantics. Current-state views may be materialized, but current rows are derived convenience views over historical journals.

A single universal fact table is not required. Domain families may have purpose-specific schemas so that health, runtime, governance, Lineage, control and Explanation evidence do not collapse into one ambiguous record shape.

### 3. Proposition/basis and derivation links

Durable link tables preserve:

- bounded proposition identity;
- statement-to-basis relationships;
- basis role where applicable;
- common derivation;
- normalization/reprocessing lineage;
- correction/supersession lineage;
- source-to-normalized relationships.

These links support later reasoning and `inspectBasis` without making graph traversal itself truth.

### 4. Payload/object plane

Large, opaque or exact source artifacts can be stored outside structured rows with a manifest reference and integrity digest.

Payload retention is selective. Data minimization remains the default; no design requirement exists to warehouse full source payloads indefinitely.

### 5. Lifecycle and retention metadata

Versioned retention profiles, lifecycle state transitions, pin/hold dependencies, archive/restore records and irreversible purge records are canonical architecture-owned state.

Retention state is separate from proposition truth and reporting relevance.

### 6. Retained communication snapshots

When exact prior Explanation/communication retention is a product requirement, Group 06 can persist authentic snapshots using this plane: immutable snapshot identity, exact rendered/proposition content as required, audience/context, basis/projection references and communication time.

Reconstruction remains separate from retained actual communication.

## Derived projections

The following are **rebuildable** and may be selected/implemented by later groups:

- graph node/edge projections for topology/reasoning traversal;
- full-text/search indexes;
- vector/embedding indexes;
- materialized current-state views;
- low-latency API caches;
- report-oriented aggregates;
- analytical marts.

Derived stores carry canonical IDs and version/projection metadata. Their loss or staleness cannot rewrite canonical evidence.

## Delta Lake usage boundary

Delta ACID/versioning/physical history is useful infrastructure, but DMTZ replay is represented in the **rows and temporal journals themselves**. Product replay MUST NOT depend on Delta transaction-log time travel remaining available for the entire product retention horizon.

This avoids coupling years of business history to Delta log/deleted-file retention settings or to `VACUUM` behavior.

## Physical optimization

Allowed physical optimizations include compaction, liquid/manual clustering where deployment-supported, partition/layout evolution, statistics, caching and archival movement.

These are valid only if durable IDs, logical record content, provenance and historical relationships remain stable. Lossy rollup/downsampling is a retention-policy action, not a physical optimization.

## Security/residency

The logical persistence plane may be physically split by tenant, region, residency zone, classification or security boundary. A single physical global evidence lake is not required.

Cross-boundary references must be authorized and must never cause restricted payload duplication merely to make traversal easier.

## MVP consequence

The bounded MVP requires only:

- Delta Lake canonical structured journals/manifests;
- a payload/object capability where exact/large artifacts actually need retention;
- durable provenance/time/retention metadata.

A dedicated graph database, search engine, vector database, relational database or event store is **not an MVP persistence dependency**. Later groups may add derived stores when measured service requirements justify them.
