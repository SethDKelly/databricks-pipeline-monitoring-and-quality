# Phase 007 Group 06 — Impact, Consumer Encounter, Exposure & Consequence

**Status:** Review complete — accepted

## Goal

Refine the path from prospective downstream candidate to actual consumer/state encounter, downstream effect and technical/analytical/business consequence without collapsing those layers into one `affected` status or promoting them into causal attribution.

## Group result

Group 06 accepts **OPS-067–OPS-085**. No new concept is required. **Impact** remains the downstream candidate/exposure/effect/consequence association owner; underlying facts remain owned by Lineage, Execution History, Observation, Assessment, Change and other source concepts, while **Causal Claim** remains the attribution owner.

The realized downstream chain is:

**bounded originating state + consumer/use context → encounter opportunity/availability/publication context → evidence-established actual encounter/exposure → downstream effect evidence → consequence evidence → optional explicit Causal Claim attribution**.

No link automatically manufactures the next.

## Accepted OPS contracts

1. [`OPS-067 — Impact Proposition: Origin, Consumer, State & Scope`](067_impact_proposition_origin_consumer_state_scope.md)
2. [`OPS-068 — Encounter Opportunity, Availability, Publication & Actual Encounter`](068_encounter_opportunity_availability_publication_actual_encounter.md)
3. [`OPS-069 — Consumer Encounter Modes & Evidence Specificity`](069_consumer_encounter_modes_evidence_specificity.md)
4. [`OPS-070 — Exposure Resolution Vocabulary & Bounded State`](070_exposure_resolution_vocabulary_bounded_state.md)
5. [`OPS-071 — Execution, Refresh & Materialization Version Binding`](071_execution_refresh_materialization_version_binding.md)
6. [`OPS-072 — Publication, Serving, Query, Application & Business-Use Chain`](072_publication_serving_query_application_business_use_chain.md)
7. [`OPS-073 — Cache, Replica, Snapshot & Stale Safe-State Semantics`](073_cache_replica_snapshot_stale_safe_state.md)
8. [`OPS-074 — Multi-Hop Encounter Chain & Non-Transitive Exposure`](074_multihop_encounter_chain_nontransitive_exposure.md)
9. [`OPS-075 — Alternate Encounter Paths, Partial Path Coverage & Aggregation`](075_alternate_paths_partial_path_coverage_aggregation.md)
10. [`OPS-076 — Non-Exposure, No Opportunity, Safe-State & Unknown Negative Claims`](076_nonexposure_no_opportunity_safe_unknown_negative_claims.md)
11. [`OPS-077 — Repeated Encounter, First Exposure & Exposure Interval`](077_repeated_first_encounter_exposure_interval.md)
12. [`OPS-078 — Downstream Effect Binding & Dimension Scope`](078_downstream_effect_binding_dimension_scope.md)
13. [`OPS-079 — No-Effect / Unchanged Claims & Downstream Coverage`](079_no_effect_unchanged_negative_coverage.md)
14. [`OPS-080 — Consequence Categories: Technical, Analytical & Business`](080_consequence_categories_technical_analytical_business.md)
15. [`OPS-081 — Business Use, Decision & Customer Consequence Provenance`](081_business_use_decision_customer_consequence_provenance.md)
16. [`OPS-082 — Origin→Effect/Consequence Causal Attribution & Multiple Origins`](082_origin_effect_consequence_causal_attribution_multi_origin.md)
17. [`OPS-083 — Impact Priority, Criticality, Severity & Aggregation Discipline`](083_impact_priority_criticality_severity_aggregation_discipline.md)
18. [`OPS-084 — Historical Impact Replay, Correction & Restricted Projection`](084_historical_impact_replay_correction_restricted_projection.md)
19. [`OPS-085 — Impact Cross-Concept Ownership & Group 07 Handoff`](085_cross_concept_ownership_group07_handoff.md)

## Impact proposition and exposure vocabulary

A realized Impact inquiry is bound to the exact originating condition/state/version/window, consumer/use/interface/population context, historical relationship/path, encounter mode, time window and knowledge cut.

Group 06 accepts the bounded exposure results:

- `exposed`;
- `not exposed`;
- `safe/other-state encounter`;
- `encountered-state unknown`;
- `no relevant encounter opportunity`;
- `indeterminate`;
- `conflicting`;
- `unavailable`.

These results are proposition-specific rather than one permanent consumer flag. Authorization/redaction remains a separate concern rather than another epistemic exposure state.

## Opportunity, publication and encounter

Group 06 preserves:

**encounter opportunity ≠ state available ≠ state published/served ≠ state actually encountered**.

This matters across asynchronous and human-facing systems. A suspect output may be published yet never queried. A report may refresh but use a safe prior snapshot. A report can be viewed without any evidence that a business decision relied on it.

Encounter evidence is therefore consumer-mode specific: execution input, refresh/materialization, publication, query/read, cache/replica, application/API use, report/dashboard use and business-process/decision use can require different evidence.

## Version binding, caches and indirect exposure

OPS-071 consumes Group 04's run-specific input/output version reconstruction where available. `Latest output`, scheduler order, producer completion and active Deployment are still insufficient substitutes.

