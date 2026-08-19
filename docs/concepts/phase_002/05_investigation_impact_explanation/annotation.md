# Concept: Annotation

**Status:** Accepted — Phase 002 Group 05

## Purpose

Let authorized humans add attributed contextual knowledge or commentary to ecosystem state without altering source evidence or silently taking over the responsibilities of more structured concepts.

## Operational principle

During an Investigation, a business stakeholder notes that a one-time month-end process made the affected period unusual. The Annotation is attached to the relevant Investigation/time context with author, time, and visibility. If the stakeholder is instead registering an intended pipeline filter, that structured fact belongs in Change Intent; if establishing an acceptable threshold, it belongs in Expectation; if confirming a cause, that action belongs on Causal Claim under the applicable confirmation standard.

## Actors

- Data Engineer / Pipeline Maintainer
- Business Analyst / Data Consumer
- Data Owner / accountable business party
- Data Steward / Governance Steward
- Incident responder / authorized reviewer

## State

- annotation identity;
- content/context;
- referent, such as Entity Identity, Observation, Assessment, Change, Investigation, Causal Claim, Impact, or Explanation snapshot;
- author/actor identity and responsibility context where relevant;
- assertion/recorded time and optional effective/context time;
- visibility/sensitivity context;
- revision/supersession history;
- withdrawal/dispute state where applicable.

## Actions

### `add`
- **Intent:** attach human-authored context to a defined referent with explicit attribution.

### `revise`
- **Intent:** create a traceable revision of material annotation content rather than silently overwriting history.

### `withdraw`
- **Intent:** mark an annotation as no longer endorsed/applicable while preserving its historical existence where required.

### `dispute`
- **Intent:** record that an annotation is contested without deleting either the original statement or the dispute.

## Invariants / behavioral expectations

- Annotation is human-authored context, not a source Observation.
- Annotation is not automatically a Causal Claim or causal confirmation.
- Annotation is not the primary mechanism for registering a planned modification; structured planned intent belongs in **Change Intent**.
- Annotation is not the mechanism for defining acceptable behavior; normative criteria belong in **Expectation**.
- Annotation is not the mechanism for assigning responsibility; that belongs in **Responsibility Assignment**.
- Annotation is not a governance Classification or Policy Context assertion merely because it mentions sensitive/policy information.
- A Causal Claim may cite an Annotation as human evidence/context, but the claim retains separate epistemic status and review semantics.
- Author identity/provenance remains explicit; organizational title alone does not make annotation content universally authoritative.
- Annotation cannot mutate or overwrite source evidence.
- Revision, dispute, and withdrawal preserve prior knowledge-time history.
- Absence of Annotation has no evidentiary meaning.

## Ambiguity and missing evidence

Annotations can be incomplete, mistaken, stale, disputed, withdrawn, or contradicted by source evidence. The product preserves these states rather than promoting human commentary to machine-observed fact.

If an Annotation contains a statement that should become structured operational truth, the appropriate owning concept must record that fact separately with its own authority/provenance semantics.

## Synchronizations

- **Investigation** can collect relevant Annotations.
- **Causal Claim** can cite Annotation as attributed human context/evidence without treating it as confirmation.
- **Change Intent**, **Expectation**, **Responsibility Assignment**, **Classification**, and **Policy Context** receive structured assertions when human context crosses into their respective purposes.
- **Impact** can reference an Annotation describing business consequence, while stronger consequence evidence remains separately attributable.
- **Explanation** may surface authorized Annotations clearly labeled as human-provided context.

## Security / privacy / governance considerations

Annotations can contain sensitive operational, personal, business, or policy information and can become a vector for accidental leakage. Authoring, revision, visibility, and retention must be controlled independently from raw-data authorization.

Documentation/tests must use synthetic annotation content and must not encourage copying real restricted values into free-form notes.

## Evidence / provenance considerations

Author, time, referent, visibility context, revision/dispute/withdrawal history, and any downstream citations are part of Annotation provenance. An Explanation or Causal Claim citing Annotation must preserve that the source is human-authored context.

## Representative scenarios

### Useful business context
A stakeholder records that a one-time month-end process changed normal comparison context. The note informs the Investigation but does not alter Observations/Baselines automatically.

### Planned change redirected to Change Intent
An engineer wants to record that a filter will be deployed tomorrow. The structured plan is registered as Change Intent rather than hidden in an Annotation.

### Incorrect note
A human states that a source outage caused the issue, but timing evidence later contradicts it. The Annotation remains attributed; the relevant Causal Claim can be weakened/rejected independently.

### Disputed context
Two stakeholders disagree about whether a business event explains the unusual volume. Both Annotations and the dispute remain visible with attribution.

### Withdrawal
An old note is no longer applicable. It is withdrawn without erasing its prior role in historical reasoning.

### Restricted note
The user can see that restricted human context exists but cannot read its sensitive text.

## Non-goals

- confirming causes by itself;
- registering structured Change Intent as a substitute;
- defining Expectations;
- changing source Observations/Assessments;
- responsibility assignment;
- chat/comment UI implementation;
- universal authority resolution.

## Deferred questions

- which actors may annotate which referents;
- whether first-MVP annotations need structured categories in addition to text;
- moderation/retention rules for unsafe or low-quality free-form content;
- whether some annotation classes require review before appearing in business-facing Explanation.
