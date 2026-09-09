# Phase 010 Group 03 — Identity, Scope, Authority, Authorization & Disclosure Architecture

**Status:** COMPLETE / ACCEPTED

## Result

Group 03 accepts **ARCH-081–ARCH-132** and **IAD03-01–IAD03-84**. Decisions D-1337–D-1382 are accepted.

The architecture realizes the Phase 005 authority model and Phase 009 governance-source gaps without collapsing identity, Monitoring Scope, Assertion Authority, Capability Authorization, vendor IAM enforcement or disclosure.

The governing chain is:

**source-local identity + organization identity evidence → canonical ecosystem Entity/Principal identity → governed Monitoring Scope → proposition-specific Assertion Authority → action-specific Capability Authorization → current/historical authorization evaluation → disclosure-dimensional projection → later source/control enforcement evidence**.

No link automatically creates the next.

## Canonical architecture

Group 03 adds organization-owned structured record families to the Group 02 canonical Delta Lake plane:

1. **Entity registry** — durable tenant-scoped ecosystem entity IDs;
2. **Source identity bindings** — evidence-bearing links from vendor-local identities/incarnations to canonical entities;
3. **Principal registry** — normalized human/group/service/workload identities plus source/IdP provenance;
4. **Monitoring Scope registry** — versioned explicit memberships/selectors and bounded materializations;
5. **Assertion Authority registry** — structured target/facet/context/time/source/actor rules, precedence/co-authority/fallback and resolution history;
6. **Capability Authorization registry** — structured principal/action/subject/context/detail rules and conditions;
7. **Authorization decision journal** — retained actual evaluations where product/audit/control commitments require them;
8. **Disclosure projection records** — current request context, authorized dimensions and exact/coarse/redacted/opaque/withheld projection metadata.

These are organization-owned governance state, not copied vendor evidence promoted to authority.

## Identity architecture

- names, paths, emails and timestamps are descriptive evidence, never sufficient exact cross-system identity by convenience;
- source-local stable IDs remain source identities and are retained even when an ecosystem entity mapping exists;
- source rename versus delete/recreate/incarnation is resolved from stable identity/evidence rather than visible naming;
- identity mappings are revisioned and can remain provisional/conflicting/unresolved;
- principal identities distinguish humans, groups, service principals, apps and workload identities;
- acting-on-behalf-of, run-as, delegation and impersonation are explicit relationships rather than identity collapse;
- current group membership cannot be projected backward as historical membership.

## Monitoring Scope architecture

No evaluated vendor owns DMTZ Monitoring Scope. Group 03 therefore makes it explicit organization state.

Scope may contain explicit entity membership and governed selectors. Dynamic selectors retain their rule revision and materialization inputs. Missing selector/source inputs produce **unknown membership**, not automatic exclusion. A scope materialization can establish an expected population for bounded collection/negative-claim coverage, but cannot prove the sources were observed successfully.

Monitoring Scope is independent from technical accessibility and authorization.

## Assertion Authority architecture

Assertion Authority is policy-as-data. Each rule binds the exact assertion family/facet, subject scope, context/time, eligible source/actor and governing conditions. Explicit precedence, co-authority and fallback are represented as rule data.

There is no implicit latest-wins, most-specific-wins, majority-wins, source-count, vendor-order or role-title precedence. Co-authoritative conflict persists until an independently authorized resolution applies.

Vendor roles/ownership can be evidence used by an organization rule but are not automatically Assertion Authority.

Causal confirmation receives an explicit authority profile but remains jointly **REF-017 evidence + AUTH-034 authority** gated.

## Capability Authorization architecture

Authorization uses a canonical action vocabulary and binds:

**principal + action + subject/resource + context/audience/purpose/delivery + time + material detail → allowed / denied / conditional / unknown / conflicting / unavailable**.

Group/role inheritance and conflict resolution are explicit rules. DMTZ introduces no universal deny-wins or allow-wins rule.

Material evaluations may persist an actual authorization-decision record with exact rule revision and inputs. A later historical replay is labeled as reconstruction and does not prove the decision actually ran.

Authorization remains separate from request, issuance, source/control enforcement, action occurrence and outcome.

## Disclosure architecture

Disclosure evaluates conclusion, material context, limitations, basis identity, provenance metadata and exact evidence detail independently. Supported projection forms are exact, coarse/generalized, redacted, opaque-reference and withheld.

Safe abstraction is epistemically monotone: it may reveal less but cannot strengthen a proposition, broaden its scope, merge distinct subjects or hide a material limitation to make the visible answer stronger.

`inspectBasis` is itemwise. Hidden basis existence/count/type/source/path/timestamp/redaction metadata can itself be sensitive, so the framework is not required to disclose how many basis items were withheld.

Retention or historical prior visibility never creates current permission.

## Vendor integration posture

Current vendor IAM/governance surfaces remain useful but bounded:

- Databricks users/groups/service principals, Unity Catalog privileges/ownership and workspace entitlements provide Databricks-local principal/access evidence;
- GitHub Apps, installations, enterprise/org/repository permissions, teams and managed-user identity provide GitHub-local authorization/identity evidence;
- Collibra resource/global roles and responsibilities can supply governed responsibilities/permissions where deployed and assigned organizational meaning;
- Immuta permissions, policy definitions and query-time policy/entitlement audit can supply bounded policy/enforcement evidence where installed and covered.

No vendor surface automatically becomes DMTZ Monitoring Scope, ecosystem Entity Identity or full Assertion Authority. Deployment availability remains subject to ARCH-001–ARCH-032.

## Security/residency

Identity/governance metadata is tenant-partitioned and residency-aware. Cross-shard decisions may exchange the minimum permitted identifiers/decision inputs, but evidence payloads are not centralized merely to simplify authorization. Even the existence of a cross-shard reference may be sensitive.

## Persistence/retention interaction

Group 02 retention tiers remain authoritative. Governance history needed for a retained authorization decision, Explanation, basis, control record, audit commitment or legal/security hold is pinned according to that dependency. Low-value evaluation telemetry can age normally; exact retained decisions or basis projections cannot be downsampled in ways that destroy the promised audit proposition.

## Group 04 handoff

Group 04 receives ARCH-001–ARCH-132 and may design source acquisition/adapters/integration health. Connectors must emit source-local identities, provenance, coverage and permission/error facts into these primitives rather than inventing connector-specific canonical identity, scope, authority or benign authorization defaults.