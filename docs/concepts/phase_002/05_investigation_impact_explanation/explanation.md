# Concept: Explanation

**Status:** Accepted — Phase 002 Group 05

## Purpose

Let an authorized audience receive an evidence-grounded, time-aware account of what happened, what was intended, what is affected, what is known or uncertain, and where the supporting basis comes from without turning the explanation into an independent truth source.

## Operational principle

A business analyst asks why Table C volume fell. The Explanation states that C fell to 14 million rows; the volume shift is consistent with a registered filter Change Intent and active Deployment; the revised volume Expectation is satisfied; a separate completeness Expectation is violated; B also changed; two Causal Claims remain supported but unconfirmed; one downstream report is exposed and has an observed metric violation while another is only reachable. The analyst receives safe business semantics and responsible team information without restricted raw evidence. An engineer can inspect deeper evidence, but both audiences see epistemically consistent conclusions.

## Actors

- Business Analyst / Data Consumer
- Data Engineer / Pipeline Maintainer
- Data Owner / accountable business party
- Data Steward / Governance Steward
- Incident responder / on-call engineer
- Executive / operational stakeholder
- Monitoring framework

## State

- explanation identity when retained;
- initiating question/request/reporting intent;
- intended audience and authorization context;
- subject(s) and relevant effective/event-time window;
- temporal perspective, including the requested recorded/knowledge-time cut when historical replay matters;
- material statements and their statement type/epistemic label, such as observed fact, normative/comparative Assessment, registered intent, realized Change, supported/rejected/confirmed Causal Claim, reachability/exposure/effect Impact statement, human Annotation, unknown, or conflict;
- references to source concept state/evidence supporting each material statement;
- Semantic Definition, Responsibility Assignment, Classification, and Policy Context used for audience interpretation;
- evidence limitations, omissions, redactions, and safe abstraction indicators;
- generation/composition time;
- retained snapshot/version linkage when explanations are preserved historically.

## Actions

### `compose`
- **Intent:** produce an audience-appropriate explanation from an authorized evidence/context view for a defined question and temporal perspective.
- **Failure / unknown behavior:** insufficient authorized basis produces an explicit limitation rather than invented narrative completion.

### `composeAt`
- **Intent:** compose an explanation for a specified effective/event-time and, when requested, a specified recorded/knowledge-time cut.
- **Use:** distinguishes "what was known then" from a later retrospective explanation using evidence learned afterward.

### `inspectBasis`
- **Intent:** allow an authorized user to trace a material statement to its source concept state, evidence, rationale, and epistemic status.

### `refresh`
- **Intent:** produce an updated explanation after materially changed evidence, Assessment, Causal Claim, Impact, or governance state.
- **State effect:** if prior explanations are retained, the refreshed version links to rather than silently overwrites the earlier snapshot.

## Invariants / behavioral expectations

- Explanation is a projection over authorized concept state; it is not an independent truth source.
- Explanation does not generate new Observations, modify Assessments, confirm Causal Claims, or create Impact evidence merely by stating them.
- Material factual/causal/impact statements are traceable to source concepts.
- Epistemic distinctions survive composition: Observation ≠ Assessment ≠ Change Intent ≠ realized Change ≠ Causal Claim ≠ Annotation.
- `consistent with intent` is not rewritten as `caused by the planned change` unless a Causal Claim supports that statement at the stated epistemic level.
- Lineage reachability is not presented as actual exposure; exposure is not presented as observed downstream consequence; downstream consequence is not automatically presented as business impact.
- Competing Causal Claims are not collapsed into one confident answer merely for readability.
- A current retrospective Explanation may differ from an Explanation of what was known at the incident time; the temporal perspective must be explicit where material.
- Audience-specific detail/redaction may differ, but conclusions derived from the same authorized evidence cannot be intentionally contradicted for presentation convenience.
- Restricted evidence is not retrieved merely so an unauthorized audience can receive a summary of it.
- Safe omission cannot be phrased in a way that falsely implies the omitted entity/evidence does not exist.
- Classification/Policy Context cannot be transformed into compliance certification.
- If retained, Explanation history follows ledger-like append/version semantics rather than invisible overwrite.

## Ambiguity and missing evidence

Missing, conflicting, stale, inaccessible, redacted, non-comparable, or insufficient evidence must remain visible at an appropriate abstraction level. The product may say that the cause remains unresolved, that downstream exposure cannot be determined, or that restricted evidence limits the answer.

