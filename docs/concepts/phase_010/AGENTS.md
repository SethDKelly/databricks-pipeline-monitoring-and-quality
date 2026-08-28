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
- Phase 010 Group 01 ARCH-001–ARCH-032;
- Phase 010 Group 02 ARCH-033–ARCH-080;
- Phase 010 Group 03 ARCH-081–ARCH-132;
- Phase 010 Group 04 ARCH-133–ARCH-190.

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
2. Evidence, Provenance, Temporal & Persistence Architecture — **accepted**;
3. Identity, Scope, Authority, Authorization & Disclosure Architecture — **accepted**;
4. Source Acquisition, Adapter, Synchronization & Integration-Health Architecture — **accepted**;
5. Runtime Provenance, Health, Lineage & Impact Evidence Architecture — **next**;
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

## Group 02 accepted discipline

ARCH-033–ARCH-080 and EPT02-01–EPT02-72 are accepted.

Later architecture work must preserve:

- framework-owned Delta Lake canonical structured evidence/provenance journals;
- Unity Catalog managed tables/volumes as preferred conditional deployment realizations, not universal requirements;
- external Delta/governed object storage as valid portability realization;
- selective data-minimized payload capture rather than wholesale raw copying;
- durable framework evidence IDs independent of source-local IDs/physical paths;
- source authority/limitations after retention/copy;
- proposition/basis and common-derivation links;
- event/effective, availability/knowledge, collection/persistence, correction/supersession and communication time separation;
- late evidence excluded from earlier K;
- append/supersede/correct semantic history despite physical file optimization;
- parser/normalizer revision provenance;
- Delta transaction-log time travel not being the product replay contract;
- graph/search/vector/serving stores as derived/rebuildable;
- storage retention, retained detail/resolution and reporting relevance as separate dimensions;
- lifecycle states for recent, warm, summary-eligible, cold/pinned, provenance-stub and expired material;
- configurable reference retention rather than a universal TTL;
- dependency pinning/holds and exact-basis non-lossy retention;
- safe trend aggregation only when future exact-evidence promises permit it;
- archive/restore/purge provenance and cost observability;
- security/residency sharding without unauthorized duplication.

Do not solve performance/cost by silently making retained evidence less exact than the product promise or by allowing old retained history to flood every report.

## Group 03 accepted discipline

ARCH-081–ARCH-132 and IAD03-01–IAD03-84 are accepted.

Later architecture work must preserve:

- tenant-scoped canonical Entity and Principal identities distinct from vendor-local identities;
- source identity bindings as evidence-bearing, revisioned and conflict-capable;
- rename continuity distinct from delete/recreate/incarnation;
- human, group, service-principal, application/workload and acting-on-behalf-of relationships kept distinct;
- current group/role membership not projected backward as historical membership;
- upstream IdP provenance retained where known without making synchronized vendor state silently authoritative;
- organization-owned Monitoring Scope rather than inference from discoverability/access;
- scope selectors and materializations retaining revision, input coverage, explicit exclusions and unresolved membership;
- unknown scope membership not converted into exclusion or a smaller negative-claim denominator;
- Monitoring Scope independent from Capability Authorization;
- Assertion Authority as structured, versioned policy-as-data with exact facet/proposition/subject/context/time targets;
- authority precedence, co-authority and fallback as explicit rule data rather than hidden engine ordering;
- co-authoritative conflict retained until an authorized resolver applies;
- vendor role/title/ownership/responsibility/permission as source evidence, never automatic DMTZ Assertion Authority;
- causal confirmation authority eligibility distinct from REF-017 evidence sufficiency and AUTH-034 confirmation;
- Capability Authorization as exact principal/action/subject/context/time/detail state;
- granular action vocabulary rather than one generic `access` Boolean;
- `allowed`, `denied`, `conditional`, `unknown`, `conflicting` and `unavailable` preserved;
- membership/inheritance composition explicit and source/rule scoped;
- no universal deny-wins, allow-wins, direct-user-wins, role-wins or latest-wins authorization rule;
- actual authorization-decision record distinct from replay-derived historical evaluation;
- authorization distinct from request, enforcement, action occurrence and outcome;
- service-principal/internal processing authorization distinct from requester visibility;
- least-privilege workload identity as source-acquisition posture where supported;
- delegation/break-glass bounded, expiring/revocable and auditable;
- disclosure bound to requester/audience/purpose/delivery/onward-use context;
- conclusion, material context, limitation, basis identity, provenance, exact detail and export/publish independently authorizable;
- exact/coarse/redacted/opaque/withheld projections as detail states, not epistemic-strength states;
- safe abstraction epistemically monotone: no strengthening, scope broadening, subject merging or material-limitation erasure;
- `inspectBasis` itemwise while internal statement-to-basis traceability remains complete;
- hidden basis existence/count/type/source/path/timestamp/provenance/redaction metadata potentially sensitive;
- mosaic/differencing/repeated-query leakage considered by disclosure policy;
- retained/cold/archived/provenance-stub material not automatically disclosable;
- current authorization distinct from historical authorization and prior visibility;
- tenant/residency boundaries limiting governance metadata/evidence movement;
- canonical identity/policy state in Group 02 structured persistence with caches/indexes as derived/rebuildable projections.

