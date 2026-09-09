# SYN-031 — Authorized Analytical Projection → Evidence-Grounded Explanation

**Status:** Accepted — Phase 003 Group 05

## Outcome

Compose an audience-appropriate Explanation that combines permitted health, execution, governance, responsibility, Lineage, investigation, causality, Impact, safeguard, Annotation, and capability context while preserving epistemic status, statement-to-basis traceability, redaction limits, and temporal perspective.

## Participating concepts and actions

- **Explanation** — `compose`, `composeAt`, `inspectBasis`, `refresh`.
- **Capability Authorization** — authorization decisions supporting the analytical projection and basis inspection.
- The authorized projections of **Semantic Definition**, **Responsibility Assignment**, **Classification**, **Policy Context**, **Expectation**, **Baseline**, **Observation**, **Assessment**, **Change Intent**, **Deployment**, **Execution History**, **Lineage**, **Change**, **Investigation**, **Causal Claim**, **Impact**, **Propagation Safeguard**, and **Annotation**.

## Trigger / initiating condition

An actor requests an explanation/report/answer about subject health, runtime state, governance/policy context, root cause, downstream Impact, safeguards, or historical state.

## Preconditions

The question/audience/time context is defined and SYN-030 has produced a sufficiently authorized analytical projection or explicit limitations.

## Coordination semantics

1. Compose only from the authorized projection; Explanation does not query hidden raw evidence merely to make the answer more complete.
2. Preserve statement type/epistemic label: observed fact, normative/comparative Assessment, registered intent, realized Change, Causal Claim status, Impact candidate/exposure/effect/consequence, safeguard state, human Annotation, governance/policy context, authorization limitation, unknown/conflict, etc.
3. Present policies/restrictions, responsibility, pipeline/table health, execution timing, Lineage, causal evidence, downstream Impact, and safeguard state side-by-side where useful without converting one category into another.
4. Preserve Impact layering explicitly: reachable candidate, exposed/not-exposed/unknown, observed downstream effect, consequence evidence, and causal attribution remain distinct.
5. Preserve causal status: `supported contributor` remains supported; multiple claims remain multiple; unresolved remains unresolved; no narrative simplification can create `confirmed`.
6. `inspectBasis` returns the authorized basis available to the requester. If a coarse statement is authorized while exact underlying evidence is not, the basis view may expose a provenance/status class and redaction indicator rather than hidden values.
7. If the requester lacks authorization even for the coarse conclusion, Explanation reports an allowed limitation/omission rather than using hidden evidence to state it indirectly.
8. Safe omission cannot be worded as evidence of absence. `Additional restricted downstream context exists` and `downstream consumers not found` are materially different statements.
9. Audience detail may vary, but projections over the same underlying state must not intentionally contradict one another for presentation convenience.
10. Where relevant, Explanation may state available operational capabilities separately, such as `job retry permitted` or `safeguard activation not permitted`; it does not perform the action.
11. `composeAt` preserves the requested evidence/knowledge-time perspective. Historical authorization can be described as evidence where permitted, but the current requester still receives only currently authorized disclosure.
12. `refresh` after new evidence/Impact/claim/authorization state creates an updated view while retained prior explanations remain reconstructable.

## State and evidence effects

Explanation owns only the composed communication/snapshot if retained. It does not create or alter underlying truth, Impact, causal status, authorization, or operational state.

## Ambiguity / failure propagation

Missing, conflicting, restricted, stale, or insufficient evidence remains visible at an appropriate abstraction. A partial authorized view can support a narrower Explanation; it never licenses plausible narrative completion.

## Temporal semantics

Explanation retains generation time, requested event-time perspective, requested knowledge-time cut, and relevant authorization/redaction context. Group 06 will consolidate end-to-end replay semantics.

## Provenance / traceability

Every material statement has an internal statement-to-basis link to the projected source concept state and its epistemic/authorization context. Visible citation UI is deferred, but internal traceability is mandatory.

## Security / authorization