An Explanation should prefer a narrower supported statement over a broader plausible-sounding conclusion.

## Synchronizations

Explanation composes authorized projections of:

- **Monitoring Scope** and **Entity Identity** for subject/boundary context;
- **Semantic Definition**, **Responsibility Assignment**, **Classification**, and **Policy Context** for meaning/governance context;
- **Expectation**, **Baseline**, **Observation**, and **Assessment** for health/reference evidence;
- **Change Intent**, **Deployment**, **Execution History**, **Lineage**, and **Change** for planned/active/historical context;
- **Investigation**, **Causal Claim**, **Impact**, and **Annotation** for inquiry, causality, downstream consequence, and human context.

## Security / privacy / governance considerations

Question answering and report composition can create cross-source inference risk. Explanation must operate over an authorized evidence view and must preserve source-system disclosure constraints.

Different audiences may receive different entity names, path detail, threshold values, claim detail, or Annotation content, but the safe projection must remain evidence-consistent and avoid using hidden evidence to smuggle restricted facts into prose.

## Evidence / provenance considerations

Each material statement should retain sufficient internal traceability to the concept state/evidence snapshot used. A retained Explanation should preserve generation time, effective/event-time perspective, recorded/knowledge-time cut when relevant, source references, and redaction context.

Visible citation/UI requirements are presentation decisions for later phases; internal statement-to-basis traceability is a product requirement.

## Representative scenarios

### Business analyst summary
The analyst sees that volume changed as planned, completeness failed unexpectedly, root cause is still supported-not-confirmed, one report is exposed/affected, and the responsible team is identified—without restricted raw data.

### Engineering detail
The engineer inspects the same conclusion with deployment activation, execution sequence, A/B/C Observations, Lineage paths, claim support/contradiction, and Impact evidence.

### Competing causes
Two Causal Claims remain supported. The Explanation presents both and the evidence limitation rather than inventing a winner.

### Historical knowledge view
A user asks what the team knew during the incident. `composeAt` excludes evidence learned later and explains the then-current uncertainty. A separate retrospective explanation can incorporate later evidence.

### Restricted upstream evidence
The Explanation states that restricted upstream evidence materially limits causal confidence without naming the entity or exposing prohibited details.

### Reachable versus exposed impact
A report reachable through Lineage but not refreshed is described as a potential downstream candidate, not as actually affected.

## Non-goals

- UI/chat/report rendering technology;
- generating new evidence;
- changing causal status;
- owning Impact truth;
- replacing governance authorities;
- granting access;
- choosing LLM, template, or rules-based generation architecture;
- requiring every internal evidence reference to be visibly rendered to every audience.

## Deferred questions

- minimum explanation structures for business, engineering, executive, and audit/review audiences;
- which material statements require visible citations/evidence links in each experience;
- retention policy for generated Explanation snapshots versus dynamically composed views;
- safe-answer behavior when authorization differs across portions of a causal path;
- deterministic versus generative composition requirements for high-consequence claims.

## Later refinement — Phase 008 Group 01

Phase 008 Group 01 refines the existing `initiating question/request/reporting intent` state rather than adding a Question concept. See [`../../phase_008/01_question_proposition_intent_scope_temporal_perspective/README.md`](../../phase_008/01_question_proposition_intent_scope_temporal_perspective/README.md).

The initiating request is now treated as a bounded question proposition that preserves:

- requested conclusion type rather than relying on natural-language wording alone;
- Entity Identity-resolved subject plus material scope such as environment/version/run/consumer/profile/path/control instance;
- event/effective-time target and, where applicable, recorded/knowledge cut;
- current-state versus as-known-at-cut versus current-retrospective perspective;
- compound-question subquestions where truth owners/evidence burdens differ;
- truth-owner routing without transferring substantive truth into Explanation;
- material ambiguity/underspecification;
- answerability limitations separated from evidence availability/sufficiency, integration support and authorization;
- source-specific negative-evidence burden even when the user asks a negative-form question.

Question-family labels are routing metadata only. They do not establish evidence sufficiency, authority or truth. Asking `why` does not relax Causal Claim requirements; asking `was nobody affected?` does not relax Impact coverage; asking for restricted information does not grant disclosure.

Group 01 accepts EXPL-001–EXPL-012 and BQ01-01–BQ01-24 without changing the 24-concept catalog.

## Later refinement — Phase 008 Group 02