Group 03 selects the canonical record/rule semantics but no external policy engine, IAM/IdP product, policy authoring UI/API/Git workflow, secrets implementation or runtime service topology.

## Group 04 accepted discipline

ARCH-133–ARCH-190 and AHI04-01–AHI04-96 are accepted.

Later architecture work must preserve:

- adapters as acquisition mechanisms, never independent owners of canonical identity/scope/authority/domain truth;
- exact capability-instance + source-surface + acquisition-plan revision binding;
- reconciliation-first hybrid collection, with incremental/stream/webhook/export/on-demand paths as source-specific accelerators;
- durable acquisition run/attempt identity;
- checkpoint/cursor/window/page/partition provenance tied to the exact query/surface;
- overlap for ambiguous ordering/late publication with idempotent deduplication;
- pagination/partition completion explicitly evidenced rather than inferred from successful HTTP response;
- expected population from Monitoring Scope/materialization, not whatever the connector can currently list;
- source request IDs and safe request/response provenance where available;
- source envelope/raw capture separated from normalized evidence and governed by minimization;
- normalized evidence bound to parser/normalizer revision and acquisition provenance;
- API/webhook/stream/export representations of one event marked common-derived rather than independent corroboration;
- additive schema evolution tolerated; breaking drift and unsupported fields explicit;
- malformed/unsupported payloads quarantined where their omission can affect coverage;
- partial collection allowed to preserve usable evidence without claiming complete coverage;
- evidence publication only after required provenance is durably persisted;
- checkpoint advancement only after corresponding evidence/provenance commit;
- retry behavior based on error taxonomy, idempotency and vendor guidance;
- authentication, permission and observer-relative not-found distinct from source/domain absence;
- 429/quota state, Retry-After/reset handling and bounded backoff;
- source-selective queries/partitioning/conditional requests used to conserve quota without hiding omitted coverage;
- source publication lag separated from event time and observed acquisition/persistence lag;
- acquisition scheduling bound to SC-01–SC-06 rather than one universal frequency;
- multidimensional integration health across presence/authn/authz/reachability/quota/publication/checkpoint/pagination/schema/parser/persistence/coverage/freshness/retention;
- no universal integration-health score;
- collection coverage manifest required for strong-negative support;
- source retention expiry distinguished from product-retained evidence;
- optional-source absence treated as proposition-bound degradation;
- acquisition request/query/compute/transfer volume and cost-relevant telemetry attributable where measurable;
- current integration recovery non-rewriting with respect to historical evidence gaps.

