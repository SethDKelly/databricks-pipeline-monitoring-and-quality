# Group 06 — Historical Replay & Phase 003 Consolidation

**Status:** Review complete — synchronizations accepted; Phase 003 exit gate satisfied

## Goal

Compose Groups 01–05 plus the Execution Gate extension across complete ecosystem scenarios; formalize bitemporal historical replay, late-evidence re-evaluation, and authorization-safe historical Explanation; verify all accepted truth/control boundaries; and perform the Phase 003 exit review.

## Accepted synchronizations

- [`SYN-033 — Event-Time + Knowledge Cut → Historical State Reconstruction`](033_event_time_knowledge_cut_reconstruction.md)
- [`SYN-034 — Late/Corrected Evidence → Retrospective Re-evaluation`](034_late_corrected_evidence_retrospective_re_evaluation.md)
- [`SYN-035 — Historical State + Current Authorization → Safe Replay Explanation`](035_current_authorization_historical_projection_explanation.md)

## Consolidation artifacts

- [`Scenario Replay Matrix`](scenario_replay_matrix.md) — E-01–E-22 end-to-end composition review.
- [`Phase 003 Exit Review`](phase_003_exit_review.md) — concept/synchronization/architecture boundary audit and Phase 004 handoff.

## Boundary decisions

### 1. Historical replay is bitemporal
A historical question resolves both **event/effective time** and **recorded/knowledge cutoff**. Same event time can have different valid `as-known` results as knowledge evolves.

### 2. Historical state is not current state projected backward
Identity, scope, governance, Expectations/Baselines, Deployments, Execution History, Lineage, authorization, gate/safeguard state, claims, Impact, Annotation, and Explanation resolve from their applicable historical versions/evidence.

### 3. Actual historical state and replay-derived state are distinct
A current system may compute an interpretation over a historical evidence cut. That does not prove an Assessment, claim, Impact conclusion, decision, or Explanation actually existed then. Replay-derived outputs are labeled as reconstruction.

### 4. Late/corrected evidence changes retrospective understanding, not historical knowledge
New evidence may produce new Assessment/Change/Causal Claim/Impact/Explanation versions with a later knowledge time. Earlier conclusions remain reconstructable.

### 5. Historical control actions are not counterfactually rewritten
Later readiness evidence may show a gate would be evaluated differently now, but the actual historical hold/admit/override remains the action that occurred. The same applies to safeguard proposal/activation/release.

### 6. Prospective knowledge stays prospective
Later realized Lineage, Impact, or causality cannot be backfilled into an earlier Prospective Impact Profile as though known before deployment.

### 7. Historical authorization is evidence, not current access
The product can reconstruct what a historical actor was permitted to know/do, but current requester Capability Authorization still governs present disclosure.

### 8. Historical Explanation snapshot and reconstructed Explanation differ
If an actual Explanation was retained, it can be identified as historical communication. Otherwise an `as-known-then` Explanation is a reconstruction and cannot be presented as something responders actually saw.

### 9. Redaction/opacity persists through replay
Restricted evidence can remain useful through authorized abstraction without being retrieved or paraphrased beyond current disclosure permission. Hidden evidence is not represented as absent.

### 10. Passive-monitoring non-interference survives consolidation
Monitoring outages do not become production outages for ungated jobs. Explicitly gated jobs use their configured unavailable-state behavior; Group 06 does not invent a global fallback.

### 11. Execution Gate and Propagation Safeguard remain independent through history
Gate state owns start admission; safeguard state owns output/consumption protection. Their actual actions and any induced delays are replayed independently.

### 12. Phase 003 requires no additional concept
The full scenario replay exposes no new truth-owning functionality. Remaining gaps are evidence, authority, policy, statistical, integration, retention, and implementation refinements.

## Seven historical questions

Group 06 makes these separately answerable when evidence permits:

1. **What happened?**
2. **What was known then?**
3. **What was believed/interpreted then?**
4. **What was authorized then?**
5. **What control state/action applied then?**
6. **What was actually explained then?**
7. **What do we know now?**

A replay may answer only some of these. Partial truth is preferable to inferred completion.

## Scenario review

All **E-01–E-22 pass**. See [`scenario_replay_matrix.md`](scenario_replay_matrix.md) for the end-to-end composition record.

Especially important stress cases pass:

- late Deployment/Lineage/consumption evidence changes retrospective interpretation while preserving incident-time uncertainty;
- a restricted-data analyst can compare contemporaneous and retrospective conclusions without receiving historical privileged evidence;
- a gate hold remains the actual historical control action even if later evidence shows the upstream was already ready;
- an actual retained incident Explanation is distinguishable from a newly generated historical reconstruction;
- passive monitoring degradation leaves ungated production independent;
- explicitly gated control degradation follows the gate's historical configured fallback rather than a framework-wide default;
- safeguard prevention and safeguard-induced lateness remain simultaneously true where supported.

## Deferred questions handed to Phase 004+

- exact evidence sufficiency/completeness standards;
- precise event-time/knowledge-cut query semantics and `not known by cutoff` proof;
- correction/reassessment/reopen materiality;
- Causal Claim confirmation standards and confidence/attribution semantics;
- exposure/non-exposure evidence classes;
- Execution Gate readiness/enforcement evidence sufficiency;
- retention versus reconstruction requirements for historical Assessment/Investigation/Impact/Explanation;
- later authority, statistical, integration, control-policy, and technical realization choices.

## Group exit gate

**Satisfied.** The 23 accepted concepts and SYN-001–SYN-035 compose into historically reproducible, authorization-safe, control-aware ecosystem behavior across E-01–E-22 without hidden architecture, forced causality, downstream-impact overstatement, historical rewriting, or accidental conversion of passive monitoring into a universal production dependency.

**Phase 003 is complete. Phase 004 — Evidence, Time, and Causality Refinement is next and has not started.**
