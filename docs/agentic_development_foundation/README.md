# DMTZ Agentic Development Foundation

**Status:** COMPLETE / EXECUTION EXIT ACCEPTED — POST-EXIT CKR DOCUMENTATION AUTHORITY RETROFIT ACTIVE

## Final execution state

- **ADF-A — Authority, Scope & Human-Directed Operating Boundary: COMPLETE / ACCEPTED.**
- **ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.**
- **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.**
- **ADF-D — Portable Skills & Human-Directed Workflow Contract: COMPLETE / ACCEPTED.**
- **ADF-E — Context Discovery, Stable References & Knowledge Maintenance: COMPLETE / ACCEPTED.**
- **ADF-F — Conformance, Validation, Drift Detection & CI: COMPLETE / ACCEPTED.**
- **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model: COMPLETE / ACCEPTED FOR PROGRESSION — ADF-EX-17 DEFERRED VERIFICATION.**
- **ADF-H — Security, Trust, Lifecycle & Governance: COMPLETE / ACCEPTED.**
- **Databricks Agent Skills Integration Addendum: COMPLETE / ACCEPTED.**
- **Execution Exit Review / Consolidation: COMPLETE / ACCEPTED.**

**ADF status mirror: COMPLETE ADF-A–ADF-H; ADF-EX-17 DEFERRED VERIFICATION; FOUNDATION EXIT ACCEPTED; IMPLEMENTATION 001-A NEXT.**

The formal ADF exit decision remains [`execution_exit_review.md`](execution_exit_review.md):

- ADF-EX-01–ADF-EX-16 — PASS;
- ADF-EX-17 — **DEFERRED / WAIVED — BOUNDED VERIFICATION DEBT**;
- ADF-EX-18–ADF-EX-20 — PASS.

The mirror above records the result of the ADF dependency itself. A later repository decision has inserted the **Canonical Knowledge & Documentation Authority Retrofit (CKR)** before product implementation. Therefore the current implementation gate is owned by `docs/canonical_knowledge_retrofit/README.md` / `docs/implementation/README.md`, not by reinterpreting the historical ADF exit.

## Post-exit CKR dependency

CKR separates current semantic authority from preserved chronological design history before code/test traceability begins.

- ADF remains complete; CKR does not reopen ADF-A–H.
- ADF authority/scope/security/conformance mechanics remain in force throughout CKR.
- `knowledge/` remains routing rather than truth.
- `docs/canonical/` becomes current authority only through CKR record-by-record cutover.
- Implementation 001-A is currently blocked until CKR-K accepts the retrofit.

Primary CKR route: [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md).

## ADF-EX-17 residual verification

Cursor, Claude Code and Codex remain runtime-`unverified` until the common `ADF-G-XT01` bounded exercise is actually run in each provider runtime and recorded in `runtime_compatibility_evidence.json`.

The waiver does not convert missing runtime evidence to PASS, permit unsupported provider claims, or weaken DMTZ semantic/change-control authority, A1–A4 human direction, current-owner discipline, security or deterministic conformance.

## Databricks Agent Skills addendum

The accepted vendor set remains:

- `databricks-core`;
- `databricks-dabs`;
- `databricks-jobs`;
- `databricks-pipelines`;
- `databricks-data-discovery`;
- `databricks-dbsql`;
- `databricks-unity-catalog`;
- `databricks-lakeflow-connect`.

Vendor skills are reviewed operational guidance, never DMTZ semantic/authorization authority. DMTZ overlays remain canonical development workflows under `.agents/skills/`. Model/AI implementation skills and managed Databricks MCP servers remain deferred.

`DBX-SKILL-RUN-01` remains a future Implementation 001-A environment obligation after CKR unlocks implementation.

## Durable foundation model

### Authority and human direction

A1–A4 remains the action model. Accepted DMTZ semantics outrank agent tooling, vendor guidance and memory. CKR migration itself is A2 documentation work unless it discovers a genuine semantic/architecture contradiction, which requires A4 change control.

### Knowledge, workflows and context

OKF remains routing. Canonical workflows live under `.agents/skills/`; Claude uses thin bridges. Progressive disclosure, stable references and context budgets remain mandatory.

CKR refines what “canonical resource” means during migration: the current owner is selected by the CKR ownership inventory rather than by path age, search order or the mere existence of `docs/canonical/`.

### Conformance and CI

Canonical command:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

The runner now also validates CKR canonical-knowledge authority and CKR status. Its PASS result remains repository configuration/documentation conformance, not DMTZ domain health or provider/Databricks runtime proof.

### Security and lifecycle

Least privilege, secret/sensitive-data boundaries, prompt/content trust, noncanonical tool memory, provider/vendor lifecycle review and G1–G5 change governance remain mandatory.

## Explicitly deferred / not authorized

- `ADF-G-XT01` provider-runtime verification remains open;
- autonomous task selection or unattended autonomous implementation;
- multi-agent implementation delegation/orchestration;
- unattended merge/deploy/external writes;
- autonomous architecture reopening;
- tool memory/personal state as canonical truth;
- automatic adoption of newly published Databricks skills;
- Databricks model/AI implementation skills until explicitly reviewed;
- managed Databricks MCP servers until separately reviewed.

## Key references

- [`execution_exit_review.md`](execution_exit_review.md) — accepted ADF exit as of its decision time;
- [`authority_scope_policy.md`](authority_scope_policy.md) — human-directed authority;
- [`okf_profile.md`](okf_profile.md) — OKF profile;
- [`stable_reference_policy.md`](stable_reference_policy.md) / [`stable_id_registry.json`](stable_id_registry.json) — stable reference discipline;
- [`conformance_policy.md`](conformance_policy.md) — conformance model;
- [`security_trust_lifecycle_policy.md`](security_trust_lifecycle_policy.md) / [`agentic_change_governance.md`](agentic_change_governance.md) — security/change governance;
- [`databricks_agent_skills_addendum.md`](databricks_agent_skills_addendum.md) — reviewed Databricks skills boundary;
- [`../canonical_knowledge_retrofit/README.md`](../canonical_knowledge_retrofit/README.md) — current post-ADF documentation-authority dependency.

## Current next dependency

**CKR-A — Authority Model, Migration Contract & Canonical Ownership Inventory is the current post-ADF work.**

Implementation 001-A becomes eligible only after CKR-K accepts the retrofit. ADF exit acceptance itself remains valid and is not rewritten retroactively.
