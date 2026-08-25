# Decision Records — Phase 006 Group 02 Structural / Schema / DDL Compatibility

Continues after D-278.

### D-279 — Group 02 requires no new concept
**Status:** Accepted — Phase 006 Group 02
The existing Semantic Definition, Entity Identity, Expectation, Change Intent, Observation, Change and Assessment concepts are sufficient. No Schema, Schema Contract, Schema Version or Compatibility concept is added.

### D-280 — Structural compatibility binds the consumer-visible contract surface
**Status:** Accepted — Phase 006 Group 02
Compatibility must bind the relevant producer/output/interface, structural version/state, consumer or consumer class, applicable contract version and time. Physical producer schema and consumer-visible interface may differ.

### D-281 — Structural change is typed rather than one generic schema-diff state
**Status:** Accepted — Phase 006 Group 02
Add, remove, rename, reorder, nested-path movement, type, precision/scale, nullability, default/generated-value, key/grain and nested-shape changes remain independently representable where material.

### D-282 — Rename identity requires evidence
**Status:** Accepted — Phase 006 Group 02
Drop/add name coincidence does not establish rename identity. Rename/continuity requires supported Entity Identity, Semantic Definition, Change Intent, explicit migration mapping or equivalent provenance. Same name likewise does not guarantee unchanged meaning.

### D-283 — Additive and removal compatibility is consumer-specific
**Status:** Accepted — Phase 006 Group 02
An added optional field may be safe for a tolerant name-based consumer and incompatible for a positional/closed contract. Removal is breaking only for consumers/contracts that require or materially depend on the field.

### D-284 — Type compatibility is semantic and directional, not engine-cast capability
**Status:** Accepted — Phase 006 Group 02
Widening/narrowing, precision/scale, timestamp/encoding and nested-shape transitions are evaluated against the consumer contract and transition direction. Technical cast/parse support does not prove compatibility.

### D-285 — Nullability/default/generated-value changes remain structurally meaningful
**Status:** Accepted — Phase 006 Group 02
Current zero-null data does not preserve a non-null structural guarantee after a nullable transition. Defaults/generated values can satisfy physical presence while violating business completeness/validity semantics.

### D-286 — Key and grain changes are structural even when column lists/types are unchanged
**Status:** Accepted — Phase 006 Group 02
Changes to record identity, key composition or grain can invalidate prior uniqueness, volume, distribution, join and reconciliation assumptions without automatically constituting a quality defect.

### D-287 — Compatibility is consumer/interface/version scoped and non-transitive
**Status:** Accepted — Phase 006 Group 02
A producer transition can be compatible for one consumer and incompatible for another. Stable intermediate views/interfaces may preserve compatibility despite physical table change; producer compatibility with an interface does not automatically prove compatibility for every downstream consumer.

### D-288 — Proposed, declared and realized structural states are distinct
**Status:** Accepted — Phase 006 Group 02
Pre-deployment/prospective validation evaluates a bounded proposal using evidence/contracts known at that cut. It does not prove deployment or realized production state. Realized differences require new Observation/Assessment while the prospective result remains historical evidence.

### D-289 — Structural validation can occur at multiple horizons without choosing placement
**Status:** Accepted — Phase 006 Group 02
Proactive proposed-state validation, realized-state validation, independent monitoring and retrospective reconstruction can coexist. Phase 006 Group 02 does not choose GitHub Actions, Unity Catalog/Databricks, DQX, Metric Views or the monitoring application as the mandatory evaluation location.

### D-290 — Structural change triggers scoped metric/Profile/Baseline review
**Status:** Accepted — Phase 006 Group 02
Only measurement dimensions whose identity, grain, field binding, population, type or transformation semantics are affected require reconsideration. Unrelated measurements may remain valid. Group 03 decides empirical comparability.

### D-291 — `Compatible` is a positive evidence-backed conclusion
**Status:** Accepted — Phase 006 Group 02
A bounded compatibility result requires sufficient evidence that every applicable required structural predicate in scope is satisfied. Missing/insufficient schema or contract coverage cannot be converted into `compatible` merely because no difference was detected.

### D-292 — Structural incompatibility does not imply downstream failure, exposure, Impact or causality
**Status:** Accepted — Phase 006 Group 02
A violated structural contract is one health dimension. Execution History, exposure, Impact and Causal Claim retain their separate evidence burdens.

### D-293 — Physical layout/property changes are not automatically logical schema incompatibility
**Status:** Accepted — Phase 006 Group 02
Clustering, optimization, storage layout and similar physical changes enter structural compatibility only when the relevant consumer/interface contract depends on them. Their performance/operational effects may be assessed elsewhere.

### D-294 — Group 02 scenario review passes
**Status:** Accepted — Phase 006 Group 02
H02-01–H02-30 pass under HLTH-009–HLTH-018 without a new concept or architecture choice.

### D-295 — Phase 006 Group 02 exits; Group 03 is next
**Status:** Accepted
HLTH-001–HLTH-018 are accepted. The concept catalog remains 24; SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged. Phase 006 Group 03 — Baselines, Comparability, Distribution & Statistical Context is next and has not started.