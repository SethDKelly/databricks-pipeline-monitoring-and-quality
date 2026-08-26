# Phase 010 Grouping & Architecture-Phase Entry Decisions

### D-1263 — Phase 010 is organized as nine dependency-ordered architecture groups
**Status:** Accepted — Phase 010 foundation

Phase 010 is reviewed as: (1) Architecture Frame, Environment Discovery & Decision Criteria; (2) Evidence, Provenance, Temporal & Persistence Architecture; (3) Identity, Scope, Authority, Authorization & Disclosure Architecture; (4) Source Acquisition, Adapter, Synchronization & Integration-Health Architecture; (5) Runtime Provenance, Health, Lineage & Impact Evidence Architecture; (6) Investigation, Reasoning, Historical Replay & Explanation Architecture; (7) Execution Gate, Propagation Safeguard & Active-Control Architecture; (8) Serving, Security, Deployment, Observability & Cost Architecture; and (9) Architecture Consolidation, Validation & Phase 010 Exit.

The order is a design/review dependency, not a required runtime service decomposition or deployment sequence.

### D-1264 — ARCH-### is the Phase 010 durable technical-architecture contract namespace
**Status:** Accepted — Phase 010 foundation

`ARCH-###` records durable technical architecture constraints/decisions needed to realize accepted Phase 002–009 semantics. ARCH contracts may not redefine source facts, product concepts, authority, evidence sufficiency, health semantics, causality, Impact, control semantics, historical views, or Explanation semantics.

No ARCH contracts are accepted by the grouping transition itself; Group 01 will establish the first accepted ARCH range after review.

### D-1265 — Architecture technology selection follows explicit environment facts and decision criteria
**Status:** Accepted — Phase 010 foundation

Phase 010 must distinguish verified vendor/public defaults, target-environment discovered facts, organization requirements, architecture assumptions, and unresolved unknowns. Major technology choices must be evaluated against explicit quality attributes, semantic requirements, operational constraints, cost/quota/retention facts and alternatives rather than selected by convention or familiarity.

### D-1266 — Every Phase 009 residual gap receives explicit Phase 010 ownership and treatment
**Status:** Accepted — Phase 010 foundation

GAP-009-01–GAP-009-40 are architecture inputs. Group 01 must assign each gap a Phase 010 owner, MVP/enterprise priority and treatment path. A gap may be resolved, reduced, deliberately scoped out or carried forward explicitly, but cannot disappear by weakening the proposition it affects.

### D-1267 — Group 01 must establish architecture frame and environment discovery before major technology selection
**Status:** Accepted — Phase 010 Group 01 entry

Group 01 establishes target-environment discovery, MVP/enterprise boundary, architecture quality attributes/tradeoff criteria, service/use classes, ADR/decision discipline, integration-capability inventory requirements, nonfunctional constraints and cross-group gap ownership.

Group 01 does not preselect final persistence, graph, event-bus, orchestration, retrieval/LLM, redaction/policy, Gate/Safeguard, service or deployment technologies.

### D-1268 — Phase 010 begins without reopening accepted Phase 002–009 functional or integration semantics
**Status:** Accepted — Phase 010 foundation

Architecture is permitted to choose technical realization but must reject solutions that rely on semantic shortcuts such as availability-as-authority, name/time joins, current-state back-projection, missing-telemetry negatives, Lineage-as-exposure/causality, control-configuration-as-enforcement, reconstructed-history-as-retained-communication, lost basis provenance or universal confidence/health/Impact/control/replay scores.
