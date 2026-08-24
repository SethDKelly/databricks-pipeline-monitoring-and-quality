# Phase 003 — Concept Synchronizations and Ecosystem Scenarios

**Status:** Active — Groups 01–04 accepted; pre-Group-05 Capability Authorization addendum accepted; Group 05 next

## Purpose

Phase 003 defines how the **22 accepted concepts** coordinate to satisfy end-to-end ecosystem behavior without collapsing independent truth boundaries or mapping synchronization chains to implementation architecture.

The original Phase 002 exit had 20 concepts. Phase 003 Group 03 exposed one missing independent behavior—protective hold/quarantine/release—and Phase 002 was narrowly reopened through the accepted Propagation Safeguard addendum. Before Group 05, authorization-separated analytical transparency exposed a second missing independent behavior: determining whether a principal may perform a named capability on a subject/context/time. Capability Authorization was therefore accepted as the 22nd concept.

A synchronization describes when concept actions/results coordinate, what information passes between them, necessary semantic ordering, and how ambiguity/failure/provenance/time/security behavior propagates. It is not automatically a workflow engine, service, transaction, event bus, database relationship, API call, or orchestration technology.

## Phase method

Every synchronization specification identifies outcome, participating concepts/actions, initiating condition, semantic preconditions, coordination/partial ordering, state/evidence ownership, ambiguity propagation, time semantics, provenance, authorization, invariants, scenarios, non-goals, and deferred questions. Use [`synchronization_template.md`](synchronization_template.md).

## Strategic groups

| Group | Theme | Primary synchronization focus | Status |
|---|---|---|---|
| 01 | Subject, Scope & Governance Context | Entity Identity → Monitoring Scope and independent governance-context resolution | **Accepted** |
| 02 | Planned Change & Reference Transition | Change Intent → prospective references / prospective Impact → Deployment realization → reference transition → empirical Baseline | **Accepted** |
| 03 | Runtime Evidence, Health & Realized Change | Deployment/Execution → timing/dependency Observations → time-valid Assessment / Change → analyst handoff / Propagation Safeguard | **Accepted** |
| 04 | Lineage, Investigation & Causal Reasoning | Bounded Investigation → historical Lineage candidate discovery → evidence assembly → competing Causal Claims / analyst research | **Accepted** |
| 05 | Downstream Impact, Annotation & Explanation | Impact reachability/exposure/effect/consequence; authorized analytical projection; Annotation/context → authorized Explanation | **Next** |
| 06 | Historical Replay & Phase 003 Consolidation | Whole-system composition; contemporaneous vs retrospective reconstruction; exit review | Planned |

The order is a reasoning dependency, not an implementation dependency.

## Accepted Group 02 results

- **SYN-004:** Change Intent can independently prepare explicit prospective Expectation review and/or Baseline comparability break.
- **SYN-005:** intent ↔ Deployment association requires provenance-bearing linkage and is not realization/health/cause.
- **SYN-006:** reference context transitions only from sufficient evidence for the relevant operating context.
- **SYN-007:** post-transition Baselines are empirical; Expectation can support immediate validation first.
- **SYN-008:** Change Intent + Lineage can produce a Prospective Impact Profile without claiming actual exposure/effect/consequence or quantified probability.

## Accepted Group 03 results

- **SYN-009:** executions associate with the active Deployment only where time/target evidence supports the mapping.
- **SYN-010:** start/completion/duration/queue and other operational timing become Observations before health interpretation.
- **SYN-011:** operational dependency timing can be assessed for readiness/latency while remaining separate from freshness, consumed-version proof, and cause.
- **SYN-012:** runtime Observations resolve against the correct time-valid Expectation/Baseline context; ordinary variation is not automatically anomalous or actionable.
- **SYN-013:** meaningful runtime/data differences may become realized Change; every numeric difference does not.
- **SYN-014:** analysts may open Investigation from material or uncertain Assessments; automatic initiation requires explicit later-accepted response criteria.
- **SYN-015:** Propagation Safeguard can protect downstream consumption proactively/reactively under explicit authority while remaining separate from Assessment/Investigation truth.

## Accepted Group 04 results

- **SYN-016:** Investigation opens around a defined question/outcome and bounded historical context rather than a presumed cause.
- **SYN-017:** historical typed Lineage yields evidence candidates; reachability and first-observed localization are not causal conclusions.
- **SYN-018:** candidate history assembles execution/timing/Observation/Assessment/Change/Deployment/intent/reference/safeguard evidence including contradiction and explicit gaps.
- **SYN-019:** causal propositions become explicit Causal Claims rather than remaining implicit in topology, timing, or narrative.
- **SYN-020:** claims are evaluated using temporal ordering, relationship applicability, encounter/consumption where required, realized state/change, mechanism compatibility, contrasts/alternatives, and evidence coverage.
- **SYN-021:** multiple contributing/competing claims and unresolved outcomes remain valid; Investigation closure never promotes claim status. `confirmed` remains gated on a later accepted evidence/authority standard.
- **SYN-022:** analyst research joins the same structured evidence model—reproducible facts become Observation/Change, causal propositions become Causal Claim, and contextual commentary remains Annotation.

