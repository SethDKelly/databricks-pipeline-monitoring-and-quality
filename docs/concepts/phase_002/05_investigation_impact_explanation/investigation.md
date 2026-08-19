# Concept: Investigation

**Status:** Accepted — Phase 002 Group 05

## Purpose

Let users organize a bounded inquiry into a question, symptom, unexpected outcome, or uncertainty by collecting and relating relevant evidence, claims, impacts, and human context without making the investigation itself a source of truth.

## Operational principle

Table C falls from roughly 20 million rows to 14 million after a registered filter Change Intent and active Deployment. The lower volume is partly expected, but a completeness Expectation also fails. An Investigation is opened for the relevant time window. It links the Change Intent, Deployment activation, execution sequence, A/B/C Observations and Assessments, historical Lineage, realized Changes, competing Causal Claims, downstream Impact state, and relevant Annotations. The investigation can close with multiple contributing causes or remain unresolved if evidence is insufficient.

## Actors

- Data Engineer / Pipeline Maintainer
- Business Analyst / Data Consumer
- Data Steward / Governance Steward
- Data Owner / accountable business party
- Incident responder / on-call engineer
- Monitoring framework

## State

- investigation identity;
- initiating question, symptom, Assessment, Change-Intent mismatch, Impact concern, or other bounded trigger;
- identified subjects and relevant effective/event-time window;
- current investigation scope and material scope-revision history;
- linked evidence references from source concepts;
- linked Causal Claims and their current epistemic states;
- linked Impact evaluations;
- linked Annotations;
- participating/responsible actors where useful;
- investigation lifecycle state;
- recorded/knowledge-time history of material investigation updates;
- known evidence gaps, restrictions, conflicts, and unresolved questions.

## Actions

### `open`
- **Intent:** create a bounded inquiry around a defined question, symptom, or uncertainty.
- **State effect:** records the initial subject/time/question context and provenance of the opening trigger.

### `linkEvidence`
- **Intent:** associate relevant evidence without copying or mutating the owning concept's state.
- **State effect:** records a provenance-bearing reference and its relevance to the inquiry.

### `linkClaim`
- **Intent:** associate one or more Causal Claims under evaluation.
- **Important:** linking a claim does not endorse or confirm it.

### `linkImpact`
- **Intent:** associate downstream Impact analysis with the investigation.

### `refineScope`
- **Intent:** revise the investigation's subject, question, or temporal boundaries as evidence changes the inquiry.
- **State effect:** preserves material prior scope rather than silently rewriting what was investigated earlier.

### `close`
- **Intent:** mark the inquiry complete for the current purpose.
- **Observable result:** resolved, unresolved, multi-causal, no actionable conclusion, or another later-agreed completion state.
- **Important:** closure does not itself confirm any Causal Claim.

### `reopen`
- **Intent:** resume a previously closed inquiry when materially new evidence or questions justify further review.
- **State effect:** preserves the earlier closure and its knowledge context.

## Invariants / behavioral expectations

- Investigation organizes inquiry; it does not own source evidence, health status, causal truth, or downstream truth.
- An Investigation can begin from a user question even when no degraded Assessment exists.
- An Investigation never requires exactly one root cause.
- Multiple contributing, competing, or unresolved Causal Claims may coexist.
- A registered Change Intent, active Deployment, or intent-consistent realized Change can be relevant evidence without proving cause.
- Evidence that contradicts the initiating theory remains eligible and must not be excluded merely because it weakens the leading explanation.
- Closing an Investigation unresolved is a valid result.
- Closing an Investigation cannot silently upgrade a Causal Claim to `confirmed`.
- Scope changes, material evidence additions, claim-status changes, and closure/reopening retain recorded/knowledge-time history.
- Restricted evidence can remain opaque or unavailable without the Investigation becoming an authorization bypass.
- An Investigation is not automatically an incident ticket, case-management workflow, or remediation workflow.

## Ambiguity and missing evidence

An Investigation may contain missing, conflicting, stale, non-comparable, inaccessible, or late-arriving evidence. Material gaps remain explicit. Lack of evidence for a candidate explanation is not evidence that the explanation is false; lack of contradicting evidence is not proof that it is true.

If historical evidence is discovered later, a retrospective investigation can distinguish what was true at the incident's effective/event time from what the product knew at the original investigation's recorded/knowledge time.

## Synchronizations

- **Assessment** can initiate an Investigation when a normative violation, atypical result, or unresolved health state merits inquiry.
- **Change Intent**, **Deployment**, **Execution History**, **Lineage**, **Change**, **Observation**, **Expectation**, and **Baseline** provide historical/evidence context.
- **Semantic Definition**, **Responsibility Assignment**, **Classification**, and **Policy Context** provide meaning, responsibility, and authorized governance context.
- **Causal Claim** owns causal propositions evaluated within the inquiry.
- **Impact** owns downstream exposure/consequence analysis linked to the inquiry.
- **Annotation** adds attributed human context.
- **Explanation** communicates an authorized synthesis of the Investigation and its underlying concept state.

## Security / privacy / governance considerations

Investigations aggregate information across sources and can create inference risk beyond any single datum. Authorization applies to the evidence view used by each audience, not merely to whether the Investigation object itself is visible.

A user may be allowed to know that restricted evidence or an opaque upstream entity materially limits the inquiry without being allowed to inspect the evidence, entity identity, policy detail, or raw values.

## Evidence / provenance considerations

Every linked material item should preserve its source-concept reference and provenance. Investigation-level history should make it possible to reconstruct what evidence was linked, what claims were under consideration, what scope applied, and what outcome was recorded at a relevant knowledge time.

## Representative scenarios

### Bounded join investigation
C falls materially. The Investigation gathers A/B/C evidence, Change Intent, Deployment, execution, Lineage, realized Change, and alternative claims without selecting a cause prematurely.

### Planned change with unintended violation
A planned filter explains the expected volume reduction, but completeness also fails. The Investigation treats the intended volume shift and unexpected completeness violation as distinct evidence rather than closing merely because a plan exists.

### No registered change
C degrades with no relevant Change Intent or Deployment. The Investigation proceeds using upstream data, execution, Lineage, and Change evidence; lack of planned-change context is an evidence gap, not evidence that nothing changed.

### Multiple contributing causes
B volume falls while join-key nulls also rise. The Investigation can retain two supported contributing Causal Claims rather than forcing a single winner.

### Historical reversal
A deployment is initially the leading explanation. Later evidence establishes that the first affected upstream Observation predates activation. The Investigation preserves the original knowledge state and the later revision.

### Unauthorized evidence
A restricted upstream dependency is known to be material but cannot be disclosed. The Investigation records the limitation and remains appropriately unresolved for the current audience.

## Non-goals

- incident/ticketing implementation;
- automatically proving causality;
- owning Causal Claim status;
- owning downstream Impact truth;
- modifying pipelines/data;
- remediation/rollback orchestration;
- broadening authorization;
- selecting an AI/agent investigation implementation.

## Deferred questions

- minimum lifecycle/status vocabulary for the first MVP;
- whether related/nested Investigations are needed beyond explicit cross-references;
- rules for automatically opening Investigations from Assessments or Change-Intent realization mismatches;
- retention/closure policies for low-value or duplicate investigations.
