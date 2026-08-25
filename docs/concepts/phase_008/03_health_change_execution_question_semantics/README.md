# Phase 008 Group 03 — Health, Change & Execution Question Semantics

**Status:** Review complete — accepted

## Goal

Refine business questions about health/status, freshness, schema/quality, changes, deployments, executions, versions and timing by mapping each requested conclusion to accepted HLTH/OPS truth without narrative shortcuts.

## Group result

Group 03 accepts **EXPL-029–EXPL-049** and scenario suite **HCE03-01–HCE03-36**.

No new concept is required. Explanation translates business/operational wording into bounded source-owned or explicitly derived propositions; Phase 006/007 remain the substantive truth owners.

The central domain-answer chain is:

**bounded operational shorthand → exact health/change/execution subquestion → source-owned HLTH/OPS proposition → Group 02 material statement/basis contract → sibling-safe multi-statement answer → explicit limitation/historical perspective → Group 04 inferential handoff**.

## Accepted contracts

- **EXPL-029** — operational-status shorthand decomposition.
- **EXPL-030** — execution occurrence and instance question.
- **EXPL-031** — execution lifecycle/success/terminal outcome.
- **EXPL-032** — output existence, qualification and publication.
- **EXPL-033** — freshness/currentness/current-cycle question.
- **EXPL-034** — health dimension/profile/composite question.
- **EXPL-035** — structural schema/realized compatibility question.
- **EXPL-036** — Baseline/typicality/statistical comparability question.
- **EXPL-037** — Expectation/quality/warning/waiver/severity question.
- **EXPL-038** — transformation/reconciliation question.
- **EXPL-039** — realized Change question.
- **EXPL-040** — Change Intent/planned/anticipated question.
- **EXPL-041** — Deployment attempt/activation/active-state question.
- **EXPL-042** — intent-to-realization match/divergence question.
- **EXPL-043** — run-specific implementation/input/output version question.
- **EXPL-044** — retry/restart/rerun/backfill question.
- **EXPL-045** — dependency sequence/waiting/consumption question.
- **EXPL-046** — expected-work/opportunity/missing-run negative question.
- **EXPL-047** — operational timing/delay/lateness/SLA question.
- **EXPL-048** — historical health/change/execution question.
- **EXPL-049** — Group 04 inferential-question handoff.

## Durable rules

- `ran` ≠ `succeeded` ≠ `produced output` ≠ `produced current/fresh output` ≠ `healthy`;
- latest successful execution ≠ current-cycle completion;
- output existence ≠ publication/availability ≠ downstream use;
- health is dimension/profile/use/context bound, not a universal scalar asset state;
- structural compatibility ≠ statistical comparability ≠ normative quality/health;
- Baseline typicality ≠ Expectation outcome;
- warning/severity/waiver ≠ criterion truth;
- reconciliation mismatch ≠ root cause;
- Change Intent ≠ Deployment ≠ activation ≠ realized Change;
- intent-realization match/divergence ≠ health/cause;
- no matching registered intent ≠ proven unplanned change;
- active Deployment ≠ run-specific implementation state;
- latest upstream output ≠ run-specific consumed input;
- retry/restart/rerun/backfill retain distinct source semantics;
- dependency ≠ actual precedence ≠ waiting ≠ version consumption;
- expected work/opportunity/Gate state ≠ execution;
- missing telemetry ≠ `no run/output/consumption`;
- timing/lateness ≠ causality;
- current retrospective answer ≠ what was known then.

## Boundary with Group 04

Direct `why` questions may expose health/change/execution evidence as basis, but causal attribution remains Causal Claim work. Likewise direct operational state does not automatically establish downstream Impact, Safeguard/Gate effectiveness, responsibility fault, policy breach or authorization.

## Architecture boundary

Do not choose vendor run-status mappings, telemetry sources, scheduler APIs, UI wording/templates, LLM/prompt architecture, freshness SLAs, version-attestation implementation, persistence schema or source integrations.

## Exit

EXPL-029–EXPL-049 and HCE03-01–HCE03-36 are accepted. The concept catalog remains 24. **Group 04 — Investigation, Causality, Impact, Control & Governance Question Semantics is next.**