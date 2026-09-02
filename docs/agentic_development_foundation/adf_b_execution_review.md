# ADF-B — Execution Review

**Status:** ACCEPTED — ADF-B COMPLETE

## Review question

Has ADF-B implemented a portable OKF v0.2 knowledge plane that improves agent/developer discovery without becoming a competing DMTZ source of truth?

**Conclusion: yes.**

## Delivered artifacts

- `knowledge/index.md` and `knowledge/log.md` — OKF v0.2 bundle root and change log.
- `knowledge/project/` — repository authority, architecture, implementation-program and ADF routing.
- `knowledge/domains/` — seven compact domain-routing concepts.
- `knowledge/implementation/` — implementation 001–011 routing concepts.
- `knowledge/workflows/` — explicit `draft` routing concepts for ADF-D workflows not yet implemented.
- `docs/agentic_development_foundation/okf_profile.md` — stricter DMTZ producer profile over base OKF v0.2.
- `docs/agentic_development_foundation/okf_maintenance_policy.md` — ownership, lifecycle, provenance and drift rules.
- `docs/agentic_development_foundation/fixtures/adf_b_knowledge_scenarios.yaml` — reusable knowledge-plane conformance scenarios.
- `scripts/agentic/validate_okf.py` — dependency-free structural/profile/resource/local-link validator.
- `external_standards_baseline.md` — OKF v0.2 reverified on 2026-09-02.

## Findings

### 1. Upstream format authority — PASS

ADF-B reverified the upstream GoogleCloudPlatform `knowledge-catalog/okf/SPEC.md` as OKF v0.2. DMTZ does not use the independent `okf.md` site as specification authority.

Base OKF remains permissive (`type` universally required; producer-defined types allowed); the DMTZ producer profile adds maintainability requirements without redefining the base format.

### 2. Knowledge is routing, not truth — PASS

Every concept routes to canonical repository resources. The root bundle and producer profile explicitly state that exact semantics remain in canonical `docs/`, code, tests and accepted program authority.

If a routing summary conflicts with its `resource`, the canonical resource wins and the knowledge entry is a defect to fix.

### 3. Progressive disclosure — PASS

The implemented path is:

`knowledge/index.md` → one category index → one routing concept → canonical resource → exact stable IDs as needed.

The bundle intentionally avoids one concept per accepted contract ID.

### 4. DMTZ OKF profile — PASS

Non-reserved concept documents require:

- `type`;
- `title`;
- `description`;
- `resource`;
- inline `tags`;
- lifecycle `status`.

The root index declares `okf_version: "0.2"`.

Unknown valid producer-defined `type` values remain allowed.

### 5. Trust/lifecycle semantic firewall — PASS

The profile and fixtures explicitly preserve:

- OKF `verified` ≠ Assertion Authority;
- OKF review/trust ≠ evidence sufficiency or causal confirmation;
- OKF `stable` ≠ DMTZ health/quality;
- OKF `stale_after` ≠ monitored-data freshness;
- OKF provenance ≠ proposition-level DMTZ evidence by default.

### 6. Lifecycle honesty — PASS

Current project/domain/implementation routing entries are `stable` because the routing artifacts are maintained/current, not because the routed implementation is complete.

Workflow entries are `draft` because ADF-D has not yet created the portable workflow artifacts.

### 7. Deterministic validation seam — PASS

`scripts/agentic/validate_okf.py` validates the DMTZ profile, root OKF version, local `resource` paths, local Markdown links and lifecycle/staleness warnings without adding a dependency stack before Implementation 001.

ADF-F remains responsible for CI integration, richer automated fixture testing and any future full-YAML parser adoption.

No claim is made in ADF-B that the validator is already a required CI gate.

### 8. Maintenance/generation boundary — PASS

Knowledge maintenance may update routing artifacts but may not generate semantic changes back into canonical DMTZ documentation. Broken knowledge references fail the knowledge layer rather than changing product truth.

### 9. Deferred capabilities remain deferred — PASS

ADF-B does not add OKF Attested Computation runtime behavior, MCP serving, remote knowledge infrastructure or autonomous knowledge-maintenance execution.

## Relationship to foundation exit gates

ADF-B establishes the implementation basis for:

- **ADF-EX-04** — structurally valid OKF v0.2/DMTZ profile bundle;
- **ADF-EX-05** — progressive disclosure to current program/domain architecture;
- **ADF-EX-06** — trust/lifecycle semantics remain separate from DMTZ semantics;
- **ADF-EX-07** — broken/deprecated/stale routing is surfaced explicitly.

These whole-foundation gates remain open until ADF-F/E/G provide the required automated and cross-tool evidence.

## Residual obligations

- ADF-C must wire Cursor/Claude/Codex adapters to `knowledge/index.md` without duplicating the knowledge corpus.
- ADF-D must replace workflow routing placeholders with portable human-directed skills/workflows.
- ADF-E must refine stable-ID retrieval and knowledge-maintenance/context-budget behavior using this bundle.
- ADF-F must execute/integrate deterministic knowledge validation in CI and automate relevant fixtures.
- ADF-H must establish the long-term external-standard/tool compatibility review horizon.

## Exit decision

**ADF-B — OKF v0.2 Knowledge Plane & DMTZ Knowledge Profile: COMPLETE / ACCEPTED.**

The next required foundation group is **ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract**. ADF-D/E remain dependent on completion of the shared instruction/adapter layer as defined by the accepted foundation dependency model.
