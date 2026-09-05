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
4. When an exact stable ID is known, bypass unnecessary OKF traversal and run `python3 scripts/agentic/resolve_stable_id.py <ID>`; use the returned canonical locator and smallest necessary owner context.
5. Use `--history` only for an explicit provenance/rationale/change question. Historical results cannot change current owner selection.
6. When location is unknown, traverse only one relevant `knowledge/index.md` category/concept, then follow its canonical resource.
7. Read only the active plan/package and canonical context needed for the task.
8. Identify unresolved target-environment facts, missing authority, broken routing or ambiguous scope; do not fill gaps from model/tool memory.
9. Return the minimum context set and stop.

## Context-budget rule

Do not preload all OKF concepts, workflows, agent rules or SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH documents. Loading another file requires a concrete question it answers.

## Output

Report resolved task/action class, relevant live status, canonical locators/files/IDs and why needed, any OKF route used, unresolved assumptions/capability facts, and explicit stop/escalation conditions.

## Stop conditions

Stop rather than guess when live authority cannot be resolved, canonical sources conflict materially, a required route is broken without a current replacement, a stable ID lacks one deterministic canonical owner, or the task would require A3/A4 authorization. Do not edit repository files.
