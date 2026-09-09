# ADF-G — Developer Tool Compatibility, Onboarding & Operating Model

**Status:** IN EXECUTION — REPOSITORY/ONBOARDING BASELINE IMPLEMENTED; PROVIDER RUNTIME SMOKES PENDING

## Objective

Prove that a developer can choose Cursor, Claude Code or Codex without changing DMTZ semantics, review requirements or implementation acceptance criteria, while preserving fully viable ordinary IDE/CLI development.

## Supported profile

Initial supported-profile candidates:

- Cursor Agent for interactive repository work;
- Claude Code for interactive repository work;
- Codex for interactive repository work;
- ordinary IDE/CLI development without an agent remains fully supported.

No coding-agent tool is required to implement DMTZ. A provider becomes runtime-supported only after actual ADF-G runtime evidence exists.

## Compatibility dimensions

Each provider runtime is checked against:

1. repository instruction loading;
2. scoped/path-specific instruction support or a non-semantic fallback;
3. portable workflow/skill invocation or equivalent;
4. repository search/read capability;
5. local edit/test capability when the selected task permits edits;
6. visibility of current implementation/ADF authority;
7. progressive knowledge retrieval through `knowledge/`;
8. safe handling of unavailable/unsupported native features;
9. human approval boundary behavior;
10. developer ability to inspect what instructions/workflow were applied.

## Human-directed operating model

A normal development session remains:

1. developer chooses tool;
2. developer starts from a repository issue/group/task;
3. agent resolves context from shared authority/OKF/canonical docs;
4. developer asks for review, plan or implementation;
5. agent works within that explicit task scope;
6. repository validation, not agent confidence, determines conformance;
7. developer reviews normal diff/test evidence;
8. normal Git/PR/team process governs integration.

No special AI branch semantics are required. Agent-created code is ordinary code subject to ordinary repository controls.

## Tool-specific expectations

### Cursor

Use root `AGENTS.md`, existing scoped `.cursor/rules/`, and canonical `.agents/skills/`. Cursor remains a supported-profile candidate, but runtime acceptance remains unverified until `ADF-G-XT01` is executed in an actual Cursor runtime.

### Claude Code

Use `.claude/CLAUDE.md` importing shared `AGENTS.md`. Current Claude Code project skills are native under `.claude/skills/`, while existing `.claude/commands/` remain supported. DMTZ intentionally uses thin command bridges to canonical `.agents/skills/` rather than duplicating workflow semantics. Runtime acceptance remains unverified until the bounded exercise is executed in an actual Claude Code runtime.

### Codex

Use root `AGENTS.md` and portable knowledge/workflows. Codex-specific environment configuration may improve execution mechanics but may not define semantic requirements absent from shared sources. Runtime acceptance remains unverified until the bounded exercise is executed in an actual Codex runtime.

## Onboarding

`developer_onboarding.md` now provides the tool-neutral onboarding exercise:

- locate current work;
- resolve one stable contract;
- follow `resolve-context`/shared routing;
- run agentic conformance;
- understand provider and ordinary CLI paths;
- understand where personal preferences may be configured without entering repository truth.

## Runtime acceptance exercise

`adf_g_runtime_probe.md` defines one shared A1 task (`ADF-G-XT01`) for all three providers. It requires current-state resolution, `AUTH-034` stable-reference handling, `run-conformance` workflow discovery, canonical command reporting, read-only behavior and stop-at-scope behavior.

`runtime_compatibility_evidence.json` is the machine-readable evidence ledger. `validate_adf_g_compatibility.py` rejects unsupported promotion from documentation/static configuration to runtime PASS.

## Compatibility degradation

If a supported-profile tool temporarily lacks a native feature:

- fall back to manual/shared Markdown workflow instructions;
- do not fork product semantics;
- mark the feature degraded/unverified in the compatibility evidence;
- do not block ordinary development if core repository read/edit/test behavior remains available.

## Evaluation approach

Use the same small representative task across all three actual provider runtimes and compare outcomes at the artifact/evidence level:

- relevant context found;
- prohibited context not unnecessarily loaded;
- semantic guardrails respected;
- no files changed for the A1 probe;
- canonical validation command found;
- no extra unrequested scope;
- developer can understand the result.

Do not rank tools with a universal score. Compatibility is multidimensional and may change with vendor releases.

## Delivered in current execution

- supported-tool compatibility matrix — implemented;
- verification/evidence separation — implemented;
- tool-neutral onboarding guide — implemented;
- representative cross-tool acceptance exercise — implemented as a probe contract;
- documented degraded/unverified behavior — implemented;
- guidance for adding another coding agent — implemented;
- ordinary non-agent development path — verified through repository-owned conformance;
- provider runtime executions — **pending because no Cursor/Claude Code/Codex runtime is available in the execution environment**.

## Acceptance status

Repository-level/tool-neutral acceptance criteria are satisfied, but the planned ADF-G runtime criterion remains open:

- the same bounded task has **not yet** been executed through actual Cursor, Claude Code and Codex runtimes in this environment;
- static/documentation compatibility is not promoted to runtime PASS;
- ADF-G remains in execution until the runtime ledger contains passing evidence for those provider profiles or a narrow explicit waiver changes the foundation acceptance decision.
