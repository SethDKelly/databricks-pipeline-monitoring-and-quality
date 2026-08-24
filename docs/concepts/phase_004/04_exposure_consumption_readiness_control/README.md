# Phase 004 Group 04 — Exposure, Consumption, Readiness & Control Evidence

**Status:** Next review group — not yet started

## Goal

Specialize REF-001–REF-020 for evidence that proves or fails to prove downstream exposure, non-exposure, upstream readiness, gate decision/enforcement, safeguard enforcement/prevented exposure, and degraded/unavailable control integration.

## Accepted handoff from Groups 01–03

- evidence sufficiency is conclusion-relative;
- applicability, bounded coverage, corroboration/conflict, and sufficiency remain separate;
- negative/non-occurrence claims require opportunity-to-observe and sufficient coverage;
- source availability, framework knowledge, and evaluation time remain distinct;
- progressive results are allowed, but a fast narrow result cannot be promoted into broader health/control/causal truth;
- late/corrected evidence may change retrospective interpretation without rewriting historical control actions;
- causal status uses `proposed`, `supported`, `weakened`, `unresolved`, `rejected`, and `confirmed`;
- causal confirmation is a separate profile/authority-gated status;
- direct control-mechanism evidence can support strong causal reasoning quickly when the applicable standard is satisfied;
- multiple contributors remain valid and no single root cause is required.

## Planned questions

- What evidence is sufficient to establish that a report, Metric View, pipeline, application, or business process actually consumed/encountered a specific affected state/version/window?
- What bounded refresh/version/consumption coverage is required for `not exposed`?
- How should the framework distinguish `consumer did not refresh`, `consumer refreshed an earlier safe version`, `consumer refresh unknown`, and `consumer inaccessible/restricted`?
- What evidence establishes that an upstream prerequisite was `ready` for a specific Execution Gate criterion?
- How should `upstream job succeeded`, `qualifying output exists`, `output is current`, `output is fresh`, and `required version is available` remain separate readiness propositions?
- What proves an external gate decision was actually enforced as a hold or admission rather than merely requested/recorded?
- What proves a Propagation Safeguard was actually active/enforced at the intended boundary?
- What evidence is required to claim `prevented exposure` rather than merely `safeguard active`?
- How should unknown/unavailable/degraded gate or safeguard telemetry be represented without inventing fail-open/fail-closed behavior?
- When can direct gate/safeguard enforcement evidence support causal claims that the control action contributed to delay/non-delivery?
- How should late enforcement/consumption evidence alter retrospective exposure/readiness interpretation while preserving the historical action?

## Non-goals

- choosing Databricks Workflows/external-orchestration implementation;
- selecting quarantine/control-plane technology;
- defining all gate timeout/fallback/override policies (later Phase 007/005 as appropriate);
- source-authority precedence (Phase 005);
- final health metric definitions (Phase 006);
- technical architecture (Phase 010).
