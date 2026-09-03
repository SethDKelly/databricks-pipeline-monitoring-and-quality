# ADF-G — Execution Review

**Status:** COMPLETE / ACCEPTED FOR FOUNDATION PROGRESSION — ADF-EX-17 DEFERRED VERIFICATION

## Review question

Can a developer choose Cursor, Claude Code, Codex, or ordinary IDE/CLI development without changing DMTZ semantics, authority, workflow obligations or acceptance criteria?

## Decision

**Yes at the repository/onboarding/ordinary-development level.**

ADF-G established the shared compatibility model, onboarding path, runtime evidence contract and evidence-integrity checks. Actual Cursor, Claude Code and Codex provider runtimes were unavailable in the execution environment, so the representative provider exercise was not run and **ADF-EX-17 is not a PASS**.

On 2026-09-02 the human owner explicitly authorized proceeding to ADF-H despite that unavailable evidence. The bounded exception is recorded in `adf_g_progression_exception.md`.

ADF-G is therefore **accepted for foundation sequencing only**, with ADF-EX-17 deferred. This does not permit any provider runtime to be called supported until actual runtime evidence exists.

## Delivered

- `tool_compatibility_matrix.md` — cross-tool repository compatibility;
- `developer_onboarding.md` — tool-neutral onboarding;
- `adf_g_runtime_probe.md` — one shared bounded A1 runtime exercise (`ADF-G-XT01`);
- `runtime_compatibility_evidence.json` — machine-readable evidence ledger;
- `scripts/agentic/probe_runtime_tools.py` — safe binary/version availability probe;
- `scripts/agentic/validate_adf_g_compatibility.py` — evidence integrity validation;
- `fixtures/adf_g_compatibility_scenarios.yaml` — ADF-G scenarios;
- unified conformance extended with ADF-G evidence validation;
- `adf_g_progression_exception.md` — bounded human-authorized deferred-verification decision.

## Findings

### Shared repository compatibility — PASS

Cursor, Claude Code, Codex and ordinary development all route to the same checked-in authority, knowledge, workflows, stable-reference discipline, conformance command and normal Git/PR process. No provider-specific semantic rulebook is required.

### Cursor — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

The repository adapter remains compatible with documented root/nested `AGENTS.md`, scoped `.cursor/rules/*.mdc` and project `.agents/skills/`. No actual Cursor Agent/CLI runtime performed `ADF-G-XT01`.

### Claude Code — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

The repository uses `.claude/CLAUDE.md` importing shared `AGENTS.md` plus thin `.claude/commands/` bridges into canonical `.agents/skills/`. No duplicate semantic skill corpus is required. No actual Claude Code runtime performed `ADF-G-XT01`.

### Codex — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

Codex uses shared repository `AGENTS.md` and portable workflows without a separate DMTZ rulebook. No actual Codex runtime performed `ADF-G-XT01`; this ChatGPT session is not counted as Codex runtime evidence.

### Ordinary IDE/CLI development — PASS

A developer without a coding agent can use the same repository authority, Markdown workflows, stable-ID helpers, deterministic conformance, normal diff review and Git/PR process.

### Tool-neutral onboarding — PASS

`developer_onboarding.md` covers authority/live state, A1–A4 scope, stable-ID resolution, conformance, provider adapters, personal-setting precedence, ordinary development, Git/PR lifecycle and adding another provider without semantic redesign.

### Representative runtime exercise contract — PASS at harness level

`ADF-G-XT01` requires each provider runtime to:

- determine current ADF state from repository authority;
- resolve `AUTH-034` through accepted-range/exact-occurrence/canonical-owner discipline;
- identify the canonical `run-conformance` workflow and command;
- make no repository edits;
- stop at the human-selected task;
- record degraded/unverified native conveniences without changing semantics.

The harness exists; provider execution remains deferred.

### Evidence integrity — PASS

`validate_adf_g_compatibility.py` prevents a provider from being marked `supported` or `degraded` without a passing exercise, runtime invocation, verification date and substantive observations. An `unverified` entry must remain `not_run`, have no runtime verification timestamp and carry a reason.

### Repository CI — PASS

ADF-G PR #2 supplied actual repository-level evidence. The finalized branch passed:

- **Agentic conformance #22** — SUCCESS;
- **Documentation consistency #140** — SUCCESS.

The preceding detailed run #21 reported 90 scenarios, 30 accepted stable-ID references, healthy context budgets, ADF-G compatibility validation with 0 errors / 3 expected runtime-unverified warnings, and 8/8 seeded negative controls detected.

### Independent compatibility state — PASS

The runtime ledger remains:

- Cursor — `unverified`;
- Claude Code — `unverified`;
- Codex — `unverified`;
- ordinary IDE/CLI — `supported`.

An unverified provider does not invalidate another provider, ordinary development, canonical DMTZ documentation or agentic configuration conformance.

### Tool switching / future providers — PASS at repository contract level

No provider owns semantic status, branch state, acceptance criteria or workflow truth. Another coding agent may be added later if it can consume or thinly bridge to shared authority, `knowledge/index.md`, canonical workflows, repository validation and A1–A4 boundaries, and then passes the same runtime-evidence discipline.

## Deferred ADF-EX-17 obligation

The provider runtime gate remains open as **deferred verification**, not PASS.

When actual runtimes become available:

1. execute `ADF-G-XT01` in Cursor;
2. execute it in Claude Code;
3. execute it in Codex;
4. record versions, invocations, observations and results in `runtime_compatibility_evidence.json`;
5. update `tool_compatibility.json` only where evidence justifies it;
6. rerun repository conformance.

A failed smoke reopens the affected provider adapter/support claim before that provider is relied on.

## Progression exception boundaries

The human-authorized exception permits ADF-H and the final foundation exit review to proceed. It does **not** waive:

- shared semantic/change-control authority;
- A1–A4 human direction;
- canonical-reference discipline;
- security/secret/data boundaries;
- deterministic conformance;
- the requirement for actual provider evidence before runtime support is claimed.

The final foundation exit review must classify ADF-EX-17 explicitly as deferred/waived unless actual provider evidence has appeared.

## Exit decision

**ADF-G — Developer Tool Compatibility, Onboarding & Operating Model: COMPLETE / ACCEPTED FOR FOUNDATION PROGRESSION WITH ADF-EX-17 DEFERRED VERIFICATION.**

ADF-H may proceed under the recorded bounded exception.