Explanation is a high-risk cross-source inference surface. It must not reveal restricted identities, thresholds, policy text, Annotation content, consumer names, or causal details through summarization, comparison, omission patterns, or generated prose beyond authorized abstraction.

## Invariants

- Explanation ≠ independent truth source;
- authorized projection ≠ unrestricted evidence;
- restricted basis cannot be smuggled through prose;
- reachability ≠ exposure ≠ downstream effect ≠ consequence;
- downstream effect ≠ causal attribution;
- supported ≠ confirmed;
- Annotation remains human context;
- Policy Context ≠ compliance conclusion;
- Responsibility Assignment ≠ authorization;
- action capability display ≠ action execution;
- redacted/omitted ≠ nonexistent;
- historical view ≠ authorization bypass.

## Scenarios

**Business analyst without raw access:** Explanation shows that C completeness failed, execution duration was acceptable, a restricted upstream contributor is supported but unconfirmed, one downstream report was exposed/affected, another was protected by safeguard, relevant handling restrictions apply, and the responsible team is visible—without rows, sensitive thresholds, restricted identities, or policy text.

**Engineering detail:** an engineer with broader capability inspects the same underlying conclusions with version/execution evidence and detailed Lineage while causal status remains identical.

**Reachable but not exposed:** Explanation says a critical report is downstream but reliable evidence shows it did not consume the affected version; it does not call the report affected.

**Multiple causes:** two supported contributors remain visible rather than being collapsed to a single root cause.

**Historical correction:** retained incident-time Explanation remains reconstructable; refreshed retrospective Explanation includes later evidence and states the changed knowledge context.

## Non-goals

UI/chat/dashboard implementation, LLM/template selection, granting authorization, generating new evidence, changing Impact/Causal Claim state, or executing operational actions.

## Deferred questions

Audience-specific minimum explanation schemas, visible evidence citation requirements, deterministic versus generative rules for high-consequence statements, retained snapshot policy, and safe-answer behavior for deeply mixed authorization paths.

## Later refinement — Phase 008 Group 01

Phase 008 Group 01 makes the SYN-031 precondition `question/audience/time context is defined` operationally precise. See [`../../phase_008/01_question_proposition_intent_scope_temporal_perspective/README.md`](../../phase_008/01_question_proposition_intent_scope_temporal_perspective/README.md).

Before composition, a material question now binds the requested conclusion, Entity Identity-resolved subject, proposition-specific scope, event/effective-time perspective and knowledge cut where applicable. Compound requests can decompose into independent subquestions when truth owners or evidence burdens differ.

Question-family labels are descriptive routing metadata only. Explanation routes each requested conclusion to the accepted truth owner and must preserve cross-concept join boundaries. In particular, causal `why` wording cannot promote Lineage/timing/Deployment/intent evidence into a Causal Claim, and broad Impact/control negatives retain their REF/OPS coverage burdens.

Answerability is also separated from semantic applicability, evidence availability/sufficiency, integration support and current disclosure authorization. A partial question can therefore produce supported subanswers while other subquestions remain ambiguous, unresolved, unavailable or restricted without being flattened into one confidence score.

These refinements do not change SYN-031's rule that composition occurs only from an authorized analytical projection and does not make the question itself a truth or authorization source.

## Later refinement — Phase 008 Group 02

Phase 008 Group 02 makes `material statement`, `statement-to-basis`, and summary/detail composition explicit. See [`../../phase_008/02_answer_structure_statement_selection_basis_traceability/README.md`](../../phase_008/02_answer_structure_statement_selection_basis_traceability/README.md).

Each material statement has proposition identity independent of wording and retains its source truth owner/epistemic type. Direct projections remain distinct from derived cross-concept statements; derived statements require an accepted join rule rather than narrative adjacency.

Supporting, contradicting and limiting basis are statement-relative roles and preserve common-derivation/independence semantics. Basis count never becomes confidence. Headline/summary/detail views may differ in verbosity but cannot strengthen scope, polarity or epistemic status, and material limitations cannot be compressed away.

