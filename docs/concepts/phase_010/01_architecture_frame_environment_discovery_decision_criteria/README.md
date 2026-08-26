# Phase 010 Group 01 — Architecture Frame, Environment Discovery & Decision Criteria

**Status:** Next — not started

## Goal

Establish the architecture decision frame and target-environment discovery contract before selecting major technologies.

Group 01 answers **what the architecture must optimize for, what environment facts must be discovered, what assumptions may be made, how alternatives will be evaluated, and what remains intentionally undecided**.

It does not yet choose the final persistence, graph, event-bus, orchestration, retrieval/LLM, control, service, or deployment architecture.

## Entry contract

Group 01 consumes:

- Phase 009 final range INTG-001–INTG-270;
- Phase 009 consolidated source capability matrix;
- GAP-009-01–GAP-009-40;
- Phase 009 `phase_010_handoff.md`;
- all durable semantic boundaries from SYN/REF/AUTH/HLTH/OPS/EXPL.

The Phase 009 conclusion that a bounded Databricks/GitHub-centered MVP is feasible is an architecture input, not a preselected topology.

## Primary questions

### A. Target deployment/environment discovery

- Which Databricks cloud/regions/workspaces/metastores/editions are in the initial target environment?
- Which system tables, APIs, Lakeflow features, Unity Catalog capabilities, DQ/metric/profile/anomaly surfaces and preview features are enabled?
- What GitHub plan/authentication model/App installation/audit streaming/Actions usage exists?
- Are Collibra and/or Immuta present, and if so which editions, APIs, history/audit settings, licenses and populations are relevant?
- What IAM/SSO/SCIM/service-principal topology exists?
- What consumer modes matter initially: Databricks SQL, dashboards, external BI, APIs/applications, exports, notifications, files, or others?
- What consequence/incident/business systems are in scope for enterprise extensions?
- What retention, audit, legal/security, regional/data-residency and disclosure constraints are organization requirements rather than vendor defaults?

Environment discovery must preserve `verified public default` ≠ `target-environment fact` ≠ `architecture assumption`.

### B. MVP versus enterprise-extension boundary

- Which GAP-009 items are mandatory for the first architecture and which are explicit enterprise extensions?
- Which organization-owned capabilities are mandatory even for a bounded MVP (for example Monitoring Scope, Assertion Authority, identity/correlation where the product asks those propositions)?
- Which optional Collibra/Immuta capabilities must degrade gracefully when absent?
- Which consumer/consequence/control capabilities are intentionally deferred without weakening core monitoring/RCA semantics?

### C. Architecture quality attributes

Define explicit priorities and tradeoff criteria for at least:

- semantic fidelity / evidence traceability;
- correctness under partial/degraded evidence;
- security, least privilege and disclosure control;
- historical replay/durability;
- availability and graceful degradation;
- latency by use class;
- scalability and source-volume growth;
- operational simplicity;
- reversibility/evolvability;
- testability/observability;
- quota efficiency;
- compute/storage/operational cost;
- portability across Databricks/GitHub environments where intended.

Do not combine these into one universal architecture score. Tradeoffs must remain decision-specific.

### D. Service/use classes

Establish architecture service classes rather than one universal freshness target, at minimum considering:

1. near-current operational facts;
2. periodic/core health and quality evaluation;
3. enriched investigation/RCA reasoning;
4. historical/as-known replay;
5. retained communication / basis inspection;
6. active control path if/when Gate or Safeguard is enabled.

Each class should define the kind of source latency, completeness and retention needed; Group 01 need not yet choose implementation mechanisms.

### E. Architecture decision discipline

Define the ADR/architecture-contract process for later groups:

- what evidence is required before selecting a technology;
- which alternatives must be evaluated;
- how decisions trace to ARCH/INTG/GAP requirements;
- how assumptions and target-environment facts are recorded;
- how reversible versus hard-to-reverse decisions are treated;
- how supersession/rollback of architecture decisions is recorded;
- what qualifies a decision for acceptance.

### F. Integration capability inventory model

Define what the architecture needs to know about every enabled source surface:

- exact product/source/version/edition;
- region/account/workspace scope;
- authentication/authorization requirements;
- proposition/evidence roles supported;
- source authority applicability;
- identity/join keys;
- time semantics and publication lag;
- retention;
- positive/negative coverage;
- pagination/query limits;
- quota/rate state;
- cost surface;
- preview/deprecation status;
- schema/API version;
- integration-health state;
- optional/required status.

Group 01 defines the required capability metadata shape, not necessarily its final storage schema.

### G. Architecture-wide nonfunctional constraints

Establish constraints that later groups must obey, including:

- no source failure may become domain absence;
- all strong-negative-capable paths require coverage/integration-health awareness;
- retained evidence preserves source provenance/common derivation;
- current state is not sufficient for historical replay where a historical proposition is promised;
- sensitive basis/provenance can require separate authorization from conclusion visibility;
- active control paths must fail observably and preserve exact enforcement evidence rather than inventing fail-open/fail-closed conclusions;
- architecture must support partial answers instead of all-or-nothing source dependency where semantics allow;
- optional sources cannot become hidden hard dependencies.

## Phase 009 residual gaps primarily owned or framed here

Group 01 should classify ownership/priority for every GAP-009 item, with particular direct responsibility for:

- GAP-009-32 — source-latency/availability SLO framing;
- GAP-009-36 — Collibra environment discovery;
- GAP-009-37 — Immuta environment discovery;
- GAP-009-38 — cost-attribution requirements;
- GAP-009-39 — graceful-degradation policy;
- GAP-009-40 — enterprise deployment-specific capability inventory.

GAP-009-01–GAP-009-35 remain later-group architecture problems but Group 01 must establish their MVP/enterprise priority and acceptance ownership.

## Explicit non-goals

Group 01 does **not** yet select:

- database/lakehouse/graph/search/object-store products;
- an event bus/queue;
- polling/streaming implementation;
- a canonical event/provenance schema;
- an orchestration engine;
- an LLM/provider/model/retrieval/embedding stack;
- a redaction/policy engine;
- a Gate or Safeguard engine;
- final API/service decomposition;
- container/Kubernetes/serverless topology;
- observability vendor;
- exact cost-control implementation.

Those decisions require the decision criteria and environment facts produced here.

## Expected Group 01 artifacts

At minimum, Group 01 should produce:

- accepted ARCH contracts for the architecture frame;
- target-environment discovery checklist/profile;
- MVP versus enterprise-extension capability boundary;
- architecture quality-attribute/tradeoff matrix;
- service/use-class matrix;
- technology/ADR decision rubric;
- cross-group gap ownership matrix for GAP-009-01–GAP-009-40;
- architecture-wide nonfunctional constraints;
- scenario/decision-quality review;
- Group 01 decision record and Group 02 handoff.

## Acceptance gate

Group 01 exits only if:

- later groups can evaluate technologies against an explicit decision rubric;
- target-environment unknowns are clearly separated from verified defaults and architecture assumptions;
- every GAP-009 item has a Phase 010 owner/priority/treatment path;
- MVP versus enterprise-extension scope is explicit enough to constrain architecture;
- service classes are explicit enough to prevent one universal latency/retention target;
- architecture-wide failure/degradation/security/history constraints are explicit;
- no major technology has been selected merely by convention;
- the group introduces no semantic shortcut prohibited by Phases 002–009.

## Handoff

After Group 01 acceptance, Group 02 may select the durable **Evidence, Provenance, Temporal & Persistence Architecture** using the criteria and environment facts established here.
