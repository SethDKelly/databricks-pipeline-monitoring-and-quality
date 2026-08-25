# Phase 007 Group 05 — Investigation Lifecycle, First-Deviation Localization & Causal Handoff

**Status:** Review complete — accepted

## Goal

Refine Investigation as a structured operational inquiry that can localize where/when relevant deviation first becomes evidenced, preserve competing explanations and hand explicit causal propositions to Causal Claim without making Investigation, localization, proximity or closure the source of causal truth.

## Group result

Group 05 accepts **OPS-050–OPS-066**. No new concept is required. **Investigation** remains the bounded-inquiry truth owner and **Causal Claim** remains the causal-proposition/epistemic truth owner.

The central inquiry chain is:

**bounded question/outcome → evidence-backed candidate leads → source-owned evidence assembly → scoped localization → narrowing/exclusion under evidence burden → explicit causal proposition handoff → independent Causal Claim evaluation → Investigation closure/reopen history**.

No link automatically manufactures the next.

## Accepted OPS contracts

1. [`OPS-050 — Investigation Proposition, Question, Outcome, Scope & Knowledge Cut`](050_investigation_proposition_question_outcome_scope_cut.md)
2. [`OPS-051 — Investigation Lifecycle, Scope Revision, Closure & Reopen`](051_investigation_lifecycle_scope_revision_closure_reopen.md)
3. [`OPS-052 — Investigation Candidate / Lead Generation, Basis & Disposition`](052_candidate_lead_generation_basis_provenance_disposition.md)
4. [`OPS-053 — Investigation Evidence Assembly, Roles, Contradiction & Gap Tracking`](053_evidence_assembly_roles_contradiction_gaps.md)
5. [`OPS-054 — Localization Vocabulary: First Observed, Earliest Evidenced, Boundary & Consumer Effect`](054_localization_vocabulary_first_observed_earliest_evidenced_boundary_consumer.md)
6. [`OPS-055 — Localization Traversal, Semantic Scope & Topology Limits`](055_localization_traversal_semantic_scope_topology_limits.md)
7. [`OPS-056 — Reconciliation, Structural & Health Boundary Localization`](056_reconciliation_structural_health_boundary_localization.md)
8. [`OPS-057 — Execution, Version, Change & Temporal Localization`](057_execution_version_change_temporal_localization.md)
9. [`OPS-058 — Multiple Deviations, Branching & Competing/Compatible Leads`](058_multiple_deviations_branching_competing_compatible_leads.md)
10. [`OPS-059 — Lead Exclusion, Narrowing & Negative Evidence`](059_lead_exclusion_narrowing_negative_evidence.md)
11. [`OPS-060 — Investigative Lead → Explicit Causal Claim Handoff`](060_investigative_lead_to_causal_claim_handoff.md)
12. [`OPS-061 — Causal Claim Evaluation & Confirmation Independence from Investigation`](061_causal_claim_evaluation_confirmation_independence.md)
13. [`OPS-062 — Investigation Outcome, Operational Resolution & Causal Independence`](062_investigation_outcome_operational_resolution_causal_independence.md)
14. [`OPS-063 — Historical Investigation Replay, Late Evidence & Reopen`](063_historical_investigation_replay_late_evidence_reopen.md)
15. [`OPS-064 — Restricted / Opaque Evidence & Localization`](064_restricted_opaque_evidence_localization.md)
16. [`OPS-065 — Analyst / Automation Research, Provenance & Evidence Parity`](065_analyst_automation_research_provenance_parity.md)
17. [`OPS-066 — Investigation/Causality Cross-Concept Ownership & Group 06 Handoff`](066_cross_concept_ownership_group06_handoff.md)

## Investigation proposition and lifecycle

Investigation binds the exact question/outcome, subject/population/use scope, event/effective-time window, evaluation/knowledge cut, trigger and limitations. Scope changes are versioned rather than silently replacing the original inquiry.

Minimal lifecycle is `open → active ↔ paused → closed`, with reopening creating a new active interval. Lifecycle is independent of causal status. A closed Investigation can still contain only `supported`, `weakened`, `rejected` or `unresolved` Causal Claims.

## Leads are inquiry state, not hypotheses with hidden causal status

Candidate/lead generation may use Lineage, Change Intent/Deployment/Change, execution/version evidence, Phase 006 health/reconciliation, Impact context, analyst research or automation. Every lead keeps its generation basis and limitations.

No universal hypothesis score/rank is accepted. Graph distance, recency, severity, Criticality, number of affected descendants, model confidence or analyst seniority do not become causal probability.

## Localization vocabulary

Group 05 explicitly distinguishes:

- **first observed deviation**;
- **earliest evidenced state change**;
- **first localized transformation/reconciliation boundary**;
- **first downstream consumer effect**.

