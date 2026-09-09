# Group 05 — Investigation, Impact & Explanation

**Status:** Review complete — concepts accepted

## Goal

Define how the product organizes inquiry, represents causal propositions and uncertainty, evaluates downstream exposure/consequence, preserves human context, and communicates authorized evidence-grounded answers without collapsing evidence, interpretation, causality, or presentation.

## Accepted concepts

- [Investigation](investigation.md)
- [Causal Claim](causal_claim.md)
- [Impact](impact.md)
- [Annotation](annotation.md)
- [Explanation](explanation.md)

## Boundary decisions

### 1. Investigation organizes inquiry; it is not incident truth

Investigation is a bounded question/evidence container. It links source evidence, Causal Claims, Impact analysis, and Annotations but does not own their truth or status. It can begin from an Assessment, user question, planned-change realization mismatch, Impact concern, or other uncertainty. It can close unresolved or multi-causal.

### 2. Causal Claim is the explicit home for causality

A causal statement is represented as a provenance-bearing proposition with supporting and contradicting evidence plus explicit epistemic status. Temporal proximity, Lineage, Deployment activation, realized Change, or consistency with Change Intent may support inquiry but cannot silently become confirmed causation.

Multiple contributing causes are allowed. A qualitative role such as primary/contributing/enabling can remain within Causal Claim; Phase 002 does not require a separate Attribution concept or quantitative percentage allocation.

`confirmed` remains available only under an explicit evidence/authority standard. Phase 002 deliberately does not invent that standard.

### 3. Impact separates reachability, exposure, effect, and business consequence

A downstream Lineage path creates a candidate, not an affected consumer. Impact preserves distinct evidence for:

1. candidate/reachability;
2. actual exposure/consumption of the affected state;
3. observed downstream condition/effect;
4. evidenced technical/analytical/business consequence.

These dimensions do not have to advance together. If the product asserts that the originating issue caused a downstream effect, that proposition belongs in Causal Claim.

### 4. Annotation is human context, not a catch-all truth mechanism

Annotation adds attributed human context without rewriting source evidence. Structured planned modifications belong in Change Intent; normative criteria belong in Expectation; responsibility belongs in Responsibility Assignment; causal confirmation belongs on Causal Claim under the applicable standard.

Human title or authorship does not automatically make Annotation content authoritative for every concept.

### 5. Explanation is an authorized projection, not a truth store

Explanation composes audience-appropriate statements from authorized concept state while preserving source epistemic distinctions and internal traceability. Business and engineering presentations may differ in detail but cannot intentionally contradict the same authorized evidence.

Explanation explicitly supports the temporal distinction between:

- **what was known then** — an historical recorded/knowledge-time cut; and
- **what we know now** — a retrospective view that may include later evidence.

### 6. Ledger semantics extend through reasoning and communication

Investigation scope/history, Causal Claim status, Impact evaluation, Annotation revision, and retained Explanation snapshots follow append/supersede/correction semantics where material. Later evidence can revise current conclusions without erasing the earlier knowledge state.

### 7. Graph reachability never silently becomes causal or impact truth

Graph-compatible Lineage is valuable for discovering upstream evidence and downstream candidates. Traversal results remain typed relationship evidence. They do not create Causal Claims or confirmed Impact automatically.

## Scenario review

### S-01 — Join-volume degradation

Pass. C's Assessment opens an Investigation. Change Intent, Deployment, A/B/C Observations, Lineage, and realized Changes support multiple Causal Claims. Impact distinguishes downstream reachability from exposure/effect. Explanation communicates the leading evidence and uncertainty without forcing one cause.

### S-02 — Stale upstream with successful downstream execution

Pass. Investigation can link successful execution and stale upstream Assessment. A Causal Claim may propose stale input as a contributor. Impact can identify downstream exposed consumers. Execution success is never rewritten as healthy data.

### S-03 — Deployment-correlated shift

Pass. A Deployment-correlated claim can remain proposed/supported/weakened according to evidence. If upstream degradation predates activation, contradiction is explicit. Temporal proximity alone cannot confirm cause.

### S-04 — Cross-repository dependency

Pass. Investigation and Impact traverse typed Lineage across repository boundaries while Entity Identity and provenance preserve source context.

### S-05 — Conflicting governance metadata

Pass. Explanation can communicate that semantics/responsibility/classification/policy context conflict without resolving authority implicitly. Investigation does not flatten governance disagreement.

### S-06 — Policy-sensitive explanation

Pass. Restricted evidence, claims, downstream consumers, and Annotations can be abstracted/redacted while the authorized Explanation remains useful. Hidden evidence is not retrieved merely to leak it through prose.

### S-07 — Historical replay

Pass. Investigation/claim/impact/annotation history plus effective/event time and recorded/knowledge time allow reconstruction of what was believed then versus what later evidence supports now.

### S-08 — Planned structural change

Pass. An intended filter can explain expected volume context without suppressing an unrelated completeness failure. Intent consistency is not causal proof. Impact and Explanation can distinguish valid expected change from unintended downstream consequences.

## Additional adversarial scenarios

### Multiple contributing causes
B volume falls and join-key quality worsens. Two causal claims remain supported as contributors; the system does not force one root cause.

### Reachable but unexposed downstream report
A report appears in downstream Lineage but has not refreshed since before the incident. It remains a candidate rather than being labeled affected.

### Exposed but resilient consumer
A downstream Metric View consumes affected data, but its monitored result still satisfies its Expectation. Exposure is recorded without inventing downstream degradation.

### Human note contradicted by evidence
An Annotation says a source outage caused the issue; timing evidence contradicts it. The note remains attributed while the related Causal Claim is weakened/rejected independently.

### Later evidence changes the conclusion
An Investigation originally closes with a supported deployment claim. Later evidence shows the issue began earlier. Claim/Explanation history preserves both the original knowledge state and the corrected retrospective conclusion.

## Deferred questions

- operational evidence/authority standard for confirmed cause;
- first-MVP Causal Claim status vocabulary;
- quantitative attribution requirements, if any;
- first-MVP Impact layer vocabulary and exposure evidence by consumer type;
- Investigation lifecycle/relationship semantics;
- visible citation requirements by Explanation audience;
- retained Explanation snapshot policy;
- deterministic versus generative explanation behavior for high-consequence conclusions.

## Group exit gate

**Satisfied.** The canonical RCA and planned-change scenarios can be expressed with explicit evidence, competing/multiple causes, downstream reachability/exposure/consequence, attributed human context, authorization-aware explanation, historical knowledge state, and unresolved outcomes without hidden functionality or causal overclaim.

## Phase 002 implication

Group 05 completes the final concept-review group. Subject to the repository-wide consolidation checks recorded in the Phase 002 index, Phase 002 is ready to exit into **Phase 003 — Concept Synchronizations and Ecosystem Scenarios**.
