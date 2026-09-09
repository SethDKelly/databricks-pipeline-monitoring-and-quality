# Group 04 — Lineage, Investigation & Causal Reasoning

**Status:** Review complete — synchronizations accepted

## Goal

Define how bounded Investigations use historical typed Lineage and runtime/change evidence to discover evidence candidates, assemble relevant history, evaluate explicit competing Causal Claims, incorporate analyst research, and close honestly without forced root cause.

## Accepted synchronizations

- [`SYN-016 — Investigation Trigger → Bounded Inquiry`](016_investigation_trigger_bounded_inquiry.md)
- [`SYN-017 — Investigation Scope + Historical Lineage → Evidence Candidate Discovery`](017_historical_lineage_evidence_candidate_discovery.md)
- [`SYN-018 — Evidence Candidate → Historical Evidence Assembly`](018_candidate_historical_evidence_assembly.md)
- [`SYN-019 — Historical Evidence → Explicit Causal Claim Proposal`](019_evidence_causal_claim_proposal.md)
- [`SYN-020 — Causal Claim + Evidence → Support / Contradiction Evaluation`](020_causal_claim_evidence_evaluation.md)
- [`SYN-021 — Competing Causal Claims → Epistemic Evolution and Investigation Outcome`](021_competing_claims_investigation_outcome.md)
- [`SYN-022 — Analyst Research → Structured Evidence / Claim / Context`](022_analyst_research_structured_evidence_context.md)

## Accepted handoff from Group 03

- Material, violated, atypical, or unresolved Assessments may be investigated manually where authorized.
- Automatic Investigation initiation still requires explicit accepted response criteria.
- Execution duration/dependency latency, missing-output evidence, safeguards, and safeguard-induced delays are eligible evidence.
- Active Propagation Safeguard does not prove protected data was defective or that cause is known.

## Boundary decisions

### 1. Investigation begins with an outcome/question, not a presumed cause
The inquiry records what is being explained and a bounded event-time context. Scope may evolve, but prior scope/history remains reconstructable.

### 2. Lineage discovers candidates, not causes
Typed historical upstream/dependency traversal yields evidence candidates. Directness, path length, repository membership, and graph reachability are not causal ranking by themselves.

### 3. First-observed localization is useful but weaker than root cause
The earliest monitored point where a related deviation becomes visible can localize the problem. If monitoring stops at an out-of-scope/restricted boundary, the system can report that boundary without claiming the first visible node is the origin.

### 4. Historical evidence assembly must include contradiction
Investigation gathers execution, timing, Observation, Assessment, Change, Deployment, Change Intent, reference, safeguard, and Lineage evidence relevant to candidates. Evidence weakening the leading theory remains first-class.

### 5. Causal propositions are explicit
No causal statement is left implicit in a Lineage path, nearby Deployment, planned change, or explanation narrative. A cause/effect proposition becomes a Causal Claim with explicit epistemic state.

### 6. Causal evidence is multidimensional, not a generic score
Temporal ordering, effective relationship, actual encounter/consumption where required, realized state/change, mechanism compatibility, contrast/intervention evidence, alternatives, and evidence coverage can each strengthen or weaken a claim. No numeric probability is invented.

### 7. Negative/exclusion evidence requires coverage
`A did not change`, `C did not consume B2`, or `no prior failure existed` can weaken/exclude a claim only when the evidence source sufficiently establishes the negative. Missing telemetry remains missing evidence.

### 8. Multiple contributors and unresolved outcomes are first-class
A+B→C may have B-population loss and join-key degradation as concurrent contributing explanations. Investigation never requires one winner.

### 9. Confirmation remains intentionally gated
A claim can become proposed/supported/weakened/rejected/unresolved according to accepted review semantics. `confirmed` requires an explicit evidence/authority standard; Phase 003 does not invent it. In the absence of that standard, automated RCA must stop short of confirmation no matter how compelling its ranking appears.

