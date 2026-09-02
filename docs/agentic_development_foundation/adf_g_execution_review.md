# ADF-G — Execution Review

**Status:** IN EXECUTION — REPOSITORY/ONBOARDING BASELINE VALIDATED; PROVIDER RUNTIME EVIDENCE PENDING

## Review question

Can a developer choose Cursor, Claude Code, Codex, or ordinary IDE/CLI development without changing DMTZ semantics, authority, workflow obligations or acceptance criteria?

## Current decision

ADF-G is **not yet COMPLETE / ACCEPTED**.

Repository portability, onboarding, evidence discipline and ordinary IDE/CLI development are established and validated. The required representative task has not yet been exercised in actual Cursor, Claude Code and Codex runtimes available to this execution environment. Those three provider entries therefore remain `unverified`, not `unsupported`.

This is an intentional acceptance boundary: documentation/static configuration must not be promoted to provider runtime proof.

## Delivered

- `tool_compatibility_matrix.md` — cross-tool repository compatibility;
- `developer_onboarding.md` — tool-neutral onboarding;
- `adf_g_runtime_probe.md` — one shared bounded A1 runtime exercise (`ADF-G-XT01`);
- `runtime_compatibility_evidence.json` — machine-readable evidence ledger;
- `scripts/agentic/probe_runtime_tools.py` — safe binary/version availability probe;
- `scripts/agentic/validate_adf_g_compatibility.py` — evidence integrity validation;
- `fixtures/adf_g_compatibility_scenarios.yaml` — ADF-G scenarios;
- ADF-F conformance extended with ADF-G evidence validation;
- status-drift validation extended to represent an explicit `IN EXECUTION` foundation group without falsely marking it complete.

## Findings

### 1. Shared repository compatibility — PASS

Cursor, Claude Code, Codex and ordinary development all route to the same checked-in authority, knowledge, workflows, stable-reference discipline, conformance command and normal Git/PR process. No provider-specific semantic rulebook is required.

The shared path remains:

```text
human-selected task
  → root/shared repository authority
  → explicit path/ID when known; otherwise knowledge/index.md
  → canonical .agents/skills workflow when useful
  → canonical docs/contracts/tests
  → repository-defined validation
  → normal diff/Git/PR review
```

Provider-native features may improve ergonomics, but correctness does not depend on semantic duplication.

### 2. Cursor — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

Current Cursor documentation remains compatible with root/nested `AGENTS.md`, scoped `.cursor/rules/*.mdc`, and project `.agents/skills/`.

No actual Cursor Agent/CLI runtime was available in the ADF-G execution environment for `ADF-G-XT01`. Runtime state therefore remains `unverified`.

### 3. Claude Code — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

Current Claude Code documentation remains compatible with `.claude/CLAUDE.md` importing shared `AGENTS.md`. Project-native skills normally live under `.claude/skills/`, while existing `.claude/commands/` remain supported. DMTZ therefore keeps thin command bridges to the canonical `.agents/skills/` workflows rather than duplicating semantic skill copies.

No actual Claude Code runtime was available in the ADF-G execution environment for `ADF-G-XT01`. Runtime state therefore remains `unverified`.

### 4. Codex — DOCUMENTATION/CONFIGURATION PASS; RUNTIME UNVERIFIED

Current Codex guidance continues to use repository `AGENTS.md` discovery and supports repository-owned development context without a separate Codex semantic rulebook.

No actual Codex runtime was available in the ADF-G execution environment for `ADF-G-XT01`. This ChatGPT session is not counted as Codex runtime evidence. Runtime state therefore remains `unverified`.

### 5. Ordinary IDE/CLI development — PASS

A developer without a coding agent can use the same authority, knowledge, stable-ID helper, workflow Markdown, conformance command, diff review and normal Git/PR process.

The canonical command remains:

```bash
python3 scripts/agentic/run_conformance.py --report agentic-conformance-report.md
```

No provider coding-agent runtime is required for the deterministic repository validation path.

### 6. Tool-neutral onboarding — PASS

`developer_onboarding.md` provides a common onboarding path for all four modes and explicitly covers:

- authority and live status;
- A1–A4 scope;
- stable-ID resolution;
- conformance;
- provider-specific adapter mechanics without semantic forks;
- ordinary IDE/CLI use;
- personal-setting precedence;
- normal Git/PR lifecycle;
- onboarding a future provider through the same shared compatibility contract.

There is no special AI branch or AI-authored-code acceptance model.

### 7. Representative runtime exercise contract — PASS at harness level

`adf_g_runtime_probe.md` defines one common A1/read-only task for Cursor, Claude Code and Codex:

- determine current ADF state from repository authority;
- resolve `AUTH-034` using accepted-range/exact-occurrence/canonical-owner discipline;
- identify the canonical `run-conformance` workflow;
- report the canonical conformance command;
- make no repository edits;
- stop without beginning ADF-H;
- record unavailable native conveniences as degraded/unverified rather than changing semantics.

The harness is ready; actual provider executions remain outstanding.

### 8. Evidence integrity — PASS

`validate_adf_g_compatibility.py` prevents a provider from being marked `supported` or `degraded` without:

- a passing representative exercise;
- an actual runtime invocation record;
- a runtime verification date;
- substantive observations.

