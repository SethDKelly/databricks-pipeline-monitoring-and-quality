# Security, Governance & Policy Transparency

**Canonical key:** `foundation.security_governance_policy`

**Kind:** POLICY

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `foundation.security_governance_policy`

**Owns current question:** Which product-security, governance, disclosure, and control-boundary rules constrain every DMTZ realization?

**Stable IDs:** N/A

## Current semantics

DMTZ should increase operational and data transparency **without increasing unauthorized exposure or creating hidden production availability dependencies**.

DMTZ aggregates metadata, evidence, topology, governance, causal/Impact state, control state, and authorization context from multiple systems. Those combined facts can themselves be sensitive even when raw rows are absent. Security therefore applies to metadata, derived state, topology, incidents, business context, and control/authority information as well as raw data.

## Trust boundaries

DMTZ treats at least these as independent trust/authority boundaries:

1. Git repositories and source-controlled configuration;
2. GitHub Actions/deployment workflows;
3. Databricks workspaces/jobs/tasks/runs;
4. Databricks catalogs/assets/Lineage/quality and system surfaces;
5. optional governance systems such as Collibra;
6. optional policy/access systems such as Immuta;
7. the DMTZ monitoring/reasoning framework;
8. optional active-control integrations for Execution Gate and/or Propagation Safeguard;
9. human principals and consuming systems.

Access, technical privilege, synchronization, or administration in one boundary does not automatically confer authority or access in another.

## Accepted security principles

### SP-01 — Least privilege
Every user, workload identity, connector, adapter, and control integration receives only the capabilities required for its accepted function.

### SP-02 — Monitoring does not grant raw-data access
Permission to see that an asset is stale, degraded, reachable, exposed, restricted, held, or otherwise relevant does not imply permission to inspect underlying rows/values.

### SP-03 — Metadata can be sensitive
Descriptions, schemas, names, Lineage paths, classifications, Responsibility Assignments, Policy Context, incidents, quality metrics, causal/Impact state, control state, consumer identity, and authorization metadata may require independent protection.

### SP-04 — Minimize copied sensitive data
Prefer metadata, aggregates, references, checks, and bounded derived evidence over copied row-level values. Real secrets/PII/PHI/customer/patient payloads do not belong in repository documentation or fixtures.

### SP-05 — Preserve source authorization intent
Synchronizing a restricted fact into DMTZ must not intentionally bypass the source/organization authorization boundary. Replication or indexing is not declassification.

### SP-06 — Provenance is security-relevant
Users/processes must be able to distinguish source assertions, measured Observations, human Annotations, derived Assessments/Impact, control decisions/enforcement evidence, authorization decisions, and Explanations.

### SP-07 — Audit material changes
Material changes to Expectations, semantic/governance assertions, responsibility, classification/policy overrides, Causal Claim status, Impact/consequence, safeguards, gate configuration/decision/override, authorization, and source-authority mappings are attributable and historically reconstructable.

### SP-08 — No secrets in source control
Credentials, tokens, private keys, connection strings, production payloads, and environment secrets are never committed to repository authority/routing/test artifacts.

### SP-09 — Safe examples
Documentation/tests use synthetic or explicitly approved sanitized data/assets. Examples must not normalize copying production-sensitive values into monitoring artifacts.

### SP-10 — Question answering is authorization-aware
Answer generation operates over an authorized analytical projection; it does not fetch hidden facts merely to summarize them. Omission/redaction must not be paraphrased into reassuring absence.

### SP-11 — Separate analytical transparency, raw-data access, and production-control authority
Direct/raw access, metadata/governance visibility, health/metric visibility, Lineage/RCA, job/run operations, safeguard actions, gate control/override, Explanation/report access, and causal confirmation are independently resolvable capabilities.

### SP-12 — Historical replay never weakens current disclosure controls
Historical authorization is evidence about historical state, not permission for the current requester. Current Capability Authorization/disclosure governs what historical evidence or conclusions may be shown now.

### SP-13 — Downstream Impact disclosure is capability-bounded
Candidate identity/path, exposure details, consumed versions, effect metrics, client/business consequence, safeguard/gate context, and causal attribution can have different disclosure sensitivity. An upstream visible subject does not make every downstream fact visible.

### SP-14 — Passive monitoring must not become a hidden production dependency
Observation, collection, Assessment, Investigation, Impact analysis, and Explanation are out-of-band by default. Monitoring degradation must not stall ungated production simply because a workload is monitored.

### SP-15 — Active execution gating requires explicit control authority and failure semantics
Execution Gate is optional active control. Enablement, readiness criteria, hold/admit/override, delivery/enforcement evidence, timeout/fallback, degraded-control behavior, and operator authority are explicit. DMTZ has no universal fail-open/fail-closed rule.

## Governance/authority categories

DMTZ preserves these as separate state/authority dimensions:

- **Semantic Definition** — what an identified entity means in a relevant context/time.
- **Responsibility Assignment** — who bears a named responsibility; not universal access/control authority.
- **Criticality** — importance/priority context; not proof of exposure/effect/consequence.
- **Classification** — membership under a named governance/sensitivity vocabulary.
- **Policy Context** — policy/handling applicability; not authorization, enforcement, legal interpretation, or compliance conclusion.
- **Assertion Authority** — whether an assertion source/actor is authoritative for the applicable proposition/category/subject/context/time.
- **Capability Authorization** — whether a principal may perform a named capability on a subject/context/time.
- **Control/evidence state** — evidence that a gate/safeguard/policy/authorization-related control actually operated; configuration/decision is not enforcement proof.

Synchronization order, platform privilege, repository ownership, job creator identity, or administrator status is never a universal authority rule.

## Disclosure and restricted-data analysis

DMTZ should support useful analysis without requiring raw-data access whenever the necessary authorized evidence can be represented safely.

An Authorized Analytical Projection may independently expose, at approved abstraction levels:

- execution state/timing/duration/readiness;
- freshness/health/quality Assessments;
- aggregate quality/volume/distribution evidence;
- Expectation/Baseline result state while withholding restricted thresholds/values;
- Semantic Definitions and Responsibility Assignments;
- Classification/Policy Context summaries;
- redacted/opaque Lineage and dependency context;
- Investigation/Causal Claim status and evidence limitations;
- Impact candidate/exposure/effect/consequence state;
- Propagation Safeguard state;
- Execution Gate state such as held/admitted/overridden and safe prerequisite context;
- authorized Annotations and Explanations.

Every abstraction must itself be authorized. Hidden evidence is not retrieved merely because a convenient summary would be useful.

## Unknown/conflict rules

DMTZ must not turn governance/authorization/control/evidence gaps into safe defaults:

- missing semantics ≠ inferred business meaning;
- missing responsibility ≠ intentional unassignment;
- missing Classification ≠ non-sensitive;
- missing Policy Context ≠ unrestricted;
- missing Capability Authorization ≠ permitted;
- missing Assertion Authority ≠ authoritative;
- missing readiness evidence ≠ ready;
- missing control telemetry ≠ enforcement/fail-open/fail-closed;
- missing consumer telemetry ≠ not exposed;
- missing consequence evidence ≠ no consequence;
- stale/conflicting policy/authorization/control metadata ≠ current certainty.

Applicable incompatible assertions remain conflicting until an accepted category/context-specific authority rule resolves them.

## Control-plane boundary

Operational authorization is independent from analytical and raw-data capabilities. Permission to retry, update, reconfigure, gate, override, quarantine, release, or otherwise control production does not imply data visibility; permission does not prove successful action.

For ungated workloads, DMTZ monitoring availability is not a production start dependency. For explicitly gated/safeguarded deployments, the selected control integration may enter the production path by design, so its availability, latency, fallback, override, enforcement evidence, audit, and recovery become explicit obligations.

## Threat themes

Every technical realization should address, proportionately:

- unauthorized inference from combined metadata;
- metadata/evidence poisoning;
- evidence/history tampering;
- over-broad integration credentials;
- stale policy/authorization/control metadata;
- source/authority confusion;
- passive-monitoring induced production failure;
- gate/safeguard control-plane failure/bypass;
- causal overstatement;
- Impact overstatement;
- cross-domain leakage through APIs/reports/conversation/cache/search/model assistance.

## Invariants / boundaries

- authentication ≠ Capability Authorization ≠ Assertion Authority;
- source availability/technical privilege ≠ authority;
- Classification ≠ Policy Context ≠ authorization ≠ compliance;
- permission/configuration/decision ≠ execution/enforcement/result;
- hidden/restricted evidence ≠ absent evidence;
- historical authorization ≠ current disclosure permission;
- passive monitoring ≠ active control;
- Gate ≠ Safeguard;
- model/search output cannot manufacture authorization, authority, evidence sufficiency, causal confirmation, Impact, or control decisions.

## Synchronizations / related canonical resources

- [Actors and stakeholders](../reference/actors-and-stakeholders.md)
- [Foundational terminology](../reference/terminology.md)
- [Architectural principles](../invariants/architectural-principles.md)
- [MVP boundary](mvp-boundary.md)
- [Shared glossary](../reference/glossary.md)

Detailed AUTH/INTG/ARCH contracts remain with their inventory-selected legacy owners until CKR-D/H/I.

## Provenance

- Original owner and SP-01–SP-15 source: [`../../foundation/006_security_governance_and_policy_model.md`](../../foundation/006_security_governance_and_policy_model.md)
- Authority/governance refinements: [`../../concepts/phase_005/README.md`](../../concepts/phase_005/README.md)
- Impact/control refinements: [`../../concepts/phase_007/README.md`](../../concepts/phase_007/README.md)
- Explanation disclosure refinements: [`../../concepts/phase_008/README.md`](../../concepts/phase_008/README.md)
- Source/integration authority refinements: [`../../concepts/phase_009/README.md`](../../concepts/phase_009/README.md)
- Technical security/serving/control architecture: [`../../concepts/phase_010/README.md`](../../concepts/phase_010/README.md)
