# Group 04 — Acquisition Reference Architecture

## Logical components

1. **Capability/Surface Registry Reader** — resolves Group 01 verified capability instance plus ARCH-135 surface definition.
2. **Acquisition Planner** — materializes ARCH-136 plan revision from service class, Monitoring Scope, source constraints and quota/cost policy.
3. **Adapter Worker** — executes one source-specific collection mode without owning domain semantics.
4. **Checkpoint & Coverage Journal** — persists progress, pages/partitions, windows, expected population and completion state.
5. **Raw/Source Envelope Writer** — retains allowed source bytes/fields, locators and integrity metadata.
6. **Normalizer** — versioned parser/mapper producing canonical evidence records while preserving source provenance/common derivation.
7. **Integration-Health Journal** — records health dimensions, lag, quota, schema/parser state, failures and recovery.
8. **Evidence Publisher** — marks durably persisted normalized evidence eligible for later reasoning.
9. **Reconciliation Scheduler** — ensures accelerator channels are periodically checked against bounded source state where completeness matters.

These are logical responsibilities, not required microservices.

## Acquisition objective

An acquisition objective binds:

- tenant/environment;
- capability instance;
- source surface;
- Monitoring Scope/materialization or explicit bounded source query population;
- service class;
- proposition/source family needs;
- temporal window;
- selected mode;
- plan revision;
- integration principal;
- quota/cost envelope.

## Hybrid pattern

### Reconciliation path

Used for enumeration, bounded current snapshots, missed-event repair, and population coverage.

### Incremental path

Uses cursor/token/timestamp/sequence/change version when the source contract supports it.

### Push/stream path

Reduces time-to-evidence. It must preserve delivery/source identity and be reconciled where missed-event completeness matters.

### Export path

Treats file/export batches as source surfaces with their own schedule, manifest and availability time.

### Demand/backfill path

Retrieves bounded material for Investigation, historical replay or basis inspection without pretending it was continuously available earlier.

## Commit boundary

The safe progression is:

**request/page received → source envelope persisted → normalization persisted → coverage/health updated → checkpoint advanced → evidence published**.

Implementations may optimize physically, but the semantic outcome must prevent progress from moving beyond unpersisted evidence.

## Multi-region/residency

Collectors execute inside or against permitted residency/security boundaries. Cross-shard coordination exchanges the minimum metadata necessary for scheduling/coverage; payloads do not move centrally merely to simplify collection.

## No hidden dependency on one scheduler

A Databricks Job, Kubernetes workload, serverless task, external scheduler or future orchestration platform can implement an acquisition objective if it preserves the accepted records and failure semantics.

Group 08 will choose deployment/runtime packaging.