Cache, replica, snapshot and copied state are explicit encounter contexts. A consumer may be **not exposed to suspect V** because it remains on safe V-1 while separately violating freshness/currentness criteria.

Exposure is not transitive through topology. If B consumed A's suspect state, C is not automatically exposed to A merely because C uses some B output. An indirect A→B→C exposure proposition needs sufficient intermediary state/transmission and C-consumption evidence for the claim being made.

## Alternate paths and strong negatives

Consumers can have multiple material encounter paths. Exposure through one qualifying path can establish exposure; path-specific non-exposure cannot establish consumer-wide non-exposure while another material path remains unresolved.

`Not exposed` remains a REF-023 negative conclusion requiring sufficient opportunity, path and version/state coverage. Missing consumer telemetry, missing complaints, unavailable query logs or a safe result on only one path are not global non-exposure evidence.

Group 06 also separates `no relevant encounter opportunity`, `opportunity but no encounter`, and `safe-state encounter`; they may all imply absence of suspect-state exposure for a bounded proposition but have different operational meaning.

## Downstream effect

Downstream effect remains linked Observation/Assessment/Change evidence with exact dimension/scope/time. Exposure can exist with no monitored degradation, and an independently observed downstream effect can exist while exposure remains unknown.

`No downstream effect` is itself a strong bounded conclusion. A satisfied freshness or metric criterion does not establish that every technical, analytical or business dimension remained unchanged.

## Consequence

Group 06 uses descriptive consequence categories rather than a universal severity model:

- **technical/operational**;
- **analytical**;
- **business/process**, including customer/client/user or decision outcomes where evidenced.

Categories organize provenance-bearing consequence evidence; they do not create causal attribution, policy breach, monetary loss or severity by themselves.

Human/business use is a separate evidence boundary. Publication ≠ view; view ≠ decision reliance; reliance ≠ adverse consequence.

## Causal attribution

Impact layers remain evidence/context. The moment a statement asserts that an origin **caused, contributed to, enabled, triggered, prevented or materially influenced** a downstream effect/consequence, OPS-082 hands the proposition to Causal Claim under OPS-060/061 and REF-013–REF-020.

Even a confirmed upstream causal claim does not prove that every downstream consumer encountered the affected state or that an encountered consumer suffered the same effect. Consumer-specific encounter/effect/consequence evidence remains necessary.

## Priority and aggregation

Criticality, Classification, Semantic Definition, Responsibility Assignment and known business use can inform response priority, but do not establish Impact occurrence or probability.

Group 06 accepts no universal Impact score, exposure probability, severity-weighted descendant count, affected-node count formula or exposure percentage as a substitute for layered evidence. Any summary must preserve material safe/unknown/exposed/effect/consequence distinctions.

## Historical and restricted behavior

Impact is bitemporal and non-rewriting. Late query, refresh, cache or business-use evidence can change today's retrospective exposure/first-encounter/consequence result without rewriting what responders knew at the incident-time knowledge cut.

Restricted consumer/path/use evidence remains restricted rather than absent. Authorized coarse projection is permitted only when the underlying internal result is actually supported, and safe projection cannot strengthen an unknown/conflicting state.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **IM06-01–IM06-36**, including safe stale caches, unknown versions, publication without use, direct queries, alternate paths, indirect exposure chains, repeated encounter intervals, exposure without degradation, effect without encounter proof, business decision consequence, restricted consumers and late query evidence.

## Durable boundaries

- candidate/reachable ≠ encounter opportunity ≠ exposed.
- available/published/served ≠ actual use at every downstream boundary.
- refresh/run timing ≠ consumed-version proof.
- stale safe state ≠ suspect-state exposure.
- upstream exposure ≠ transitive downstream exposure.
- one safe path ≠ global non-exposure.
- `not exposed` requires bounded negative path/opportunity/version coverage.
- exposed ≠ downstream effect.
- downstream effect ≠ consequence.
- consequence ≠ causal attribution.
- `no effect`/`no consequence` require their own bounded evidence.
- Criticality/Classification/priority ≠ realized Impact.
- no universal Impact/exposure/severity score is accepted.
- confirmed upstream cause ≠ consumer encounter/effect/consequence.
- restricted ≠ absent.
- current retrospective Impact ≠ what was known then.

## Architecture boundary

Group 06 does not select consumer/query/cache instrumentation, event schemas/stores, BI/report/application integrations, version-attestation mechanisms, exposure algorithms, scoring models, Impact UI or technical architecture. Concrete source capability/coverage belongs to Phase 009 and implementation placement to Phase 010.

## Group exit gate

**Satisfied.** OPS-067–OPS-085 and IM06-01–IM06-36 establish exact realized Impact proposition binding, consumer-mode encounter evidence, bounded exposure vocabulary, safe/unknown/non-exposure semantics, caches/alternate/multi-hop paths, downstream effect/consequence evidence, causal handoff, prioritization discipline and historical/restricted behavior without a 25th concept.

**Next: Phase 007 Group 07 — Propagation Safeguard Scope, Enforcement, Release & Recovery.**
