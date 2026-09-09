# SYN-026 — Impact Evidence + Business Context → Consequence Evidence

**Status:** Accepted — Phase 003 Group 05

## Outcome

Record evidence that a downstream candidate experienced a technical, analytical, or business consequence while keeping consequence evidence separate from criticality, reachability, exposure, and causal attribution to the originating condition.

## Participating concepts and actions

- **Impact** — `recordConsequence`.
- **Semantic Definition** — business/technical meaning needed to interpret the downstream subject.
- **Responsibility Assignment** — relevant accountable/technical/steward contacts.
- **Observation**, **Assessment**, and **Change** — consequence facts where represented operationally.
- **Annotation** — attributed human consequence/context evidence where appropriate.
- **Classification** and **Policy Context** — disclosure/handling context, not consequence proof.
- **Capability Authorization** — controls which consequence/context details may be disclosed.

## Trigger / initiating condition

Evidence exists that a downstream candidate's availability, analysis, delivery, application behavior, process, client deliverable, decision, or other business context was materially affected or explicitly remained unaffected with sufficient coverage.

## Preconditions

The downstream subject and consequence assertion/evidence are identified with relevant time/provenance. Business meaning is not invented from a technical name alone.

## Coordination semantics

1. Resolve the downstream candidate and the semantic/business context needed to interpret the evidence.
2. Associate provenance-bearing technical, analytical, or business consequence evidence with Impact.
3. Preserve the strength/source type of that evidence. A human report remains attributed human evidence unless independently established through another concept/source.
4. `Client-facing`, `regulated`, `high-criticality`, or `executive report` may increase priority but are not evidence that a consequence occurred.
5. Exposure is not required for recording a downstream consequence fact, but if the consequence is claimed to have resulted from the originating condition, that causal proposition belongs in Causal Claim.
6. Policy/Classifications may determine handling and disclosure; they cannot be converted into `policy violation`, `regulatory harm`, or `non-compliance` without separate authoritative evidence.
7. `No business consequence` requires sufficient evidence/coverage appropriate to the claimed domain; absence of reported harm is not proof of no harm.

## State and evidence effects

Impact owns consequence associations. The underlying factual/context source remains owned by Observation/Assessment/Change/Annotation/Semantic Definition/etc.

## Ambiguity / failure propagation

Unknown client use, incomplete business-process telemetry, restricted consumer context, or ambiguous human reports preserve consequence as unknown/partial. High criticality never fills an evidence gap.

## Temporal semantics

Consequence evidence retains event/effective time and recorded/knowledge time. A business consequence learned later may enrich retrospective Impact without rewriting what responders knew earlier.

## Provenance / traceability

Every consequence statement identifies its source, time, and evidence class/limitations.

## Security / authorization

Business consequence can reveal client identity, strategic metrics, regulated workflows, decision pathways, or commercial harm. Safe explanations may use an authorized abstraction such as `one restricted client delivery was delayed` without exposing identity.

## Invariants

- criticality ≠ consequence;
- business-facing ≠ business harm;
- exposure ≠ consequence;
- downstream failure ≠ originating-condition causation;
- policy sensitivity ≠ policy breach/non-compliance;
- missing reported harm ≠ no harm;
- human consequence report retains human provenance.

## Scenarios

**Delayed client delivery:** delivery evidence establishes a business/operational consequence even before causal attribution is settled.

**Critical report not refreshed:** criticality raises priority, but no exposure/effect/consequence is manufactured.

**Report metric failed, use unknown:** analytical effect is known while business-decision consequence remains unknown.

**Restricted client:** an authorized audience sees an aggregate consequence without client identity.

## Non-goals

Criticality taxonomy, financial-loss calculation, legal/compliance determination, causal attribution, or incident prioritization policy.

## Deferred questions

Whether consequence categories need stronger first-class taxonomy in later refinement and what evidence is sufficient for specific client/business-process consequence classes.

## Later refinement — Phase 007 Group 06

OPS-080–OPS-081 retain technical/operational, analytical and business/process as descriptive consequence categories without a universal severity model. Publication, report view, decision reliance and resulting consequence are separately evidenced; human reports retain attributed provenance; `no consequence` requires domain-appropriate coverage; and Criticality/Classification/priority never manufactures consequence occurrence.
