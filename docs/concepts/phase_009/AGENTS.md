# Phase 009 Agent Handoff

Applies to work under `docs/concepts/phase_009/` and complements the repository root `AGENTS.md`.

## Current status

- Phase 008 is complete with EXPL-001–EXPL-160 final.
- Phase 009 logical grouping is accepted.
- **Group 01 is complete with INTG-001–INTG-022; IC01-01–IC01-40 pass.**
- **Group 02 is complete with INTG-023–INTG-050; GOV02-01–GOV02-48 pass.**
- **Group 03 — Change Intent, Deployment, Execution, Version & Runtime Evidence is next.**
- Accepted concept count remains 24.
- Canonical repository status remains in `../../README.md#current-state`.

## Phase purpose

Phase 009 maps accepted functional semantics to actual source/integration capabilities. It discovers feasibility and limitations; it does not redesign the accepted truth model around vendor convenience.

## Accepted Group 01 rules

Preserve:

- integration contracts are capability mappings, not new product truth concepts;
- capability identity binds exact source surface/API/table/event/query/export/object class plus material semantic/version/edition context;
- vendor/system name alone is too coarse;
- every capability row binds an accepted proposition and bounded subject/context;
- evidence role is descriptive and does not create Assertion Authority;
- source availability ≠ relevance ≠ eligibility ≠ authority ≠ sufficiency ≠ authorization;
- internal retrievability ≠ requester-visible disclosure;
- source-local IDs require reconciliation before becoming Entity Identity or another ecosystem identity;
- name equality and timestamp proximity do not prove identity/association;
- exact cross-system associations require explicit join/reconciliation evidence;
- event/effective, recorded/knowledge/availability and retrieval times remain distinct;
- old event timestamp returned today does not prove historical availability;
- grain/cardinality/context constrain the conclusion grain;
- positive-evidence capability does not imply corresponding negative-evidence capability;
- strong negatives require the exact opportunity/population/path/window plus sufficient source/query coverage and source health;
- no record returned during outage/partial pagination/permission failure/throttling/unknown coverage is not evidence of absence;
- coverage is bounded and non-transitive;
- current-state availability does not imply historical replay;
- retention, mutation, correction, backfill, deletion and tombstone behavior are material to replay;
- late evidence does not enter an earlier knowledge cut without evidence it was available then;
- duplicate/common-derived surfaces are not independent corroboration;
- source conflicts remain conflicts absent accepted authority/evidence rules;
- fallback accessibility does not inherit authority;
- support classification is proposition + source set + context bound;
- accepted feasibility outcomes are supported, partially supported, unsupported, unknown/not yet verified and not applicable;
- unsupported is allowed and never weakens REF/AUTH/HLTH/OPS/EXPL semantics;
- quotas/rates/cost may reduce feasible coverage/latency but cannot change truth;
- integration observability is separate from monitored-product state;
- no universal vendor support/confidence/completeness score is accepted;
- capability rows compose only through explicit product semantics, not matrix adjacency.

See [`01_integration_contract_vocabulary_source_roles_capability_matrix/README.md`](01_integration_contract_vocabulary_source_roles_capability_matrix/README.md).

## Accepted Group 02 rules

Preserve:

- Unity Catalog object/principal identity is platform-local until explicit cross-system mapping proves wider identity;
- Collibra UUID and GitHub repository/path identity remain source-local;
- synchronized identity/group/attribute state retains upstream IAM provenance;
- no evaluated source natively owns DMTZ Monitoring Scope;
- Collibra operating-model `scope` is not Monitoring Scope;
- no vendor owner/role/permission surface automatically implements full Assertion Authority;
- semantic authority is facet-specific; Responsibility Assignment authority is responsibility-type specific; Classification authority is scheme/context specific;
- Unity Catalog comments are semantic assertions whose origin does not grant business authority;
- Unity Catalog ownership is platform-operational ownership rather than general business responsibility;
- Collibra Responsibilities retain direct/inherited role semantics; Collibra permissions authorize Collibra actions only;
- ordinary Collibra tags are not strictly governed Classification evidence; Data Classes/governed attributes require an accepted scheme-authority rule;
- Immuta tags/policies retain their policy-metadata/access-control meaning rather than becoming Classification or Policy Context truth by convenience;
- Unity Catalog privileges/ownership/ABAC/workspace state are authoritative only for exact Unity Catalog access propositions in their documented scope;
- Immuta is authoritative for Immuta-managed policy decisions in registered scope, with integration/user-registration semantics preserved;
- effective Immuta + Unity Catalog authorization may require composed evidence and population-specific reasoning;
- GitHub CODEOWNERS/rulesets/custom properties remain repository-governance facts;
- Information Schema and other principal-filtered metadata are observer-relative; hidden/non-returned ≠ absent;
- current governance state ≠ historical governance state;
- source history/retention/configuration limits remain explicit;
- optional-source absence creates gaps rather than benign defaults;
- source conflict/fallback still follows AUTH-001–AUTH-008 rather than source count, recency or product prominence.