Phase 008 Group 02 refines the existing `material statements`, `references to source concept state/evidence`, and `inspectBasis` requirements without adding an Answer/Statement truth-owning concept. See [`../../phase_008/02_answer_structure_statement_selection_basis_traceability/README.md`](../../phase_008/02_answer_structure_statement_selection_basis_traceability/README.md).

A material answer statement is now treated as a bounded proposition independent of wording. It preserves source truth owner/epistemic type and is classified as either a direct projection of source-owned truth or an explicit derived cross-concept statement using an accepted semantic join rule.

Statement selection is question-relative. Answer-bearing conclusions, contextual statements and limitations can have different presentation roles while retaining their source proposition types. Supporting, contradicting and limiting basis are statement-relative roles; basis sufficiency remains conclusion-relative, and duplicate/common-derived basis cannot be counted as independent corroboration.

Headline/summary/detail views may compress detail but cannot change scope, polarity or epistemic strength, and cannot omit a qualification when doing so would materially overstate causality, exposure, health, control effectiveness or another conclusion. Multi-statement answers preserve sibling independence rather than creating a synthetic global answer truth.

Every material statement retains internal statement-to-basis identity/provenance even if Group 06 later restricts what basis may be visibly disclosed. Answer coverage is tracked by bounded subquestion/proposition rather than a universal confidence/completeness score.

Group 02 accepts EXPL-013–EXPL-028 and AS02-01–AS02-30 without changing the 24-concept catalog.

## Later refinement — Phase 008 Group 03

Phase 008 Group 03 refines how common health/change/execution wording maps to accepted Phase 006/007 propositions without adding an operational-status concept. See [`../../phase_008/03_health_change_execution_question_semantics/README.md`](../../phase_008/03_health_change_execution_question_semantics/README.md).

It preserves execution occurrence versus lifecycle outcome versus output existence/qualification versus freshness/currentness versus health; health dimension/profile/use binding; realized structure versus compatibility versus comparability versus normative quality; Baseline versus Expectation; warning/waiver/severity separation; and reconciliation versus causal attribution.

Change answers preserve realized Change versus Change Intent versus Deployment attempt/activation and intent-to-realization comparison. Run-specific implementation/input/output versions require Execution History binding rather than active Deployment/latest-output inference. Retry/rerun/backfill, dependency/precedence/waiting/consumption, expected-work negatives and timing/lateness remain independently answerable.

Historical health/change/execution answers retain event/effective time plus knowledge perspective. Direct state evidence can support an inquiry but cannot become Causal Claim truth through wording, sequence or temporal proximity.

Group 03 accepts EXPL-029–EXPL-049 and HCE03-01–HCE03-36 without changing the 24-concept catalog.

## Later refinement — Phase 008 Group 04

Phase 008 Group 04 refines how inferential, Impact, control and governance wording maps to accepted truth without adding an RCA, affected-state, control-effectiveness, blame, compliance or authority-summary concept. See [`../../phase_008/04_investigation_causality_impact_control_governance_question_semantics/README.md`](../../phase_008/04_investigation_causality_impact_control_governance_question_semantics/README.md).

Investigation lifecycle, leads and localization remain distinct from Causal Claim. Causal answers preserve explicit cause→effect identity, causal role and accepted claim status; `root cause` wording does not force a singular winner and `confirmed` remains REF-017 + AUTH-034 governed.

Impact answers preserve candidate/reachability, encounter opportunity, exposure, downstream effect, consequence and causal attribution. `Affected` must resolve to the intended layer and strong `all`/`none` summaries retain population/path coverage burdens.

Safeguard and Gate questions preserve lifecycle/authorization/decision/enforcement/outcome boundaries. Safeguard enforcement does not itself prove REF-028 prevented exposure or recovery; Gate HOLD does not mean failed execution, ADMIT does not mean run, and broader control-effect attribution remains Causal Claim work except the accepted narrow prevented-exposure determination.

Governance answers preserve Responsibility Assignment versus fault/cause/authority/permission; Semantic Definition versus realized state/health; Classification versus Policy Context/authorization/Impact/compliance; Policy Context versus enforcement/legal interpretation/compliance; Capability Authorization versus responsibility/authority/action success; and Assertion Authority versus factual truth/evidence sufficiency/permission/enforcement.

Group 04 accepts EXPL-050–EXPL-080 and ICG04-01–ICG04-48 without changing the 24-concept catalog.

## Later refinement — Phase 008 Group 05

