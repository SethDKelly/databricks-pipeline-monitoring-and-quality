# ADF-F — Execution Review

**Status:** ACCEPTED — ADF-F COMPLETE

## Review question

Has ADF-F integrated the ADF-A–ADF-E validation seams into one deterministic repository conformance path that detects representative drift before merge while keeping agentic configuration health separate from DMTZ domain/runtime health?

**Conclusion: yes.**

ADF-F is accepted on actual repository-level GitHub Actions evidence, including both positive conformance and deliberately seeded negative controls. It does not claim Cursor, Claude Code, or Codex runtime compatibility; that remains ADF-G evidence.

## Delivered artifacts

- `scripts/agentic/run_conformance.py` — one canonical runner plus human-readable Agentic Conformance Report;
- `scripts/agentic/validate_status_drift.py` — live ADF status-mirror drift;
- `scripts/agentic/validate_agentic_references.py` — local agent-facing links and accepted stable-ID citations;
- `scripts/agentic/validate_fixture_catalog.py` — ADF scenario-catalog integrity;
- `scripts/agentic/test_conformance_guards.py` — seven isolated negative controls in a temporary checkout;
- existing ADF-B–ADF-E validators integrated rather than replaced;
- `.github/workflows/agentic-conformance.yml` — dedicated agentic conformance CI;
- `docs/agentic_development_foundation/conformance_policy.md` — conformance/failure semantics;
- `compatibility_smoke_checklist.md` — ADF-G runtime checklist;
- `fixtures/adf_f_conformance_scenarios.yaml` — ADF-F structural/boundary scenarios;
- `knowledge/log.md` record of ADF-F realization;
- `run-conformance` workflow updated to route agentic changes through the canonical ADF-F command.

## Findings

### 1. Unified deterministic path — PASS

The canonical command is:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

It composes, in order:

1. documentation consistency;
2. OKF structure/resources/profile validation;
3. tool-adapter validation;
4. portable skill validation;
5. agent-facing canonical link/stable-ID validation;
6. ADF status drift validation;
7. fixture catalog validation;
8. deterministic context-budget validation;
9. negative controls proving that targeted defects are rejected.

The path is repository-owned, dependency-light, safe/non-destructive, and does not require provider coding-agent binaries or Databricks credentials.

### 2. Dedicated CI boundary — PASS

`.github/workflows/agentic-conformance.yml` runs the canonical command on relevant pull requests and pushes to `main` with read-only repository permissions.

The workflow is independent of future DMTZ product/runtime tests. A failed agentic check means repository agentic configuration/routing/workflow/reference/context drift, not monitored-pipeline health, data quality, source health, application correctness, or production readiness.

### 3. First real CI run detected real ADF-F defects — PASS / useful failure evidence

The first inspectable Agentic conformance validation run was GitHub Actions run **#11**, run ID **33692085995**, job **100452826714**.

It failed for two legitimate implementation defects:

1. the shortened Cursor routing rule had accidentally dropped its explicit `authority_scope_policy.md` route, which the existing adapter validator correctly rejected;
2. the initial stale-status negative-control mutation merely prefixed the valid status mirror, so the valid substring remained and `validate_status_drift.py` correctly continued to pass—revealing that the test mutation itself was insufficient.

The same run showed the other positive layers passing and six of seven negative controls working. ADF-F did not weaken those validators to obtain a green result.

Corrections:

- restored the shared authority-policy route in `.cursor/rules/00-implementation-routing.mdc`;
- changed the stale-status negative control to replace the actual current state with the prior ADF-E/ADF-F state;
- made the `implement-group` autonomy boundary explicit enough to eliminate an earlier advisory wording warning.

### 4. Positive repository conformance — PASS

After correction, Agentic conformance run **#14** (run ID **33692203727**, job **100453193652**) passed, as did Documentation consistency run **#132**.

A final verification was then performed after modernizing the GitHub Actions wrapper versions. Agentic conformance run **#16** (run ID **33692307114**, job **100453521846**) passed, and Documentation consistency run **#134** (run ID **33692307271**) passed.

Final run #16 results:

- documentation consistency — PASS;
- OKF structure/resources — PASS, **0 errors / 0 warnings**;
- tool adapters — PASS, **0 errors**;
- portable skills — PASS, **0 errors / 0 warnings**;
- agentic canonical references — PASS, **30 unique accepted stable IDs checked**;
- ADF status drift — PASS, **0 errors**;
- fixture catalog — PASS, **78 scenarios** across ADF-A–ADF-F;
- context budgets — PASS;
- negative controls — PASS, **7 / 7 defects detected**;
- generated Agentic Conformance Report — **PASS**;
- deprecated knowledge entries — **0**;
- stale knowledge entries — **0**.

The only adapter messages in the final report are expected warnings that Cursor, Claude Code, and Codex runtime smoke verification remains pending ADF-G.

### 5. Negative controls prove guards fail closed — PASS

The final run verifies that each temporary-checkout mutation is rejected:

1. malformed OKF metadata;
2. provider-specific metadata in the canonical portable skill;
3. accidental `alwaysApply: true` Cursor routing;
4. persistent-context budget overflow;
5. stale ADF status mirror;
6. broken canonical OKF resource route;
7. unaccepted stable-ID citation `ARCH-501`.

