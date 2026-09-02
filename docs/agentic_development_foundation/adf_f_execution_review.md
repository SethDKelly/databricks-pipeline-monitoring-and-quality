# ADF-F — Execution Review

**Status:** PROVISIONAL — REPOSITORY CI EVIDENCE PENDING

## Review question

Has ADF-F integrated the ADF-A–ADF-E validation seams into one deterministic repository conformance path that detects representative drift before merge while keeping agentic configuration health separate from DMTZ domain/runtime health?

The repository artifacts are implemented. Final acceptance requires the real `Agentic conformance` GitHub Actions job to pass on the synchronized ADF-F closure commit. This file will be finalized with that run evidence.

## Implemented artifacts

- `scripts/agentic/run_conformance.py` — unified runner and human-readable report;
- `validate_status_drift.py` — live ADF status-mirror drift;
- `validate_agentic_references.py` — local link and accepted stable-ID references;
- `validate_fixture_catalog.py` — ADF scenario-catalog integrity;
- `test_conformance_guards.py` — seven temporary-checkout negative controls;
- existing ADF-B–E validators integrated rather than replaced;
- `.github/workflows/agentic-conformance.yml` — dedicated CI job;
- `conformance_policy.md` — conformance/failure semantics;
- `compatibility_smoke_checklist.md` — ADF-G runtime checklist;
- `fixtures/adf_f_conformance_scenarios.yaml`.

## Acceptance evidence required

- real repository positive checks all PASS;
- all seven negative controls PASS by causing their targeted validators to fail;
- generated Agentic Conformance Report explicitly remains non-domain health;
- dedicated CI workflow completes successfully on `main`;
- no ADF-G runtime/tool compatibility claim is manufactured by deterministic CI.

## Residual groups

- **ADF-G:** actual Cursor / Claude Code / Codex runtime compatibility, onboarding and representative bounded-task exercise;
- **ADF-H:** security, trust, lifecycle and compatibility-review governance;
- foundation execution exit review after ADF-H.
