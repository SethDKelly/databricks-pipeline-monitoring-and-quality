# ADF-C — Execution Review

**Status:** ACCEPTED — ADF-C COMPLETE

## Review question

Has ADF-C implemented a shared instruction hierarchy and thin native adapters so Cursor, Claude Code and Codex reach the same DMTZ authority/knowledge model without maintaining separate semantic rulebooks?

**Conclusion: yes, at the repository-configuration layer.**

ADF-C verifies documented native mechanisms and repository adapter topology. It does not claim that a particular installed Cursor/Claude/Codex binary has executed a live smoke task; ADF-G owns that runtime verification.

## Delivered artifacts

- `.claude/CLAUDE.md` — thin Claude Code bridge importing `../AGENTS.md`.
- root `AGENTS.md` — synchronized shared constitution and tool-adapter discipline.
- `.cursor/rules/00-implementation-routing.mdc` — synchronized Cursor router using shared authority and `knowledge/index.md`.
- `docs/agentic_development_foundation/tool_compatibility.json` — machine-readable compatibility manifest.
- `docs/agentic_development_foundation/tool_adapter_authority_checklist.md` — completed adapter authority audit.
- `docs/agentic_development_foundation/fixtures/adf_c_adapter_scenarios.yaml` — reusable adapter conformance scenarios.
- `scripts/agentic/validate_agent_adapters.py` — dependency-free static adapter validator.
- `knowledge/project/tool-compatibility.md` — OKF routing concept for operational compatibility.
- `external_standards_baseline.md` — current native instruction-mechanism baseline.

## Findings

### 1. Shared instruction authority — PASS

Root `AGENTS.md` remains the only shared repository behavioral constitution.

All tool-specific mechanics are lower-precedence adapters. No tool-specific file owns DMTZ product semantics, live implementation status, the A1–A4 action model, or validation/change-control obligations.

### 2. Cursor adapter — PASS

Cursor continues to use:

- root `AGENTS.md` for shared instructions;
- `.cursor/rules/*.mdc` for scoped/relevance-driven domain mechanics;
- `knowledge/index.md` for portable discovery.

No new universal Cursor rule was introduced. Repository search during ADF-C found no `alwaysApply: true` project rule.

The routing rule now records ADF-A/B/C complete and routes later work through the shared compatibility model.

### 3. Claude Code adapter — PASS

Current Claude Code documentation was reverified to support project instructions at either root `CLAUDE.md` or `.claude/CLAUDE.md`, plus `@path` imports resolved relative to the containing file.

ADF-C deliberately uses:

`.claude/CLAUDE.md` → `@../AGENTS.md`

rather than copying shared rules.

Repository readback confirmed the committed adapter imports `../AGENTS.md` and contains only Claude-specific mechanics: portable knowledge discovery, memory non-authority, workflow ownership in ADF-D, and the current no-delegation boundary.

### 4. Root CLAUDE.md avoidance — PASS

Current Cursor documentation states that Cursor also reads a root `CLAUDE.md` as persistent project instructions.

Using `.claude/CLAUDE.md` avoids creating a second always-on Cursor instruction surface while remaining a supported Claude Code project-instruction location.

Repository readback confirmed root `CLAUDE.md` is absent.

This is a context-efficiency/tool-compatibility decision only; it does not change DMTZ semantic authority.

### 5. Codex adapter — PASS

Current Codex/OpenAI guidance confirms `AGENTS.md` as the native repository instruction mechanism.

ADF-C therefore adds no `CODEX.md` or repository-local `.codex/AGENTS.md` semantic rulebook. Repository readback confirmed both are absent. Codex consumes the same root `AGENTS.md`, portable `knowledge/index.md`, canonical docs, and repository validation as other developers/tools.

### 6. Compatibility manifest — PASS

`tool_compatibility.json` records for Cursor, Claude Code and Codex:

- shared instruction surfaces;
- scoped-rule mechanisms;
- portable knowledge entry;
- workflow/skill ownership/deferred status;
- verification owner;
- known compatibility notes.

