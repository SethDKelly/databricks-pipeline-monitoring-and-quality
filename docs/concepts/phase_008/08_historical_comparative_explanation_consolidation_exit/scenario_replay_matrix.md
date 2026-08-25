# Phase 008 Group 08 — Historical / Comparative Consolidation Replay

**Result:** **HCX08-01–HCX08-48 PASS**

| ID | Scenario | Required result |
|---|---|---|
| HCX08-01 | Same historical exposure, K1 lacks consumer telemetry, K2 includes it | `unknown at K1` → `exposed at K2`; do not say exposure began at K2 |
| HCX08-02 | Historical run occurred but telemetry arrived late | as-known `not evidenced`; retrospective `ran`; no rewrite |
| HCX08-03 | No retained incident Explanation exists | reconstruction allowed; never label exact prior communication |
| HCX08-04 | Retained incident Explanation says cause unresolved | preserve actual communication even if cause later confirmed |
| HCX08-05 | Current access reveals evidence hidden incident-time | current replay may show detail; retained snapshot unchanged |
| HCX08-06 | Current access revoked for evidence previously visible | current projection narrows; prior communication history not erased |
| HCX08-07 | Historical actor had raw access, current requester does not | historical access is context, not current permission |
| HCX08-08 | Same proposition, summary wording changes only | presentation-only delta |
| HCX08-09 | Same proposition, new independent basis added, status unchanged | basis-enrichment delta only |
| HCX08-10 | Duplicate telemetry added | no status/confidence strengthening |
| HCX08-11 | Earlier source assertion corrected | current retrospective re-evaluates; earlier knowledge/communication retained |
| HCX08-12 | Question population changes from one consumer to all consumers | different proposition/scope, not status transition |
| HCX08-13 | Historical currentness question compared across two cycles | cycle/use-bound results; no universal asset health |
| HCX08-14 | Run succeeded in both periods; second output stale | success unchanged; freshness changed independently |
| HCX08-15 | Schema compatible at T1, incompatible at T2 | compatibility change; do not imply statistical/quality change without evidence |
| HCX08-16 | Baseline typicality changes but Expectation outcome does not | descriptive change only |
| HCX08-17 | Deployment activated before T2; realized Change appears later | activation and realized Change transitions separate |
| HCX08-18 | Active Deployment same, actual run-specific version changes | Execution History owns version transition |
| HCX08-19 | Latest upstream output differs, consumed input remains old | no consumption inference from latest output |
| HCX08-20 | Retry evidence added after incident | retrospective execution reconstruction enriches without phantom earlier knowledge |
| HCX08-21 | Earliest evidenced deviation moves upstream with late telemetry | localization changes; no automatic root-cause promotion |
| HCX08-22 | Investigation closed then reopened | lifecycle change independent of causal confirmation |
| HCX08-23 | Causal Claim supported at K1, confirmed at K2 through governed status change | exact causal transition; no confidence score |
| HCX08-24 | Competing causal claim remains supported after another confirms | preserve both statuses; no forced deletion |
| HCX08-25 | Candidate consumer later proven exposed | Impact-layer transition based on evidence |
| HCX08-26 | Consumer exposed but no effect evidence at either cut | exposure does not become effect |
| HCX08-27 | Late alternate-path evidence invalidates broad non-exposure | retrospective negative re-evaluates; earlier coverage limitation retained |
| HCX08-28 | Consequence evidence appears later | consequence newly established; exposure time not rewritten |
| HCX08-29 | Safeguard active historically, late opportunity evidence establishes prevention | prevention is retrospective derived transition; enforcement action unchanged |
| HCX08-30 | Late bypass evidence removes prevention conclusion | safeguard enforcement remains actual; prevention re-evaluates |
| HCX08-31 | Safeguard released; data health still degraded | release transition separate from recovery |
| HCX08-32 | Gate HOLD decision actual; late start evidence contradicts full enforcement | decision stable; enforcement interpretation changes |
| HCX08-33 | Gate ADMIT actual; no run occurred | ADMIT stable; execution remains separate |
| HCX08-34 | Override later disclosed to broader audience | projection detail changes; readiness/decision truth unchanged |
| HCX08-35 | Responsibility assignment changes teams | responsibility history changes; no blame/cause inference |
| HCX08-36 | Classification revised | classification history changes; no automatic policy/compliance conclusion |
| HCX08-37 | Policy Context becomes applicable after rule revision | effective policy comparison; do not back-project current rule |
| HCX08-38 | Capability Authorization expands | newly visible projection; internal truth unchanged |
| HCX08-39 | Assertion Authority resolver changes prospectively | later standing does not rewrite earlier authoritative resolution |
| HCX08-40 | Same source truth, limitation becomes newly restricted | authorization/projection delta, not evidence strengthening |
| HCX08-41 | Statement removed because no longer material to narrower question | materiality delta; not false/retracted |
| HCX08-42 | Statement removed because source claim rejected | source-status delta, distinguish from mere omission |
| HCX08-43 | `Why did the answer change?` because late telemetry arrived | descriptive basis/knowledge-cut reason; no domain causal claim required |
| HCX08-44 | `Why did the pipeline fail?` after answer changed | Causal Claim semantics still required |
| HCX08-45 | Three retained snapshots show unknown → supported → confirmed | proposition transitions listed; no scalar maturity score |
| HCX08-46 | Recompose same state hourly for a day | no-op; elapsed time does not mature truth |
| HCX08-47 | Full Phase 008 compound question spans health, cause, Impact, control and owner | sibling statements preserve independent truth/basis/status/auth |
| HCX08-48 | Historical compound replay asks what was true, known, communicated and concluded now | four views + current projection remain distinct; no new truth concept |

## Consolidation result

All scenarios pass without a new Question, Answer, statement, historical-answer, confidence, maturity, RCA, Impact-summary or control-effectiveness concept. **EXPL-001–EXPL-160 are sufficient and final.**