Multiple statements remain independent rather than forming one synthetic global answer truth. Internal basis traceability is required for every material statement, while authorized visible basis inspection remains governed later by Phase 008 Group 06.

## Later refinement — Phase 008 Group 03

Phase 008 Group 03 applies SYN-031 to direct health/change/execution questions without adding a new source-truth layer. See [`../../phase_008/03_health_change_execution_question_semantics/README.md`](../../phase_008/03_health_change_execution_question_semantics/README.md).

Composition preserves execution occurrence versus lifecycle outcome versus output existence/qualification versus freshness/currentness versus health; profile-bound health versus structure/comparability/quality; Baseline versus Expectation; warning/waiver/severity; realized Change versus Change Intent/Deployment/activation; intent-realization comparison; and run-specific version use versus active Deployment/latest output.

Repeated execution, dependency/precedence/waiting/consumption, missing-work negatives and timing/lateness remain separately answerable. Historical domain answers retain event/effective time and knowledge cut. Causal `why` wording may consume these statements as basis but cannot strengthen them into Causal Claim truth through composition.

## Later refinement — Phase 008 Group 04

Phase 008 Group 04 applies SYN-031 to Investigation, causality, Impact, control and governance questions. See [`../../phase_008/04_investigation_causality_impact_control_governance_question_semantics/README.md`](../../phase_008/04_investigation_causality_impact_control_governance_question_semantics/README.md).

Composition preserves Investigation lifecycle/lead/localization versus Causal Claim and retains exact causal role/status. Singular `root cause` wording cannot collapse multiple/competing claims or create confirmation. Impact layering remains candidate/reachability → opportunity → exposure → effect → consequence → optional causal attribution, and broad `affected`/`nobody affected` language retains the exact layer/population/coverage burden.

Safeguard and Gate statements preserve proposal/authorization/request/decision/enforcement/outcome boundaries, REF-028 prevented-exposure requirements, release-versus-recovery, readiness-versus-Gate-decision/enforcement/execution, HOLD-versus-failure, ADMIT-versus-run, and Gate/Safeguard independence. Broader control-effect attribution is Causal Claim work except the accepted narrow prevention determination.

Governance projection preserves responsibility versus blame/cause/authority/permission; semantic meaning versus realized state; Classification versus Policy Context/authorization/Impact/compliance; Policy Context versus enforcement/legal interpretation/compliance; capability permission versus action success; and assertion standing versus truth/evidence sufficiency/permission.

These refinements keep inferential/governance statements independent and traceable rather than manufacturing a universal RCA, Impact, control-effectiveness, blame, compliance or governance-confidence result.

## Later refinement — Phase 008 Group 05

Phase 008 Group 05 makes SYN-031's `missing/conflicting/restricted/stale/insufficient evidence remains visible` rule proposition-specific. See [`../../phase_008/05_uncertainty_conflict_negative_claims_epistemic_language/README.md`](../../phase_008/05_uncertainty_conflict_negative_claims_epistemic_language/README.md).

Composition now distinguishes unknown/unresolved, unavailable, insufficient/indeterminate, conflict, restricted/redacted, stale-for-use, non-comparable, not-applicable, not-evidenced/not-known and evidence-backed negative results. Missing or inaccessible basis does not become an absence claim, and unresolved conflict does not license winner selection.

Strong negatives preserve their conclusion-specific opportunity/coverage/authority burdens. Causal claim statuses, Impact exposure/effect/consequence states, control telemetry limitations, and governance unknown/conflict states retain their accepted vocabulary. Positive statements are not decorated with unsupported probability/confidence language.

Multiple material statements retain independent epistemic states, so one answer can simultaneously contain confirmed, supported, conflicting, unavailable and bounded-negative conclusions without an overall confidence/completeness score. Historical as-known state may differ from current retrospective resolution without rewriting either view.

## Later refinement — Phase 008 Group 06

