# ADF-E — Context Discovery, Stable References & Knowledge Maintenance

**Status:** COMPLETE / ACCEPTED

## Objective

Make correct context easy to discover while keeping agent startup context small and preventing knowledge-routing artifacts from drifting away from canonical DMTZ sources.

## Implemented decisions

ADF-E establishes four complementary controls:

1. `context_discovery_policy.md` — shortest-path progressive disclosure and retrieval-failure semantics;
2. `stable_reference_policy.md` + `stable_id_registry.json` — accepted stable-ID ranges and exact-occurrence resolution without first-match canonicality;
3. `context_budget_policy.md` + `context_budget.json` — deterministic UTF-8 byte budgets for persistent/routing/workflow surfaces;
4. `knowledge_maintenance_workflow.md` — changed-source impact review without forcing ceremonial OKF rewrites.

## Default context path

Routine work uses the shortest authoritative path:

```text
human-selected task
  → shared authority/live status
  → explicit path/ID if known; otherwise knowledge/index.md
  → one route/group
  → canonical resource
  → exact stable IDs/tests as required
```

Preloading the entire DMTZ corpus remains explicitly discouraged.

## Stable-reference behavior

Accepted SYN/REF/AUTH/HLTH/OPS/EXPL/INTG/ARCH IDs remain the semantic lookup keys. `scripts/agentic/resolve_stable_id.py` validates accepted ranges and returns every exact occurrence with a mechanical `definition_candidate`/`reference` role.

The helper never equates `definition_candidate` or first search result with canonical authority. The owning accepted document/live repository authority determines meaning.

## Context budgets

ADF-E uses byte limits rather than guessed cross-provider token counts. The current root `AGENTS.md` (12,699 bytes) and Claude bridge (1,054 bytes) are below their configured limits. Detailed skills, OKF concepts, scoped rules, and canonical docs remain on demand.

`scripts/agentic/measure_context_budget.py` provides deterministic measurement; ADF-F owns CI enforcement.

## Knowledge maintenance

Canonical changes may create routing review candidates. They do not automatically make every referencing OKF concept stale. `scripts/agentic/knowledge_impact.py` identifies direct resource references for review while `validate_okf.py` continues to catch broken paths/links.

Knowledge may be corrected from canonical sources; it may never generate semantic changes back into canonical DMTZ authority.

## Workflow integration

`resolve-context` and `resolve-contract` now consume the ADF-E discovery/reference policies and deterministic helper seams. The secondary `agent_reference_index.md` remains a compact human bridge rather than becoming a duplicate semantic registry.

## Validation ownership

ADF-E supplies policies, fixtures, registries, and dependency-free helpers. ADF-F is responsible for executing them as an integrated deterministic conformance/CI suite. ADF-G remains responsible for observed runtime/tool-specific context behavior.

## Exit

Execution evidence and the final decision are recorded in `adf_e_execution_review.md`.
