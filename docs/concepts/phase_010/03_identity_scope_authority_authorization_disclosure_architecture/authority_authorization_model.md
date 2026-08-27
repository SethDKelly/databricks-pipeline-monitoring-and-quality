# Phase 010 Group 03 — Authority & Authorization Architecture

## Purpose

Realize Assertion Authority and Capability Authorization as explicit organization-owned policy state while preserving vendor-local enforcement evidence.

## Assertion Authority rule

Logical fields include:

- `authority_rule_id` / revision;
- tenant;
- target assertion/facet/proposition family;
- subject selector/scope;
- context/purpose/time constraints;
- eligible source/actor/principal predicate;
- authority state/standing condition;
- explicit precedence/co-authority/fallback relationship where applicable;
- governing basis/reference;
- effective/knowledge coordinates;
- supersession.

Free-form governance prose can be linked as basis, but executable resolution requires structured target/condition fields.

## Authority resolution

Resolution returns the applicable standing and any conflict/limitation. It never decides factual evidence sufficiency. Source availability, role title, source count, recency and ingestion order are not default resolvers.

A separate resolution record may establish which assertion governs after a conflict when an authorized resolver exists.

## Causal confirmation

Causal-confirmation authority profiles reference the claim class and eligible confirmer/reviewer rules. The authority resolver may say a principal is eligible to confirm; it cannot mark the Causal Claim confirmed unless REF-017 evidence and AUTH-034 conditions are also met.

## Capability Authorization rule

Logical fields include:

- `authorization_rule_id` / revision;
- tenant;
- principal or principal selector;
- canonical action;
- subject/resource selector;
- purpose/audience/delivery/environment context;
- detail/projection class where material;
- allow/deny/conditional effect or composition instruction;
- membership/inheritance requirements;
- explicit conflict resolver where applicable;
- effective/knowledge coordinates;
- supersession.

## Canonical action vocabulary

At minimum distinguish `query`, `inspect`, `view_result`, `inspect_basis`, `export`, `forward`, `publish`, `annotate`, `review`, `approve`, `confirm`, `configure`, `execute`, `override`, `release`, and `administer` where relevant.

Actions may be refined later but are never inferred from one generic `access` Boolean when the distinction affects accepted semantics.

## Evaluation states

`allowed`, `denied`, `conditional`, `unknown`, `conflicting`, `unavailable`.

There is no universal deny-wins/allow-wins. The organization rule must state the composition semantics. Missing rule/membership/context cannot silently allow.

## Evaluation manifest

Material decisions can retain:

- decision ID/time;
- exact policy revisions;
- principal identity and memberships used;
- subject identity;
- action/context;
- relevant classification/policy inputs;
- decision and unresolved limitations;
- resolver revision.

This is an actual decision record when emitted at decision time. A later reconstruction is separately identified.

## Vendor IAM composition

Vendor privileges/permissions are independent facts. A DMTZ action may require both organization authorization and source-native permission. Organization `allowed` does not mean the source will enforce/permit it, and source permission does not mean DMTZ should expose the action.

## Service identity

Source acquisition uses dedicated workload/service identity wherever supported. The application may process evidence a requester cannot see. Requester rights are never inherited from the service principal.

## Break-glass and delegation

Temporary/emergency grants are explicit, bounded and auditable with issuer authority, reason, action/scope, activation, expiry/revocation and later review requirements where policy says so.