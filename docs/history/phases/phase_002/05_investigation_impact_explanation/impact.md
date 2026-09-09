# Concept: Impact

**Status:** Accepted — Phase 002 Group 05; prospective candidate semantics refined by Phase 007 Group 03

## Purpose

Let users understand the downstream exposure and consequences associated with an originating issue or condition while preserving the difference among graph reachability, actual exposure/consumption, observed downstream effect, and evidenced business consequence.

## Operational principle

A degraded Table C has downstream Lineage to a Metric View and two reports. All three are downstream candidates. The Metric View and Report 1 are proven to have refreshed from the affected C output, establishing exposure. Report 2 has not refreshed, so it is reachable but not yet exposed. Report 1 also shows a degraded business metric, establishing an observed downstream effect, while no evidence yet shows that a business decision was made from the bad result. Impact preserves these layers rather than calling every reachable node "affected."

## Actors

- Business Analyst / Data Consumer
- Data Engineer / Pipeline Maintainer
- Data Owner / accountable business party
- Data Steward / Governance Steward
- Incident responder / on-call engineer
- Monitoring framework

## State

- originating issue/condition/investigation reference and relevant time context;
- downstream candidate Entity Identity;
- Lineage/reachability basis and path provenance;
- **candidate/reachability state** — whether the entity is a plausible downstream candidate under authorized topology;
- **exposure/consumption state** — whether evidence shows the candidate consumed, depended on, or otherwise encountered the affected state/version/time window;
- **downstream-effect evidence** — linked Observation/Assessment/Change evidence showing whether the candidate's own condition changed or violated a criterion;
- **business-consequence evidence** — known effect on a report, metric use, application behavior, process, decision, customer/user outcome, or other business context where established;
- timing alignment and uncertainty for each layer;
- criticality/Semantic Definition/Responsibility Assignment context references where useful;
- revision/history as later downstream evidence arrives;
- authorization/redaction state for restricted downstream entities.

## Actions

### `identifyCandidates`
- **Intent:** use authorized Lineage and relationship context to enumerate plausible downstream candidates.
- **Observable result:** candidates with relationship/path basis and completeness limitations.

### `evaluateExposure`
- **Intent:** determine whether a candidate actually encountered the affected source/state/time window.
- **Observable result:** exposed, not exposed, unknown/insufficient, conflicting, unauthorized, or unavailable with evidence basis.

### `linkDownstreamEffect`
- **Intent:** associate downstream Observation/Assessment/Change evidence that describes what happened at the candidate.
- **Important:** an observed downstream degradation does not by itself prove that the originating issue caused it.

### `recordConsequence`
- **Intent:** associate evidence of a technical, analytical, or business consequence when such evidence exists.
- **Important:** consequence evidence retains its source/provenance and does not automatically establish causal attribution.

### `revise`
- **Intent:** update the impact picture as downstream evidence arrives while preserving prior knowledge-time state.

## Invariants / behavioral expectations

- Lineage reachability creates an Impact candidate, not proof of exposure or effect.
- Actual exposure/consumption is stronger than reachability but is not automatically equivalent to downstream degradation.
- A downstream Observation/Assessment change can coexist with uncertain causality to the originating issue.
- If the product asserts that the origin caused a downstream effect, that causal proposition belongs in **Causal Claim** with evidence and epistemic status.
- Business criticality influences priority/significance but is not evidence that an impact occurred.
- Business consequence is not inferred merely because a business-facing report is reachable or exposed.
- `not exposed` or `not affected` requires sufficient evidence for the relevant dimension; missing evidence cannot be converted into a reassuring negative.
- Restricted or out-of-scope downstream entities may remain opaque without being treated as absent.
- Different impact layers can disagree: a consumer may be exposed but unchanged, or may have an observed downstream issue without enough evidence to attribute it to the origin.
- Impact history preserves what was known at each relevant knowledge time.

## Phase 007 Group 03 prospective refinement

Impact's existing **candidate/reachability layer** can also be used before realization when the originating condition is an exact Change Intent revision/component.

Prospective candidate analysis consumes an OPS-021–OPS-022 scenario built from then-effective Lineage plus explicit planned additions/removals/modifications while preserving that planned relationships remain Change Intent state. Candidate bases can be effective-path, planned-added-path, path-loss/change or indeterminate.

Candidate relevance is field/key/population/interface/consumer/version scoped under OPS-024. Asset reachability does not prove every narrower use is relevant; missing fine-grained evidence remains indeterminate.

Prospective candidate/review findings do not populate the exposure, downstream-effect or business-consequence layers. They may identify proposal-bound structural compatibility or other Phase 006 review surfaces, but those remain their owning concepts' Assessments/review context rather than Impact truth.

Criticality/path properties may prioritize review but do not create probability, severity or actual Impact. No universal prospective risk score is accepted.

`Not a candidate`/`no blast radius` is a strong bounded negative proposition requiring sufficient topology, semantic relevance and alternate-path coverage. Restricted/opaque/incomplete topology remains a limitation, not absence.

Historical prospective analysis distinguishes the retained review actually produced, reconstructed `as-known-then` review and current retrospective recomputation. Late Lineage discovery may expand retrospective candidates without rewriting what was known during the original review.

## Ambiguity and missing evidence

Incomplete Lineage, delayed consumer refresh data, restricted entities, uncertain version association, ambiguous timing, or missing downstream monitoring can leave exposure or consequence unresolved.

A candidate outside Monitoring Scope can still be known as reachable when authorized, but the product should explicitly communicate reduced evidence/topology coverage rather than manufacturing downstream health evidence.

The same discipline applies prospectively: a known candidate set may be non-exhaustive, and zero discovered candidates is not automatically proof of no downstream candidate.

## Synchronizations

