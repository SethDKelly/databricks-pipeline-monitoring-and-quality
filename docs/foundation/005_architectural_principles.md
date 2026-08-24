# 005 — Architectural Principles

## Scope

These are constraints on future architecture, not an architecture selection.

## AP-01 — Conceptual architecture precedes technical architecture
Technical modules emerge from accepted concepts/synchronizations, not vice versa.

## AP-02 — The ecosystem is the reasoning boundary
Reason across repository/job/workspace/pipeline/domain boundaries while preserving them for provenance/responsibility.

## AP-03 — Time and history are first-class
Future architecture must support point-in-time questions about intent, active Deployment, executions, Lineage/topology, Expectations, Baselines, Observations, Assessments, realized Changes, Investigations, causal knowledge, Impact, control state, authorization, and Explanation history.

## AP-04 — Evidence is preserved separately from interpretation, intent, and causality
Change Intent, Deployment evidence, execution facts, Observations, Baselines, Expectations, Assessments, realized Changes, Causal Claims, Annotations, and Explanation remain distinguishable.

## AP-05 — Provenance is part of every material fact
Responsibility Assignments, semantic definitions, classifications, Policy Context, Change Intents, Deployments, executions, Lineage, Expectations, Observations, Baselines, Assessments, Changes, gate/safeguard state, claims, Impact evidence, Annotations, authorization, and Explanations retain source/temporal provenance appropriate to use.

## AP-06 — Lineage is typed
Distinguish data derivation, operational dependency, production/consumption, and deployment provenance rather than one ambiguous edge.

## AP-07 — Monitoring models degradation, not only failure
Successful execution can coexist with freshness/quality violations; Baseline deviation alone is not normative degradation.

## AP-08 — Expectations, Baselines, Observations, and Assessments are separate
What should happen, reference behavior, observed fact, and interpretation remain distinct. Planned values do not become Baselines; planned effects do not become Expectations automatically.

## AP-09 — Historical comparisons and assessments must be reproducible
Historical Assessment should resolve the evidence/reference versions available/used at the time. Late/corrected evidence creates traceable reassessment without deleting prior knowledge.

## AP-10 — Security boundaries follow data authority, not monitoring convenience
Monitoring does not broaden raw-data access; metadata, causal claims, topology, intent, Impact state, control state, and Annotations may also be sensitive.

## AP-11 — Data minimization is a design requirement
Prefer metadata/aggregates/checks/fingerprints over copied row-level sensitive data.

## AP-12 — Governance metadata participates in reasoning
Semantics, Responsibility Assignment, criticality, Classification, and Policy Context affect explanations/impact/escalation without owning health evidence.

## AP-13 — Policy transparency is not compliance certification
Policy/classification/control evidence never mechanically becomes legal compliance conclusion.

## AP-14 — Tool integration is replaceable at the concept boundary
Databricks, GitHub/GitHub Actions, Collibra, Immuta, DQX, Metric Views, and future tools are providers/realizations, not concept definitions.

## AP-15 — Databricks-native capabilities are favored, not worshipped
Prefer native capabilities where they satisfy accepted concepts cleanly; add only missing functionality.

## AP-16 — Question answering is a view over evidence
Conversational/reporting experiences derive from authorized evidence/context and never become independent truth sources.

## AP-17 — Unknown is a valid result
Incomplete, insufficient, non-comparable, conflicting, unavailable, unauthorized, or unknown context is valid.

## AP-18 — Human/planned intervention has explicit semantics
Expectation revision, Change Intent registration, Baseline comparability decisions, Causal Claim review/confirmation, or Annotation remain distinct from machine-derived Observations.

## AP-19 — Business and engineering views share underlying state
Different projections may expose different authorized detail but derive from the same evidence/history and cannot intentionally contradict it.

## AP-20 — The product remains useful with optional systems absent
Collibra/Immuta absence should degrade enrichment, not invalidate core operation.

