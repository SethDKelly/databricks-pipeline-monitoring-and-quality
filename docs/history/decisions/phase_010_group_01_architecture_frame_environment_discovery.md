# Phase 010 Group 01 — Architecture Frame, Environment Discovery & Decision Criteria

### D-1269 — Enterprise deployment variability is a first-class architecture condition
**Status:** Accepted

Vendor-documented capability does not establish target-enterprise availability or usability. Phase 010 resolves capabilities against concrete deployment context before relying on them.

### D-1270 — Capability identity is deployment-bound
**Status:** Accepted

Capability instances bind vendor/product plus material deployment model, cloud/region/Geo, account/tenant/workspace scope, edition/plan/version and exact surface.

### D-1271 — Architecture fact classes remain explicit
**Status:** Accepted

Verified public/vendor facts, target-environment facts, organization requirements, architecture assumptions and unresolved unknowns are retained separately.

### D-1272 — Capability support is multidimensional
**Status:** Accepted

Presence, enablement, entitlement, permission, reachability, observability, retention and integration health are separate dimensions; there is no universal availability Boolean.

### D-1273 — Unverified capability remains unknown
**Status:** Accepted

Missing verification cannot be converted into support, absence, disablement, denial or lack of license by convenience.

### D-1274 — Target-environment facts require provenance
**Status:** Accepted

Environment metadata, configuration/API evidence, permission-aware probes, administrator attestations or contract/license evidence must support material tenant facts.

### D-1275 — Capability facts are revisioned and time-aware
**Status:** Accepted

Environment capabilities can drift through upgrade, preview, permission, license, network and configuration change. Current discovery does not rewrite prior capability state.

### D-1276 — Cloud, region, Geo and government deployment differences are material when documented or observed
**Status:** Accepted

Later ADRs must bind those dimensions whenever they affect feature availability, residency, system-table coverage, networking or processing location.

### D-1277 — Plan, edition, version and license differences are material capability facts
**Status:** Accepted

GitHub deployment/version/plan, Collibra offering/site model, Immuta package/deployment constraints and analogous vendor distinctions cannot be flattened into vendor names.

### D-1278 — Preview/feature enablement is separate from documented existence
**Status:** Accepted

Account/workspace preview state, feature flags, release channel and default enablement are discovered rather than inferred from documentation.

### D-1279 — Permission and network reachability are separate from capability presence
**Status:** Accepted

An installed feature inaccessible to the integration principal or unreachable from the deployment path is not usable integration support.

### D-1280 — Residency/compliance/organization policy can constrain technically available capability
**Status:** Accepted

Architecture must preserve the distinction between technical possibility and permitted use.

### D-1281 — Capability usability is proposition and service-class specific
**Status:** Accepted

A source can be sufficient for one bounded conclusion and insufficient for another; no vendor/source-wide usability status is accepted.

### D-1282 — Optional-source absence degrades exact capabilities only
**Status:** Accepted

Collibra/Immuta and other optional enrichments cannot become hidden core dependencies or benign-default generators.

### D-1283 — Databricks/GitHub-centered passive monitoring/RCA remains the bounded MVP posture
**Status:** Accepted

This is a capability boundary rather than a preselected component topology. Exact environment support remains deployment-discovered.

### D-1284 — Organization-owned truth sources remain required where the product promises dependent propositions
**Status:** Accepted

Monitoring Scope, Assertion Authority and durable identity/correlation cannot disappear because an optional governance vendor is absent.

### D-1285 — Active Gate/Safeguard control remains an enterprise/explicit extension at this architecture stage
**Status:** Accepted

Passive monitoring is the default MVP posture; active-control architecture is owned by Group 07 and requires explicit scope and enforcement evidence.

### D-1286 — External consumer and business-consequence telemetry is an explicit extension
**Status:** Accepted

The bounded MVP does not pretend Databricks-side reads prove every external report/application use or organizational consequence.

### D-1287 — Long-horizon replay and authentic communication retention are product-commitment dependent
**Status:** Accepted

Group 02/06 must architect them when promised; otherwise the bounded limitation is explicit rather than silently approximated.

### D-1288 — Semantic/evidence/security/degraded-state rules are architecture hard constraints
**Status:** Accepted

An option violating these is rejected rather than compared through a lower tradeoff score.

### D-1289 — Architecture optimization remains decision-specific
**Status:** Accepted

Latency, durability, availability, scalability, simplicity, reversibility, observability, portability, quota and cost are evaluated per decision after hard constraints.

### D-1290 — No universal architecture score is accepted
**Status:** Accepted

Phase 010 does not produce a scalar vendor/architecture/readiness/maturity score that obscures material tradeoffs.

### D-1291 — Six service classes structure latency/completeness/retention decisions
**Status:** Accepted

SC-01 operational facts, SC-02 health/quality, SC-03 Investigation/RCA, SC-04 historical/as-known replay, SC-05 communication/basis inspection and SC-06 active control are accepted.

### D-1292 — Numeric service SLOs are deferred until environment and implementation facts justify them
**Status:** Accepted

Service classes constrain later design without fabricating universal source latency numbers.

### D-1293 — Major technology decisions require explicit ADR evidence and alternatives
**Status:** Accepted

Requirements, environment facts, assumptions, hard constraints, alternatives, tradeoffs, failure behavior, reversibility and verification are mandatory decision material.

### D-1294 — Decision reversibility is explicit
**Status:** Accepted

Readily reversible, costly-to-reverse and hard-to-reverse choices are distinguished; high uncertainty favors option preservation where semantically safe.

### D-1295 — Architecture assumptions and unknowns are a governed register
**Status:** Accepted

They carry owner/impact/validation context and cannot silently mature into facts.

### D-1296 — GAP-009-01–GAP-009-40 have explicit Phase 010 ownership and treatment
**Status:** Accepted

The Group 01 matrix defines primary owners, MVP/enterprise priority and expected treatment; later group exits must close or explicitly carry their assigned gaps.

### D-1297 — Cost, quota, retention and license numbers retain fact class and deployment scope
**Status:** Accepted

Public defaults, enterprise contract values, measured values, assumptions and unknowns remain distinguishable.

### D-1298 — Group 01 accepts ARCH-001–ARCH-032 and promotes Group 02
**Status:** Accepted — Group 01 closure

AFE01-01–AFE01-60 pass. Group 01 closes without selecting final persistence, graph, queue/event bus, orchestration, LLM/retrieval, policy/control, service or deployment technology. Group 02 — Evidence, Provenance, Temporal & Persistence Architecture is next.