See [`02_identity_scope_governance_authority_authorization_sources/README.md`](02_identity_scope_governance_authority_authorization_sources/README.md).

## Required evaluation dimensions

For every material source surface, evaluate as applicable:

- exact source surface and semantic/version/edition context;
- accepted proposition(s) it may inform;
- evidence role and proposition-specific authority applicability;
- source-local identity plus join/reconciliation keys;
- event/effective, recorded/knowledge/availability and retrieval-time semantics;
- granularity/cardinality and version/context binding;
- positive evidence support;
- strong-negative opportunity/coverage support;
- known completeness/coverage boundaries;
- access/authorization and disclosure sensitivity;
- availability and failure/unavailable behavior;
- latency and freshness characteristics;
- retention/history/replay behavior;
- correction, mutation, supersession and late-arrival behavior;
- rate/quota/cost characteristics where material;
- observability of the integration itself;
- duplicate/common-derivation relationships to other sources;
- support classification and residual gaps.

## Permanent boundaries

Never convert:

- available → authoritative;
- authoritative → sufficient;
- accessible → authorized for disclosure;
- missing → false/zero/no-event/no-path/no-exposure/no-effect/no-control;
- current state → historical state;
- Lineage → encounter/exposure;
- workflow success → deployment activation or run-specific version;
- active Deployment → actual run version;
- latest upstream output → consumed input;
- metric/check availability → governed Expectation/Baseline/Assessment;
- control configuration/decision → enforcement;
- Safeguard active + non-exposure → prevented exposure without REF-028 evidence;
- Gate HOLD → failed execution;
- Gate ADMIT → run;
- restricted/redacted → absent;
- source count → confidence;
- synchronization order → authority or causality.

## Source-family discipline

Do not structure the product around vendor names. Databricks, Unity Catalog, GitHub, DQX, Metric Views, Collibra, Immuta and downstream instrumentation may each support multiple accepted concepts, and one accepted proposition may require multiple source families.

A source may be authoritative for one metadata category and merely supporting/observational for another. Preserve proposition-, subject-, context- and time-specific authority.

## Group 02 gaps carried forward

- a deliberate governed Monitoring Scope source remains required;
- an explicit governed Assertion Authority rule source remains required;
- cross-system Entity Identity crosswalks remain required;
- long-horizon governance replay may require retention beyond vendor defaults;
- actual organizational IAM/IdP and synchronization mode remain environment-specific unknowns until verified;
- observer-relative metadata cannot support absence by non-return;
- effective multi-plane authorization may require composition rather than source precedence.

## Group 03 entry contract

Group 03 may consume source-local identities, explicit crosswalks, principal provenance, bounded authority rules, current authorization/disclosure limits and history constraints from Group 02.

It must independently prove repository revision/change-intent association, CI/CD workflow attempt/outcome, Databricks Deployment attempt/activation, actual execution opportunity/run identity, run-specific implementation/input/output version, dependency sequence/waiting, retry/rerun/backfill identity and any strong no-run/no-output/no-consumption claim.

Group 02 identity, ownership, repository path, responsibility, deployment name and timestamp proximity cannot substitute for these joins.

## External-fact discipline

Groups 02–08 necessarily evaluate evolving vendor capabilities. Verify current external documentation when executing a group, distinguish product documentation from repository assumptions, record meaningful edition/feature/retention/permission limitations, and avoid treating undocumented behavior as guaranteed.

Group 02 records its verified public sources in [`02_identity_scope_governance_authority_authorization_sources/external_source_review.md`](02_identity_scope_governance_authority_authorization_sources/external_source_review.md).

## Architecture boundary

Do not select SDK/client libraries, polling versus streaming, event buses, storage schemas, graph databases, caches, credential mechanisms, deployment topology, retry infrastructure, orchestration, LLM/retrieval architecture or UI. Phase 010 owns technical architecture.

## Group sequence

1. integration contract vocabulary/source roles/capability matrix — **accepted**;
2. identity/scope/governance/authority/authorization sources — **accepted**;
3. change/deployment/execution/version/runtime evidence — **next**;
4. health/schema/metrics/Expectations/Baselines/reconciliation evidence;
5. Lineage/consumer use/exposure/Impact evidence;
6. Investigation/causality/Safeguard/Gate/control evidence;
7. Explanation/historical replay/basis/disclosure source contracts;
8. cross-source coverage/latency/retention/cost consolidation and exit.