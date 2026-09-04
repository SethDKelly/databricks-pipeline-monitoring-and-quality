# Ecosystem Lifecycles

**Canonical key:** `foundation.ecosystem_lifecycles`

**Kind:** REFERENCE

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `foundation.ecosystem_lifecycles`

**Owns current question:** Which product-state lifecycles must DMTZ preserve independently of storage/workflow implementation?

**Stable IDs:** N/A

## Current semantics

DMTZ lifecycle semantics are **history-preserving and provenance-bearing**. Lifecycle transitions do not erase prior accepted-at-the-time state needed to explain what happened, what was known, what was believed/decided, or what changed later.

A correction or supersession can change current truth without rewriting prior knowledge history.

## 1. Planned change and realization lifecycle

Change Intent → anticipated effects/monitoring implications → explicit prospective Expectation/comparability decisions where authorized → source/configuration implementation → Deployment attempt → activation state → executions under active state → Observations → realized Change → Assessment → optional Investigation/Impact/causal reasoning.

Intent, activation, execution, realized Change, Assessment, and cause remain distinct. A plan can fail to activate; activated behavior can differ from intent; intended Change can coexist with unintended degradation.

## 2. Source-to-deployment lifecycle

Repository revision/configuration → Deployment attempt → runtime activation evidence → active/superseded/rollback history.

Workflow/attempt success is not activation, and activation is not proof of data effect or health.

## 3. Pipeline execution lifecycle

Execution instance begins/progresses/terminates, with implementation/input/output/run context associated where evidence supports it. Expected-but-never-started work is evaluated from applicable expectations/opportunities plus sufficient absence evidence; DMTZ does not fabricate missing Run records.

## 4. Data availability and consumption lifecycle

Produced/published state becomes observable → freshness/quality/availability evidence is collected → Assessments evaluate applicable criteria → downstream encounter/consumption evidence may establish exposure/effect/consequence. Reachability alone does not prove consumption.

## 5. Expectation lifecycle

Expectation is established/revised/excepted/retired with authority, provenance, effective time, and history. Change Intent may trigger review, but plan detail does not become normative automatically.

## 6. Baseline lifecycle

Comparable Observations derive a versioned Baseline → a prospective comparability break may be registered → realized Change may render an older Baseline non-comparable for later Assessment → sufficient post-change comparable evidence may derive a new Baseline. Prior Assessments retain their historical basis.

## 7. Observation and Assessment lifecycle

Observation/evidence is recorded with applicable event/source/availability/collection/knowledge provenance → applicable Expectation/Baseline/reference context resolves → Assessment is produced with explicit basis and epistemic/coverage limits → later evidence may produce reassessment without deleting the prior conclusion.

## 8. Lineage lifecycle

Relationship is asserted/observed/inferred with type, direction, identity, provenance, confidence/epistemic state where applicable, effective interval, and correction/supersession history. Planned topology remains intent until realization evidence establishes active Lineage.

## 9. Investigation lifecycle

Question/symptom/uncertainty opens an Investigation → scope/time/question are established → evidence/claims/Impact/Annotations are linked without copying their truth ownership → scope evolves with history → gaps/conflicts/restrictions remain explicit → Investigation may close resolved/unresolved/multi-causal/otherwise complete → material later evidence may reopen without erasing prior closure.

## 10. Causal Claim lifecycle

Causal proposition is proposed → applicable supporting/contradicting evidence and alternatives are evaluated → epistemic status may become supported/weakened/unresolved/rejected → confirmation is available only when the applicable evidence profile and independently resolved confirmation authority are satisfied → later evidence may challenge/supersede current status while preserving historical confirmation/review provenance.

## 11. Impact lifecycle

Historical Lineage identifies downstream candidates → encounter/exposure evidence determines affected-state consumption where possible → downstream Observation/Assessment/Change evidence records effect → consequence evidence is associated where available → causal attribution remains a Causal Claim when required → Impact state may change as late consumer/consequence evidence arrives while prior knowledge remains reconstructable.

## 12. Annotation lifecycle

Human context is added with author/time/referent → revisions/disputes/withdrawal remain attributable → if input becomes structured intent, Expectation, responsibility, governance, authorization, causal, Impact, or control truth, the appropriate owning concept records it separately.

## 13. Governance and authority lifecycle

Semantic Definition, Responsibility Assignment, Classification, Policy Context, Assertion Authority, and Capability Authorization assertions/decisions retain source, scope, effective/knowledge time, conflict, correction, and supersession rather than last-write-wins mutation.

Historical authorization/authority is evidence about the historical state; it does not grant current disclosure.

## 14. Explanation lifecycle

Question/reporting event → current requester/temporal perspective are established → Authorized Analytical Projection is assembled → material statements are composed with basis/epistemic/control/Impact labels → redaction/opacity is applied without converting hidden state into absence → contemporaneous/retrospective/reconstructed distinctions are preserved → materially changed evidence creates a refreshed Explanation rather than silently rewriting retained historical communication.

## Ledger / bitemporal lifecycle principle

No lifecycle may erase states needed to explain prior behavior or prior knowledge. Where material:

- effective/event time remains distinct from source availability, framework knowledge, and derived evaluation time;
- corrections/supersessions are non-rewriting;
- actual historical state remains distinct from replay-derived reconstruction;
- current disclosure permission is evaluated independently from historical authorization state.

This is a semantic contract, not a mandate for a particular event store, temporal database, blockchain, or Delta implementation technique.

## Invariants / boundaries

- Change Intent ≠ Deployment ≠ Execution ≠ realized Change ≠ Assessment;
- planned topology ≠ active Lineage;
- expected-but-missing work ≠ fictional Run;
- Observation ≠ Assessment;
- late evidence ≠ evidence known then;
- historical correction ≠ historical rewrite;
- Investigation container ≠ evidence/claim/Impact owner;
- reachability ≠ exposure ≠ effect ≠ consequence ≠ cause;
- current computation ≠ actual historical decision/communication.

## Synchronizations / related canonical resources

- [Foundational terminology](terminology.md)
- [Architectural principles](../invariants/architectural-principles.md)
- [Security and governance](../policies/security-governance.md)
- [Shared glossary](glossary.md)

Detailed lifecycle action/state contracts remain with their inventory-selected concept/stable-ID owners until CKR-C–I.

## Provenance

- Original owner: [`../../foundation/007_ecosystem_lifecycles.md`](../../foundation/007_ecosystem_lifecycles.md)
- Evidence/time/replay refinement: [`../../concepts/phase_004/README.md`](../../concepts/phase_004/README.md)
- Governance/authority refinement: [`../../concepts/phase_005/README.md`](../../concepts/phase_005/README.md)
- Operational/control/Impact lifecycle refinement: [`../../concepts/phase_007/README.md`](../../concepts/phase_007/README.md)
- Explanation lifecycle refinement: [`../../concepts/phase_008/README.md`](../../concepts/phase_008/README.md)