Group 04 selects no universal event bus, queue product, orchestration engine, worker runtime, secret store, observability vendor, API gateway or deployment topology.

## Group 05 discipline

Group 05 must design runtime provenance, health, Lineage and Impact evidence over ARCH-001–ARCH-190.

It must not:

- infer exact deployment/run/input/output identity from names or timestamp proximity;
- infer run-specific implementation state from current Deployment alone;
- infer consumed input version from latest/current source state;
- infer output existence/health/currentness from run success alone;
- treat a connector gap as no run/output/measurement/dependency/encounter/exposure/effect;
- use Lineage reachability as encounter/exposure/Impact/cause;
- ignore source acquisition coverage when issuing strong operational/Impact negatives;
- turn health measurement availability into normative authority;
- collapse source publication time, run time, measurement time and knowledge time.

## Cross-group invariants

Preserve all accepted durable boundaries, especially:

- source availability ≠ Assertion Authority;
- Entity Identity ≠ source-local name equality;
- Monitoring Scope ≠ accessibility ≠ authorization;
- current state ≠ historical state;
- copied/retained evidence ≠ independent/newly authoritative evidence;
- missing/degraded integration telemetry ≠ source/domain negative truth;
- checkpoint progress ≠ source completeness/domain truth;
- HTTP/request success ≠ page/population/window completeness;
- webhook/stream silence ≠ no event;
- integration recovery ≠ historical gap erasure;
- storage retention ≠ reporting relevance;
- retained/archived evidence ≠ disclosure permission;
- payload expired ≠ source absent;
- graph/search/cache projection ≠ canonical truth;
- current authorization ≠ historical authorization;
- actual authorization decision ≠ replay-derived authorization ≠ enforcement/action;
- service processing authorization ≠ requester visibility;
- Assertion Authority ≠ evidence sufficiency ≠ Capability Authorization;
- Baseline ≠ Expectation ≠ Observation ≠ Assessment;
- Lineage ≠ exposure ≠ effect ≠ consequence ≠ causality;
- Investigation/localization ≠ Causal Claim truth;
- readiness ≠ Gate decision ≠ enforcement ≠ execution;
- Execution Gate ≠ Propagation Safeguard;
- Safeguard enforcement ≠ REF-028 prevention;
- reconstructed historical Explanation ≠ authentic retained communication;
- internal basis traceability ≠ universal visible raw evidence;
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

When capability is material, bind exact deployment model/cloud/region/Geo/account/workspace/tenant/edition/plan/version/license/release/enablement/permission/reachability/coverage/health dimensions as applicable.

## Decision quality

Prefer architecture decisions that are:

- traceable to accepted contracts/gaps;
- reversible where uncertainty remains high;
- explicit about capability loss and graceful degradation;
- observable in operation;
- secure by least privilege and disclosure-aware design;
- cost/quota aware without weakening truth/evidence semantics;
- testable through scenario replay;
- modular enough that optional integrations/derived stores do not become hidden canonical dependencies.

Material decisions must follow the accepted ADR rubric rather than relying on familiarity.

## Documentation discipline

- Keep Phase 010 architecture documentation under `docs/concepts/phase_010/` unless another repository authority explicitly owns the artifact.
- Preserve source references and architecture rationale.
- Prefer additive decisions/supersession over silent historical rewrite.
- Update canonical repository phase status only through `docs/README.md`; keep `docs/phase_status.md` synchronized.
- Do not claim `scripts/check_docs_consistency.py` ran unless it actually ran.
- Group exit reviews must state accepted ARCH range, scenario/validation results, unresolved architecture risks, and next-group entry conditions.

## Current state

**Phase 010 is IN PROGRESS. Groups 01–04 are accepted: ARCH-001–ARCH-190; AFE01-01–AFE01-60, EPT02-01–EPT02-72, IAD03-01–IAD03-84 and AHI04-01–AHI04-96 pass. Group 05 — Runtime Provenance, Health, Lineage & Impact Evidence Architecture is next.**
