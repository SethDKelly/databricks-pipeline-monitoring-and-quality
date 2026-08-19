# Databricks Pipeline Monitoring and Quality

A planning-first product for understanding the **operational health, freshness, quality, lineage, governance, planned/realized change history, causal evidence, downstream business impact, and protective propagation state** of a Databricks-based Spark data pipeline ecosystem.

The central product idea is an **evidence-grounded reasoning layer over the data ecosystem**: a person should be able to ask what is happening, what was intended, what changed, whether timing or data behavior is acceptable, where a degradation first became observable, where it likely originated, what is actually supported as cause, what may be at risk downstream before a planned change, what is actually exposed or affected afterward, who is responsible, whether analyst intervention is warranted, whether suspect output is intentionally held, and what evidence supports each conclusion.

## Current design state

**Phase 003 — Concept Synchronizations and Ecosystem Scenarios: ACTIVE**

Phase 002 originally completed with 20 retained concepts. During Phase 003 Group 03, quarantine/hold/release requirements exposed one missing independent behavior, so **Propagation Safeguard** was accepted as a narrow post-exit Phase 002 addendum. The current catalog contains **21 accepted concepts**.

**Groups 01–04 are accepted. Group 05 — Downstream Impact, Annotation & Explanation is next.**

Group 02 includes prospective downstream blast-radius reasoning for planned changes. Group 03 formalized active Deployment/execution association, run-duration and dependency-latency evidence, time-valid health evaluation, analyst Investigation handoff, and Propagation Safeguard coordination. Group 04 now formalizes bounded Investigation, incident-time Lineage candidate discovery, historical evidence assembly, explicit Causal Claim formation/evaluation, multiple-contributor/unresolved outcomes, and analyst research entering the same structured evidence model.

A core Group 04 distinction is **first-observed localization ≠ root cause**. The earliest monitored point where a related deviation appears is useful for narrowing investigation, but it may sit downstream of an unobserved, restricted, or out-of-scope origin. Likewise, automated reasoning may propose/support/weaken causal claims but `confirmed` remains gated on a later accepted evidence/authority standard.

See [`docs/concepts/phase_003/README.md`](docs/concepts/phase_003/README.md) for the active Phase 003 plan and [`docs/concepts/phase_002/README.md`](docs/concepts/phase_002/README.md) for the accepted concept model/addendum history.

## Product thesis

A modern data pipeline can be operationally successful and still produce an unhealthy ecosystem outcome. A job may complete successfully but far too late, its inputs may be stale, a join may lose matches, a source feed may change shape, a planned filter may legitimately reduce volume, a missing output may threaten downstream client delivery, or an output may be risky enough that propagation should be held while evidence is reviewed.

The product therefore treats **execution occurrence, execution timing, dependency readiness, freshness, data quality, planned intent, realized change, historical topology, governance, causality, downstream consequence, human investigation, and propagation protection as related but distinct concerns** that must be reasoned about together.

The system should ultimately make questions like these straightforward to answer:

- Did this pipeline run, and how long did it take?
- Is a run merely slower than usual or does it violate an explicit completion/readiness requirement?
- Did an upstream delay put downstream delivery at risk even though downstream execution succeeded?
- Is current data behavior ordinary Baseline variation, materially atypical, or normatively unacceptable?
- Was a relevant change planned?
- What downstream blast radius should be reviewed before that change becomes active?
- Which Change Intent was associated with which Deployment, and what state actually became active?
- Did a planned change require a new Expectation or make an old Baseline non-comparable?
- Is a post-change run being evaluated against the correct time-valid reference context?
- Did a planned change behave as intended while another health dimension failed?
- Where in historical upstream Lineage did a relevant condition first become observable?
- Does that first-observed point represent the causal origin, or does monitoring coverage stop farther upstream?
- Which causal explanations are proposed, supported, weakened, rejected, confirmed, or unresolved?
- What evidence supports and contradicts each Causal Claim?
- Did the proposed cause actually precede the effect and traverse an applicable dependency/consumption path?
- Are multiple contributing causes supported rather than one forced root cause?
- Is automated evidence sufficient, or should an analyst open/reopen an Investigation and add structured research?
- Which downstream entities are only reachable, which actually consumed affected state, and which show observed/business consequences?
- Should a particular output or downstream boundary be held/quarantined, and is that safeguard actually active?
- Who bears the relevant technical/business/governance responsibility?
- What policy/sensitivity context applies?
- What evidence supports each material conclusion?
- What was known at the incident time versus what later evidence reveals retrospectively?

## Operating environment

Known environment facts remain deliberately small:

- Spark ETL pipelines execute in Databricks;
- pipelines are maintained across multiple Git repositories;
- GitHub Actions deploys jobs to Databricks;
- cross-pipeline/cross-repository dependencies exist;
- Databricks is a key execution and metadata source;
- Databricks Metric Views and DQX are strongly favored capabilities for later evaluation;
- Collibra and Immuta are available but optional.

These are environmental facts, not an implementation architecture.

## Design method: Concept Design

The product uses Concept Design, following Daniel Jackson's approach, before technical architecture. Phase 002 established independently understandable concepts; Phase 003 composes them through explicit synchronization contracts.

A concept is **not automatically** a class, service, database table, graph node, UI page, API, Databricks job, vendor feature, or quarantine mechanism. A synchronization is **not automatically** a service call, workflow engine, transaction, event, database relation, API, graph traversal implementation, or orchestration mechanism.

See [`docs/foundation/004_concept_design_method.md`](docs/foundation/004_concept_design_method.md), [`docs/concepts/`](docs/concepts/), and [`docs/concepts/phase_003/`](docs/concepts/phase_003/).

## Foundational principles

