---
name: resolve-context
description: Resolve the minimum authoritative DMTZ repository context for a human-selected task or group. Use when live status, scope, domain routing, active plans, or governing contracts are unclear. This workflow is read-only and never authorizes repository edits.
---
# Resolve context

## Human-directed boundary

This workflow is **A1 — read/review/plan**. The human-selected task remains the scope anchor; retrieval does not authorize edits or follow-on work.

## Workflow

1. Identify the operative human request, action, exclusions and active group if named.
2. Read root `AGENTS.md` and the live status authority relevant to the task.
3. Apply `docs/agentic_development_foundation/context_discovery_policy.md`.
4. When an exact stable ID is known, bypass unnecessary discovery and run `python3 scripts/agentic/resolve_stable_id.py <ID>`; use the returned current `owner_path::ID` and smallest necessary owner context.
5. Use `--history` only for an explicit provenance/rationale/change question. Historical results cannot change current owner selection.
6. When repository-native location is unknown, traverse `docs/index.md` to the smallest relevant first-class current owner. Use generated `knowledge/index.md` only when an OKF v0.2 compatibility surface is explicitly useful.
7. Read only the active plan/package and current owner context needed for the task.
8. Identify unresolved target-environment facts, missing authority, broken routing or ambiguous scope; do not fill gaps from model/tool memory.
9. Return the minimum context set and stop.

## Context-budget rule

Do not preload generated OKF concepts, workflows, agent rules or SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documents. Loading another file requires a concrete question it answers.

## Output

Report resolved task/action class, relevant live status, current owner locators/files/IDs and why needed, any discovery route used, unresolved assumptions/capability facts, and explicit stop/escalation conditions.

## Stop conditions

Stop rather than guess when live authority cannot be resolved, current owners conflict materially, a required route is broken, a stable ID lacks one deterministic current owner, or the task would require A3/A4 authorization. Do not edit repository files.