Phase 008 Group 05 refines how Explanation communicates epistemic limitation without adding an uncertainty/confidence concept. See [`../../phase_008/05_uncertainty_conflict_negative_claims_epistemic_language/README.md`](../../phase_008/05_uncertainty_conflict_negative_claims_epistemic_language/README.md).

Material statements now preserve proposition-specific distinctions among unknown/unresolved, unavailable source/evidence, insufficient/indeterminate evidence, unresolved conflict, restricted/redacted context, stale-for-use evidence/result, non-comparable context, not-applicable criteria, not-evidenced/not-recorded/not-known-by-cutoff state, and evidence-backed negative conclusions.

Absence of evidence cannot be rendered as evidence of absence. Strong negatives retain their REF/HLTH/OPS/AUTH opportunity, coverage and authority burdens; negative-form questions do not lower those burdens. Positive conclusions use the owning concept's status rather than invented probability/confidence language.

Causal proposed/supported/weakened/unresolved/rejected/confirmed states, Impact candidate/exposure/effect/consequence states, degraded control evidence, and governance unknown/conflict states retain their exact semantics. Multiple sibling statements keep independent epistemic states rather than producing an overall confidence/completeness score.

Historical Explanation may therefore state `unknown at the incident-time knowledge cut; retrospectively established from later evidence` without rewriting the earlier unknown state. Group 05 accepts EXPL-081–EXPL-100 and UNC05-01–UNC05-40 without changing the 24-concept catalog.

## Later refinement — Phase 008 Group 06

Phase 008 Group 06 refines audience/purpose/delivery-specific projection and `inspectBasis` over the internally valid Explanation without adding a new audience/projection truth concept. See [`../../phase_008/06_audience_authorization_safe_abstraction_basis_inspection/README.md`](../../phase_008/06_audience_authorization_safe_abstraction_basis_inspection/README.md).

The visible projection now separately binds requester, target audience, purpose, delivery and information/detail class. Conclusion visibility remains separate from context, limitation, basis, provenance and exact-detail visibility. Safe abstraction can expose exact, coarse, redacted, generalized, opaque or withheld information only when independently authorized and semantically valid.

Authorized abstraction is epistemically monotone: it may reduce detail or narrow a conclusion but cannot strengthen scope, polarity, causal role, epistemic status, negative coverage or authority standing. Material hidden limitations must constrain the visible answer; if even an abstract limitation cannot be disclosed, the affected conclusion is narrowed or withheld rather than overstated.

`inspectBasis` is itself requester-specific. Exact evidence, provenance class, basis role/status, redacted reference, opaque limitation or safe non-disclosure can each be valid; internal statement-to-basis traceability remains complete regardless. Explanation cannot use otherwise hidden evidence to invent a new coarse conclusion merely because the final wording appears less sensitive.

Cross-audience views remain projections over one truth and need not have identical detail, while mosaic/differencing/repeated-query leakage remains a compositional disclosure concern. Historical actor authorization, retained historical communication and current requester disclosure remain separate.

Group 06 accepts EXPL-101–EXPL-120 and AUD06-01–AUD06-44 without changing the 24-concept catalog.

## Later refinement — Phase 008 Group 07

Phase 008 Group 07 makes `refresh`, partial delivery and retained Explanation history operationally precise without adding a maturity/snapshot truth concept. See [`../../phase_008/07_progressive_maturity_partial_answers_refresh_retention/README.md`](../../phase_008/07_progressive_maturity_partial_answers_refresh_retention/README.md).

A narrow trustworthy authorized answer may be emitted before all sibling subquestions are resolved. Progressive maturity requires material source/evidence/authorization/context change; elapsed time, repeated recomposition and wording changes do not strengthen truth.

Material statement proposition identity persists across refresh while its defining subject/scope/event-time/knowledge perspective remains the same. Basis may enrich without changing status; conflict/correction/supersession and derived statements change only through source-owned proposition re-evaluation. Statement deltas distinguish presentation-only, basis-only, status, scope, materiality and authorization changes, so removal from the current projection does not automatically mean false/retracted/nonexistent.

A retained Explanation snapshot is evidence of actual prior communication for its bound context, not timeless source truth. Refreshed current projections link to predecessors/superseded snapshots rather than overwriting them. Current access changes affect current projection without backfilling or erasing retained communication; missing retained snapshots remain missing and reconstruction cannot be labeled exact prior communication.

Group 07 accepts EXPL-121–EXPL-140 and PMR07-01–PMR07-44 without changing the 24-concept catalog.
