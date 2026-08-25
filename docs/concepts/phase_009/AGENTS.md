# Phase 009 Agent Handoff

Applies to work under `docs/concepts/phase_009/` and complements the repository root `AGENTS.md`.

## Current status

- Phase 008 is complete with EXPL-001–EXPL-160 final.
- Phase 009 logical grouping is accepted.
- No INTG contracts are accepted yet.
- **Group 01 — Integration Contract Vocabulary, Source Roles & Capability Matrix is next.**
- Canonical repository status remains in `../../README.md#current-state`.

## Phase purpose

Phase 009 maps accepted functional semantics to actual source/integration capabilities. It discovers feasibility and limitations; it does not redesign the accepted truth model around vendor convenience.

## Required evaluation dimensions

For every material source surface, evaluate as applicable:

- source/system and exact surface/object/event/query/API class;
- accepted proposition(s) it may inform;
- evidence role and proposition-specific authority applicability;
- source-local identity plus join/reconciliation keys;
- event/effective time, recorded/knowledge time and clock semantics;
- granularity/cardinality and version/context binding;
- positive evidence support;
- strong-negative opportunity/coverage support;
- known completeness/coverage boundaries;
- access/authorization and disclosure sensitivity;
- availability and failure/unavailable behavior;
- latency and freshness characteristics;
- retention/history/replay behavior;
- correction, mutation, supersession and late-arrival behavior;
- rate/quota/cost characteristics where material;
- observability of the integration itself;
- duplicate/common-derivation relationships to other sources;
- support classification and residual gaps.

## Permanent boundaries

Never convert:

- available → authoritative;
- authoritative → sufficient;
- accessible → authorized for disclosure;
- missing → false/zero/no-event/no-path/no-exposure/no-effect/no-control;
- current state → historical state;
- Lineage → encounter/exposure;
- workflow success → deployment activation or run-specific version;
- active Deployment → actual run version;
- latest upstream output → consumed input;
- metric/check availability → governed Expectation/Baseline/Assessment;
- control configuration/decision → enforcement;
- Safeguard active + non-exposure → prevented exposure without REF-028 evidence;
- Gate HOLD → failed execution;
- Gate ADMIT → run;
- restricted/redacted → absent;
- source count → confidence;
- synchronization order → authority or causality.

## Source-family discipline

Do not structure the product around vendor names. Databricks, Unity Catalog, GitHub, DQX, Metric Views, Collibra, Immuta and downstream instrumentation may each support multiple accepted concepts, and one accepted proposition may require multiple source families.

A source may be authoritative for one metadata category and merely supporting/observational for another. Preserve proposition-, subject-, context- and time-specific authority.

## External-fact discipline

Phase 009 necessarily evaluates evolving vendor capabilities. Verify current external documentation when executing a group, distinguish product documentation from repository assumptions, record meaningful edition/feature/retention/permission limitations, and avoid treating undocumented behavior as guaranteed.

## Architecture boundary

Do not select SDK/client libraries, polling versus streaming, event buses, storage schemas, graph databases, caches, credential mechanisms, deployment topology, retry infrastructure, orchestration, LLM/retrieval architecture or UI. Phase 010 owns technical architecture.

## Group sequence

1. integration contract vocabulary/source roles/capability matrix;
2. identity/scope/governance/authority/authorization sources;
3. change/deployment/execution/version/runtime evidence;
4. health/schema/metrics/Expectations/Baselines/reconciliation evidence;
5. Lineage/consumer use/exposure/Impact evidence;
6. Investigation/causality/Safeguard/Gate/control evidence;
7. Explanation/historical replay/basis/disclosure source contracts;
8. cross-source coverage/latency/retention/cost consolidation and exit.
