# ADF-G — Execution Review

**Status:** IN EXECUTION — REPOSITORY/ONBOARDING BASELINE IMPLEMENTED; PROVIDER RUNTIME EVIDENCE PENDING

## Decision

ADF-G is not yet COMPLETE / ACCEPTED.

Repository portability and ordinary IDE/CLI development are established, but the required representative task has not yet been exercised in actual Cursor, Claude Code, and Codex runtimes available to this execution environment. Those three entries therefore remain `unverified`, not `unsupported`.

## Delivered

- `tool_compatibility_matrix.md` — cross-tool repository compatibility;
- `developer_onboarding.md` — tool-neutral onboarding;
- `adf_g_runtime_probe.md` — one shared bounded A1 runtime exercise;
- `runtime_compatibility_evidence.json` — machine-readable evidence ledger;
- `scripts/agentic/probe_runtime_tools.py` — safe binary/version availability probe;
- `scripts/agentic/validate_adf_g_compatibility.py` — evidence integrity validation;
- `fixtures/adf_g_compatibility_scenarios.yaml` — ADF-G scenarios;
- ADF-F conformance extended with ADF-G evidence validation.

## Findings

### Shared repository compatibility — PASS

Cursor, Claude Code, Codex, and ordinary development all route to the same checked-in authority, knowledge, workflows, stable-reference discipline, conformance command, and normal Git/PR process. No provider-specific semantic rulebook is required.

### Cursor — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

Current Cursor documentation remains compatible with root/nested `AGENTS.md`, scoped `.cursor/rules/*.mdc`, and project `.agents/skills/`. No Cursor runtime was available here for the bounded exercise.

### Claude Code — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

Current Claude Code documentation remains compatible with `.claude/CLAUDE.md` importing shared `AGENTS.md`. Project skills are native under `.claude/skills/`, while existing `.claude/commands/` remain supported. DMTZ therefore keeps its thin command bridges to the canonical `.agents/skills/` workflows instead of duplicating semantic skill copies. No Claude Code runtime was available here for the bounded exercise.

### Codex — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

Current Codex guidance continues to use repository `AGENTS.md` discovery. No separate Codex semantic adapter is needed. No Codex runtime was available here for the bounded exercise, and this ChatGPT session is not counted as Codex runtime evidence.

### Ordinary IDE/CLI — PASS

A developer without a coding agent can use the same authority, knowledge, stable-ID helper, workflow Markdown, conformance command, diff review, and normal Git/PR process. ADF-F already proved the repository-owned validation path executes without provider coding-agent binaries.

## Evidence integrity — PASS

The ADF-G validator prevents a provider from being marked `supported` or `degraded` without a dated passing exercise and actual invocation observations. An `unverified` entry must remain `not_run`, have no runtime verification timestamp, and carry an explicit reason.

## Remaining acceptance gap

ADF-EX-17 requires the same representative bounded task to be completed in actual Cursor, Claude Code, and Codex environments. That evidence is not present yet.

To close ADF-G, execute `ADF-G-XT01` from `adf_g_runtime_probe.md` in each provider runtime, update `runtime_compatibility_evidence.json`, and rerun repository conformance.

## Current conclusion

**ADF-G remains IN EXECUTION / BLOCKED ONLY ON PROVIDER RUNTIME SMOKE EVIDENCE.**

ADF-H is not automatically started.
