# Lineage, Encounter & Impact Architecture

## Lineage journal

A Lineage edge records:

- exact source/target identities
- relationship family
- field/key/population/version scope where available
- direct/indirect status where source exposes it
- event/effective interval
- source event/statement/run IDs
- source/acquisition provenance
- coverage/limitation state

The graph is historical and non-rewriting.

## Query/read encounter

Where Databricks lineage supplies `statement_id`, it can be joined to query history for query execution context. Other execution modes may use native entity/run metadata or DMTZ instrumentation.

A query/read encounter is still distinct from human viewing or decision reliance.

## Cache/result state

Cached/materialized/copied/served state has an independent identity/version. Upstream current state cannot be assumed to be the state the consumer encountered.

## Exposure derivation

Exposure requires:

1. exact originating affected state;
2. consumer opportunity/availability;
3. actual encounter;
4. affected version/state binding;
5. path/use context.

Multi-hop exposure evaluates each hop. Alternate paths matter for global negatives.

## Effects and consequences

Technical effect, analytical/decision effect and business/customer/financial consequence are separate evidence families.

A vendor `downstream impact` or Criticality label can be retained as a bounded vendor assessment. It does not replace realized encounter/effect/consequence evidence.

## Causality

Impact proximity, timing and sequence are evidence inputs only. Group 06 owns explicit Causal Claim reasoning under REF/AUTH.