### 10. Investigation closure does not change causal truth
An Investigation may close resolved for an operational purpose, multi-causal, unresolved, or with no actionable conclusion. Closing does not promote any Causal Claim.

### 11. Analyst research participates in the same evidence model
Reproducible analyst facts become Observation/Change; analyst causal propositions become Causal Claims; commentary remains Annotation; structured intent/norm/governance assertions go to their owning concepts.

### 12. Prospective blast radius is not retrospective causality
A pre-change Prospective Impact Profile can seed where to look but cannot support a retrospective causal claim merely because a later incident fell inside the predicted blast radius. Incident-time Lineage and realized evidence are still required.

### 13. Safeguards may themselves become causal conditions for operational outcomes
An active, enforced safeguard may support a claim that it contributed to delivery delay when timing/enforcement evidence supports that proposition. This does not imply that the protected data was actually defective.

## Scenario review

### E-01 — A+B→C unplanned degradation
Pass. A/B are discovered as candidates; B volume and join-key evidence can support distinct contributing claims; no single root is forced.

### E-04 — Unregistered change
Pass. Investigation proceeds from realized evidence without treating missing Change Intent as proof of impropriety or no change.

### E-05 — Stale upstream with successful downstream execution
Pass. Operational dependency and actual consumed-state evidence distinguish a successful run from a claim that stale upstream state caused stale downstream output.

### E-06 — Deployment-correlated shift
Pass. A degradation predating activation materially contradicts the deployment-cause claim while preserving Deployment as historical evidence.

### E-07 — Cross-repository dependency
Pass. Candidate discovery/evidence assembly cross repository boundaries while retaining provenance.

### E-09 — Restricted context
Pass. Opaque upstream evidence can limit or support a safe claim state without exposing restricted identities/details; uncertainty remains explicit.

### E-10 — Historical correction
Pass. Late evidence can reverse claim support and reopen a closed Investigation while preserving contemporaneous states.

### E-11 — Long-running upstream threatens delivery
Pass. Timing/dependency evidence can support a claim that upstream delay contributed to missed readiness when the required dependency/timing relationship is established.

### E-12 — Missing output and protective hold
Pass. Coverage-bearing absence evidence and safeguard history remain separate; the hold can be investigated as protection and as a possible contributor to later delivery delay.

### E-14 — Material atypicality with analyst research
Pass. Analyst research can add reproducible Observation/Change evidence and explicit claims without turning atypicality into failure or human notes into unstructured truth.

### E-15 — Safeguard creates delivery delay
Pass. Active safeguard/enforcement/timing can support a delivery-delay claim while protected-data quality remains a separate Assessment question.

## Additional adversarial scenarios

- current Lineage differs from incident-time Lineage;
- the earliest monitored deviation sits behind an out-of-scope upstream boundary;
- A appears unchanged but monitoring coverage was missing;
- two sources disagree on event ordering;
- retry/rollback changes the outcome under comparable conditions;
- a prospective blast-radius profile predicted C exposure but the incident is caused by an unrelated upstream condition;
- several supported contributing claims remain and evidence cannot justify `confirmed`.

## Deferred questions

- exact operational evidence/authority standard for `confirmed` Causal Claim;
- first-MVP epistemic status/review vocabulary and which transitions may be automated;
- evidence sufficiency rules for reliable negative/exclusion claims;
- whether causal chains among claims need first-class structured relationship semantics;
- how controlled contrasts/retries/rollback evidence should affect confidence without overstating causal inference;
- duplicate/related Investigation semantics and retention;
- automated hypothesis generation/ranking methods, if any.

## Group exit gate

**Satisfied.** Investigation now has explicit contracts for bounded scope, historical candidate discovery, evidence assembly, causal proposition formation, support/contradiction, competing/multiple claim outcomes, and analyst contribution. Historical topology, missing evidence, safeguard context, and prospective blast radius remain useful without being promoted to causal certainty.

The next group is **Group 05 — Downstream Impact, Annotation & Explanation**.
