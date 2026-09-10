# ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract

**Status:** COMPLETE / ACCEPTED

Execution evidence: [`adf_c_execution_review.md`](adf_c_execution_review.md).

## Objective

Give Cursor, Claude Code and Codex equivalent project guidance without maintaining three semantic instruction systems.

## Canonical instruction hierarchy

### Shared repository constitution

Root `AGENTS.md` remains the primary shared behavioral contract for agents and developers. It owns only durable, repository-wide rules:

- project authority and live status locations;
- frozen contract-stack precedence;
- core non-negotiable distinctions;
- implementation/testing/security/change-control discipline;
- reference to the portable knowledge/index layer.

Keep it concise enough to be appropriate as persistent context.

### Tool-specific adapters

Adapters may express native loading/scoping mechanics but must not copy the full shared constitution.

#### Cursor

Retain the existing `.cursor/rules/*.mdc` structure as a scoped reference/guardrail layer. Rules should remain `alwaysApply: false` unless a future measured failure justifies otherwise.

Cursor rules point to `knowledge/index.md`, the active program/group and canonical references; they do not recreate historical phase rulebooks.

#### Claude Code

ADF-C implements `.claude/CLAUDE.md` importing `../AGENTS.md`. Current Claude Code supports `.claude/CLAUDE.md` as a project instruction location and resolves the relative import from that file.

The adapter is deliberately under `.claude/` rather than repository-root `CLAUDE.md` because current Cursor also loads a root `CLAUDE.md` as persistent instructions. This avoids adding duplicate always-on context to Cursor.

Use `.claude/rules/` only when a path-specific Claude behavior is demonstrated and cannot be expressed portably. No Claude rules are required by ADF-C.

Claude auto-memory remains noncanonical; persistent discoveries that matter to the team must be promoted to repository artifacts.

#### Codex

Use root `AGENTS.md` directly as the primary repository instruction surface. No Codex-specific semantic configuration is required by ADF-C.

No Codex-specific file may redefine DMTZ semantics or implementation status.

## Adapter invariants

- shared rule stated once whenever feasible;
- tool adapter contains mechanics, not product truth;
- tool-specific convenience cannot reduce tests/review/change-control obligations;
- tool-specific native memory is noncanonical;
- unsupported native feature causes graceful loss of convenience, not loss of semantic guardrails;
- tool upgrade must not silently change which repository document is authoritative.

## Context budget

Persistent instruction surfaces are intentionally small:

- root `AGENTS.md`: shared universal rules;
- `.claude/CLAUDE.md`: thin import plus Claude-specific mechanics;
- Cursor rules: scoped/relevance-driven;
- `.claude/rules`: none until a demonstrated path-specific need exists;
- detailed procedures remain deferred to ADF-D skills/workflows and canonical docs.

## Tool compatibility manifest

[`tool_compatibility.json`](tool_compatibility.json) records, per supported tool:

- instruction root used;
- scoped-rule mechanism;
- workflow/skill mechanism or deferred status;
- knowledge-index entry point;
- known design/degraded boundaries;
- documentation-verification date;
- runtime-smoke owner.

This manifest is operational compatibility data, not product semantics.

## Delivered artifacts

- `.claude/CLAUDE.md` thin shared-authority bridge;
- reviewed/synchronized Cursor routing over `AGENTS.md` + `knowledge/index.md`;
- Codex compatibility through native root `AGENTS.md` without a semantic fork;
- `tool_compatibility.json` compatibility manifest;
- `tool_adapter_authority_checklist.md` completed repository-adapter audit;
- `fixtures/adf_c_adapter_scenarios.yaml` conformance fixtures;
- `scripts/agentic/validate_agent_adapters.py` deterministic static validator;
- `knowledge/project/tool-compatibility.md` OKF routing concept;
- `external_standards_baseline.md` current tool-mechanics verification.

## Acceptance result

ADF-C passes at the repository-configuration layer because:

- the same repository-wide invariant appears canonically once and is reachable by all three tools;
- Claude consumes shared `AGENTS.md` via import rather than a copied semantic fork;
- Cursor remains scoped/relevance-driven;
- Codex operates from shared `AGENTS.md` plus the portable knowledge plane;
- loss of a native convenience feature does not change DMTZ truth or acceptance criteria;
- contradictory/duplicative adapter states have deterministic static validation seams.

Runtime tool-in-the-loop verification remains explicitly owned by ADF-G. CI enforcement remains owned by ADF-F.