The mutations occur only in a temporary copied checkout and are discarded after execution.

### 6. Context budgets are enforced on the real checkout — PASS

Final run #16 measured:

- root `AGENTS.md`: **9,906 / 16,384 bytes**;
- `.claude/CLAUDE.md`: **1,054 / 2,048 bytes**;
- Cursor rules aggregate: **18,640 / 32,768 bytes**;
- Cursor routing rule: **3,129 / 6,144 bytes**;
- Cursor root baseline: **9,906 / 20,480 bytes**;
- Claude root baseline: **10,960 / 18,432 bytes**;
- Codex root baseline: **9,906 / 16,384 bytes**;
- every canonical skill, Claude bridge, OKF index and concept remained below its configured budget.

This closes the repository-execution portion of the ADF-E context-budget obligation while leaving observed vendor prompt/token behavior to ADF-G.

### 7. Status drift is deterministic — PASS

The ADF README remains the ADF progression authority. `validate_status_drift.py` derives the current mirror:

`ADF status mirror: COMPLETE ADF-A–ADF-F; NEXT ADF-G.`

and requires it across the shared live routing surfaces.

The negative control proves a stale prior state is rejected.

### 8. Canonical references remain bounded — PASS

`validate_agentic_references.py` validates repository-relative agent-facing links and stable-ID citations in operational agentic surfaces.

The final run checked **30 unique stable IDs**, ensured each was inside the accepted registry range and present in canonical non-implementation DMTZ documentation, and rejected a seeded `ARCH-501` citation.

This validation checks reference integrity; it does not convert occurrence order into semantic ownership.

### 9. Scenario corpus is present and non-duplicated — PASS

The fixture catalog now covers ADF-A through ADF-F and contains **78 unique scenarios**. Each completed group has an execution review. These artifacts provide deterministic structural/boundary inputs without pretending that repository fixtures are equivalent to provider runtime behavior.

### 10. Drift report semantics remain non-domain — PASS

The generated report explicitly states:

> This report describes repository agentic configuration health only. It is not DMTZ domain health, data quality, source health, or production readiness.

A tool may be degraded/unverified independently without causing another tool or a DMTZ domain state to fail.

### 11. CI action runtime modernization — PASS

The initial green run exposed a GitHub runner warning that the older `actions/checkout@v4` and `actions/setup-python@v5` actions targeted deprecated Node 20 execution.

Current official release metadata was rechecked on 2026-09-02 and showed current v7 releases for both actions. The Agentic conformance and Documentation consistency workflows were updated to `actions/checkout@v7` and `actions/setup-python@v7`.

Final run #16 executed those v7 majors successfully and no longer emitted the Node-20-targeting action warning.

This is CI platform maintenance, not DMTZ semantic authority.

### 12. Tool runtime evidence remains separate — PASS

Final deterministic validation intentionally reports:

- Cursor: `documentation_verified_runtime_smoke_pending`;
- Claude Code: `documentation_verified_runtime_smoke_pending`;
- Codex: `documentation_verified_runtime_smoke_pending`.

ADF-F does not turn static repository configuration into runtime certification. `compatibility_smoke_checklist.md` carries those obligations into ADF-G.

### 13. Normal developer/product validation remains separate — PASS

Agentic conformance is an early repository-configuration gate. It does not replace ordinary documentation checks, future unit/property/contract/persistence/adapter/integration/scenario tests, deployment validation, or production acceptance.

A non-agent developer may invoke the same conformance command without any coding-agent product installed.

### 14. Autonomous scope remains deferred — PASS

ADF-F adds no unattended task allocation, multi-agent implementation delegation, autonomous continuation, unattended merge/deployment, or agent-controlled architecture reopening.

The CI runner performs deterministic repository checks only.

## Relationship to foundation exit gates

ADF-F provides direct repository execution evidence for:

- **ADF-EX-14** — deterministic validation catches malformed agentic metadata, broken canonical references, and stale duplicated status;
- **ADF-EX-15** — deterministic context-budget checks prevent accidental return to monolithic always-loaded instructions;
- **ADF-EX-16** — one drift/conformance report summarizes agentic configuration health without presenting it as DMTZ domain health.

It also strengthens evidence for ADF-EX-04, ADF-EX-07, ADF-EX-11, ADF-EX-12, and ADF-EX-13 through integrated execution of their ADF-B–ADF-E validators and fixtures.

Whole-foundation acceptance still requires ADF-G runtime compatibility evidence, ADF-H governance/security/lifecycle consolidation, and the final ADF-EX-01–20 exit review.

## Residual obligations

- **ADF-G:** exercise representative bounded work in actual Cursor, Claude Code, and Codex environments; record supported/degraded/unverified behavior, onboarding, and ordinary non-agent compatibility.
- **ADF-H:** consolidate security, trust, lifecycle, verification horizons, secrets/data boundaries, and governance.
- **Foundation exit:** evaluate all ADF-EX-01–ADF-EX-20 using ADF-A–ADF-H evidence before Implementation 001-A begins.

## Exit decision

**ADF-F — Conformance, Validation, Drift Detection & CI: COMPLETE / ACCEPTED.**

The next required foundation group is **ADF-G — Developer Tool Compatibility, Onboarding & Operating Model**.
