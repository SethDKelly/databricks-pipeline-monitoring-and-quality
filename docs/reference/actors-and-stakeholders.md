# Actors and Stakeholders

**Canonical key:** `foundation.actors_stakeholders`

**Kind:** REFERENCE

**Authority:** CANONICAL CURRENT AUTHORITY

**Migration record:** `foundation.actors_stakeholders`

**Owns current question:** Which human and external-system actors materially participate in or constrain DMTZ, and what authority boundaries apply to them?

**Stable IDs:** N/A

## Current semantics

DMTZ actors are defined by **goals, responsibilities, evidence relationships, and authority boundaries**, not by UI screens, implementation roles, or organizational titles alone. One person may occupy several actor roles, and one role does not automatically inherit the authority of another.

## Human actors

### Data engineer / pipeline maintainer

Needs to understand owned pipeline behavior, localize degradation, relate evidence to inputs/code/configuration/deployments, inspect downstream consequences, and provide evidence during resolution. Ability to change pipeline code or jobs does not automatically grant governance, policy, disclosure, or causal-confirmation authority.

### Data platform engineer / platform operator

Needs ecosystem-level operational understanding, scalable integrations, platform/pipeline fault separation, and reliable onboarding. Platform administration does not automatically grant unrestricted sensitive-data visibility, Assertion Authority, or business-policy authority.

### Business analyst / data consumer

Needs to know whether an authorized dataset/metric/report is current and trustworthy, what changed, what may be affected, and who owns the issue. Business-facing Explanation may expose only authorized evidence/abstraction and must remain evidence-consistent with engineering views.

### Data owner

Needs accountability for business use and fitness of important assets, awareness of quality/freshness risk, and participation in appropriate Expectations or business-use policy. Ownership is not universal technical or security authority.

### Data steward / governance steward

Needs to maintain or validate Semantic Definitions, classifications, criticality, stewardship/responsibility context, and provenance. Stewardship does not automatically grant raw-data, job-control, safeguard-control, gate-control, or causal-confirmation capability.

### Security / privacy / compliance stakeholder

Needs visibility into sensitive-data/policy context, safe monitoring behavior, authorization/audit boundaries, and relevant control evidence. Monitoring metadata or control evidence must not be presented as legal/compliance certification unless an independently authorized compliance process supplies that conclusion.

### Incident responder / on-call engineer

Needs rapid symptom-to-origin investigation, blast-radius/Impact analysis, recent-change context, ownership, and clear separation of evidence from hypotheses. Incident participation does not by itself grant hidden evidence access or confirmation authority.

### Monitoring framework administrator

Needs to configure monitoring scope/integrations and maintain framework-level operational integrity. Framework administration is not an omnipotent bypass around source authorization, Assertion Authority, disclosure, or production-control rules.

## External-system actors

External systems can contribute evidence, assertions, configuration, or enforcement without becoming DMTZ semantic authority merely because they are technically privileged.

- **Git repository** — source-controlled code/configuration/tests/history and ownership/provenance context.
- **GitHub Actions** — deployment-workflow evidence that can contribute to revision-to-deployment provenance.
- **Databricks** — execution, asset/catalog, platform Lineage, quality/monitoring, and related platform evidence where verified in the target deployment.
- **Collibra** — optional source for business glossary/stewardship/catalog/governance assertions when an accepted authority rule applies.
- **Immuta** — optional source for policy/classification/access context when an accepted authority rule applies.
- **Downstream analytical/operational system** — dashboard, metric product, application, export, client delivery, or business process whose encounter/exposure/effect/consequence may matter to Impact reasoning.
- **Active-control integration** — optional external execution/propagation control plane used only when an explicitly accepted Execution Gate or Propagation Safeguard realization requires it.

## Invariants / boundaries

1. One person or system does not own all meanings of an asset.
2. Technical ownership, business ownership, stewardship, policy authority, Assertion Authority, Capability Authorization, and control authority remain distinct.
3. Authentication, platform administration, repository ownership, or source availability does not manufacture semantic authority.
4. Administrative power does not imply unrestricted raw or metadata visibility.
5. Answers may be audience-specific but cannot intentionally contradict the authorized underlying evidence state.
6. Source-system assertions retain provenance and applicable authority/coverage limits after synchronization.
7. Permission to perform an action does not prove the action occurred or succeeded.
8. Actor definitions remain functional; IAM groups, screens, services, and organizational titles are implementation mappings rather than conceptual definitions.

## Synchronizations / related canonical resources

- [Product definition](product-definition.md)
- [Foundational terminology](terminology.md)
- [Security and governance policy](../policies/security-governance.md)
- [Shared glossary](glossary.md)

Detailed Capability Authorization and Assertion Authority ownership remains with the inventory-selected AUTH/reference sources until CKR-D.

## Provenance

- Original owner: [`../../foundation/002_actors_and_stakeholders.md`](../../foundation/002_actors_and_stakeholders.md)
- Security/authority boundary refinement: [`../../foundation/006_security_governance_and_policy_model.md`](../../foundation/006_security_governance_and_policy_model.md)
- Current authority vocabulary pending CKR-D: [`../../reference/authority_vocabulary.md`](../../reference/authority_vocabulary.md)
- Integration/source-role refinement: [`../../concepts/phase_009/README.md`](../../concepts/phase_009/README.md)
