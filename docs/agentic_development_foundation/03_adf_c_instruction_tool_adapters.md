# ADF-C — Shared Instruction Hierarchy & Tool Adapter Contract

**Status:** PLANNED / READY TO EXECUTE

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

Cursor rules should point to `knowledge/index.md`, the active implementation package and canonical references; they must not recreate historical phase rulebooks.

#### Claude Code

Introduce a small root `CLAUDE.md` that imports or references root `AGENTS.md` using Claude's supported import mechanism, then adds only Claude-specific mechanics.

Use `.claude/rules/` only when path-specific Claude behavior is necessary and cannot be expressed portably. Unscoped Claude rules should be avoided because they consume persistent context.

Do not allow Claude auto-memory to become project authority; persistent discoveries that matter to the team must be promoted to repository artifacts.

#### Codex

Use root `AGENTS.md` directly as the primary repository instruction surface. Add Codex-specific configuration only for capabilities not expressible through shared files.

No Codex-specific file may redefine DMTZ semantics or implementation status.

## Adapter invariants

- shared rule stated once whenever feasible;
- tool adapter contains mechanics, not product truth;
- tool-specific convenience cannot reduce tests/review/change-control obligations;
- tool-specific native memory is noncanonical;
- unsupported native feature causes graceful loss of convenience, not loss of semantic guardrails;
- tool upgrade must not silently change which repository document is authoritative.

## Context budget

Persistent instruction surfaces should be intentionally small.

Targets during ADF execution:

- root `AGENTS.md`: shared universal rules only;
- `CLAUDE.md`: thin import + Claude-specific notes;
- Cursor rules: scoped/relevance-driven;
- `.claude/rules`: path-scoped whenever practical;
- detailed procedures moved to skills or canonical docs rather than persistent prompts.

## Tool compatibility manifest

Create a machine-readable or easily diffable compatibility manifest recording, per supported tool:

- instruction root used;
- scoped-rule mechanism;
- skill/workflow mechanism;
- manual invocation syntax where relevant;
- knowledge-index entry point;
- known unsupported/degraded features;
- version/date last verified.

This manifest is operational compatibility data, not product semantics.

## Deliverables

- minimal `CLAUDE.md` adapter;
- any justified `.claude/rules/` adapters;
- reviewed Cursor rule references to the portable knowledge plane;
- Codex compatibility notes where required;
- compatibility manifest and verification checklist;
- adapter drift tests/checks.

## Acceptance scenarios

ADF-C passes when:

- the same repository-wide invariant appears canonically once and is reachable by all three tools;
- Claude consumes the shared `AGENTS.md` authority rather than a copied semantic fork;
- Cursor continues to load only relevant domain rules;
- Codex can operate from `AGENTS.md` plus shared knowledge/workflows;
- disabling a tool-specific convenience feature does not change DMTZ truth or acceptance criteria;
- an intentionally contradictory adapter rule is caught by review/validation rather than silently becoming effective policy.
