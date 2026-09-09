# 006 — Security, Governance, and Policy Transparency Model

## Purpose

Define trust boundaries and non-negotiable security/privacy/governance principles before implementation. This document is a product-security model, not a detailed IAM, network, scheduler, or control-plane design.

## Security objective

The monitoring system should increase operational and data transparency **without increasing unauthorized data exposure or unintentionally creating new production availability dependencies**.

The product has unusual risk because it aggregates metadata from many systems. Even if it avoids raw row-level data, the combined metadata may reveal sensitive facts about schemas, table names, classifications, semantics, responsibilities, incidents, business processes, policies, downstream usage, health metrics, causal conclusions, Impact/consequence, safeguard state, Execution Gate state, or authorization state.

## Trust boundaries

The initial ecosystem contains distinct trust/authority boundaries:

1. Git repositories;
2. GitHub Actions deployment workflows;
3. Databricks workspaces/jobs/tasks/runs;
4. Databricks catalogs/data assets/lineage/quality metadata;
5. optional governance systems such as Collibra;
6. optional policy/access systems such as Immuta;
7. the monitoring/quality framework itself;
8. optional future execution-control integration used for an explicitly enabled Execution Gate;
9. human users and consuming systems.

The monitoring framework must not assume that access or authority in one boundary implies access or authority in another.

## Security principles

### SP-01 — Least privilege
Every integration and user capability should require only the authority necessary for its approved function.

### SP-02 — Monitoring does not grant raw-data access
A user who can see that a restricted table is stale should not automatically be able to see rows from that table.

### SP-03 — Metadata can be sensitive
Descriptions, business definitions, column names, lineage paths, classification labels, responsibility assignments, policy context, incident notes, quality metrics, causal claims, downstream Impact/consequence, safeguard state, Execution Gate state, Annotation, and authorization metadata may themselves reveal sensitive information and need access control.

### SP-04 — Minimize copied sensitive data
The default monitoring design should prefer metadata and aggregates over row-level values. Real PII/PHI must never be placed in repository fixtures or documentation.

### SP-05 — Preserve source authorization intent
If a source system restricts a fact, synchronizing that fact into monitoring must not intentionally bypass that restriction. The exact authorization mechanism is deferred, but the product semantics are not.

### SP-06 — Provenance is security-relevant
Users should be able to distinguish a classification asserted by a policy/governance source, a definition sourced from a catalog, an Observation measured in Databricks, a human Annotation, an Impact/consequence assertion, a gate decision/control result, and an authorization decision supplied by an access authority.

### SP-07 — Audit material changes
Changes to expectations, semantic definitions, responsibility assignments, classification/policy overrides, incident conclusions, Causal Claim status, Impact/consequence state, safeguard state, Execution Gate configuration/hold/admit/override state, authorization state, and system-of-record mappings should be attributable and historically visible.

### SP-08 — No secrets in source control
Credentials, tokens, connection strings, patient/customer values, production payloads, and environment secrets must not be committed to the repository.

### SP-09 — Safe examples
Documentation and tests created later should use synthetic assets and synthetic data unless an approved sanitized dataset is explicitly provided.

### SP-10 — Question answering is authorization-aware
A natural-language interface can create data-leakage risk by composing facts from several sources. Any future answer-generation layer must operate over an Authorized Analytical Projection and must not retrieve hidden values merely to summarize them.

### SP-11 — Separate analytical transparency from raw-data and production-control authority
The product must support independent authorization for direct/raw data access, derived health/metric visibility, governance/metadata visibility, Lineage/RCA participation, job/run operational actions, safeguard-control actions, and Execution Gate configuration/override actions.

A user may be denied raw rows while still being permitted to investigate approved health metrics, execution timing, redacted Lineage, policy/restriction summaries, responsibility context, causal evidence, downstream Impact, safeguard state, and an authorized `waiting on prerequisite` gate state. Conversely, permission to analyze metadata does not imply authority to modify a job, activate quarantine, or override a gate. Permission to operate a job does not imply permission to inspect the data it processes.

Derived or aggregate evidence is not automatically unrestricted; safe analytical projection remains authorization-aware.

### SP-12 — Historical replay never weakens current disclosure controls
Historical Capability Authorization is evidence about what a past principal could know or do at an earlier time. It does not grant the current requester access to evidence that is currently restricted.

A retrospective Explanation may state, at an authorized abstraction, that an incident responder had broader access or that restricted evidence informed a historical conclusion. The current requester's applicable Capability Authorization still governs present disclosure.

### SP-13 — Downstream Impact disclosure is capability-bounded
Candidate identity, Lineage path, exposure evidence, consumer/version details, downstream-health metrics, client/business consequence, safeguard placement, Execution Gate context, and causal attribution may each have different disclosure sensitivity.

The fact that an upstream subject is visible does not grant visibility into every downstream consumer, prerequisite, or consequence. Safe Impact/Explanation may expose aggregate or opaque statements such as `one restricted downstream client delivery was affected` or `execution is waiting on a restricted prerequisite` only where that abstraction itself is authorized.

