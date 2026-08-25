# Phase 009 Agent Handoff

Applies to work under `docs/concepts/phase_009/` and complements the repository root `AGENTS.md`.

## Current status

- Phase 008 is complete with EXPL-001–EXPL-160 final.
- Phase 009 logical grouping is accepted.
- **Group 01 is complete with INTG-001–INTG-022; IC01-01–IC01-40 pass.**
- **Group 02 is complete with INTG-023–INTG-050; GOV02-01–GOV02-48 pass.**
- **Group 03 is complete with INTG-051–INTG-083; RTE03-01–RTE03-54 pass.**
- **Group 04 — Health, Schema, Metrics, Expectations, Baselines & Reconciliation Evidence is next.**
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

## Accepted Group 03 rules

Preserve:

- Git commit SHA is repository revision identity; PR/merge/commit metadata becomes Change Intent only under explicit governance;
- `github.sha` is event-semantic triggering revision and can differ in meaning from `github.workflow_sha`;
- GitHub `run_id` identifies a workflow run while `run_attempt` identifies a re-run attempt;
- a GitHub re-run retains the original triggering SHA/ref and does not become a new source revision by default;
- CI job/step/workflow success does not prove Databricks target activation;
- GitHub Deployment SHA/ref/environment records identify GitHub deployment requests/status, not target activation by default;
- GitHub→Databricks association requires explicit shared identifiers/manifests/fingerprints/target-recorded provenance;
- names, actors, branch labels and timestamp proximity cannot establish cross-system operational joins;
- Databricks job/task SCD2 configuration history constrains effective config but does not prove run-specific state;
- bundle/external-deployment metadata identifies management/provenance context but does not itself attest a commit;
- bundle/workspace-source run Git revision is unsupported out of the box unless explicit immutable attestation is retained;
- direct remote-Git Jobs can expose `git_snapshot.used_commit` as strong run-specific Git code evidence;
- implementation state remains composite across code, job/task configuration, params, runtime/libraries and target facets;
- trigger/schedule/opportunity ≠ actual run;
- run occurrence ≠ complete lifecycle;
- retry/repair/rerun/backfill retain distinct source semantics;
- task/root/source run associations use explicit IDs where available; missing older fields remain missing;
- configured dependency ≠ actual precedence ≠ waiting ≠ consumption;
- timeline rows must be assembled before deriving run/task duration/order;
- Lakeflow pipeline update identity remains distinct from Jobs execution identity;
- recent Jobs API detail and longer system-table history are different replay surfaces;
- audit events can support operational reconstruction but common derivation prevents automatic independent-corroboration credit;
- Delta output version binding is conditional and per output;
- run success ≠ output existence/version/currentness/health;
- Delta `readVersion` is not a generic upstream input manifest;
- exact generic multi-input version consumption is unsupported out of the box and requires explicit workload/query/source evidence when needed;
- no-run/no-output/no-consumption retain opportunity/coverage/source-health burdens.

See [`03_change_deployment_execution_version_runtime_evidence/README.md`](03_change_deployment_execution_version_runtime_evidence/README.md).

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

## Group 03 gaps carried forward

- generic CI→Databricks association requires explicit correlation where platform-native evidence is absent;
- bundle/workspace-source runs need explicit commit/content attestation when exact Git revision matters;
- composite run-specific implementation state requires multiple evidence facets;
- exact generic multi-input consumption requires explicit workload/query/source instrumentation or manifests;
- output version binding remains conditional and per output;
- recent Jobs API versus longer system-table history creates replay-detail boundaries;
- operational negative claims remain source-coverage bound.

## Group 04 entry contract

Group 04 may consume exact run/task identity, timing, implementation facets and input/output versions only where INTG-051–INTG-083 establish them.

It must independently evaluate realized schema, structural compatibility evidence, metric/DQ Observations, governed Expectations, Baseline membership/comparability, reconciliation, freshness/current-cycle state and exact-use suitability. Execution success, CI success, active job configuration or output existence cannot substitute for those health propositions.

## External-fact discipline

Groups 02–08 necessarily evaluate evolving vendor capabilities. Verify current external documentation when executing a group, distinguish product documentation from repository assumptions, record meaningful edition/feature/retention/permission limitations, and avoid treating undocumented behavior as guaranteed.

Group 02 records sources in [`02_identity_scope_governance_authority_authorization_sources/external_source_review.md`](02_identity_scope_governance_authority_authorization_sources/external_source_review.md); Group 03 records sources in [`03_change_deployment_execution_version_runtime_evidence/external_source_review.md`](03_change_deployment_execution_version_runtime_evidence/external_source_review.md).

## Architecture boundary

Do not select SDK/client libraries, polling versus streaming, event buses, storage schemas, graph databases, caches, credential mechanisms, deployment topology, retry infrastructure, orchestration, attestation implementation, LLM/retrieval architecture or UI. Phase 010 owns technical architecture.

## Group sequence

1. integration contract vocabulary/source roles/capability matrix — **accepted**;
2. identity/scope/governance/authority/authorization sources — **accepted**;
3. change/deployment/execution/version/runtime evidence — **accepted**;
4. health/schema/metrics/Expectations/Baselines/reconciliation evidence — **next**;
5. Lineage/consumer use/exposure/Impact evidence;
6. Investigation/causality/Safeguard/Gate/control evidence;
7. Explanation/historical replay/basis/disclosure source contracts;
8. cross-source coverage/latency/retention/cost consolidation and exit.
