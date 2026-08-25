# Decision Records — Phase 006 Group 04 Expectations, Thresholds, Margins, Waivers & Assessment Semantics

Continues after D-314.

### D-315 — Group 04 requires no new concept
**Status:** Accepted — Phase 006 Group 04
Expectation remains the normative truth owner and Assessment remains the evaluation truth owner. No Threshold, Margin, Waiver, Severity, Normative Result or Health concept is added.

### D-316 — Normative criteria require explicit evaluation binding
**Status:** Accepted — Phase 006 Group 04
A criterion binds subject/dimension, metric/check/structural definition, grain/population/window/context, comparator/direction, boundary semantics, unit/denominator and required reference basis where material.

### D-317 — Boundary semantics are first-class
**Status:** Accepted — Phase 006 Group 04
Inclusive/exclusive limits, units, denominator/population, direction and temporal/calendar semantics are not inferred from labels or vendor defaults. Material changes create revised criterion semantics/version.

### D-318 — Warning/proximity and hard criterion outcome are separate
**Status:** Accepted — Phase 006 Group 04
A criterion can `meet + warning` when nearing a limit. `Warning` is not synonymous with violation or low severity. Tolerance semantics must explicitly state whether they change the criterion, create a secondary band or affect response only.

### D-319 — Relative criteria must bind their reference explicitly
**Status:** Accepted — Phase 006 Group 04
A rule such as `within 10% of Baseline B` is normative only because Expectation explicitly adopts that relationship. Baseline remains descriptive; unusable required reference yields indeterminate/unavailable evaluation rather than silent substitution.

### D-320 — Evidence suitability gates normative pass/fail
**Status:** Accepted — Phase 006 Group 04
Authoritative criterion plus sparse, approximate, unavailable, misaligned or otherwise unsuitable evidence does not produce `meets`/`violates`. Evidence suitability remains conclusion-relative and preserves Phase 004 standards.

### D-321 — Approximation uncertainty can make a boundary result indeterminate
**Status:** Accepted — Phase 006 Group 04
Approximate/sampled evidence can support a conclusion when material method uncertainty cannot change the side of the boundary. When uncertainty spans the boundary, preserve indeterminate/insufficient evidence unless the criterion explicitly defines a valid treatment.

### D-322 — Normative criterion outcomes use a bounded basis-specific vocabulary
**Status:** Accepted — Phase 006 Group 04
For a bound criterion use at least `meets`, `violates`, `indeterminate/insufficient evidence`, `conflicting`, `unavailable`, and `not applicable`. Warning, severity, waiver and descriptive atypicality remain separate.

### D-323 — Baseline and Expectation results can coexist independently
**Status:** Accepted — Phase 006 Group 04
Typical/atypical descriptive results and meets/violates normative results can form any evidence-supported combination. Within Baseline is not pass; outside Baseline is not failure.

### D-324 — A Baseline is not required for independently evaluable normative rules
**Status:** Accepted — Phase 006 Group 04
A new/post-change regime can lack sufficient historical Baseline while a current Observation still receives a normative result under an independent explicit Expectation with sufficient evidence.

### D-325 — Multiple normative rules compose only under explicit scope/logic
**Status:** Accepted — Phase 006 Group 04
Rules in different dimensions/consumers/contexts can coexist. For the same proposition/context, co-authoritative incompatible criteria remain conflict absent an accepted resolver. AND/OR/conditional composition must be explicit.

### D-326 — No hidden normative precedence
**Status:** Accepted — Phase 006 Group 04
Strictest, loosest, newest, business, technical, highest-severity or numerically closest rule never wins by convenience.

### D-327 — Waived violation and non-applicable exception are distinct
**Status:** Accepted — Phase 006 Group 04
A waiver can leave the criterion result intact while changing response (`violates + waived`) or a governing exception can make the criterion non-applicable for a bounded context. The model preserves whichever semantics actually govern.

### D-328 — Waivers do not rewrite evidence or propagate beyond scope
**Status:** Accepted — Phase 006 Group 04
Waiver/exception does not mutate Observation, Baseline, structural compatibility or historical facts. Alert waiver does not automatically waive gate/control behavior or another consequence class.

### D-329 — Severity/priority is independent from criterion outcome
**Status:** Accepted — Phase 006 Group 04
Low-severity violation remains violation; high-severity criterion can meet. Criticality may affect priority but does not tighten thresholds automatically or prove Impact.

### D-330 — Missing telemetry is not normative violation by default
**Status:** Accepted — Phase 006 Group 04
A required-occurrence criterion can be violated only when evidence/opportunity/coverage sufficiently establish non-occurrence. Source/query unavailability produces unresolved/insufficient/unavailable state rather than fabricated failure.

### D-331 — Historical criterion, reference and waiver versions are non-rewriting
**Status:** Accepted — Phase 006 Group 04
Historical Assessment retains the exact applicable rule, warning/tolerance structure, waiver, evidence and reference versions. Later rule changes, Baseline refreshes or waiver revocations do not rewrite earlier results.

### D-332 — Corrected evidence produces reassessment, not silent mutation
**Status:** Accepted — Phase 006 Group 04
Later corrected/late evidence can justify a new Assessment with supersession provenance while preserving the earlier conclusion and its then-available basis.

### D-333 — Group 04 scenario review passes
**Status:** Accepted — Phase 006 Group 04
H04-01–H04-40 pass under HLTH-030–HLTH-040 without a new concept, universal health score or architecture choice.

### D-334 — Phase 006 Group 04 exits; Group 05 is next
**Status:** Accepted
HLTH-001–HLTH-040 are accepted. The concept catalog remains 24; SYN-001–SYN-035, REF-001–REF-030 and AUTH-001–AUTH-053 remain unchanged. Phase 006 Group 05 — Transformation Reconciliation & Metric Propagation is next and has not started.