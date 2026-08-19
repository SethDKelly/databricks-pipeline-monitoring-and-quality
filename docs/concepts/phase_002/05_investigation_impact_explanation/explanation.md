# Concept: Explanation

**Status:** Candidate (refined from Report / Explanation)

## Purpose

Let an authorized audience receive an evidence-grounded account of what happened, what is affected, what is known or uncertain, and where the supporting evidence comes from.

## Operational principle

A business analyst asks why Table C volume fell. The explanation states that C is degraded relative to baseline, B's volume changed first, A remained stable, a deployment occurred nearby in time but lacks causal confirmation, downstream reports may be affected, the responsible owners are identified, and the leading causal claim remains only supported—not confirmed. Each material statement is traceable to authorized evidence.

## Actors

- Business Analyst
- Data Engineer
- Data Owner / Steward
- Executive / operational stakeholder
- Monitoring framework

## State

- question/request or reporting intent;
- audience/context/time;
- material claims and their epistemic labels;
- evidence references/provenance;
- semantic/ownership/policy context used;
- generated/refreshed time and historical snapshot if retained;
- redaction/omission indicators where useful and safe.

## Actions

### `compose`
Produces a layered explanation from authorized concept state/evidence.

### `inspectEvidence`
Allows an authorized user to trace a material statement to supporting evidence/context.

### `refresh`
Produces an updated explanation as evidence/assessment/investigation state changes without silently rewriting a retained historical explanation.

## Invariants / behavioral expectations

- Explanation is not an independent truth source.
- Material factual/causal statements are traceable to source concepts.
- Epistemic status is preserved: observed, assessed, proposed, supported, confirmed, unknown, etc.
- Audience-specific detail may differ, but conclusions must not contradict the same authorized evidence merely for presentation convenience.
- Restricted evidence is not retrieved merely to summarize it for an unauthorized user.
- Policy/classification context is not translated into compliance claims.

## Ambiguity and missing evidence

If evidence is missing, conflicting, stale, insufficient, or redacted, the explanation must say so at the appropriate level. It must not fill gaps with plausible-sounding conclusions.

## Synchronizations

Explanation consumes authorized projections of Semantic Definition, Ownership, Classification, Policy Context, Assessment, Investigation, Causal Claim, Impact, Observation/Change, and other supporting concepts.

## Security / privacy / governance considerations

Question answering can combine individually harmless metadata into sensitive inference. Explanation must operate on an authorized evidence view and make safe omission/redaction behavior explicit.

## Evidence / provenance considerations

Each material claim should retain links to its source concept state and the evidence snapshot/time used. Audience-specific redaction must not destroy internal traceability of how the safe explanation was derived.

## Representative scenarios

### Happy path
A business analyst receives a concise account of degradation, likely source, impact, owner, and evidence status.

### Degraded path
The explanation states that the issue is confirmed degraded but root cause remains unresolved because upstream evidence is incomplete.

### Conflicting evidence
Competing causal claims are presented with their differing support rather than collapsed into one answer.

### Unauthorized evidence
The explanation safely abstracts a sensitive upstream asset and omits protected values while remaining useful.

## Non-goals

- defining the UI/chat/report rendering technology;
- generating new observations;
- changing causal status;
- replacing governance authorities;
- granting access.

## Open questions

- Which explanation structures are required for business analysts versus engineers?
- Which claims always require visible citations/evidence links?
- Should retained explanations be immutable snapshots or dynamically resolved views, or both?
