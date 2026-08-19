# Concept: Impact

**Status:** Candidate

## Purpose

Let users understand which downstream assets, consumers, metrics, reports, applications, or business processes may be affected by a monitored issue.

## Operational principle

A degraded Table C feeds a Metric View and two reports. Downstream lineage identifies them as impact candidates. One report is confirmed to have refreshed from the affected C version; another has not refreshed yet. Impact distinguishes potential exposure from confirmed affected consumption.

## Actors

- Business Analyst
- Data Engineer
- Data Owner / Steward
- Monitoring framework

## State

- originating issue/subject/time context;
- downstream candidate identity;
- relationship/evidence basis;
- impact status such as potential, exposed, confirmed affected, not affected, unknown (vocabulary deferred);
- timing and uncertainty;
- criticality/business context references where available.

## Actions

### `identifyCandidates`
Uses authorized downstream relationships/context to enumerate possible exposure.

### `evaluate`
Adds evidence about whether/how a candidate was actually affected.

### `revise`
Updates impact status as new evidence arrives while preserving history.

## Invariants / behavioral expectations

- Downstream lineage creates candidates, not automatic proof of impact.
- Impact status and evidence basis are explicit.
- Restricted downstream entities may be redacted/abstracted without falsely implying no impact.
- Business criticality may influence prioritization but is not itself proof of impact.

## Ambiguity and missing evidence

Incomplete lineage, delayed consumption evidence, restricted consumers, or ambiguous incident timing can make impact only potential/unknown. The concept must not equate reachability with actual affected consumption.

## Synchronizations

- Investigation supplies issue context.
- Lineage supplies downstream relationships.
- Execution History/Observation/Assessment can confirm whether a consumer used affected data.
- Semantic Definition/Ownership add business context.
- Explanation communicates blast radius appropriately.

## Security / privacy / governance considerations

Downstream impact can reveal sensitive reports, applications, business processes, or decision pathways. Results must respect audience authorization and policy context.

## Evidence / provenance considerations

Each impact status retains the relationship and consumption/assessment evidence that supports it, plus time context and revisions as downstream state becomes clearer.

## Representative scenarios

### Happy path
A report is confirmed to have refreshed from the affected C output.

### Degraded path
A downstream dashboard is reachable in lineage but has not refreshed, so impact remains potential.

### Conflicting evidence
Consumer refresh metadata disagrees with lineage timing.

### Unauthorized evidence
A user sees that one restricted downstream consumer may be affected without learning its identity.

## Non-goals

- remediation workflow;
- causal root determination;
- access granting;
- business criticality definition itself.

## Open questions

- What is the minimum distinction between potential and confirmed impact?
- Are business processes first-class identified entities in MVP?
