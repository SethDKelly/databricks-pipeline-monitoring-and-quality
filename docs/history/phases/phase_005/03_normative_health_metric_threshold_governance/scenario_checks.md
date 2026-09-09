# Phase 005 Group 03 — Scenario Checks

**Status:** Accepted

These scenarios stress AUTH-016–AUTH-023 while preserving Phase 004 evidence standards and deferring metric/statistical/schema-health computation to Phase 006.

| Scenario | Governance question | Accepted result |
|---|---|---|
| Pipeline owner proposes a business population threshold | technical Responsibility exists; business Expectation authority does not | threshold remains advisory/unresolved, not authoritative merely from ownership |
| Business authority owns population threshold; platform team owns technical freshness warning | different dimensions/layers | both rules can coexist when contexts are explicit |
| Baseline shows usual null rate under 1% but no normative rule exists | can historical regularity become failure threshold? | no; Baseline remains descriptive until an authoritative Expectation is established |
| Three monitoring tools recommend the same threshold | all advisory | agreement does not manufacture normative authority |
| Two co-authoritative business sources set incompatible failure thresholds | same target/context/time | authoritative normative conflict; no strictest/latest winner |
| Table marked Tier-1 critical | does criticality tighten all thresholds? | no; criticality may trigger review/priority but cannot silently create stricter Expectations |
| Metric exists because Metric View/DQX makes it easy to compute | should it enter the asset profile? | not automatically; profile inclusion needs purpose/applicability/lifecycle authority |
| New nullable column added | should every column receive null/quantile checks? | no; governed profile decides relevance; availability does not justify metric bloat |
| `customer_id` is authoritative business key | does this prove uniqueness? | no; semantic key role is descriptive, uniqueness requirement needs Expectation, actual uniqueness needs Observation/Assessment |
| Required column removed in realized schema | structural Expectation was authoritative | realized Observation/Change can support a structural violation Assessment; authority does not itself prove the drop |
| Optional column added | consumer A allows additive evolution; positional export B forbids it | safe for A and violating for B can coexist under consumer-specific schema Expectations |
| Grain changes after planned deployment | metrics/Baselines reviewed | affected metrics may be revised/retired; Baseline comparability remains evidence/Phase-006 question, not something authority can force |
| Authorized reviewer says old Baseline is still usable despite changed meaning | evidence shows non-comparability | authority cannot manufacture empirical comparability; use decision must preserve the limitation |
| One-week migration waiver covers a row-count Expectation | observed count violates old threshold | Observation remains; normative state reflects bounded waiver/suspension rather than false pass |
| Waiver expires | next run still violates threshold | then-applicable Expectation resumes; no silent indefinite suppression |
| Metric is business-critical and authoritative for reporting | may it automatically block downstream execution? | no; separate high-consequence-use eligibility is required |
| Metric is control-eligible but source data is unavailable | can gate treat it as satisfied? | no; evidence/readiness remains unknown and only explicit fallback semantics may act |
| CI file contains schema rule written by developer | repository syntax exists | code/config does not create authority unless applicable Assertion Authority grants standing |
| Control-use eligibility later revoked | historical gate used rule while eligible | historical use remains reconstructable; revocation changes future eligibility only |
| Metric retired from current profile | historical incident used it | historical Observations/Assessments/profile state remain reconstructable |

## Group result

AUTH-016–AUTH-023 compose with the existing 24 concepts and AUTH-001–AUTH-015. No 25th concept is required.

The scenarios preserve:

- metric/profile selection ≠ metric meaning ≠ threshold authority ≠ severity authority ≠ waiver authority ≠ control-use eligibility;
- normative rule ≠ observed value/Assessment evidence;
- Baseline ≠ Expectation;
- criticality ≠ normative failure/Impact;
- schema declaration ≠ structural Expectation ≠ realized schema;
- control-use eligibility ≠ control capability ≠ evidence readiness ≠ enforcement.