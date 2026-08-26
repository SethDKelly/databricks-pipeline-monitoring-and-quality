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
- Phase 009 `phase_010_handoff.md`;
- Phase 010 Group 01 ARCH-001–ARCH-032 after Group 01 acceptance.

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

1. Architecture Frame, Environment Discovery & Decision Criteria — **accepted**;
2. Evidence, Provenance, Temporal & Persistence Architecture — **next**;
3. Identity, Scope, Authority, Authorization & Disclosure Architecture;
4. Source Acquisition, Adapter, Synchronization & Integration-Health Architecture;
5. Runtime Provenance, Health, Lineage & Impact Evidence Architecture;
6. Investigation, Reasoning, Historical Replay & Explanation Architecture;
7. Execution Gate, Propagation Safeguard & Active-Control Architecture;
8. Serving, Security, Deployment, Observability & Cost Architecture;
9. Architecture Consolidation, Validation & Phase 010 Exit.

This is a design dependency order, not a mandate for runtime service boundaries.

## Group 01 accepted discipline

ARCH-001–ARCH-032 and AFE01-01–AFE01-60 are accepted.

Later architecture work must preserve:

- `verified_public_vendor_fact` ≠ `target_environment_fact` ≠ organization requirement/policy ≠ architecture assumption ≠ unknown/unverified;
- documented vendor capability ≠ deployment presence ≠ enablement ≠ entitlement ≠ permission ≠ reachability ≠ observable coverage ≠ proposition-specific usability;
- capability identity bound to deployment model/cloud/region/Geo/account/workspace/edition/version/surface where material;
- capability facts as provenance-bearing, revisioned and time-aware;
- unknown deployment facts as unknown rather than guessed support/absence;
- proposition/service-class usability rather than one vendor-wide availability flag;
- optional Collibra/Immuta absence as bounded degradation rather than hidden hard dependency;
- explicit MVP/enterprise capability boundaries;
- architecture hard constraints before optimization;
- decision-specific tradeoffs with no universal architecture score;
- explicit reversibility and assumption/unknown register;
- SC-01 through SC-06 service classes;
- GAP-009-01–GAP-009-40 ownership/treatment.

A public vendor document can justify a public capability statement. It cannot alone justify an architecture assumption that a particular enterprise deployment exposes that capability.

## Group 02 discipline

Group 02 may select concrete evidence/provenance/time/persistence architecture only after evaluating alternatives against ARCH-001–ARCH-032.

It must especially preserve:

- source evidence identity and source ownership after retention/copy;
- proposition/basis identity and common derivation;
- event/effective, availability/knowledge, correction/supersession and communication time separation;
- historical replay without current-state back-projection;
- service-class-specific durability/latency requirements;
- security/disclosure/residency constraints;
- capability-dependent designs that degrade when a required source surface is unavailable;
- decision evidence, alternatives and reversibility.

Group 02 must not choose a database/graph/search/lakehouse pattern by convention or because a vendor feature is documented as generally available.

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

Documented vendor defaults are architecture inputs, not tenant facts. Every later group must distinguish:

- verified public capability/default;
- target-environment discovered fact;
- organization policy/requirement;
- architecture assumption;
- unresolved unknown.

Do not silently promote a public default into a production tenant contract.

When capability is material, bind the exact deployment instance: deployment model, cloud/region/Geo, account/workspace/tenant scope, edition/plan/version/license, feature/release status, enablement, permission, reachability, coverage and current integration health as applicable.

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

Material decisions must follow the accepted ADR rubric rather than relying on familiarity.

## Documentation discipline

- Keep Phase 010 architecture documentation under `docs/concepts/phase_010/` unless another repository authority explicitly owns the artifact.
- Preserve source references and architecture rationale.
- Prefer additive decisions/supersession over silent historical rewrite.
- Update canonical repository phase status only through `docs/README.md`; keep `docs/phase_status.md` synchronized.
- Do not claim `scripts/check_docs_consistency.py` ran unless it actually ran.
- Group exit reviews must state accepted ARCH range, scenario/validation results, unresolved architecture risks, and next-group entry conditions.

## Current state

**Phase 010 is IN PROGRESS. Group 01 is accepted: ARCH-001–ARCH-032; AFE01-01–AFE01-60 pass. Group 02 — Evidence, Provenance, Temporal & Persistence Architecture is next.**
