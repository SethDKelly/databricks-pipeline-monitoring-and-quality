# Concept: Classification

**Status:** Candidate

## Purpose

Let the ecosystem state that an identified subject belongs to one or more sensitivity, governance, or handling categories without treating those categories as access grants or compliance conclusions.

## Operational principle

A table involved in an investigation is classified as containing PHI and PII by an authoritative source. A business-facing explanation may disclose the classification and risk context while withholding restricted values. If another source disagrees, the conflict is visible rather than silently resolved by whichever source synchronized last.

## Actors

- Governance / Data Steward
- Privacy / Security stakeholder
- Monitoring framework
- Business Analyst
- Data Engineer

## State

- classification assertions;
- subject identity and optionally classified facet/scope;
- category/label and source meaning;
- effective time;
- provenance/authority context;
- conflict/status information.

## Actions

### `classify`
Records or synchronizes a classification assertion.

### `reclassify`
Supersedes or changes an assertion prospectively while preserving history.

### `resolve`
Returns applicable classification assertions and conflicts for a subject/time.

## Invariants / behavioral expectations

- Classification is not authorization.
- Classification is not policy itself.
- PII/PHI/HIPAA-related labels are not proof of legal compliance.
- Source terminology should not be silently normalized in a way that loses meaning/provenance.
- Historical classification remains distinguishable from current classification.

## Ambiguity and missing evidence

Missing classification is `unknown/unclassified`, not automatically `non-sensitive`. Conflicts are explicit.

## Synchronizations

- Asset Identity identifies the classified subject.
- Policy Context may use classification as one input to applicable handling context.
- Explanation uses classification only within the viewer's authorized disclosure boundary.

## Security / privacy / governance considerations

Classification metadata can itself disclose the presence of sensitive information and may require restricted visibility.

## Evidence / provenance considerations

Classification assertions retain the original category vocabulary, source, effective time, and any normalization mapping used for cross-system interpretation. An effective classification must remain traceable to its assertions.

## Representative scenarios

### Happy path
A table is consistently classified as PHI/PII by the applicable authority.

### Degraded path
An important asset lacks classification; the result is unknown rather than non-sensitive.

### Conflicting evidence
One source marks an asset confidential while another marks it unrestricted; the conflict remains explicit.

### Unauthorized evidence
A user may be told that special handling applies without being shown the sensitive classification details that would reveal restricted information.

## Non-goals

- enforcing access;
- deciding regulatory compliance;
- defining business meaning;
- defining policy rules.

## Open questions

- Which classification vocabularies must be preserved verbatim versus normalized?
- Are classifications attached only to assets, or also columns/metrics/pipelines?
