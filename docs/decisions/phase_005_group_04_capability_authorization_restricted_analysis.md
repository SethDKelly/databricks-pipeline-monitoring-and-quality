# Decision Records — Phase 005 Group 04 Capability Authorization & Restricted Analytical Visibility

Continues after D-202.

### D-203 — Group 04 requires no new concept
**Status:** Accepted — Phase 005 Group 04
Capability Authorization remains the truth owner for principal/capability/subject/context/time permission state. Authorized Analytical Projection is a synchronization/view over existing truth, not a 25th concept.

### D-204 — Capability authorization is exact-action/detail scoped
**Status:** Accepted — Phase 005 Group 04
Authorization binds principal, capability/action, subject, environment/purpose/tenant/consumer context, time, and material detail level. Asset-wide `can access` labels must not silently grant raw, metric, threshold, schema, Lineage, RCA, or control access together.

### D-205 — Authorization state and fail-safe behavior are separate
**Status:** Accepted — Phase 005 Group 04
`allowed`, `denied`, `conditional`, `unknown`, `conflicting`, and `unavailable` remain distinct. Missing/conflicting/unavailable authorization never becomes allow. A future system may refuse action without positive allow, but must not rewrite unresolved truth into an invented deny.

### D-206 — No hidden authorization-combination precedence
**Status:** Accepted — Phase 005 Group 04
`deny wins`, `direct user wins`, `role wins`, `latest wins`, `most specific wins`, source count, and source availability are not universal resolution rules. Any precedence/combination behavior must be explicit and provenance-bearing.

### D-207 — Principal composition requires historical membership evidence
**Status:** Accepted — Phase 005 Group 04
User/group/role/service-principal entitlements apply only through evidenced applicable membership/assumption and explicit combination rules. Current membership is not projected backward.

### D-208 — Capability inheritance is never implicit
**Status:** Accepted — Phase 005 Group 04
Domain/catalog/schema/table/pipeline/repository/Lineage containment or adjacency does not silently propagate capabilities. Derived/inherited grants require explicit scope, relationship, provenance, and governing rule.

### D-209 — Analytical visibility is detail-decomposed
**Status:** Accepted — Phase 005 Group 04
Raw rows, sensitive fields, schema, governance metadata, metric values, Assessment summaries, thresholds, Baselines, Lineage identities/paths, RCA evidence, causal/Impact/control details, and Explanation can be independently authorized.

### D-210 — Result visibility does not imply basis visibility
**Status:** Accepted — Phase 005 Group 04
A requester may be authorized to see a health/Assessment/causal result while some underlying metric, threshold, raw evidence, schema, topology, or authority basis remains restricted. Hidden basis is represented as restricted, never absent.

### D-211 — Normative governance actions require capability and authority independently
**Status:** Accepted — Phase 005 Group 04
View, propose, edit, approve, revise, waive/suspend, retire, and high-consequence-use approval can be independently authorized. Permission to act does not make the resulting assertion authoritative; Assertion Authority standing does not grant permission to perform the action.

### D-212 — Authorized Analytical Projection is not declassification
**Status:** Accepted — Phase 005 Group 04
Projection is a requester-capability-filtered view over existing truth. It may expose exact state, authorized abstraction, opaque reference, limitation, or nothing. It does not mutate concept state or make restricted evidence unrestricted.

### D-213 — Framework processing authorization and requester visibility are separate
**Status:** Accepted — Phase 005 Group 04
The framework/service principal may be independently authorized to process evidence needed for a result that a requester can see only abstractly. If the framework itself lacks required access, the evidence cannot be counted as internally available/sufficient.

### D-214 — Derived/aggregate monitoring evidence can be sensitive
**Status:** Accepted — Phase 005 Group 04
Counts, thresholds, schemas, topology, hidden-node existence, causal/Impact/control state, authority/authorization metadata, and combinations of otherwise permitted facts can leak restricted information. Aggregation/redaction is not automatic declassification.

### D-215 — Historical authorization is non-rewriting and not reusable permission
**Status:** Accepted — Phase 005 Group 04
Historical replay can reconstruct what an actor was authorized to know/do then. Current requester authorization governs present disclosure; later grants/revocations do not rewrite historical state.

### D-216 — Authorization is not enforcement or action-success evidence
**Status:** Accepted — Phase 005 Group 04
Allowed/denied permission state does not prove external enforcement, attempted action, or successful action. Operational/control concepts and evidence remain responsible for what actually happened.

### D-217 — Group 04 exit gate satisfied; Group 05 next
**Status:** Accepted
Phase 005 Group 04 is complete with AUTH-024–AUTH-032. AUTH-001–AUTH-032 are accepted overall. Group 05 — High-Consequence Action, Control & Causal-Confirmation Authority is next and has not started.
