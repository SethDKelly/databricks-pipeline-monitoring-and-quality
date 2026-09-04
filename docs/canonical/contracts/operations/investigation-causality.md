# Investigation Lifecycle, Localization & Causal Handoff

**Canonical key:** `operations.investigation-causality`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.OPS`

**Owns current question:** How does Investigation organize bounded inquiry and localization, preserve competing leads, and hand causal propositions to Causal Claim without making localization, closure, analyst/model confidence or remediation causal truth?

**Stable IDs:** OPS-050–OPS-066

## Current semantics

Operational reasoning chain: **bounded question/scope/cut → evidence-backed leads → source-owned evidence assembly → scoped localization → evidence-bearing narrowing/exclusion → explicit Causal Claim handoff → independent causal evaluation → closure/reopen history**.

### OPS-050 — Investigation Proposition, Question, Outcome, Scope & Knowledge Cut
Bind Investigation to exact question/outcome, subject/population/use scope, event/effective window, evaluation/knowledge cut, trigger and limitations.

### OPS-051 — Investigation Lifecycle, Scope Revision, Closure & Reopen
Version scope changes and preserve open/active/paused/closed/reopened intervals; lifecycle is independent from causal status.

### OPS-052 — Investigation Candidate / Lead Generation, Basis & Disposition
Generate candidate leads from provenance-bearing evidence and retain basis/disposition without universal hypothesis scoring or causal probability.

### OPS-053 — Investigation Evidence Assembly, Roles, Contradiction & Gap Tracking
Assemble source-owned evidence by role while preserving contradiction, missing evidence and gaps rather than copying facts into Investigation ownership.

### OPS-054 — Localization Vocabulary: First Observed, Earliest Evidenced, Boundary & Consumer Effect
Distinguish first observed deviation, earliest evidenced state change, first localized transformation/reconciliation boundary and first downstream consumer effect.

### OPS-055 — Localization Traversal, Semantic Scope & Topology Limits
Bind localization traversal to semantic scope, topology time/cut, path relevance and coverage; search stopping point is not root cause.

### OPS-056 — Reconciliation, Structural & Health Boundary Localization
Use structural/health/reconciliation evidence to localize a boundary where expected relationships diverge without asserting why.

### OPS-057 — Execution, Version, Change & Temporal Localization
Use execution/version/change timing to localize last unaffected/first affected evidence and contrasts while keeping proximity below causality.

### OPS-058 — Multiple Deviations, Branching & Competing/Compatible Leads
Preserve multiple deviation branches and compatible or competing leads; Investigation need not force one winner.

### OPS-059 — Lead Exclusion, Narrowing & Negative Evidence
Exclude or narrow leads only with sufficient discriminating/negative evidence; lack of support is not rejection.

### OPS-060 — Investigative Lead → Explicit Causal Claim Handoff
When language asserts caused/contributed/enabled/triggered/prevented/materially influenced, create an explicit Causal Claim with cause/effect/role/context/mechanism/evidence binding.

### OPS-061 — Causal Claim Evaluation & Confirmation Independence from Investigation
Evaluate Causal Claim under REF-013–REF-020 independently from Investigation; `confirmed` additionally requires REF-017 plus AUTH-034.

### OPS-062 — Investigation Outcome, Operational Resolution & Causal Independence
Operational resolution, mitigation or closure does not create causal confirmation; causal state can remain unresolved after closure.

### OPS-063 — Historical Investigation Replay, Late Evidence & Reopen
Historical Investigation replay is non-rewriting; late evidence may change localization, leads or justify reopen while preserving prior knowledge/action state.

### OPS-064 — Restricted / Opaque Evidence & Localization
Restricted/opaque evidence can limit localization but does not become absent; current authorized projection cannot strengthen the internal state.

### OPS-065 — Analyst / Automation Research, Provenance & Evidence Parity
Analysts and automation use the same provenance/evidence/authority rules; model output or human title is not fact or confirmation authority.

### OPS-066 — Investigation/Causality Cross-Concept Ownership & Group 06 Handoff
Investigation owns bounded inquiry and Causal Claim owns causal proposition/status; source facts remain with their original concepts.

## Invariants / boundaries

- Investigation ≠ source evidence truth store.
- question/trigger ≠ presumed cause.
- lead ≠ Causal Claim.
- first observed ≠ earliest evidenced ≠ reconciliation boundary ≠ first consumer effect.
- localization ≠ cause.
- lack of evidence ≠ exclusion/rejection.
- multiple deviations ≠ forced single root cause.
- operational resolution ≠ causal confirmation.
- Investigation closure ≠ Causal Claim status transition.
- `confirmed` remains REF-017 + AUTH-034 gated.
- restricted ≠ absent.
- analyst/model result ≠ fact/authority by origin.

## Cross-concept ownership

OPS refinement coordinates accepted concepts; it does not create an `Operations` truth owner. Investigation owns bounded inquiry; Causal Claim owns cause→effect propositions and epistemic status; source facts remain with their original concepts. REF governs causal evidence and AUTH governs confirmation authority.

## Historical / disclosure rule

Event/effective state, framework knowledge cut and current retrospective interpretation remain distinct. Current requester authorization controls present disclosure; restricted or unavailable evidence is not absence and safe projection cannot strengthen the underlying result.

## Architecture boundary

This contract does not select RCA algorithms, graph-search heuristics, hypothesis scoring, LLM/agent workflows, case-management systems, event stores, source integrations or technical architecture.

## Provenance

- `docs/concepts/phase_007/05_investigation_localization_causal_handoff/README.md`
- Phase 007 Group 05 accepted OPS-050–OPS-066.
