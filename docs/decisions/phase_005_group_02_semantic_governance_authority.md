# Decision Records — Phase 005 Group 02 Semantic / Governance Authority

Continues after D-172.

### D-173 — Schema/DDL compatibility is a first-class validation concern
**Status:** Accepted — pre-Group-02 refinement
A successful load/run does not prove structural compatibility. Column add/drop/rename/type/nullability/key/grain and related schema changes can break downstream consumers, invalidate metrics/Baselines, or alter join/reconciliation semantics even when execution succeeds.

### D-174 — No new Schema concept is required at this stage
**Status:** Accepted — pre-Group-02 refinement
Governed schema meaning belongs to Semantic Definition, normative compatibility to Expectation, realized schema evidence/change to Observation/Change, conformance to Assessment, planned evolution to Change Intent, and downstream consequences to Lineage/Impact/Investigation/Causal Claim.

### D-175 — Declared schema, normative schema contract, and realized schema are separate truths
**Status:** Accepted — pre-Group-02 refinement
A source-controlled or governed declaration does not prove production state; a runtime catalog observation does not establish business meaning or desired compatibility. Schema validation composes those separate truths explicitly.

### D-176 — Schema validation location is not schema semantics
**Status:** Accepted — pre-Group-02 refinement
Pre-deployment CI, Databricks/Unity Catalog realized-state checks, independent monitoring, and retrospective RCA may all be useful because they answer different temporal questions. Phase 005/006/007 define semantics; Phase 009/010 decide source contracts and technical placement. No universal validation location is selected now.

### D-177 — Schema changes trigger scoped metric/Baseline applicability review
**Status:** Accepted — pre-Group-02 refinement
Structural change may invalidate particular metric definitions, key/join relationships, or Baseline comparability without requiring a global reset. Applicability must be evaluated by affected dimension/consumer/semantic role.

### D-178 — Semantic authority is facet-specific
**Status:** Accepted — Phase 005 Group 02
Business definition, technical description/schema declaration, grain, units, population, calculation meaning, column role, and key role may have different authoritative holders. One semantic authority does not silently govern every facet.

### D-179 — Authoritative schema meaning does not prove realized schema conformance
**Status:** Accepted — Phase 005 Group 02
A governed schema/key declaration remains descriptive governance truth. Actual physical schema, nullability, uniqueness, and structural conformance require Observation/Change/Assessment evidence and applicable Expectations.

### D-180 — Responsibility authority is responsibility-type scoped
**Status:** Accepted — Phase 005 Group 02
Technical ownership, business accountability, stewardship, security/privacy responsibility, operational responsibility, and platform administration are independently governable responsibility types. Assignment does not grant semantic, policy, metric, access, or control authority.

### D-181 — Classification authority is scheme/context specific
**Status:** Accepted — Phase 005 Group 02
Sensitivity, confidentiality, PHI/PII, business/operational criticality, and other vocabularies remain named schemes. Authority for one scheme does not transfer to another; crosswalks are separately governed assertions.

### D-182 — Criticality remains Classification unless later behavior requires more
**Status:** Accepted — Phase 005 Group 02
Business, operational, delivery, or consumer criticality can be represented as Classification under explicit schemes/contexts. Criticality influences priority/context but does not establish health failure, exposure, consequence, or cause.

### D-183 — Policy reference and policy applicability may have different authorities
**Status:** Accepted — Phase 005 Group 02
Authority over policy text/framework does not automatically confer authority to assert subject/context applicability. Classification may inform applicability but does not decide it. Policy Context remains separate from access, enforcement, compliance, and legal interpretation.

### D-184 — Contextual/local governance does not imply specific-over-broad precedence
**Status:** Accepted — Phase 005 Group 02
Context-specific assertions may coexist when they apply to distinct declared contexts. Where assertions overlap and conflict, narrower scope does not automatically win unless an accepted authority rule explicitly defines that behavior.

### D-185 — Governance assertions do not propagate implicitly
**Status:** Accepted — Phase 005 Group 02
Lineage, repository/container membership, schema similarity, tag inference, or parent-domain state do not silently propagate Semantic Definition, Responsibility Assignment, Classification, Policy Context, criticality, or authority. Derived/inherited assertions require provenance and explicit standing.

### D-186 — Descriptive governance state does not become normative or operational truth
**Status:** Accepted — Phase 005 Group 02
Semantic/schema authority, responsibility, Classification/criticality, and Policy Context do not by themselves establish Expectations, health, Impact, Capability Authorization, control enforcement, or compliance.

### D-187 — Group 02 schema/governance scenarios require no 25th concept
**Status:** Accepted — Phase 005 Group 02
AUTH-009–AUTH-015 plus the existing 24 concepts represent the schema, semantic, responsibility, classification, criticality, policy, inheritance, and conflict cases without another truth owner.

### D-188 — Group 02 exit gate satisfied; Group 03 next
**Status:** Accepted
Phase 005 Group 02 is complete with AUTH-009–AUTH-015. Group 03 — Normative Health, Metric & Threshold Governance is next and has not started. Group 03 must include authority for structural/schema Expectations and compatibility rules without defining Phase 006 schema-health computation.