1. **Concepts before architecture.**
2. **Ecosystem over repository.** Repository/job boundaries preserve provenance but do not limit reasoning.
3. **Time/history are first-class.** Effective/event time and recorded/knowledge time remain distinguishable where material.
4. **Evidence over narrative completion.** Missing evidence may leave an answer unresolved.
5. **Intent, fact, assessment, causality, and protective control are distinct.** Change Intent ≠ Deployment ≠ realized Change ≠ Assessment ≠ Causal Claim ≠ Propagation Safeguard.
6. **Expectation is normative; Baseline is descriptive.** Planned values do not become empirical Baselines; ordinary variation should not become alert noise.
7. **Prospective reference preparation is not realized transition.** Reference context changes only when sufficient realization evidence establishes the relevant operating boundary.
8. **Prospective Impact is not actual Impact.** Planned blast radius identifies candidates/risk context, not actual exposure or consequence.
9. **Observation is not Assessment.** Missing telemetry is not observed absence.
10. **Successful execution is not timely execution.** Run duration, completion timing, dependency latency, freshness, and data quality can disagree.
11. **Lineage is typed, temporal, and graph-compatible.** Reachability is not cause or confirmed Impact.
12. **First-observed localization is not root cause.** The first monitored deviation may sit downstream of an unobserved/restricted origin.
13. **Historical state has ledger-like semantics.** Corrections/supersessions preserve prior knowledge rather than silently rewriting history.
14. **Degradation is not execution failure or mere atypicality.** Direction/normative context matters.
15. **Causal claims remain epistemically explicit.** Supporting and contradicting evidence remain traceable; correlation, Deployment timing, safeguard state, and intent consistency do not confirm cause.
16. **Multiple contributors and unresolved outcomes are valid.** The product never forces one root cause merely for narrative completion.
17. **Confirmed cause is gated.** Automated ranking/support cannot become `confirmed` until an explicit evidence/authority standard is accepted.
18. **Analyst Investigation is first-class.** Insufficient automated evidence can legitimately lead to human research, and structured analyst findings join the same concept/evidence model.
19. **Impact has layers.** Reachability, exposure, downstream effect, and business consequence are different strengths of statement.
20. **Propagation Safeguard is protective state, not a defect label.** Proposal ≠ active quarantine; release ≠ proof of health.
21. **Human context remains attributed.** Annotation does not rewrite evidence or substitute for structured concepts.
22. **Explanation is a view over authorized evidence.** Business and engineering views may differ in detail but remain evidence-consistent.
23. **Synchronization never manufactures authority.** Coordination order cannot choose a source of truth.
24. **Monitoring must not broaden raw-data or production-control authority.** Metadata, topology, intent, claims, safeguards, and annotations can themselves be sensitive.
25. **Databricks-native first where it fits; integrate before duplicate.** Favored tools remain evaluations, not concept definitions.

## Canonical example

Suppose **Table C** is produced by joining **Table A** and **Table B**. C historically produces about 20 million rows.

A planned filter on A may legitimately move C toward ~14 million. Before deployment, Change Intent + Lineage can identify a prospective downstream blast radius including C and client-facing consumers without claiming they will actually be affected. A prospective post-change Expectation may be established, and the old C-volume Baseline may receive a pending comparability break.

After the changed configuration becomes active, the first relevant execution may run for 55 minutes instead of its typical 20–30. The output may meet the revised volume Expectation while independently failing completeness. The model preserves separate run-duration, dependency-readiness, volume, completeness, freshness, and other Assessments. A materially atypical or violated result can be investigated by an analyst even if automated causal evidence is incomplete.

Suppose B's population drop is the earliest monitored deviation before C's loss. Group 04 can report **B as the first-observed localization** while still traversing B's historical upstream boundary. It then assembles incident-time evidence and evaluates explicit claims such as `B population reduction contributed to C loss`, `join-key null increase contributed to C loss`, and `the nearby Deployment caused C loss`. If C's degradation predates Deployment activation, that is material contradiction for the Deployment claim. If monitoring coverage stops upstream of B, causal origin remains appropriately unresolved.

Analyst research can add reproducible measurements as Observations/Changes, causal propositions as Causal Claims, and human business context as Annotations. Multiple contributing claims may remain supported. Until the later evidence/authority phase accepts a confirmation standard, automated RCA stops short of calling a supported claim a confirmed root cause.

If client-facing propagation risk is unacceptable, an authorized Propagation Safeguard can hold C's publication boundary while Investigation continues. That quarantine does not itself prove the data is defective, and any delivery delay created by the safeguard remains observable/assessable and can itself become a separately evaluated Causal Claim when evidence supports it.

This A+B→C scenario remains the recurring design test.

## Repository map

- [`docs/README.md`](docs/README.md) — documentation system of record and navigation.
- [`docs/foundation/`](docs/foundation/) — accepted product foundation and roadmap.
- [`docs/concepts/phase_002/`](docs/concepts/phase_002/) — accepted concept specifications and post-exit addendum.
- [`docs/concepts/phase_003/`](docs/concepts/phase_003/) — active synchronization contracts and ecosystem scenarios.
- [`docs/planning/`](docs/planning/) — earlier discovery tracks retained as non-authoritative inputs where superseded.
- [`docs/reference/glossary.md`](docs/reference/glossary.md) — canonical vocabulary.
- [`docs/decisions/`](docs/decisions/) — durable decision history/addenda.
- [`AGENTS.md`](AGENTS.md) — repository-agent instructions.
- [`.cursor/rules/`](.cursor/rules/) — Cursor project rules.

## Phase direction

Phase 003 remains documentation/design-first. The project must not jump from synchronization semantics directly to technical architecture: evidence/time/causality, governance/authority, quality/statistics, Lineage/Impact/safeguard behavior, business explanation, and integration contracts are refined before architecture selection.
