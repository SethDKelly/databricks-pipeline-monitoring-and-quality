# Phase 005 Group 04 — Scenario Checks

**Status:** Accepted

These scenarios stress AUTH-024–AUTH-032 while preserving Assertion Authority, Phase 004 evidence semantics, and Group 03 normative governance.

| Scenario | Authorization question | Accepted result |
|---|---|---|
| Analyst denied Table C rows but allowed health summary | can RCA proceed? | yes; authorized Assessment/freshness/opaque Lineage can be visible without raw rows |
| Analyst may see `completeness violated` but not exact threshold/value | result versus basis | Assessment summary may be visible while threshold/value remain restricted; hidden basis is not absence |
| Analyst can see schema health but not sensitive field names | detail-specific visibility | authorized structural summary allowed; field identities remain hidden |
| Restricted upstream is material to RCA | may path remain useful? | opaque dependency/reference may be shown only if existence/path abstraction is authorized; hidden node is not treated as nonexistent |
| Exact count of hidden downstream consumers would reveal restricted topology | is aggregate count automatically safe? | no; derived/aggregate detail requires its own authorization and leakage review |
| Direct user allow conflicts with group deny | no combination rule | authorization remains conflicting; no implicit direct-wins or deny-wins truth |
| Explicit policy says direct deny overrides group allow | resolver exists | denied for the bound target; both assertions/provenance retained |
| Group grant exists but incident-time membership cannot be established | can grant apply? | no positive allow; membership limitation leaves authorization unknown/insufficient as applicable |
| Current role membership did not exist during incident | historical reconstruction | current membership is not projected backward |
| Service principal may process restricted metrics; analyst may only see Assessment | processing versus requester access | framework can use evidence if service principal is authorized; analyst projection remains limited |
| Monitoring service itself lacks access to restricted evidence | source exists elsewhere | evidence is unavailable to framework and cannot count toward internal sufficiency |
| User can edit Expectation draft but lacks normative authority | action permission versus standing | edit/proposal may be recorded but cannot silently become authoritative rule |
| Steward has normative authority but lacks approval capability | authority versus permission | authoritative standing does not bypass required Capability Authorization to perform approval action |
| User can view threshold but not waive it | action granularity | view does not grant waiver capability |
| Domain-level metadata grant exists; child-table raw grant is unspecified | inheritance | no implicit raw-data inheritance from container/domain access |
| User can inspect upstream A but downstream B is restricted | Lineage propagation | access to A does not grant B or full path visibility |
| Classification says PHI | does label deny access? | no; Classification may inform an authorization rule but is not itself Capability Authorization |
| User is platform admin | universal capability? | no; title/admin status does not create universal permission |
| Authorization source unavailable | runtime wants fail-safe behavior | truth remains unavailable; implementation may refuse without positive allow but cannot record an invented deny |
| Capability revoked today; incident occurred yesterday while allowed | history | past authorization remains reconstructable; current permission changes prospectively/effectively |
| Historical analyst could see raw data, present reviewer cannot | can current reviewer inspect old raw evidence? | no; current requester authorization governs current disclosure |
| User was allowed to retry a job | did retry succeed? | permission does not prove attempt or success; Execution History/operational evidence must show outcome |
| Metric is control-eligible but analyst can only view it | may analyst configure gate? | no; high-consequence eligibility is separate from operational capability; Group 05 governs gate authority |

## Group result

AUTH-024–AUTH-032 compose with the existing 24 concepts and AUTH-001–AUTH-023. No 25th concept is required.

The scenarios preserve:

- authorization target ≠ asset-wide access;
- `unknown/conflicting/unavailable` ≠ explicit deny ≠ allow;
- principal membership ≠ implicit entitlement;
- raw-data visibility ≠ derived health visibility ≠ threshold/schema/Lineage/RCA/control visibility;
- Capability Authorization ≠ Assertion Authority;
- Authorized Analytical Projection ≠ declassification/new truth;
- requester visibility ≠ framework processing authorization;
- authorization decision ≠ external enforcement/action success;
- historical authorization ≠ current requester permission.
