# Phase 010 Group 03 — Monitoring Scope Registry

## Purpose

Realize GAP-009-01 as explicit organization-owned state rather than inferred from discoverability or source permissions.

## Scope revision

A scope revision contains:

- `scope_id` and `revision_id`;
- tenant/organization;
- purpose/profile;
- effective interval and knowledge coordinates;
- entity classes / relationship families / proposition families in scope;
- explicit inclusions/exclusions;
- governed selector definitions;
- owner/assertion authority for scope governance;
- supersession history.

## Membership methods

### Explicit

A canonical entity is directly included or excluded.

### Selector

A revisioned expression selects entities from governed/source metadata. Selectors may use classifications, domains, catalog/schema boundaries, repository sets, environment labels or other available metadata, but the selector must retain the authority/limitations of those inputs.

## Materialization

For questions requiring bounded coverage, the selector can be materialized into an expected population. Materialization records:

- selector revision;
- evaluation/knowledge time;
- input-source coverage;
- included identities;
- explicit exclusions;
- unresolved candidate membership;
- source limitations.

Materialization is not required for every routine query, but is required when the conclusion depends on knowing the bounded population.

## Unknown membership

If a relevant selector input is unavailable, permission-filtered or ambiguous, membership is `unknown`. The architecture must not interpret missing metadata as exclusion, because that would silently shrink the denominator of `none`, `all`, `no event`, `no exposure` or similar claims.

## Scope versus access

In-scope does not mean accessible. Accessible does not mean in-scope. Source collection authorization and requester disclosure are independent.

## Scope history

Revisions are non-rewriting. Historical replay uses the scope effective/known at the requested cut. Later scope expansion cannot retroactively make earlier monitoring coverage complete.