# Concept: Capability Authorization

**Status:** Accepted — Phase 002 post-exit addendum discovered before Phase 003 Group 05

## Purpose

Let users and the monitoring ecosystem determine whether an identified principal is permitted to perform a named capability on an identified subject in a relevant context and time, without conflating responsibility, policy applicability, monitoring scope, raw-data visibility, metadata visibility, analytical reasoning, or production-control authority.

## Operational principle

A business analyst investigates Table C. The analyst is not permitted to read C's underlying rows or restricted columns, but is permitted to view approved aggregate health metrics, runtime/freshness Assessments, a redacted Lineage path, applicable policy/restriction summaries, responsibility contacts, and Causal Claim status. The analyst can therefore perform meaningful root-cause analysis without direct data access.

Separately, the same analyst may or may not be permitted to perform an operational action such as retrying, updating, or otherwise controlling a pipeline job. That operational capability is resolved independently from raw-data read and analytical visibility. Permission to operate a job does not imply permission to inspect its underlying data, and permission to analyze metadata does not imply permission to modify the job.

## Actors

- Business Analyst / Data Consumer
- Data Engineer / Pipeline Maintainer
- Data Platform Administrator
- Data Steward / Governance Steward
- Security / Privacy / Compliance Stakeholder
- Incident responder / on-call engineer
- Monitoring framework
- External identity/access/policy authority

## State

- principal identity or principal reference, such as user, group, role, or service principal;
- named capability;
- identified subject/resource or bounded subject set;
- relevant context, such as environment, purpose/use, tenant, consumer, or operational target;
- authorization state such as permitted, denied, conditional, unknown, conflicting, or unavailable;
- conditions or constraints attached to the authorization where supplied;
- source/authority/provenance for the authorization decision or entitlement;
- effective interval and recorded/knowledge time;
- supersession, revocation, correction, and conflict history;
- safe decision explanation/reference where disclosure is permitted;
- visibility restrictions on the authorization record itself where applicable.

## Capability categories

Capability vocabulary remains implementation-neutral and extensible. The functional model must be able to distinguish at least:

- direct/raw data read or sample access;
- sensitive column/value access;
- metadata/semantic/governance visibility;
- derived health/metric/Assessment visibility;
- Lineage/dependency traversal visibility;
- Investigation/RCA participation and evidence inspection;
- job/run operational action, such as retry/update/control where later defined;
- Change Intent or Expectation authoring/revision where separately governed;
- Propagation Safeguard proposal/activation/release;
- Explanation/report access.

These are capability classes, not a settled role model, UI permission matrix, or vendor ACL scheme.

## Actions

### `recordDecision`
Records or synchronizes a provenance-bearing authorization decision/entitlement for a principal, capability, subject, context, and effective interval.

### `supersedeDecision`
Ends, replaces, revokes, or corrects a prior authorization state while preserving historical state and knowledge-time context.

### `resolveFor`
Returns the applicable authorization state for a principal + capability + subject + context + time, including conditions, conflicts, unknown/unavailable state, and safe provenance where disclosure permits.

### `explainBasis`
Returns an authorized explanation/reference for why the capability resolved as it did when the source authority permits disclosure. A decision may remain usable even when detailed policy or entitlement evidence is restricted.

## Invariants / behavioral expectations

- Raw-data read authorization is independent from metadata/health-analysis authorization.
- Raw-data read authorization is independent from Lineage/RCA authorization.
- Analytical visibility is independent from job/run operational authority.
- Job/run operational authority does not imply permission to inspect the data processed by that job.
- Responsibility Assignment does not grant Capability Authorization.
- Policy Context does not itself grant or deny Capability Authorization.
- Classification does not itself grant or deny Capability Authorization.
- Monitoring Scope does not grant Capability Authorization.
- Repository ownership, commit history, job creator identity, or platform-administrator status is not silently converted into universal authorization.
- Permission to see a derived Assessment does not automatically permit access to every underlying Observation, threshold, Baseline, raw value, or restricted evidence item.
- Permission to perform Investigation/RCA does not imply complete evidence visibility; restricted evidence may remain opaque while the Investigation records the limitation.
- Permission to view Lineage does not imply permission to see every node name, path detail, schema, or business consumer.
- Permission to operate a job does not imply that an attempted action succeeded; the resulting Deployment/Execution History/Observation evidence remains separately owned.
- Capability Authorization is a decision/entitlement truth, not enforcement proof. Where enforcement is external, actual enforcement evidence remains separate.
- Missing authorization evidence is not permission. `unknown` must not be converted into allow merely to keep analysis or workflow moving.
- Authorization may vary by subject, capability, environment, purpose, consumer, and time.
- Current authorization does not overwrite historical authorization relevant to incident replay.