## AP-21 — Planned intent, active deployment, realized change, and health are distinct
Architecture must preserve **Change Intent → Deployment activation → Execution → Observation/realized Change → Assessment** without collapsing links. Planned change can be valid yet coexist with unintended violation; violation can occur without change; Deployment can occur without material data Change.

## AP-22 — Historical state has ledger-like semantics
Material facts/assertions are append/supersede/correct rather than silently overwritten. Where material, distinguish effective/event time from recorded/knowledge time.

This is a semantic constraint, not a selection of blockchain, event sourcing, temporal database, or append-only storage technology.

## AP-23 — Relationship semantics are graph-compatible
Entity Identity plus typed temporal Lineage must support upstream/downstream traversal, historical subgraphs, incomplete/uncertain paths, and authorization-aware opaque nodes.

This is a semantic constraint, not a selection of graph database, graph query language, or graph-processing framework.

## AP-24 — Inquiry containers do not own truth
Investigation may organize/link evidence, Causal Claims, Impact, and Annotations but future architecture must not make an Investigation record the authoritative copy of those states.

## AP-25 — Causality is explicit and evidence-bearing
Causal propositions remain Causal Claims with epistemic status, support/contradiction, and review provenance. Temporal proximity, graph reachability, Deployment, realized Change, intent consistency, or model ranking cannot bypass claim semantics.

## AP-26 — Impact is multi-layered, not graph reachability
Future architecture must preserve candidate/reachability, actual exposure/consumption, observed downstream effect, and evidenced business consequence separately. Missing evidence cannot become `not affected`.

## AP-27 — Explanation is authorization- and time-aware projection
Explanation derives from authorized concept state, preserves material statement-to-basis traceability and epistemic labels, and supports contemporaneous, retrospective, and comparative knowledge views.

Choice of LLM, rules engine, templates, report generator, or conversational UI remains deferred.

## AP-28 — Passive monitoring is non-blocking and out-of-band by default
Baseline monitoring, evidence collection, Assessment, Investigation, Impact analysis, and Explanation should not become a mandatory runtime dependency for production jobs. A monitoring outage or collection delay must not itself stall production unless an explicitly enabled active-control concept requires that behavior.

Future architecture should prefer asynchronous/platform metadata observation where it can satisfy accepted evidence needs without adding work to the production critical path.

## AP-29 — Baseline onboarding prefers production-repository independence
The monitoring framework should be independently deployable and versioned from production Git repositories/GitHub Actions workflows. Where Databricks/platform/source metadata can supply required evidence, baseline onboarding should not require ETL-code changes, framework libraries, or monitoring workflow steps in every production repository.

This is an architectural objective, not a claim that no specialized future integration will ever require source changes. Exceptions must be explicit, minimal, and justified.

## AP-30 — Active execution control is explicit and separable from observation
Dependency-aware execution gating is an optional control capability, not an automatic consequence of monitoring or Lineage. When an Execution Gate is enabled, intentional waiting can become part of the production path; the gate's availability, decision basis, fallback/timeout behavior, authorization, override, and induced delay must therefore be explicit and observable.

No universal fail-open/fail-closed rule is selected. Execution Gate and Propagation Safeguard remain separate protective boundaries: one controls downstream start admission, the other controls output/consumption propagation.

## AP-31 — Historical replay is bitemporal and non-mutating
Future architecture must support historical questions over both **event/effective time** and **recorded/knowledge cutoff**. Evidence that became known later cannot appear in a contemporaneous cut merely because its effective time was earlier.

Late/corrected evidence may create a new retrospective conclusion, but prior knowledge, Assessment, causal/Impact state, authorization/control state, and retained Explanation remain historically reconstructable.

This principle does not select a temporal database, event store, snapshot strategy, or query engine.

## AP-32 — Actual history and replay-derived reconstruction remain distinguishable
A current computation over historical inputs is not proof that the result was actually assessed, believed, decided, controlled, or communicated at the time. Actual gate/safeguard actions are not counterfactually rewritten from later evidence, and a reconstructed `as-known-then` Explanation is distinguishable from an actual retained historical Explanation.

Future architecture must preserve this distinction even if both views are rendered through the same user experience.
