# Phase 006 Group 04 — Expectations, Thresholds, Margins, Waivers & Assessment Semantics Scenario Review

All scenarios are synthetic and test functional semantics rather than vendor implementation.

| ID | Scenario | Expected reasoning | Result |
|---|---|---|---|
| H04-01 | Null rate 1.8%; Expectation <=2% | `meets`; no Baseline required | **PASS** |
| H04-02 | Null rate exactly 2%; Expectation <=2% | `meets` because boundary is inclusive | **PASS** |
| H04-03 | Null rate exactly 2%; Expectation <2% | `violates`; exclusive boundary is material | **PASS** |
| H04-04 | Threshold says 2% but denominator/population is unknown | criterion/evidence binding unresolved; do not evaluate | **PASS** |
| H04-05 | Freshness required by 07:00 with warning after 06:45; completes 06:52 | hard criterion `meets` + warning/proximity state | **PASS** |
| H04-06 | Same freshness rule; completes 07:08 | `violates`; warning is not a substitute for violation | **PASS** |
| H04-07 | Low-severity threshold violated | remains `violates`; severity does not change outcome | **PASS** |
| H04-08 | High-severity threshold currently satisfied | `meets`; severity does not create failure | **PASS** |
| H04-09 | Baseline null rate historically 12%; Expectation <=2%; current 12% | `typical` relative to Baseline + `violates` normatively | **PASS** |
| H04-10 | Baseline 19–21M; no volume Expectation; current 14M | descriptive atypical only; no normative fail | **PASS** |
| H04-11 | New post-change regime has no Baseline; explicit volume Expectation 13–15M; current 14M | normative `meets`; Baseline can remain insufficient | **PASS** |
| H04-12 | New regime has no Baseline and no volume Expectation | no normative result; descriptive reference insufficient | **PASS** |
| H04-13 | Expectation is within 10% of Baseline B; B is comparable and current is within band | `meets` based on explicitly adopted relative rule | **PASS** |
| H04-14 | Same relative rule but B is non-comparable after grain change | normative result indeterminate; do not substitute another Baseline | **PASS** |
| H04-15 | Relative rule references Baseline B but B source unavailable | `unavailable`/indeterminate, not pass/fail | **PASS** |
| H04-16 | Approximate null rate ~1.95% with material uncertainty spanning 2% limit | insufficient/indeterminate near boundary | **PASS** |
| H04-17 | Approximate null rate ~5% with bounded uncertainty far above 2% | can support `violates` when method limits cannot change outcome | **PASS** |
| H04-18 | Approximate null rate ~0.2% with bounded uncertainty far below 2% | can support `meets` when method limits cannot change outcome | **PASS** |
| H04-19 | Required-run source unavailable at deadline | insufficient/unavailable; do not claim missed run | **PASS** |
| H04-20 | Complete query proves no required run occurred | sufficient absence evidence can support `violates` | **PASS** |
| H04-21 | Two co-authoritative row-count thresholds 15M and 18M for same context | normative conflict; do not use strictest/latest | **PASS** |
| H04-22 | Business freshness rule and technical completeness rule both apply | distinct dimensions compose without conflict | **PASS** |
| H04-23 | Consumer A requires field X; Consumer B does not | different consumer contexts; not normative conflict | **PASS** |
| H04-24 | Explicit rule defines warning >1.5% and violation >2% | secondary warning band composes with criterion | **PASS** |
| H04-25 | Platform defaults a 5% tolerance not present in governed rule | ignore hidden default; do not invent tolerance | **PASS** |
| H04-26 | Violation occurs during authorized response waiver window | preserve `violates + waived disposition`; no false pass | **PASS** |
| H04-27 | Waiver explicitly makes criterion non-applicable for migration window | represent `not applicable under bounded exception`, not `meets` | **PASS** |
| H04-28 | Alert waiver exists but gate-use waiver does not | alert response may be waived; gate semantics not automatically waived | **PASS** |
| H04-29 | Waiver expired before current run | evaluate normally; prior waiver history remains | **PASS** |
| H04-30 | Waiver source unavailable | missing waiver evidence is not a waiver | **PASS** |
| H04-31 | Criticality Tier 1 but threshold currently met | criterion `meets`; criticality may affect priority only | **PASS** |
| H04-32 | Same observation is atypically improved and meets Expectation | preserve atypical descriptive result + normative meet | **PASS** |
| H04-33 | Current value meets one criterion but another unrelated criterion conflicts | preserve resolved result and conflict separately | **PASS** |
| H04-34 | Historical threshold changed last month | incidents before change use old version; current uses new version | **PASS** |
| H04-35 | Historical waiver valid then but revoked today | historical waived disposition remains; no retroactive rewrite | **PASS** |
| H04-36 | Source corrects a metric after initial violation Assessment | create reassessment; preserve original result/provenance | **PASS** |
| H04-37 | Current Baseline version differs from one referenced by historical relative Expectation | replay uses historical reference version | **PASS** |
| H04-38 | Structural incompatibility is waived for response but still observed | compatibility Assessment remains incompatible; waiver affects disposition only | **PASS** |
| H04-39 | Warning state is labeled `degraded` by UI convention | functional model retains criterion outcome + warning separately; UI must not redefine truth | **PASS** |
| H04-40 | A criterion is authoritative but the current evidence is restricted from requester | framework may assess if independently authorized; disclosure can hide basis without changing result | **PASS** |

## Review result

**H04-01–H04-40 pass.**

No new Threshold, Waiver, Severity, Normative Result or Health concept is required. Expectation owns normative rule state; Observation/Baseline provide evidence/reference; Assessment owns basis-specific evaluation. HLTH-030–HLTH-040 refine their composition.

No DQX/Metric Views expression model, statistical library, alert engine, overall-health score, control policy, storage or compute architecture is selected.