## Ambiguity and missing evidence

Multiple identity/access sources can disagree. Conflicting authorization states remain conflicting until an accepted authority/source-precedence rule resolves them. A source can be unavailable, stale, or unable to decide for the requested context. Restricted authorization details may be abstracted while still returning a usable permitted/denied/conditional result if the authoritative source allows that projection.

A viewer denied direct-data access may still receive approved derived analytical context. Conversely, some metadata can itself be sensitive, so lack of row access is not a blanket grant to every metric, schema, Lineage edge, Classification, Policy Context, or causal detail.

## Synchronizations

- **Entity Identity** supplies subjects/resources on which capabilities resolve.
- **Responsibility Assignment** may identify the party expected to act but never grants the capability.
- **Classification** and **Policy Context** can provide restriction/context evidence to an external or later authorization rule without themselves becoming access decisions.
- **Monitoring Scope** states monitoring responsibility and remains independent of actor authorization.
- **Observation**, **Assessment**, **Execution History**, **Lineage**, **Investigation**, **Causal Claim**, **Impact**, and **Propagation Safeguard** can each expose authorized projections appropriate to the resolved capability.
- **Investigation** can continue over partial/opaque evidence when the actor has RCA capability but not direct access to every evidence item.
- **Explanation** uses Capability Authorization to compose an audience-appropriate evidence projection without retrieving hidden raw values merely to summarize them.
- Operational actions on jobs/runs, future Change Intent authoring, and Propagation Safeguard activation consume their own capability authorization rather than borrowing raw-data or metadata permissions.
- External IAM/access systems may be authoritative sources later; this concept does not choose Databricks ACLs, Immuta, RBAC, ABAC, or another mechanism.

## Security / privacy / governance considerations

The concept exists to support least privilege and intentional separation of analytical transparency from raw-data exposure and production-control authority. Authorization metadata can itself reveal privileged roles, restricted resources, incident access, or security design and therefore requires appropriate disclosure controls.

Safe analytical access should prefer derived/aggregate/provenance-bearing evidence where it can answer the monitoring question without exposing restricted rows or values. However, aggregation is not automatically safe; sensitive metrics, thresholds, counts, or topology may still require restriction.

## Evidence / provenance considerations

Every material authorization decision should retain its authoritative source, principal, capability, target/context, effective interval, decision/conditions, record time, and correction/revocation history. Historical Investigation/Explanation must be able to distinguish what an analyst was authorized to know or do at the incident time from permissions granted later.

## Representative scenarios

### Restricted data, permitted analysis
An analyst cannot query Table C rows but can see approved row-count/completeness Assessments, execution duration, freshness, a redacted A+B→C Lineage view, policy restriction summary, responsibility team, and supported Causal Claims. RCA proceeds without direct-data access.

### Restricted threshold
The analyst may see `completeness expectation violated` but not the sensitive threshold or raw offending values. Assessment remains useful with an explicit restricted-basis indicator.

### Opaque upstream
The analyst can see that a restricted upstream dependency materially limits confidence and that a supported upstream claim exists, while the upstream entity name and raw evidence remain hidden.

### Job operation without raw data
A user is permitted to retry or update an operational job under an explicit job-operation capability but is denied raw-data read. The action and its resulting execution/deployment evidence remain traceable; no data-read authority is implied.

### Analysis without operational control
A business analyst can inspect health metrics, Investigation, Impact, and Explanation but cannot retry, modify, or quarantine the pipeline.

### Safeguard authority differs
An incident responder can propose a safeguard but activation requires a separate capability held by a data/platform authority.

### Historical authorization
An analyst had RCA access during an incident but receives broader raw-data access later. A historical `what could the analyst know then?` view uses the earlier capability state rather than current permissions.

## Non-goals

- authentication or identity-provider selection;
- RBAC/ABAC model selection;
- defining Databricks/Immuta/Collibra permissions;
- enforcing row/column access directly;
- replacing source-system access controls;
- legal/policy interpretation;
- assigning responsibility;
- proving compliance;
- defining job-update semantics or workflow implementation;
- treating monitoring visibility as production-control authority.

## Deferred questions

- minimum capability vocabulary for MVP;
- which systems are authoritative for each capability category;
- how allow/deny precedence and conditional decisions are resolved across sources;
- whether capability inheritance exists across domains/pipelines/assets and under what explicit rules;
- safe disclosure levels for health metrics, thresholds, Lineage, policy metadata, and causal evidence;
- exact operational actions represented by job/run capability categories;
- how authorization decisions and external enforcement evidence are audited/retained;
- whether purpose-of-use or just-in-time access requires additional structured semantics.
