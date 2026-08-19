# Concept: Annotation

**Status:** Candidate (split from Annotation / Confirmation)

## Purpose

Let authorized humans add contextual knowledge to monitored evidence or investigations without altering the underlying source facts.

## Operational principle

A business owner notes that a planned month-end source reduction explains part of a volume shift. The note is attached to the relevant investigation/time window with author and provenance. Original observations remain unchanged, and the note is not automatically promoted to a confirmed causal claim.

## Actors

- Data Engineer
- Business Owner / Analyst
- Data Steward
- Authorized reviewer

## State

- annotation content/context;
- subject/evidence/investigation reference;
- author/actor and timestamp;
- visibility/sensitivity context;
- revision/supersession history where allowed.

## Actions

### `add`
Adds contextual information to a referent.

### `revise`
Creates a traceable revision rather than silently rewriting material historical context.

### `withdraw`
Marks an annotation no longer applicable/endorsed while preserving history as required.

## Invariants / behavioral expectations

- Annotation is not source observation.
- Annotation is not automatically a causal confirmation.
- Author/provenance is explicit.
- An annotation cannot overwrite machine/source evidence.
- Visibility respects authorization/policy context.

## Ambiguity and missing evidence

Annotations can be incomplete, mistaken, disputed, stale, or withdrawn. Their human-authored nature and status must remain explicit; absence of annotation carries no evidentiary implication.

## Synchronizations

- Investigation can collect annotations.
- Causal Claim may cite an annotation as contextual evidence with appropriate weight.
- Explanation may surface relevant annotations when authorized and clearly labeled.

## Security / privacy / governance considerations

Annotations may contain sensitive organizational context or accidentally include restricted values. Authoring and visibility must be controlled, and examples in this repository must remain synthetic.

## Evidence / provenance considerations

Author, time, referent, revision/withdrawal history, and visibility context are part of the annotation provenance. Downstream use must cite the annotation rather than presenting its content as machine-observed fact.

## Representative scenarios

### Happy path
A business owner documents a planned source-volume reduction for the incident window.

### Degraded path
An old annotation is no longer applicable and is withdrawn without erasing history.

### Conflicting evidence
Two authorized humans provide incompatible context; both remain attributed.

### Unauthorized evidence
Sensitive annotation text is omitted while the investigation can still state that additional restricted context exists.

## Non-goals

- confirming causes by itself;
- changing source observations;
- chat/comment implementation details;
- ownership assignment.

## Open questions

- Which actors may annotate which subjects?
- Do annotations need structured types or only contextual text at MVP?
