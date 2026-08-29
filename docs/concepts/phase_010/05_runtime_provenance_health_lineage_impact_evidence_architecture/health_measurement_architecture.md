# Health Measurement Architecture

## Separation

**definition/profile → Observation → applicability/comparability context → Assessment → exact-use suitability/readiness handoff**.

Group 05 realizes the persistence/provenance side; Phase 006 semantics remain authoritative.

## Measurement record

Material fields include:

- measurement ID/type
- canonical/source target IDs
- field/population/slice
- run/output/version when exact binding exists
- definition revision
- health-profile revision where assessed
- event/measurement/evaluation window
- observed value/count/status
- vendor/source status vocabulary
- acquisition run/surface/parser
- coverage/publication-lag/integration-health context
- derivation/basis IDs

## Source families

- Lakeflow expectation/event-log observations
- data-quality monitoring freshness/completeness/anomaly results
- profiling/drift metric tables
- Jobs/run metrics and health rules
- schema/compatibility observations
- organization-owned DQX/custom checks
- reconciliation checks
- domain event-time/watermark instrumentation

No source becomes universal health authority merely because it emits a health label.

## Freshness

Keep at least:

- commit freshness
- event-time/domain freshness
- source publication delay
- ingestion delay
- processing delay
- acquisition delay

They answer different questions.

## Historical relevance

Group 02 retention/relevance policy applies. Fine-grained measurements can age into approved trend aggregates only when future exact replay promises are preserved. Incident/report/claim basis remains pinned as needed.