Phase 008 Group 06 makes the authorized analytical projection operationally precise for Explanation. See [`../../phase_008/06_audience_authorization_safe_abstraction_basis_inspection/README.md`](../../phase_008/06_audience_authorization_safe_abstraction_basis_inspection/README.md).

Current visible projection binds requester, target audience, purpose, subject/context, temporal perspective, delivery and material information/detail class. Result, context, limitation, basis, provenance and exact-detail visibility can differ without changing internal source truth.

Safe abstraction is epistemically monotone and not automatic declassification. Restricted detail may be represented only through an independently authorized exact/coarse/redacted/generalized/opaque/withheld projection. A material hidden limitation constrains or withholds the visible conclusion rather than allowing an unqualified stronger statement.

`inspectBasis` is separately authorized and may return exact evidence, coarse provenance/status, redaction/opaque limitation or safe non-disclosure while internal traceability remains intact. Explanation cannot combine otherwise hidden evidence into a new coarse conclusion merely because its wording appears safe.

Cross-audience views may differ in detail and scope but remain projections over one truth. Mosaic/repeated-query leakage, high-consequence communication release and historical/current authorization separation remain governed by AUTH-044–AUTH-053.

EXPL-101–EXPL-120 and AUD06-01–AUD06-44 are accepted without a new concept.

## Later refinement — Phase 008 Group 07

Phase 008 Group 07 makes refresh evolution and retained communication semantics explicit. See [`../../phase_008/07_progressive_maturity_partial_answers_refresh_retention/README.md`](../../phase_008/07_progressive_maturity_partial_answers_refresh_retention/README.md).

SYN-031 may emit a bounded partial authorized Explanation when supported subquestions are answerable while other siblings remain unresolved. A later composition is materially newer only when source truth/evidence, accepted derivation, authorization, or material question context changes; elapsed time and repeated prose generation are no-op for epistemic maturity.

Material statement identity survives wording/detail changes within the same proposition. Basis enrichment can occur without status change. Conflict, correction, supersession and derived-statement changes are projected only after source-owned re-evaluation. Current statement deltas distinguish presentation, basis, status, scope, materiality and authorization changes rather than flattening all refresh into one maturity state.

When retained, a refreshed Explanation links to its predecessor and may supersede it for present use without overwriting actual prior communication. A retained snapshot is evidence of what was communicated then, while a reconstruction is a present derivation and cannot substitute for missing retained history. Current authorization changes current projection without rewriting earlier communication.

EXPL-121–EXPL-140 and PMR07-01–PMR07-44 are accepted without a new concept.

## Later refinement — Phase 008 Group 08

Phase 008 Group 08 completes historical/comparative composition and Phase 008 exit. See [`../../phase_008/08_historical_comparative_explanation_consolidation_exit/README.md`](../../phase_008/08_historical_comparative_explanation_consolidation_exit/README.md).

SYN-031 now preserves four independently meaningful explanatory views: source-owned historical state, as-known-at-cut Explanation, retained actual prior communication where available, and current retrospective Explanation. Present disclosure applies current requester authorization separately and does not become another truth state.

Historical/comparative statements retain stable proposition identity only when material subject/predicate/scope/event target match. Differences are typed as source/status, evidence/basis/knowledge, derivation, scope/materiality, authorization/detail, presentation, or retained-versus-reconstructed changes. A newly available basis can change what is known without implying the historical source state changed at the same moment.

Corrections/supersessions change current preferred interpretation non-rewritingly. A retained historical message can remain authentic while becoming unsuitable for current use, and missing retained communication cannot be recreated as exact communication by `composeAt`.

Comparative domain statements preserve all accepted health/change/execution, Causal Claim, Impact, Safeguard/Gate and governance boundaries. Explanation-delta reasons do not substitute for domain Causal Claims.

EXPL-141–EXPL-160 and HCX08-01–HCX08-48 are accepted. **EXPL-001–EXPL-160 is final; no EXPL-161 is required; Phase 008 exits complete with no new truth concept.**