- **Investigation** supplies the originating question/issue context.
- **Change Intent** can supply a proposed originating condition for prospective candidate review without creating realized Impact.
- **Lineage** supplies typed downstream candidate paths but not impact proof; planned scenario topology remains a derived review view rather than Lineage state.
- **Execution History**, **Deployment**, **Observation**, **Assessment**, and **Change** can establish consumption/exposure and downstream state.
- **Causal Claim** owns propositions that an originating condition caused a downstream effect.
- **Semantic Definition** provides business meaning; **Responsibility Assignment** identifies relevant responsible parties; **Classification** and **Policy Context** constrain safe disclosure.
- **Explanation** communicates downstream reachability, exposure, effect, and business consequence without collapsing them.

## Security / privacy / governance considerations

Impact analysis can reveal sensitive reports, applications, business processes, strategic metrics, customer outcomes, or decision pathways. Authorization applies to candidate identity, path detail, exposure evidence, downstream effect, and business-consequence detail independently.

A safe explanation may state that additional restricted downstream consumers are potentially exposed without naming them.

Prospective review may likewise disclose that restricted downstream candidates exist without revealing their identity/path when authorized.

## Evidence / provenance considerations

Each reachability path, exposure determination, downstream-effect link, business-consequence assertion, and revision retains provenance, temporal context, and evidence limitations. Historical replay must be able to reconstruct what downstream state was known at the time.

Prospective candidate state additionally retains exact intent revision/component, effective/planned path basis, semantic relevance context and review knowledge cut.

## Representative scenarios

### Reachable but not exposed
Report 2 is downstream of C but has not refreshed since before the affected output. It remains a candidate, not an exposed consumer.

### Prospective planned-only candidate
A Change Intent proposes A→D. D is a prospective planned-added-path candidate; the relationship is not active Lineage and no exposure/effect is asserted.

### Prospective path-loss candidate
A Change Intent proposes removing B→C. C remains a candidate because loss of the currently effective dependency may be material if realized.

### Exposed but no observed degradation
A Metric View refreshes from affected C, but its aggregated metric remains within its Expectation. Exposure is established while downstream health remains acceptable on the monitored dimension.

### Exposed and downstream effect observed
Report 1 refreshes from affected C and its key metric violates an Expectation. Impact records both exposure and the downstream Assessment; a separate Causal Claim is needed to state that C caused the metric failure if that inference is not directly established.

### Business consequence unknown
A report is affected, but no evidence shows whether a business decision used it. Business consequence remains unknown rather than assumed.

### Cross-repository blast radius
A source issue traverses several repositories through typed Lineage. Repository boundaries do not prevent candidate discovery or exposure analysis.

### Restricted consumer
A viewer is told that an additional restricted business process may be exposed but cannot see its identity or detailed path.

## Non-goals

- defining Lineage itself;
- causal root determination;
- business criticality definition;
- incident remediation;
- granting access;
- assuming every reachable downstream node is affected;
- universal prospective risk scoring;
- selecting a graph traversal/storage implementation.

## Deferred questions

- exact realized exposure vocabulary/display semantics are refined further in Phase 007 Group 06;
- which consumers/business processes require first-class Entity Identity in MVP;
- what evidence is sufficient to establish version-level exposure for each consumer class;
- whether formal business-consequence categories are needed beyond provenance-bearing assertions;
- how impact prioritization combines criticality, exposure, and consequence without hiding uncertainty;
- concrete source/coverage support belongs to Phase 009 and technical graph architecture to Phase 010.

## Later refinement — Phase 007 Group 06

Phase 007 Group 06 accepts [`OPS-067–OPS-085`](../../phase_007/06_impact_consumer_encounter_exposure_consequence/README.md) and resolves the earlier realized-exposure questions without adding a concept.

The accepted realized downstream model is:

**exact originating state + consumer/use context → encounter opportunity/availability/publication context → consumer-mode actual encounter/exposure → downstream effect evidence → technical/analytical/business consequence evidence → optional explicit Causal Claim attribution**.

Additional accepted rules:

- opportunity, availability, publication/serving, and actual encounter are separate propositions;
- consumer-mode evidence may differ for execution input, refresh/materialization, query/read, cache/replica/snapshot, application/report, and human/business-process use;
- bounded exposure results are `exposed`, `not exposed`, `safe/other-state encounter`, `encountered-state unknown`, `no relevant encounter opportunity`, `indeterminate`, `conflicting`, `unavailable`, with authorization/redaction handled separately;
- Group 04 run/version evidence establishes exposure only where the exact encounter binding is supported;
- a safe prior-state encounter can establish non-exposure to suspect V while freshness/currentness is separately degraded;
- exposure is not transitively propagated through multi-hop Lineage, and alternate paths must be considered before consumer-wide non-exposure;
- `not exposed` requires REF-023/OPS-076 bounded opportunity/path/version coverage; the original `Report 2 has not refreshed` example is therefore only a strong non-exposure result when those conditions are satisfied;
- exposure is event/interval specific and can change with later encounters without rewriting history;
- `no downstream effect` and `no consequence` are also bounded negative claims with their own evidence burdens;
- consequence evidence may be organized descriptively as technical/operational, analytical, or business/process without creating universal severity or harm scores;
- publication ≠ view ≠ decision reliance ≠ adverse consequence;
- causal attribution remains Causal Claim truth under OPS-060/061/082 and REF-013–REF-020;
- confirmed upstream cause does not manufacture consumer-specific exposure/effect/consequence;
- Criticality/Classification/priority do not establish realized Impact, and no universal Impact/exposure/severity score is accepted;
- historical/restricted Impact remains bitemporal, non-rewriting and authorization-safe.

Concrete consumer-class source support remains Phase 009; instrumentation and technical architecture remain Phase 010.
