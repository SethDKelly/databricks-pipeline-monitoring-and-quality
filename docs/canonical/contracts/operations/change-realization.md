# Change Intent, Deployment Realization & Realized Change

**Canonical key:** `operations.change-realization`

**Kind:** CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.OPS`

**Owns current question:** How do registered Change Intent, deployment attempts/activation, realized Change and intent-to-realization comparison coordinate without collapsing plan, attempt, active state, effect or conformance?

**Stable IDs:** OPS-010–OPS-020

## Current semantics

Operational reasoning chain: **registered intent → deployment association → attempt/outcome → target/facet activation → evidence-established realized Change → derived intent-to-realization comparison**.

### OPS-010 — Change Intent Proposition Identity, Version & Target Scope
Bind Change Intent to exact revision/component, target/facet/slice and intended activation/effect context so comparisons do not float across revisions.

### OPS-011 — Implementation-State Reference, Version & Deployment Payload Binding
Represent active implementation state as provenance-bearing composite references across code/build, transformation/job definition, configuration, schema/interface and target context; no universal deployment version exists.

### OPS-012 — Deployment Attempt, Activation & Active-State Resolution
Separate deployment attempt, attempt outcome, target/facet activation, active-state interval and supersession/deactivation; successful delivery tooling is not activation proof by itself.

### OPS-013 — Change Intent ↔ Deployment Association, Evidence & Cardinality
Associate intents and Deployments with evidence and many-to-many cardinality; temporal/name/repository proximity is insufficient.

### OPS-014 — Realized Change Proposition, Before/After State & Transition Binding
Bind realized Change to exact before/after state, affected subject/facet, transition interval and evidence; Change does not own intent or conformance.

### OPS-015 — Intent-to-Realization Comparison Layers & Vocabulary
Compare intent and realization through separate association, activation, realized-state and conformance layers using matched/partially matched/diverged/not realized/not evidenced/indeterminate/conflicting/unavailable.

### OPS-016 — Partial, Phased, Multi-Target & Overlapping Realization
Represent partial, phased, regional/cohort, multi-target and overlapping realization slice by slice; target counts do not create a global completion percentage.

### OPS-017 — Unregistered, Outside-Declared-Scope & Unplanned Change Semantics
Distinguish no known matching intent, unregistered activity, outside-declared-scope activity and proven unplanned change; `unplanned` requires an applicable rule plus evidence.

### OPS-018 — Rollback, Reversion, Supersession & Restoration Semantics
Preserve rollback/reversion, supersession/deactivation, realized reversion and bounded restoration separately; reactivation creates new history and does not universally restore downstream state.

### OPS-019 — Historical Realization Replay, Correction & Negative Claims
Historical realization replay is bitemporal and non-rewriting; strong negatives such as no activation or not realized retain conclusion-specific coverage burdens.

### OPS-020 — Change/Deployment Cross-Concept Ownership & Group 03 Handoff
Keep Change Intent, Deployment and Change independent truth owners; derived realization comparison owns no new underlying facts.

## Invariants / boundaries

- Change Intent ≠ Deployment ≠ Change.
- repository revision ≠ deployed runtime identity absent evidence.
- attempt ≠ success ≠ activation ≠ effect.
- association ≠ activation ≠ conformance.
- activation ≠ specific execution version use.
- `not evidenced` ≠ `not realized`.
- matched intent ≠ healthy/acceptable/authorized/cause.
- partial rollout ≠ global activation.
- no matching intent known ≠ proven unplanned.
- rollback ≠ historical erasure ≠ universal downstream restoration.

## Cross-concept ownership

OPS refinement coordinates accepted concepts; it does not create an `Operations` truth owner. Lineage, Change Intent, Deployment, Change, Execution History, Investigation, Causal Claim, Impact, Propagation Safeguard and Execution Gate retain their accepted concept ownership. REF governs evidence/negative/causal proof; AUTH governs assertion/capability/high-consequence authority; HLTH governs health, evidence suitability and readiness inputs.

## Historical / disclosure rule

Event/effective state, framework knowledge cut and current retrospective interpretation remain distinct. Current requester authorization controls present disclosure; restricted or unavailable evidence is not absence and a safe projection cannot strengthen underlying truth.

## Architecture boundary

This contract is implementation-neutral. It does not select graph/event storage, source integrations, orchestration/control mechanisms, scoring algorithms, persistence schema, polling/streaming behavior or concrete operational SLAs.

## Provenance

- `docs/concepts/phase_007/02_change_intent_deployment_realized_change/README.md`
- Phase 007 Group 02 accepted OPS-010–OPS-020.
