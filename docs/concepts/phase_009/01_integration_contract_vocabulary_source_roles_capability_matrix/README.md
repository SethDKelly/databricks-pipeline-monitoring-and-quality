# Phase 009 Group 01 — Integration Contract Vocabulary, Source Roles & Capability Matrix

**Status:** Review complete — accepted

## Goal

Define the reusable integration-contract vocabulary and evaluation matrix that every later Phase 009 source review must populate.

## Group result

Group 01 accepts **INTG-001–INTG-022** and the scenario suite **IC01-01–IC01-40**.

No new product concept is required. Integration contracts describe what actual source surfaces can and cannot evidence while accepted concepts retain truth ownership.

The central contract chain is:

**exact source surface + semantic/version context → bounded accepted proposition → evidence role → authority applicability → identity/join contract → temporal coordinates → evidence grain/context → positive capability → negative/opportunity/coverage capability → availability/latency → retention/replay → mutation/correction → disclosure constraints → derivation/independence → quota/cost → integration observability → proposition-specific support classification + residual gaps**.

No arrow creates stronger truth automatically.

## Accepted contracts

1. **INTG-001** — Source Surface Capability Identity & Version Context
2. **INTG-002** — Proposition Binding & Truth-Owner Boundary
3. **INTG-003** — Evidence Role Taxonomy & Source Assertion Type
4. **INTG-004** — Authority Applicability & Standing Boundary
5. **INTG-005** — Relevance, Sufficiency, Eligibility & Authorization Separation
6. **INTG-006** — Access, Retrieval & Disclosure Capability
7. **INTG-007** — Subject Identity & Join Contract
8. **INTG-008** — Cross-System Association Strength & Join Evidence
9. **INTG-009** — Temporal Coordinate Contract
10. **INTG-010** — Granularity, Cardinality & Context Binding
11. **INTG-011** — Positive Evidence Capability
12. **INTG-012** — Negative Evidence Capability & Opportunity Coverage
13. **INTG-013** — Coverage, Completeness & Observable Population Boundary
14. **INTG-014** — Availability, Latency, Freshness & Knowledge Eligibility
15. **INTG-015** — Retention, Historical Replay & Snapshot Capability
16. **INTG-016** — Mutation, Correction, Backfill, Deletion & Supersession
17. **INTG-017** — Duplicate, Common Derivation & Independence
18. **INTG-018** — Conflict, Fallback & Source-Precedence Boundary
19. **INTG-019** — Support Classification & Residual Gap Taxonomy
20. **INTG-020** — Quota, Rate, Cost & Operational Constraints
21. **INTG-021** — Integration Observability & Failure-State Evidence
22. **INTG-022** — Capability Matrix Composition & Group 02 Handoff

## Source roles

A source surface may be observational/measured, declarative/assertive, normative/reference-bearing, an operational event/action record, relationship/association evidence, authorization/permission evidence, contextual/limiting evidence, or a derived/projection/reporting surface.

These roles are descriptive only. They do not grant Assertion Authority, establish evidence sufficiency, make evidence independent, or authorize disclosure.

A surface can have different roles for different propositions.

## Capability matrix identity

`Databricks`, `GitHub`, `Collibra`, `Immuta` or another product name is not sufficient source identity for a capability decision.

Each evaluated row binds the exact source surface/API/table/event/query/export/object class and the semantic/version/edition context that materially affects identifiers, timestamps, fields, coverage, retention, permission or behavior.

Multiple surfaces from one system can therefore receive different support classifications.

## Support classification

Support classification is bound to **proposition + source set + context**, not vendor.

Accepted outcomes are:

- `supported`;
- `partially supported`;
- `unsupported`;
- `unknown / not yet verified`;
- `not applicable`.

These describe integration feasibility only. They are not truth, confidence, completeness, health or quality states.

`unsupported` is a valid design finding. It does not permit weakening accepted REF/AUTH/HLTH/OPS/EXPL requirements.