An `unverified` entry must remain `not_run`, have no runtime verification timestamp, and carry an explicit reason. The compatibility manifest must continue to say `runtime_smoke_pending` while evidence remains unverified.

This protects against both false PASS and false global failure.

### 9. ADF-G repository CI — PASS

PR #2 (`Execute ADF-G compatibility and onboarding baseline`) provided inspectable repository-level execution evidence on the ADF-G branch.

Initial validated branch head: `ed8d345f0c6c066d3ffdd61d679501a1af0061b8`.

GitHub Actions results:

- **Agentic conformance #21** — run ID `33696321616`, job `100465844212`: **SUCCESS**;
- **Documentation consistency #139** — run ID `33696321737`: **SUCCESS**.

Agentic conformance #21 reported:

- documentation consistency — PASS;
- OKF structure/resources — PASS, 0 errors / 0 warnings;
- tool adapters — PASS, with the expected 3 provider-runtime-pending warnings;
- portable skills — PASS;
- agentic references — PASS, 30 unique stable IDs checked;
- ADF status drift — PASS using `COMPLETE ADF-A–ADF-F; IN EXECUTION ADF-G`;
- fixture catalog — PASS, **90 scenarios** across ADF-A–ADF-G;
- context budgets — PASS;
- ADF-G compatibility evidence — PASS, **0 errors / 3 expected unverified-runtime warnings**;
- negative controls — PASS, **8 / 8** seeded defects detected;
- generated Agentic Conformance Report — PASS;
- deprecated knowledge entries — 0;
- stale knowledge entries — 0.

The eighth negative control specifically attempts to promote an unverified provider to `supported` without runtime evidence and confirms the ADF-G validator rejects that false promotion.

### 10. Context budgets remain healthy — PASS

Agentic conformance #21 measured:

- root `AGENTS.md`: **9,963 / 16,384 bytes**;
- `.claude/CLAUDE.md`: **1,054 / 2,048 bytes**;
- Cursor rules aggregate: **18,904 / 32,768 bytes**;
- Cursor routing rule: **3,393 / 6,144 bytes**;
- Cursor root baseline: **9,963 / 20,480 bytes**;
- Claude root baseline: **11,017 / 18,432 bytes**;
- Codex root baseline: **9,963 / 16,384 bytes**;
- every canonical skill, Claude bridge and OKF routing artifact remained below its configured budget.

ADF-G therefore did not reintroduce a monolithic persistent prompt in order to obtain cross-tool compatibility.

### 11. Independent compatibility states — PASS

The current runtime ledger records:

- Cursor — `unverified`;
- Claude Code — `unverified`;
- Codex — `unverified`;
- ordinary IDE/CLI — `supported`.

One unverified provider does not poison another provider, ordinary development, agentic configuration conformance, or DMTZ domain health.

### 12. Tool switching model — PASS at repository level

No provider owns branch state, semantic status, acceptance criteria or workflow truth. A developer may switch tools against the same checkout and recover project state from checked-in authority rather than provider memory.

Actual cross-provider runtime execution remains part of the open `ADF-G-XT01` evidence requirement.

### 13. Adding another coding agent — PASS at contract level

A future provider can be added without redesigning DMTZ when it can consume or thinly bridge to:

- root/shared repository authority;
- `knowledge/index.md`;
- canonical `.agents/skills/` workflows;
- repository validation;
- A1–A4 boundaries;
- normal Git/PR process.

It must receive a compatibility-manifest entry and pass the same bounded runtime exercise before being called runtime-supported.

## Remaining acceptance gap

**ADF-EX-17 remains OPEN.**

The planned foundation gate requires the same representative bounded task to be completed through actual Cursor, Claude Code and Codex environments. That runtime evidence does not exist yet because those runtimes were unavailable in the ADF-G execution environment.

To close ADF-G:

1. execute `ADF-G-XT01` from `adf_g_runtime_probe.md` in an actual Cursor runtime;
2. execute the same task in an actual Claude Code runtime;
3. execute the same task in an actual Codex runtime;
4. record tool versions/invocations/observations/results in `runtime_compatibility_evidence.json`;
5. update `tool_compatibility.json` only where actual evidence justifies it;
6. rerun repository conformance;
7. update this review to COMPLETE / ACCEPTED only if all mandatory ADF-G criteria pass.

## Relationship to foundation exit gates

Current ADF-G evidence materially supports:

- **ADF-EX-09 / ADF-EX-10 / ADF-EX-11 / ADF-EX-13:** shared adapter/workflow portability at repository configuration level;
- **ADF-EX-18:** ordinary non-agent developer path — PASS at repository execution level.

Still open:

- **ADF-EX-17:** representative bounded task in actual Cursor / Claude Code / Codex runtimes.

ADF-H and the final foundation exit review must not treat ADF-G as complete until this runtime evidence is present or an explicit narrow waiver intentionally changes the foundation acceptance decision.

## Current conclusion

**ADF-G remains IN EXECUTION / BLOCKED ONLY ON PROVIDER RUNTIME SMOKE EVIDENCE.**

The repository/onboarding/evidence baseline is suitable to merge while preserving that open gate. ADF-H is not automatically started by this review.