They may coincide, differ or remain indeterminate. Every `first` claim is bounded to searched topology/semantic scope, version/time ordering and evidence coverage.

Therefore **first observed ≠ earliest true deviation ≠ root cause**.

## Reconciliation and execution localization

Phase 006 reconciliation can identify the first transformation/version boundary where an expected relationship becomes mismatched without saying why. OPS-034–OPS-049 can identify last evidenced unaffected/first affected run, consumed version sets, run-specific implementation differences, retries/reruns and rollback contrasts.

These facts may be powerful causal evidence later, but they remain localization/contrast evidence until an explicit cause→effect proposition is created.

## Multiple deviations and narrowing

Investigation can retain several branches when deviations are simultaneous, dimension-specific, mutually exclusive alternatives or compatible contributors. It never requires one winner.

Excluding a lead is a strong bounded conclusion. `No deviation found`, `version not consumed`, `condition occurred after effect`, or similar narrowing is valid only when the evidence mechanism had adequate opportunity/coverage for that exact proposition. Lack of support is not rejection.

## Exact causal handoff

A lead remains investigative while it asks **where/when/what changed or merits examination**.

When an actor or system asserts **X caused, contributed to, enabled, triggered, prevented or materially influenced Y**, OPS-060 requires a Causal Claim binding cause, effect, role, time/context, mechanism/transmission assumptions and motivating evidence.

The claim then follows REF-013–REF-020. Investigation priority/localization does not transfer as claim status.

`confirmed` additionally remains evidence- and authority-gated under REF-017 and AUTH-034. Investigation closure, analyst consensus, model ranking, remediation success or incident-owner role cannot self-authorize confirmation.

## Operational resolution versus causal resolution

An Investigation may close because the operational question is resolved, the issue is sufficiently narrowed for action, available evidence remains unresolved, no actionable conclusion exists, or the inquiry is explicitly superseded/duplicated.

Operational mitigation can succeed while causality remains unresolved. Conversely, a Causal Claim can later change status after an Investigation closes.

## Historical and restricted investigation

Investigation history is bitemporal/non-rewriting. Late evidence can move the retrospective earliest deviation, change version association, add/exclude leads, challenge a claim or justify reopen while preserving what investigators knew and did earlier.

Restricted/opaque evidence can bound localization without becoming absent. Audience visibility of an Investigation does not imply visibility of every linked item, and safe projection cannot strengthen the underlying localization/claim state.

## Human and automated parity

Analysts and automation may suggest leads, organize evidence and propose claims under the same provenance/evidence rules. Reproducible facts must be recorded through their owning concepts; commentary stays Annotation. Neither human title nor model output is magic truth or confirmation authority.

## Scenario review

[`scenario_review.md`](scenario_review.md) passes **I05-01–I05-34**, including clear and ambiguous first-deviation localization, simultaneous deviations, deployment correlation, stale/mixed versions, retry/rerun/backfill effects, incomplete execution evidence, reconciliation boundaries, planned-versus-unplanned effects, historical topology, restricted evidence, negative lead exclusion, competing/compatible explanations, analyst/automation contributions, closure without confirmation and late-evidence reopen.

## Durable boundaries

- Investigation ≠ source evidence truth store.
- question/trigger ≠ presumed cause.
- lead ≠ Causal Claim.
- first observed/earliest evidenced/boundary mismatch/consumer effect are distinct.
- localization ≠ cause.
- Lineage/reachability/path length ≠ causal ranking.
- execution/version/deployment proximity ≠ cause.
- reconciliation mismatch ≠ cause.
- lack of evidence ≠ exclusion/rejection.
- multiple deviations ≠ forced single root cause.
- operational resolution ≠ causal confirmation.
- Investigation closure ≠ Causal Claim status transition.
- `confirmed` remains REF-017 + AUTH-034 gated.
- restricted ≠ absent.
- analyst/model result ≠ fact/authority by origin.
- current retrospective localization ≠ what investigators knew then.

## Architecture boundary

Group 05 does not select RCA algorithms, graph-search heuristics, hypothesis-ranking/scoring models, LLM/agent workflows, ticket/case-management systems, Investigation UI, event stores, source integrations or technical architecture.

## Group exit gate

**Satisfied.** OPS-050–OPS-066 and I05-01–I05-34 establish bounded inquiry identity/lifecycle, provenance-bearing lead/evidence organization, precise localization vocabulary, reconciliation/execution/change localization, multiple branches, evidence-bearing exclusion, explicit causal handoff, REF/AUTH confirmation separation, honest closure/reopen and restricted/human/automation handling without a 25th concept.

**Next: Phase 007 Group 06 — Impact, Consumer Encounter, Exposure & Consequence.**