### SP-14 — Passive monitoring must not become a hidden production dependency
Observation, evidence collection, Assessment, Investigation, Impact analysis, and Explanation should be out-of-band by default. Monitoring service degradation must not delay ungated production jobs merely because they are monitored.

Future architecture should prefer integrations that observe Databricks/platform/source metadata without requiring production code changes or adding framework work to the production critical path when the required evidence is otherwise available.

### SP-15 — Active execution gating requires explicit control authority and failure semantics
Execution Gate is optional active control. A dependency, schedule, Lineage edge, or readiness Assessment does not automatically authorize a block. Gate enablement, hold/admit/override actions, enforcement evidence, timeout/fallback behavior, and operator authority must be explicit.

The project does not assume a universal fail-open or fail-closed rule. An enabled gate whose readiness/control source is unavailable must follow an explicitly accepted gate policy/class rather than silently improvising behavior at runtime.

## Governance model

The project distinguishes several governance/security facts rather than treating them as one field.

### Semantic definition
What an identified entity means and how it should be interpreted in a relevant business or technical context.

### Responsibility assignment
Who bears a named responsibility for an identified subject. A responsibility assignment does not grant access or operational authority.

### Criticality
How important the entity is to downstream business or operational processes. Group 05 confirms criticality can influence prioritization but is not evidence that exposure, downstream effect, or business consequence occurred. Exact representation remains deferred.

### Classification
Category membership under a named governance or sensitivity vocabulary. Classification does not itself encode policy obligations, grant access, or establish compliance.

### Policy context
A declared assertion that a policy, handling expectation, restriction, or governance obligation applies to an identified subject in a relevant context/time. Policy Context does not itself grant or deny a user capability or prove a policy breach/consequence.

### Capability authorization
A provenance-bearing resolution of whether a principal may perform a named capability on a subject/context/time. Capability Authorization is separate from Responsibility Assignment, Classification, Policy Context, Monitoring Scope, and enforcement evidence.

The model must be able to distinguish at least raw-data read, metadata/health-analysis visibility, Lineage/RCA participation, job/run operational action, safeguard-control, **Execution Gate control/override**, and Explanation access without selecting an IAM implementation.

### Execution Gate control state
An explicit control state governing whether a downstream execution opportunity is held, admitted, or overridden based on declared prerequisite readiness. Gate state does not imply that the upstream data is healthy beyond the configured criterion, and gate admission does not prove that the downstream execution actually occurred.

### Control/evidence state
Evidence that a policy-related, authorization-related, safeguard, or Execution Gate control operated, where available. This remains separate from policy applicability, authorization intent/decision, health truth, causal truth, and legal compliance conclusions.

## PII, PHI, and HIPAA-related transparency

The product should make policy context visible in careful vocabulary:

- `classified as PII` means a source or authorized actor assigned a PII classification under a relevant vocabulary;
- `classified as PHI` means a source or authorized actor assigned a PHI classification;
- `HIPAA-related policy context applies` means an authoritative policy-context assertion says related handling expectations are relevant;
- `capability permitted/denied/conditional` means an applicable authorization source resolved a named principal capability for the relevant subject/context;
- `control evidence present` means a particular control/check produced evidence;
- `downstream consequence observed` means consequence evidence exists for the stated technical/analytical/business outcome;
- none of the above, by itself, means `HIPAA compliant`, `HIPAA violation`, or another legal/compliance conclusion.

The product should avoid broad legal conclusions unless an authorized compliance process explicitly supplies them.

## Authority and conflict

Different systems may disagree about semantic definitions, responsibility assignments, classifications, policy context, Capability Authorization, gate configuration/authority, Impact consequence context, or other governance/evidence state.

The product must preserve source provenance, metadata category/capability, context, conflict visibility, assertion/decision time, relevant effective time, attributable overrides/corrections, and explicit unknown/conflicting/stale/unavailable states where appropriate.

**Synchronization order is never an authority rule.** Until an accepted source-precedence/authority rule exists for a category or capability, incompatible applicable assertions remain conflicting rather than silently collapsing to the most recently synchronized value.

## Unknown is not a safe default

Governance, Impact, control, and authorization gaps must not be converted into reassuring assumptions:

- missing semantics does not authorize inferred business meaning;
- missing responsibility does not prove intentional unassignment;
- missing classification does not mean non-sensitive;
- missing policy context does not mean unrestricted;
- missing capability authorization does not mean permitted;
- missing gate/readiness evidence does not mean `ready`;
- missing consumer telemetry does not mean `not exposed`;
- missing business consequence evidence does not mean `no harm`;
- stale policy/classification/authorization/gate metadata must not be presented as current certainty.

## Restricted-data analysis principle

A restricted-data analyst should be able to perform as much monitoring/RCA/Impact work as their explicit capabilities permit without requiring direct row access as a prerequisite.