## Accepted pre-Group-05 authorization refinement

- **Capability Authorization** determines whether a principal may perform a named capability on a subject/context/time without selecting IAM/enforcement architecture.
- Raw-data read, metadata/governance visibility, derived health/metric visibility, Lineage/RCA participation, job/run operational control, Change/Expectation authoring where later governed, safeguard control, and Explanation access are independently resolvable capability categories.
- Denial of raw-data access does not automatically deny approved monitoring/RCA analysis.
- Permission to operate/update a job does not imply raw-data access; permission to analyze does not imply production-control authority.
- Responsibility Assignment, Classification, Policy Context, and Monitoring Scope remain separate from Capability Authorization.
- Authorized analytical projection may safely expose derived/aggregate/redacted/opaque evidence while preserving restricted details and explicit limitations.
- Metadata and derived evidence can themselves be sensitive; they are not globally exempt from authorization.

## Cross-cutting synchronization rules

- Concepts own their own state/truth; synchronization does not manufacture umbrella state.
- Synchronization order is never authority; trigger is never causation.
- Unknown/conflicting/unauthorized/unavailable/insufficient/non-comparable results remain first-class.
- Partial progress is valid; one unresolved branch does not erase another.
- Monitoring Scope ≠ Responsibility Assignment ≠ Policy Context ≠ Capability Authorization.
- Raw-data read authorization ≠ metadata/health-analysis authorization ≠ Lineage/RCA authorization ≠ job-operation authorization ≠ safeguard authority.
- An authorized evidence projection may hide raw values/identities while retaining usable Assessment, timing, Lineage, policy, responsibility, causal, and Impact context where separately permitted.
- Restricted evidence must never be retrieved merely to create an unauthorized summary.
- Change Intent does not create Observation, realized Change, Expectation, Baseline, actual Impact, or cause.
- Prospective Impact ≠ actual exposure/effect/consequence and ≠ retrospective causal evidence by itself.
- Planned reference preparation ≠ realized transition.
- Deployment attempt/association/activation/intended-effect realization remain separate.
- Execution success ≠ timely execution ≠ freshness ≠ data quality.
- Missing telemetry ≠ missing run/output; absence requires sufficient coverage.
- Raw difference ≠ material Change; atypicality ≠ normative violation; violation ≠ cause.
- Investigation starts from an outcome/question; Lineage produces evidence candidates, not causes.
- First-observed deviation/localization ≠ root cause.
- Causal support and contradiction both remain provenance-bearing; absence/exclusion evidence requires adequate coverage.
- Multiple contributing causes and unresolved outcomes are valid.
- Automated reasoning may propose/support/weaken claims but cannot call a cause `confirmed` without an accepted confirmation standard.
- Human research routes to the concept owning the statement's meaning; Annotation is not a shadow evidence store.
- Baseline atypicality alone does not mandate Investigation or quarantine.
- Propagation Safeguard proposal ≠ active safeguard; active quarantine ≠ proof of defect; release ≠ proof of health.
- Downstream graph traversal does not create confirmed Impact or causal proof.
- Ledger-like correction/supersession semantics and event-time vs knowledge-time distinctions persist through every chain.
- No synchronization requires DQX, Metric Views, Collibra, Immuta, GitHub Actions, graph database, event store, message bus, workflow engine, LLM, IAM model, quarantine implementation, or selected technical architecture.

## Required ecosystem scenarios

Existing E-01 through E-15 remain required. Group 05 must additionally stress-test restricted-data analyst scenarios in which direct data access is denied but independently authorized health metrics, governance context, Lineage/RCA evidence, and Explanation remain usable; as well as the converse case where an operator may perform a job action without obtaining raw-data read authority.

## Phase 003 exit gate

Phase 003 is complete when all retained synchronization chains have explicit contracts; group scenarios compose without hidden state/architecture; planned change, runtime timing, health, safeguard, authorization, causality, Impact, and Explanation remain distinct; ambiguity and authorization are explicit; historical replay works across event/knowledge time; and ecosystem scenarios can be walked end-to-end using accepted concepts/synchronizations.

## Current review state

**Groups 01–04 are accepted. Capability Authorization is accepted as a pre-Group-05 addendum. Group 05 — Downstream Impact, Annotation & Explanation is next and has not yet started.**
