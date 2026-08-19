# Concept: Lineage

**Status:** Accepted — Phase 002 Group 04

## Purpose

Let users trace typed, directed relationships among identified ecosystem entities for the topology that was applicable at a relevant time, with provenance and uncertainty explicit.

## Operational principle

Table C is derived by joining A and B, is produced by Pipeline P, and feeds a Metric View/report. Lineage traverses upstream/downstream using typed relationships and historical validity. If a planned change says a new source D will be added, that proposed topology remains in Change Intent until runtime/catalog evidence establishes the actual relationship. An incident replay before activation continues to show the old topology.

## Actors

- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Monitoring framework
- Business Analyst / Data Consumer
- Data Steward / Governance Steward
- Integration/metadata sources

## State

- identified source and target entity identities;
- directed relationship type;
- relationship meaning/context;
- effective/valid interval when known;
- provenance/source and assertion/observation time;
- knowledge/record time where material;
- evidence quality/confidence for asserted, observed, or inferred relationships;
- supersession/correction history;
- conflict/ambiguity/completeness context.

## Actions

### `assertRelationship`
- **Intent:** record a source/authorized assertion that a typed relationship applies.

### `observeRelationship`
- **Intent:** record a relationship established/inferred from runtime, catalog, code, query, or other evidence with provenance/confidence.

### `supersedeRelationship`
- **Intent:** end/revise relationship validity without erasing historical topology.

### `correctRelationship`
- **Intent:** preserve a correction to earlier relationship evidence while retaining knowledge history.

### `traverseAt`
- **Intent:** traverse typed upstream/downstream relationships applicable at a relevant time.
- **Observable result:** path/subgraph plus relationship type, provenance, completeness/ambiguity, and authorized redaction context.

## Invariants / behavioral expectations

- Every relationship used for serious reasoning has an explicit type/meaning; generic untyped edges are insufficient.
- Data derivation, operational/execution dependency, production/consumption, and deployment provenance are not silently conflated.
- Current topology does not overwrite historical topology.
- Planned/proposed topology is not active Lineage until realization evidence establishes the relationship.
- Lineage represents relationship/dependency, not causal blame.
- Reachability does not prove actual downstream impact or upstream cause.
- Missing Lineage is not proof that no relationship exists.
- Inferred relationships retain confidence/evidence basis and are distinguishable from authoritative assertions.
- Entity identities remain distinct even when connected by replacement/migration/derivation relationships.
- Event/effective time and knowledge/record time remain distinguishable where correction/late discovery matters.

## Graph compatibility

Lineage is inherently graph-shaped: identified entities participate as nodes/referents and typed directed relationships form traversable edges over time. The accepted functional model therefore requires graph-compatible traversal semantics, including historical/authorized/incomplete subgraphs.

This does **not** select a graph database, RDF/property-graph standard, graph query language, or service architecture. A later technical design may realize the accepted semantics with graph-native storage, relational structures, lakehouse tables, indexes, or a hybrid approach.

## Ambiguity and missing evidence

Partial topology, stale metadata, conflicting edges, ambiguous identity, inferred relationships, and unauthorized nodes/edges remain explicit. Traversal may return `incomplete` with reason rather than presenting a falsely complete dependency model.

## Synchronizations

- **Entity Identity** supplies relationship endpoints.
- **Monitoring Scope** controls monitoring responsibility without erasing known relationships that cross scope boundaries.
- **Change Intent** can describe anticipated topology changes, but planned relationships do not become active Lineage automatically.
- **Deployment/Execution History** can provide evidence/context for relationships without being merged into Lineage state.
- **Change** can describe realized topology transitions using historical Lineage versions.
- **Observation/Assessment** attach health evidence to entities/runs without becoming edges.
- **Investigation** later traverses upstream Lineage to discover evidence candidates.
- **Impact** later traverses downstream Lineage to identify exposure candidates without treating reachability as confirmed impact.

## Security / privacy / governance considerations

Lineage can reveal sensitive asset names, architecture, business processes, restricted systems, and indirect relationships. Authorized traversal may return opaque/redacted nodes or indicate that a path/subgraph is incomplete without disclosing restricted details.

## Evidence / provenance considerations

Every material relationship retains its type, source, effective interval, assertion/observation basis, confidence where inferred, and correction/supersession history. Traversal completeness should be explainable from source coverage and authorization rather than implied.

## Representative scenarios

### A + B → C
C has typed derivation edges from A and B plus production/consumption relationships to its pipeline/consumers. An upstream RCA traversal can inspect A/B without conflating those data edges with deployment provenance.

### Planned new source
A Change Intent says D will become an additional source. Before activation, D is planned context only. After deployment/execution/catalog evidence establishes D→C, the Lineage relationship becomes effective from the supported time.

### Historical topology
C used B1 in January and B2 after a migration in February. January incident replay traverses B1; current topology does not replace the historical path.

### Cross-repository dependency
Pipeline P in repository X consumes an asset produced by pipeline Q in repository Y. The relationship remains first-class across repository boundaries.

### Incomplete restricted path
A business user sees that C depends on a restricted upstream entity represented opaquely and that upstream analysis is incomplete, without receiving the restricted identity.

## Non-goals

- root-cause determination;
- confirmed impact determination;
- execution lifecycle history;
- deployment activation history;
- planned-change registration;
- selecting graph storage/query architecture.

## Deferred questions

- minimum MVP relationship taxonomy;
- evidence hierarchy for code/catalog/runtime-derived Lineage;
- column-level Lineage scope for MVP;
- historical topology retention granularity;
- graph architecture evaluation criteria for later technical design.
