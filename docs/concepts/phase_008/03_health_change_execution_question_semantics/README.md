# Phase 008 Group 03 — Health, Change & Execution Question Semantics

**Status:** Next — not started

## Goal

Refine business questions about health/status, freshness, schema/quality, changes, deployments, executions, versions and timing by mapping each requested conclusion to accepted HLTH/OPS truth without narrative shortcuts.

## Accepted input

Consumes **EXPL-001–EXPL-028**, including stable question proposition identity, source-owner routing, material statement identity, direct-versus-derived classification, statement-relative basis, summary/detail constraints and internal traceability.

## Primary questions

- How should `Did it run?`, `did it succeed?`, `did it produce current output?` and `is it healthy?` remain separate?
- How do freshness, currentness, structural compatibility, statistical comparability, quality dimensions and composite profiles answer business shorthand safely?
- How do `what changed?`, `was it intended?`, `was it deployed?`, and `did reality match intent?` map to Change Intent/Deployment/Change?
- How are actual run-specific input/output/implementation versions communicated without inferring them from active Deployment or latest output?
- How should partial lifecycle/telemetry and historical knowledge cuts constrain these answers?

## Key boundary

`Did it run?`, `is it healthy?`, `is it current?`, `what changed?`, `was the change intended?`, `which version was used?`, and causal `why did it change?` are different propositions with different truth owners/evidence burdens. Causal questions remain bounded by Causal Claim semantics and are refined more deeply in Group 04.
