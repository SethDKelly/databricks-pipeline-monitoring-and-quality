# Phase 005 Group 01 — Scenario Checks

**Status:** Accepted

These scenarios stress Assertion Authority and AUTH-001–AUTH-008 without selecting concrete vendor authority or IAM architecture.

| Scenario | Authority question | Accepted result |
|---|---|---|
| Business definition from Collibra, repository note disagrees | Collibra explicitly authoritative for business-definition facet; repository advisory | authoritative definition resolves from Collibra; advisory disagreement retained |
| Technical schema vs business meaning | Unity Catalog authoritative for schema; steward authoritative for business definition | no conflict because authority targets/facets differ |
| Two co-authoritative stewards disagree | both have authoritative standing; no resolver | authoritative assertion conflict; no arbitrary winner |
| Three advisory sources agree | no authoritative rule exists | agreement remains advisory; no authority by majority |
| Latest assertion is advisory | authoritative older assertion still applicable | recency alone does not displace authoritative state |
| More-specific rule overlaps broader rule | no explicit specificity precedence exists | authority-rule conflict/unknown rather than automatic specific-wins |
| Primary authority unavailable, no fallback rule | secondary source is online | authority remains unavailable/unknown; availability does not confer standing |
| Primary authority unavailable, explicit conditional fallback | fallback rule applies and primary-unavailable condition is evidenced | fallback source may resolve authoritative for that bounded condition |
| Two authority rules disagree about precedence | no higher-order resolver | authority-rule conflict; rules cannot self-resolve |
| Engineer can edit business definition but is advisory | Capability Authorization permits edit; Assertion Authority is advisory | assertion recorded but does not replace authoritative definition |
| Technical owner asserts business criticality | Responsibility Assignment exists but no criticality authority rule | responsibility does not confer authority; criticality authority unknown/advisory as applicable |
| Policy source asserts access entitlement | Policy Context applies but authorization source not resolved | policy assertion does not become Capability Authorization |
| Authoritative source says `no run` but run-history coverage is incomplete | source authority known | Phase 004 negative-evidence burden still fails; authority cannot manufacture evidence sufficiency |
| Authority changes prospectively from A to B | transfer effective next month | historical pre-transfer view uses A; later view uses B |
| Rule corrected later for prior interval | correction known after incident | retrospective authority may change; `as-known-then` preserves earlier authority understanding |
| Restricted authority basis | requester may see standing but not governance hierarchy | safe abstracted authority result allowed; hidden basis not treated as absent |

## Group result

All scenarios compose without using source count, recency, specificity, availability, repository ownership, responsibility, policy applicability, or synchronization order as hidden authority.

The scenarios require a distinct Assertion Authority truth owner because the same authority-rule/history behavior applies across several assertion-owning concepts and cannot be cleanly duplicated inside each one.
