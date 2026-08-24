# Decision Records — Phase 006 Group 01 Measurement Vocabulary, Metric Families, Profiles & Applicability

Continues after D-265.

### D-266 — Phase 006 uses HLTH-### refinement contracts
**Status:** Accepted — Phase 006 Group 01
Phase 006 health/metric/schema/statistical contracts use `HLTH-###`. They refine existing concepts and do not extend SYN, REF, or AUTH ranges or create a hidden Health concept.

### D-267 — Phase 006 delivery is decomposed into seven logical groups
**Status:** Accepted — Phase 006 Group 01
The accepted review sequence is: (1) measurement vocabulary/profiles/applicability; (2) structural/schema/DDL compatibility; (3) Baselines/comparability/statistical context; (4) Expectations/thresholds/margins/waivers/Assessment semantics; (5) transformation reconciliation/metric propagation; (6) composite health/readiness suitability/result timing; (7) consolidation/exit. The grouping is functional review order, not service architecture.

### D-268 — Group 01 requires no new concept
**Status:** Accepted — Phase 006 Group 01
Metric/check definitions synchronize with Semantic Definition/Entity Identity; metric/check measured facts are Observation; comparative/normative interpretation is Assessment; profile selection remains the non-concept governed structure accepted in AUTH-017. No Metric, Metric Profile, Check, DQ Result, or Health Result concept is added.

### D-269 — Every material measurement is bound to exact subject/grain/window/version semantics
**Status:** Accepted — Phase 006 Group 01
A numeric/categorical/boolean measurement is not reusable health evidence unless its subject, metric definition/version, grain/population, evaluation window, relevant output/data/schema version or current-cycle context, and material time context are sufficiently identified.

### D-270 — Metric Observation and health Assessment remain separate
**Status:** Accepted — Phase 006 Group 01
Observed metric values and structural predicates remain Observation. Normative/comparative pass/fail/warning/degraded/atypical interpretation belongs to Assessment against explicit Expectation/Baseline basis. Calculation success is not health pass.

### D-271 — Ten canonical metric families are accepted as a functional taxonomy
**Status:** Accepted — Phase 006 Group 01
The families are operational/output; temporal/freshness; structural/schema; volume/population; completeness/missingness; uniqueness/key integrity; validity/domain; distribution/shape; relational/transformation integrity; and business-semantic measurement. Family membership neither mandates profile inclusion nor creates implementation modules.

### D-272 — Metric definition identity changes with material calculation semantics
**Status:** Accepted — Phase 006 Group 01
Material changes in formula, denominator, filters/population, unit, grain/window, missing-value handling, approximation/sampling or equivalent semantics require explicit definition revision/version handling. Same display name is insufficient for historical continuity; Group 03 later decides comparability.

### D-273 — Metric-profile roles are core, critical/business, transformation-specific, and diagnostic/on-demand
**Status:** Accepted — Phase 006 Group 01
These roles describe why a metric/check is selected. High-consequence/control eligibility remains AUTH-023 governance, audience remains disclosure context, and criticality remains Classification rather than a profile role by itself.

### D-274 — Semantic applicability, profile selection, computability/support, availability, and Assessment outcome are independent
**Status:** Accepted — Phase 006 Group 01
`Not applicable`, `not selected`, `unsupported`, `unavailable`, `pending/not evaluated`, and unknown/conflicting applicability remain distinct. None may be rewritten as zero, false, pass, or no issue.

### D-275 — Routine metric profiles follow an explicit anti-bloat principle
**Status:** Accepted — Phase 006 Group 01
Technical availability does not justify routine computation. Routine profiles should remain purpose-driven and bounded; broader exploratory metrics can be diagnostic/on-demand. Investigation-time use does not automatically create permanent profile membership.

### D-276 — Metric/check observations require provenance sufficient for later reasoning
**Status:** Accepted — Phase 006 Group 01
Material Observations retain definition/version, subject/field/relationship, source/input evidence, window/grain/population, relevant temporal context, approximation/sampling/coverage limitations and restriction state where material. Mirrored measurements do not create false corroboration.

### D-277 — Local metric existence does not imply downstream propagation
**Status:** Accepted — Phase 006 Group 01
A metric may be locally useful without being a downstream metric. Lineage alone never copies metrics or creates arithmetic relationships. Group 05 owns transformation-aware reconciliation/propagation semantics.

### D-278 — Phase 006 Group 01 exits; Group 02 is next
**Status:** Accepted
HLTH-001–HLTH-008 and H01-01–H01-20 are accepted. The concept catalog remains 24; SYN-001–SYN-035, REF-001–REF-030, and AUTH-001–AUTH-053 remain unchanged. Phase 006 Group 02 — Structural / Schema / DDL Compatibility is next and has not started.