All tools are intentionally marked `documentation_verified_runtime_smoke_pending`.

This prevents documentation verification from being mislabeled as runtime certification.

### 7. Adapter-context minimization — PASS

ADF-C does not create `.claude/rules/` merely for symmetry, does not create a Codex-specific instruction copy, and does not expand every Cursor rule with repeated shared policy text.

Detailed repeated procedures remain correctly deferred to the portable ADF-D workflow/skill layer.

### 8. Deterministic static validation seam — PASS

`scripts/agentic/validate_agent_adapters.py` is designed to reject:

- missing shared authority/knowledge artifacts;
- repository-root `CLAUDE.md` duplication;
- a Claude adapter that does not import `../AGENTS.md`;
- an oversized Claude adapter;
- Cursor rules with `alwaysApply: true`;
- Cursor rules beyond the focused-rule budget;
- missing shared references from Cursor routing;
- competing `CODEX.md` or `.codex/AGENTS.md` semantic adapters;
- missing/invalid manifest authority/tool entries.

Repository-static readback during ADF-C verified the high-risk topology checks directly: root `CLAUDE.md` absent, `.claude/CLAUDE.md` present with the shared import, no `alwaysApply: true` search result, and no competing Codex semantic file.

The validator is committed but is not yet represented as a required CI gate; ADF-F owns execution/integration and richer automated fixture coverage. It emits warnings—not false failures—for runtime smoke checks that remain pending ADF-G.

### 9. Human-directed boundary — PASS

Native tool capabilities such as Claude subagents/teams or other agent delegation features do not authorize repository implementation delegation.

All supported tools continue to inherit ADF-A A1–A4 scope. Tool capability is not repository permission.

### 10. Tool neutrality — PASS

Repository acceptance remains based on artifacts, executable validation, traceability, security/change-control compliance and review—not which tool/model generated the change.

No supported tool is semantically privileged.

## External documentation evidence

ADF-C reverified on 2026-09-02 that:

- Cursor supports root/nested `AGENTS.md`, scoped `.cursor/rules/*.mdc`, and root `CLAUDE.md` compatibility loading;
- Claude Code supports `.claude/CLAUDE.md`, `@path` imports, path-scoped rules and on-demand skills;
- Codex uses repository `AGENTS.md` and benefits from a map-to-structured-knowledge pattern rather than monolithic persistent instructions.

These are compatibility facts recorded in `external_standards_baseline.md`; they are not DMTZ product contracts.

## Relationship to foundation exit gates

ADF-C establishes repository-configuration evidence for:

- **ADF-EX-01** — common shared authority topology;
- **ADF-EX-03** — adapters cannot legitimately supersede DMTZ semantic/change-control authority;
- **ADF-EX-08** — Cursor adapter structure is ready for runtime verification;
- **ADF-EX-09** — Claude Code consumes shared authority through a thin import adapter;
- **ADF-EX-10** — Codex uses shared `AGENTS.md`/knowledge without a separate rulebook.

Whole-foundation gates remain open until ADF-F/G execute deterministic/runtime verification.

## Residual obligations

- **ADF-D:** realize portable human-directed workflows/skills without duplicating adapter semantics.
- **ADF-E:** refine context discovery, stable references, and knowledge-maintenance behavior over the implemented adapters/OKF plane.
- **ADF-F:** execute/integrate adapter and OKF validators/fixtures in deterministic CI/conformance.
- **ADF-G:** execute representative bounded tasks in Cursor, Claude Code and Codex and record actual runtime/degraded states.
- **ADF-H:** define the long-term compatibility review horizon and lifecycle governance.

## Exit decision

**ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract: COMPLETE / ACCEPTED.**

The next eligible groups are **ADF-D — Portable Skills & Human-Directed Workflow Contract** and **ADF-E — Context Discovery, Stable References & Knowledge Maintenance**. They may proceed according to the accepted dependency model.
