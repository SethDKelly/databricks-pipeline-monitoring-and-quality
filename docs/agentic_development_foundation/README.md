# DMTZ Agentic Development Foundation

**Status:** COMPLETE / EXECUTION EXIT ACCEPTED — CKR EXIT ACCEPTED — DPTN EXIT ACCEPTED

**Current handoff:** Implementation 001-A NEXT / READY / NOT STARTED.

The Agentic Development Foundation is complete. This directory contains durable current human-directed authority, context, workflow, conformance, security, compatibility, stable-reference and lifecycle policy/configuration. Completed ADF phase-design/execution evidence is preserved under [`../history/foundations/adf/`](../history/foundations/adf/) and remains provenance only.

## Final execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.**
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.**
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.**
- **ADF-D — Portable Skills & Human-Directed Workflow Contract: COMPLETE / ACCEPTED.**
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance: COMPLETE / ACCEPTED.**
- **ADF-F — Conformance, Validation, Drift Detection & CI: COMPLETE / ACCEPTED.**
- **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model: COMPLETE / ACCEPTED FOR PROGRESSION — ADF-EX-17 DEFERRED VERIFICATION.**
- **ADF-H — Security, Trust, Lifecycle & Governance: COMPLETE / ACCEPTED.**

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED.**

The formal ADF exit decision is preserved at [`../history/foundations/adf/execution_exit_review.md`](../history/foundations/adf/execution_exit_review.md). ADF-EX-01–16 and 18–20 PASS; ADF-EX-17 remains bounded deferred verification.

## Relationship to completed CKR and DPTN

ADF exit was accepted before CKR and DPTN. Both later programs completed without reopening the historical ADF exit.

- CKR-A–K — COMPLETE / ACCEPTED;
- CKR EXIT — ACCEPTED;
- DPTN-A–G — COMPLETE / ACCEPTED;
- DPTN EXIT — ACCEPTED;
- **Implementation 001-A — NEXT / READY / NOT STARTED.**

[`../index.md`](../index.md) is the single authored repository-native discovery root. Top-level `knowledge/` is deterministic generated OKF v0.2 compatibility. Current workflows, tool adapters, stable-reference guidance, scoped rules and current link/drift validation use the normalized first-class documentation topology.

The completed DPTN program is preserved under [`../history/retrofits/dptn/`](../history/retrofits/dptn/) as provenance only. It is not a live routing layer.

## ADF-EX-17 residual verification

Cursor, Claude Code and Codex remain runtime-`unverified` until `ADF-G-XT01` is actually run and recorded in `runtime_compatibility_evidence.json`. The waiver does not convert missing runtime evidence to PASS or weaken DMTZ authority/security/change control.

## Durable foundation model

A1–A4 remains the action model. Accepted DMTZ semantics outrank agent tooling, generated routing, vendor guidance and memory. Canonical workflows live under `.agents/skills/`. Progressive disclosure, stable references, context budgets, least privilege, prompt/content trust and G1–G5 change governance remain mandatory.

For unknown-location repository-native discovery use `docs/index.md`; generic OKF consumers may use generated `knowledge/index.md`. For a known stable ID use `scripts/agentic/resolve_stable_id.py <ID>` directly; `--history` is explicit provenance only. History and generated routing never compete with the ownership inventory.

Canonical conformance command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

Current conformance validates the final documentation topology. Completed CKR checks alone may use bounded ephemeral accepted-era compatibility projections.

## Explicitly deferred / not authorized

- `ADF-G-XT01` provider-runtime verification;
- autonomous task selection or unattended autonomous implementation;
- multi-agent implementation delegation/orchestration;
- unattended merge/deploy/external writes;
- autonomous architecture reopening;
- starting Implementation 001-A without explicit human selection.

## Key current references

- [`authority_scope_policy.md`](authority_scope_policy.md)
- [`stable_reference_policy.md`](stable_reference_policy.md) / [`stable_id_registry.json`](stable_id_registry.json)
- [`context_discovery_policy.md`](context_discovery_policy.md)
- [`okf_profile.md`](okf_profile.md) / [`okf_maintenance_policy.md`](okf_maintenance_policy.md)
- [`conformance_policy.md`](conformance_policy.md)
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md)
- [`../index.md`](../index.md) — authored discovery root
- [`../implementation/README.md`](../implementation/README.md) — current implementation state
- [`../history/retrofits/dptn/`](../history/retrofits/dptn/) — completed topology-normalization provenance

## Current next dependency

**Implementation 001-A — NEXT / READY / NOT STARTED.**

Readiness does not authorize work. Begin 001-A only after a separate explicit human-selected implementation task.