An Authorized Analytical Projection may include, independently and at safe abstraction levels:

- pipeline/job execution state, timing, duration, and readiness;
- table/pipeline freshness and health Assessments;
- aggregate quality/volume/distribution indicators where allowed;
- Expectation/Baseline result state while hiding restricted thresholds/raw values when required;
- Semantic Definition appropriate to the audience;
- Responsibility Assignment/contact context;
- Classification and Policy Context summaries;
- redacted/opaque Lineage and dependency context;
- Investigation and Causal Claim status/evidence limitations;
- Impact candidate/exposure/effect/consequence state;
- Propagation Safeguard state;
- Execution Gate state such as held/admitted/overridden and safe prerequisite context;
- Annotation where independently authorized.

The product must clearly identify redaction, opacity, missing evidence, and authorization-limited confidence. It must not convert an unavailable restricted fact into a reassuring negative.

## Downstream Impact disclosure principle

The monitoring system should maximize useful downstream reasoning without turning topology or business context into a leakage channel.

- Reachability can be disclosed opaquely when consumer identity/path is restricted.
- Exposure status can be exposed while consumed-version details remain hidden if the abstraction is authorized.
- A health-effect statement can be visible while exact metric/threshold is hidden.
- Business consequence can be summarized at an authorized level without exposing client or strategic-process identity.
- Causal status can be visible while protected supporting evidence remains opaque, if the claim/status itself is independently authorized.
- Gate state can be disclosed as `waiting on prerequisite` without exposing the restricted prerequisite identity when that abstraction is independently authorized.

Every such abstraction must already be supported by concept state and an applicable authorization/disclosure rule; hidden evidence is not retrieved merely to construct a convenient summary.

## Operational authority and control-plane principle

Authorization to retry, update, reconfigure, gate, override, or otherwise control a job/run is independent from analytical and data-read capabilities. A later technical design must enforce these separately.

The monitoring model may show that an actor is permitted to perform a job operation while being denied raw-data read, or may allow an analyst to investigate while denying all production-control actions. Actual operational action success remains evidence in Deployment/Execution History rather than being implied by permission.

For **ungated** pipelines, production execution should not rely on monitoring-framework availability. For an **explicitly gated** pipeline, the gate/control integration may become part of the production path by design; therefore control-plane availability, latency, timeout/fallback behavior, override, and audit become first-class reliability/security concerns.

## Threat themes to carry forward

### Unauthorized inference
Combining harmless metadata may reveal a restricted fact.

### Metadata poisoning
Incorrect responsibility, classification, expected cadence, semantics, lineage, health metrics, gate readiness, Impact/consequence, or authorization state can cause incorrect operational decisions.

### Evidence tampering
If historical metrics, gate decisions, authorization, causal, Impact, or incident evidence can be silently rewritten, root-cause/impact reports become untrustworthy.

### Over-broad integration credentials
A monitoring or control connector with unnecessary privileges creates an attractive escalation path.

### Stale policy/authorization/control metadata
A policy, capability, or gate assertion copied once and never refreshed can provide false confidence or unsafe control behavior.

### Authority confusion
Treating synchronization order, repository ownership, technical ownership, platform administration, responsibility, criticality, or monitoring visibility as universal authorization/control authority can silently grant inappropriate access/control or overstate impact.

### Monitoring-induced production failure
If passive monitoring is accidentally placed on the critical path, monitoring slowness/outage could delay otherwise healthy production jobs. The architecture must prevent this by default.

### Gate/control-plane failure
An explicitly gated production dependency can stall or incorrectly admit work if its readiness/control integration fails. Later design must define gate-specific availability, timeout, fallback, override, and audit behavior rather than relying on hidden defaults.

### Root-cause overstatement
An automated explanation that presents a correlation as a confirmed cause can lead to unsafe action.

### Impact overstatement
A report that presents every reachable or high-criticality downstream consumer as `affected` can create false business alarms and unsafe operational response.

### Cross-domain leakage through reporting
Reports or conversational answers can reveal restricted asset names, definitions, classifications, policy context, thresholds, downstream consumer identities, client consequences, gate prerequisites/control state, incident details, authorization state, or causal conclusions even when raw data is hidden.

## Security design questions deferred to technical design

- identity provider and authentication method;
- RBAC/ABAC/entitlement mechanism;
- authoritative source(s) by capability category;
- row/column-level authorization mechanics for monitoring metadata;
- safe metric/threshold/Lineage/Impact/gate disclosure levels;
- operational action and gate-control enforcement/audit;
- passive-monitoring isolation from production critical path;
- gate/control-plane availability and latency objectives;
- gate timeout/fallback/override mechanisms;
- historical authorization/control query/enforcement architecture;
- secret storage and rotation;
- encryption architecture;
- network topology;
- service identities;
- audit-log storage/retention;
- detailed threat model and abuse cases;
- whether raw/sampled values are ever required.
