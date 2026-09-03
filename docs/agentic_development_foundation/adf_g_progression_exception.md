# ADF-G — Bounded Progression Exception

**Status:** ACCEPTED FOR FOUNDATION PROGRESSION — ADF-EX-17 DEFERRED VERIFICATION

**Recorded:** 2026-09-02

## Purpose

The human owner explicitly authorized proceeding to ADF-H even though the current execution environment cannot perform the required Cursor, Claude Code and Codex runtime smoke exercise.

This exception is intentionally narrow. It permits **foundation sequencing only**; it does not convert missing runtime evidence into a PASS.

## Scope

Only **ADF-EX-17** is deferred:

> one representative bounded task is successfully exercised with Cursor, Claude Code and Codex using the same repository acceptance criteria.

All repository/configuration/onboarding evidence delivered by ADF-G remains accepted. The provider runtime ledger remains authoritative for runtime-verification state:

- Cursor — `unverified`;
- Claude Code — `unverified`;
- Codex — `unverified`;
- ordinary IDE/CLI — `supported`.

## Non-waived boundaries

This exception does **not** waive or weaken:

- DMTZ semantic/change-control authority;
- A1–A4 human-directed scope;
- canonical-reference requirements;
- secret/sensitive-data controls;
- least privilege or external-action approvals;
- repository conformance/CI;
- the requirement to record actual runtime evidence before calling a provider runtime-supported.

`tool_compatibility.json` must continue to report runtime smoke pending for an unverified provider.

## Reverification obligation

When an actual provider runtime becomes available, execute `ADF-G-XT01` and update `runtime_compatibility_evidence.json`. A failed smoke reopens the affected adapter/compatibility work before that provider is relied on for supported DMTZ development.

## Foundation exit treatment

The final Agentic Development Foundation execution exit review may accept ADF-EX-17 only as this **specific bounded deferred-verification waiver**. It must remain visible as residual verification debt and cannot be generalized into permission to waive shared-authority, security, canonical-reference or human-direction failures.
