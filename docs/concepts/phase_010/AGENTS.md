# Phase 010 AGENTS.md — Technical Architecture Discipline

## Scope

This directory owns Phase 010 technical architecture. It may select concrete architecture only where the accepted Phase 002–009 contracts and verified environment facts justify the choice.

## Mandatory incoming authorities

Before accepting an `ARCH-###` contract, preserve and consult:

- Phase 003 SYN-001–SYN-035;
- Phase 004 REF-001–REF-030;
- Phase 005 AUTH-001–AUTH-053;
- Phase 006 HLTH-001–HLTH-066;
- Phase 007 OPS-001–OPS-123;
- Phase 008 EXPL-001–EXPL-160;
- Phase 009 INTG-001–INTG-270;
- Phase 009 Group 08 consolidated capability matrix;
- Phase 009 residual gap register GAP-009-01–GAP-009-40;
- Phase 009 `phase_010_handoff.md`.

Earlier functional/integration semantics remain authoritative. Architecture may realize them; it may not simplify them away.

## Namespace

Use **ARCH-###** for durable technical architecture contracts.

An ARCH contract should state at least:

1. architecture proposition/decision;
2. accepted semantic requirements it realizes;
3. environment/source assumptions;
4. alternatives considered where material;
5. consequences/tradeoffs;
6. failure/degradation behavior;
7. historical/security/disclosure implications where applicable;
8. verification/acceptance evidence;
9. residual gaps or later-group dependencies.

Do not use ARCH contracts to redefine a product concept, source fact, authority rule, evidence threshold, health proposition, causal status, Impact layer, or Explanation semantic.

## Review sequence

Review Phase 010 in this order:

1. Architecture Frame, Environment Discovery & Decision Criteria;
2. Evidence, Provenance, Temporal & Persistence Architecture;
3. Identity, Scope, Authority, Authorization & Disclosure Architecture;
4. Source Acquisition, Adapter, Synchronization & Integration-Health Architecture;
5. Runtime Provenance, Health, Lineage & Impact Evidence Architecture;
6. Investigation, Reasoning, Historical Replay & Explanation Architecture;
7. Execution Gate, Propagation Safeguard & Active-Control Architecture;
8. Serving, Security, Deployment, Observability & Cost Architecture;
9. Architecture Consolidation, Validation & Phase 010 Exit.

This is a design dependency order, not a mandate for runtime service boundaries.

## Group 01 discipline

Group 01 must establish the decision frame before selecting major technologies.

It must define:

- deployment/environment discovery requirements;
- MVP and enterprise-extension boundary assumptions;
- architecture quality attributes and explicit tradeoff criteria;
- service/use classes for latency and replay;
- architecture decision record discipline;
- technology-selection evidence requirements;
- capability inventory and unsupported/unknown handling;
- cost/quota/retention assumptions that require environment confirmation;
- architecture-wide nonfunctional constraints;
- unresolved architecture questions that later groups own.

Group 01 must **not** select final persistence, graph, event-bus, orchestration, LLM/retrieval, policy-engine, Gate/Safeguard, service, or deployment technologies merely to create momentum.

## Cross-group invariants

Preserve all accepted durable boundaries, especially:

- source availability ≠ Assertion Authority;
- Entity Identity ≠ source-local name equality;
- current state ≠ historical state;
- copied/retained evidence ≠ independent/newly authoritative evidence;
- missing/degraded integration telemetry ≠ source/domain negative truth;
- Baseline ≠ Expectation ≠ Observation ≠ Assessment;
- Lineage ≠ exposure ≠ effect ≠ consequence ≠ causality;
- Investigation/localization ≠ Causal Claim truth;
- readiness ≠ Gate decision ≠ enforcement ≠ execution;
- Execution Gate ≠ Propagation Safeguard;
- Safeguard enforcement ≠ REF-028 prevention;
- reconstructed historical Explanation ≠ authentic retained communication;
- internal basis traceability ≠ universal visible raw evidence;
- current authorization ≠ historical authorization;
- cost/quota optimization ≠ relaxed evidence burden;
- optional source absence ≠ benign default;
- architecture convenience ≠ semantic permission.

## Environment facts

Documented vendor defaults are architecture inputs, not tenant facts. Group 01 and Group 04 must distinguish:

- verified public capability/default;
- target-environment discovered fact;
- organization policy/requirement;
- architecture assumption;
- unresolved unknown.

Do not silently promote a public default into a production tenant contract.

## Decision quality

Prefer architecture decisions that are:

- traceable to accepted contracts/gaps;
- reversible where uncertainty remains high;
- explicit about capability loss and graceful degradation;
- observable in operation;
- secure by least privilege and disclosure-aware design;
- cost/quota aware without weakening truth/evidence semantics;
- testable through scenario replay;
- modular enough that optional Collibra/Immuta integration does not become a universal core dependency.

## Documentation discipline

- Keep Phase 010 architecture documentation under `docs/concepts/phase_010/` unless another repository authority explicitly owns the artifact.
- Preserve source references and architecture rationale.
- Prefer additive decisions/supersession over silent historical rewrite.
- Update canonical repository phase status only through `docs/README.md`; keep `docs/phase_status.md` synchronized.
- Do not claim `scripts/check_docs_consistency.py` ran unless it actually ran.
- Group exit reviews must state accepted ARCH range, scenario/validation results, unresolved architecture risks, and next-group entry conditions.

## Current state

**Phase 010 is IN PROGRESS. Group 01 — Architecture Frame, Environment Discovery & Decision Criteria is next. No ARCH contracts are accepted yet.**
