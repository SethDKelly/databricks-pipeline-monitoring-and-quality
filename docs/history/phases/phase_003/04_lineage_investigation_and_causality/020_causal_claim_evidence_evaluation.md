# SYN-020 — Causal Claim + Evidence → Support / Contradiction Evaluation

**Status:** Accepted — Phase 003 Group 04

## Outcome

Evaluate a Causal Claim against evidence dimensions that can strengthen, weaken, exclude, or leave the proposition unresolved without confusing plausibility with proof.

## Participating concepts and actions

- **Causal Claim** — `support`, `contradict`, `reviseStatus`, and later `confirm`/`reject` only under accepted standards.
- **Investigation** — links evaluated claim/evidence.
- **Lineage**, **Execution History**, **Observation**, **Assessment**, **Change**, **Deployment**, **Change Intent**, **Baseline**, **Expectation**, **Propagation Safeguard**, and **Annotation** — evidence/context.

## Trigger / initiating condition

A proposed or previously evaluated claim has material new/current evidence available.

## Coordination semantics

Evaluate evidence across relevant dimensions rather than using one generic score:

1. **Temporal ordering:** did the proposed cause precede the effect under the relevant event semantics? Reliable evidence that the effect predates the cause materially contradicts the claim.
2. **Relationship applicability:** did the required Lineage/dependency relationship exist at the relevant time?
3. **Encounter/consumption context:** where causal transmission requires a particular upstream version/state, is there evidence the downstream subject actually encountered it?
4. **State/change evidence:** did the proposed cause condition actually occur, rather than merely being planned/deployed/reachable?
5. **Semantic/mechanism compatibility:** is the observed direction/property capable of explaining the defined outcome? Compatibility supports plausibility but is not proof.
6. **Contrast/intervention evidence:** retries, rollback, unaffected peers/cohorts, restored inputs, or other controlled contrasts may strengthen or weaken a claim when comparability is sufficient.
7. **Alternative explanations:** evidence supporting competitors remains visible and may reduce certainty without automatically falsifying the claim.
8. **Coverage:** absence/unchanged evidence can contradict only when measurement/topology coverage is sufficient for the relevant condition.

Record support and contradiction separately; a claim may have both.

## State and evidence effects

Causal Claim stores evidence links/rationales/status history. Evidence concepts remain unchanged.

## Ambiguity / failure propagation

Uncertain clocks, incomplete Lineage, unknown consumed version, restricted upstream evidence, non-comparable cohorts, or missing telemetry limit the strength of causal conclusions. Lack of contradicting evidence is never proof.

## Temporal semantics

Status revisions preserve when the evidence became known. Late evidence can weaken a previously strong claim without rewriting earlier knowledge state.

## Provenance / traceability

Every support/contradiction rationale points to exact source evidence and the reasoning dimension it affects.

## Security / authorization

A user may see claim status/limitations without seeing restricted evidence details when policy allows.

## Invariants

- correlation ≠ causation;
- active Lineage ≠ causal proof;
- Deployment activation ≠ intended-effect realization;
- intent consistency ≠ cause;
- absence of contradiction ≠ confirmation;
- reliable temporal impossibility is valid contradicting evidence;
- unchanged/absence evidence requires sufficient coverage;
- multiple contributors may all be supported.

## Scenarios

B drops before C and C consumes the affected B state: support for B-contribution claim. C degradation predates Deployment R2: strong contradiction for R2-cause claim. A appears unchanged but A monitoring was unavailable: do not treat that as evidence excluding A. Safeguard activation directly precedes and blocks a client publication: support for a safeguard-caused delivery-delay claim without implying the quarantined data was defective.

## Non-goals

Formal causal-inference algorithm selection, quantitative causal attribution, or defining the organization-wide confirmation standard.
