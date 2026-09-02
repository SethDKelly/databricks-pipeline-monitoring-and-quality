---
name: resolve-context
description: Resolve the minimum authoritative DMTZ repository context for a human-selected task or group. Use when live status, scope, domain routing, active plans, or governing contracts are unclear. This workflow is read-only and never authorizes repository edits.
---
# Resolve context

## Human-directed boundary

This workflow is **A1 — read/review/plan** under `docs/agentic_development_foundation/authority_scope_policy.md`.

The human-selected task is the scope anchor. Resolving context does not authorize edits, follow-on work, external actions, or architecture changes.

## Workflow

1. Identify the operative human request, requested action, explicit exclusions, and active ADF/implementation group if named.
2. Read root `AGENTS.md` and the live status authority relevant to the task. Do not infer current status from memory or historical phase documents.
3. Follow `docs/agentic_development_foundation/context_discovery_policy.md`: use an explicit path/group/ID directly when known; otherwise use `knowledge/index.md` and traverse one category/concept at a time.
4. Read the active group/package plan and only the domain-routing entries needed for the task.
5. When a stable contract/scenario ID is known or becomes material, resolve the exact token under `docs/`. `scripts/agentic/resolve_stable_id.py` is the deterministic helper when a local checkout is available; its definition-candidate label is not canonicality.
6. Read only the smallest surrounding canonical context needed to apply the relevant definitions, conditions, exceptions, and relationships.
7. Identify unresolved target-environment facts, missing authority, broken/deprecated routing, or ambiguous scope. Do not fill gaps from model/tool memory.
8. Return the minimum context set needed for the task and stop.

## Context-budget rule

Do not preload all OKF concepts, all seven workflows, all Cursor rules, or all SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documents. Loading another file requires a concrete question it answers.

`docs/agentic_development_foundation/context_budget_policy.md` defines deterministic repository byte budgets for persistent/routing surfaces.

## Output

Report:

- resolved task/action class;
- live ADF/implementation status relevant to the task;
- canonical files/contract IDs to use and why each is needed;
- any knowledge-routing entries used;
- unresolved assumptions or capability facts;
- explicit stop/escalation conditions.

## Stop conditions

Stop and report instead of guessing when:

- live authority cannot be resolved;
- canonical sources conflict materially;
- a required resource is missing/stale/deprecated without a current replacement;
- a stable ID cannot be resolved or only ambiguous candidates remain where exact ownership matters;
- the task would require A3 external/destructive/scope expansion or A4 semantic/architecture change.

Do not edit repository files in this workflow.