## Authority and evidence discipline

Group 01 preserves:

**available ≠ relevant ≠ eligible ≠ authoritative ≠ sufficient ≠ authorized for disclosure**.

Authority remains proposition/category/context/time specific. A fallback source does not inherit authority from an unavailable preferred source. Source recency, count, specificity, synchronization order and product prominence create no hidden precedence.

## Identity and association discipline

Source-local identity and cross-system association are first-class contracts.

Names, labels and timestamp proximity cannot establish ecosystem Entity Identity, deployment↔run association, run↔version binding, consumer↔version encounter, or control decision↔enforcement by convenience.

Where exact association cannot be supported, later groups must preserve partial/unknown state or candidate evidence rather than invent a join.

## Temporal discipline

Event/effective time, source recorded/committed time, correction/supersession time, first reliable availability time and framework retrieval time are distinct.

A record with an old event timestamp retrieved today does not prove the record was available at an earlier knowledge cut. Late/backfilled evidence may improve current retrospective interpretation without entering the earlier cut.

Clock precision, timezone, ordering guarantees and known skew matter when a proposition depends on sequence or cutoff.

## Positive and negative evidence

Positive and negative capability are independently evaluated.

A source that reliably records runs may establish that a run occurred while being unable to prove `no run` if expected opportunity, collection completeness or source-health coverage is unavailable.

Strong negatives require the exact opportunity/population/path/window and sufficient collection/query coverage. `No record returned` during outage, throttling, partial pagination, permission failure or unknown coverage is not evidence of absence.

## Coverage and granularity

Coverage is bounded by the population, mode, path, workspace/account, time window, event class and grain actually observable.

One fully covered consumer mode cannot establish consumer-wide non-exposure. Asset-level state cannot silently answer a field-, run-, consumer-, path- or version-specific proposition.

No universal integration-completeness score is accepted.

## History and correction

Current-state availability is separate from historical replay capability.

Retention horizon, mutation model, explicit correction history, late/backfill behavior, deletion/tombstones and recorded-time semantics determine whether as-known-at-cut replay is supported.

Destructive mutation or missing history is allowed to produce a partial/unsupported replay result; reconstruction by assumption is not.

## Independence and conflict

Different APIs/exports may derive from the same underlying telemetry and must not be counted as independent corroboration.

Source conflicts remain conflicts absent an accepted authority/evidence rule. A different endpoint, fallback source or later synchronization does not automatically resolve them.

## Operational feasibility

Quota, rate, volume and cost constraints are recorded where they can change feasible coverage or latency. They cannot change proposition semantics.

Integration observability must distinguish source-side absence from auth failures, permission denial, throttling, pagination failure, schema/API drift, parser failure, delayed indexing and source outage when those failures affect evidence interpretation.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **IC01-01–IC01-40**, including surface/version ambiguity, authority/sufficiency separation, joins, T/K ambiguity, late evidence, current-only history, negative evidence under outage, partial path/population coverage, duplicate/common-derived evidence, conflict/fallback, control and Lineage overreach, quotas and integration failure.

## Decisions

Durable Group 01 decisions are recorded in [`../../../decisions/phase_009_group_01_integration_contract_vocabulary.md`](../../../decisions/phase_009_group_01_integration_contract_vocabulary.md) as **D-900–D-934**.

## Architecture boundary

This group defines evaluation semantics only. It does not choose adapter interfaces, SDKs, ingestion jobs, schemas, queues, polling/streaming, caches, credentials, persistence or deployment topology.

## Handoff

Group 02 applies INTG-001–INTG-022 first to Entity Identity, Monitoring Scope, Semantic Definition, Responsibility Assignment, Classification, Policy Context, Assertion Authority and Capability Authorization source families.

Every material Group 02 source claim must populate the accepted matrix rather than relying on vendor reputation or convenience.