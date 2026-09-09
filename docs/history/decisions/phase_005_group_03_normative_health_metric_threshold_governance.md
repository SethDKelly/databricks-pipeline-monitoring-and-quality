# Decision Records — Phase 005 Group 03 Normative Health, Metric & Threshold Governance

Continues after D-188.

### D-189 — Group 03 requires no new concept
**Status:** Accepted — Phase 005 Group 03
Metric profiles and normative health governance compose from Assertion Authority, Expectation, Semantic Definition, Baseline, Observation, Assessment, Change, and existing control concepts. A metric profile is a governed selection/applicability structure, not a new truth owner.

### D-190 — Expectation authority is dimension/context/action scoped
**Status:** Accepted — Phase 005 Group 03
Normative authority resolves by subject, Expectation class/dimension, property/metric/schema condition, context, effective time, and lifecycle action where needed. Semantic authority, responsibility, criticality, policy, or metric-computation ownership do not silently grant Expectation authority.

### D-191 — Metric-profile governance is purposeful and anti-bloat
**Status:** Accepted — Phase 005 Group 03
Metric/check availability is not sufficient reason for profile inclusion. Governed profiles should retain purpose, applicability, use/audience, authority/owner, and lifecycle/retirement context while Phase 006 defines the actual taxonomy/calculation semantics.

### D-192 — Metric meaning, profile selection, threshold, severity, waiver, and control use are independently governable
**Status:** Accepted — Phase 005 Group 03
One source/actor need not be authoritative for every layer. No layer silently grants authority over the others.

### D-193 — Baseline-derived ranges remain descriptive until explicitly adopted normatively
**Status:** Accepted — Phase 005 Group 03
Historical typicality or statistical regularity never self-promotes into an Expectation. Authority can adopt a normative rule informed by Baseline evidence, but the resulting Expectation remains a distinct provenance-bearing action.

### D-194 — Structural/schema compatibility Expectations require explicit normative authority
**Status:** Accepted — Phase 005 Group 03
Governed technical schema meaning does not by itself define what structural evolution is acceptable. Required/optional fields, accepted types/nullability/key/grain conditions, additive-evolution rules, and consumer-specific compatibility are normative state under explicit authority.

### D-195 — Authority cannot manufacture Baseline comparability
**Status:** Accepted — Phase 005 Group 03
Governance can retire or suspend use of a Baseline or trigger scoped review after structural Change, but empirical comparability remains evidence/health semantics. A new Baseline must be derived from sufficient comparable evidence rather than approved target values.

### D-196 — Exceptions/waivers do not rewrite observed health evidence
**Status:** Accepted — Phase 005 Group 03
A bounded exception, waiver, or suspension can change normative applicability/required response but does not change the Observation, structural state, Baseline deviation, or historical evidence. Do not report a false `pass` merely because a waiver exists.

### D-197 — Normative conflicts remain explicit without hidden strictest/business/technical precedence
**Status:** Accepted — Phase 005 Group 03
Different contexts/dimensions may coexist. Incompatible co-authoritative rules for the same bound normative proposition remain conflict unless an explicit authority resolver applies. `Strictest wins`, `business wins`, `technical wins`, `highest severity wins`, and recency are not implicit rules.

### D-198 — Criticality influences governance priority, not threshold truth
**Status:** Accepted — Phase 005 Group 03
A critical asset/metric may warrant stronger review, escalation, or control eligibility, but criticality does not automatically create a threshold, tighten an existing rule, prove a violation, or establish actual Impact/consequence.

### D-199 — High-consequence metric/Expectation use requires explicit eligibility
**Status:** Accepted — Phase 005 Group 03
A metric or structural Expectation does not become an Execution Gate, safeguard, or automated high-consequence predicate merely because it is authoritative or business-critical. Explicit use eligibility is required for the bound control/use context.

### D-200 — Control-use eligibility is not control authority, evidence readiness, or enforcement
**Status:** Accepted — Phase 005 Group 03
Group 03 eligibility does not grant gate/safeguard configuration/activation/override capability, prove the metric is timely/sufficient, or prove control enforcement. Group 05, Phase 004, Phase 006, and Phase 009 retain those independent concerns.

### D-201 — Normative lifecycle is historical and non-rewriting
**Status:** Accepted — Phase 005 Group 03
Revision, exception, waiver, suspension, expiry, retirement, and later correction preserve prior normative state and the Assessments/controls/Explanations that legitimately referenced it at earlier knowledge cuts.

### D-202 — Group 03 exit gate satisfied; Group 04 next
**Status:** Accepted
Phase 005 Group 03 is complete with AUTH-016–AUTH-023. AUTH-001–AUTH-023 are accepted overall. Group 04 — Capability Authorization & Restricted Analytical Visibility is next and has not started. Phase 006 retains metric/statistical/schema-health computation semantics.