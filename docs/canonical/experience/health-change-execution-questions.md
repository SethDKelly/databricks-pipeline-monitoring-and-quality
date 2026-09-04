# Health, Change & Execution Question Semantics

**Canonical key:** `experience.health-change-execution-questions`

**Kind:** EXPERIENCE CONTRACT

**Authority:** CANDIDATE / NOT CURRENT AUTHORITY

**Migration record:** `stable_family.EXPL`

**Owns current question:** How does Explanation translate operational shorthand about health, change, execution, versions and timing into exact HLTH/OPS propositions without narrative collapse?

**Stable IDs:** EXPL-029–EXPL-049

## Current semantics

### EXPL-029 — Operational-Status Shorthand Decomposition
Decompose broad status wording into the specific execution, output, freshness, health, structural, comparability, quality, change, version or timing propositions actually requested.

### EXPL-030 — Execution Occurrence & Instance Question
Resolve whether a specific execution instance occurred from Execution History evidence; expected work, opportunity, schedule or Gate state does not create a run.

### EXPL-031 — Execution Lifecycle, Success & Terminal Outcome Question
Keep occurrence, lifecycle completeness, attempt outcome, terminal result and logical execution assembly distinct when answering whether work succeeded, failed, cancelled or remains unresolved.

### EXPL-032 — Output Existence, Qualification & Publication Question
Separate output existence from commit/qualification/current-cycle association, publication/availability, freshness, health and downstream encounter.

### EXPL-033 — Freshness, Currentness & Current-Cycle Question
Answer freshness/currentness only for the bound use, expected opportunity/cycle, timing criterion and evidence window; latest or successful alone is insufficient.

### EXPL-034 — Health Dimension, Profile & Composite Question
Health questions resolve to dimension/profile/use/context-bound Assessments or bounded composite health rather than one universal scalar asset state.

### EXPL-035 — Structural Schema & Realized Compatibility Question
Keep governed/declared schema meaning, realized structure and structural compatibility Assessment distinct; proposed compatibility does not establish realized compatibility.

### EXPL-036 — Baseline, Typicality & Statistical Comparability Question
Separate descriptive Baseline typicality from empirical comparability and normative acceptability; historical similarity alone does not create an Expectation result.

### EXPL-037 — Expectation, Quality, Warning, Waiver & Severity Question
Answer normative quality from the exact Expectation/criterion result while preserving warning/proximity, severity/priority and waiver/disposition as separate layers.

### EXPL-038 — Transformation & Reconciliation Question
Use transformation-specific reconciliation Observations/Assessments for relationship integrity; mismatch or first boundary localization remains evidence, not root cause.

### EXPL-039 — Realized Change Question
Answer what actually changed from evidence-established Change propositions with before/after state, scope and time rather than from intent or deployment activity alone.

### EXPL-040 — Change Intent, Planned & Anticipated Question
Answer what was planned from the exact Change Intent revision/component and declared scope/effects without projecting later realized state backward into intent.

### EXPL-041 — Deployment Attempt, Activation & Active-State Question
Keep deployment attempt/outcome, target/facet activation and active implementation intervals distinct; successful delivery tooling is not runtime activation absent sufficient evidence.

### EXPL-042 — Intent-to-Realization Match & Divergence Question
Use the bounded derived intent-to-realization comparison vocabulary; matched/partial/diverged/not-evidenced/not-realized states do not imply health, authorization or causality.

### EXPL-043 — Run-Specific Implementation/Input/Output Version Question
Bind actual executions to implementation, input and output versions only through sufficient run-specific evidence; active Deployment and latest upstream output are not substitutes.

### EXPL-044 — Retry, Restart, Rerun & Backfill Question
Preserve source/evidence-specific distinctions among retry, restart/resume, rerun and backfill, including whether activity belongs to one logical execution or another execution.

### EXPL-045 — Dependency Sequence, Waiting & Consumption Question
Keep logical dependency, expected order, actual precedence, evidenced waiting and version consumption separate; one does not prove the next.

### EXPL-046 — Expected Work, Opportunity & Missing-Run Negative Question
Expected work and execution opportunity can support a missing-work inquiry, but `no run` requires bounded opportunity-to-observe and Execution History coverage rather than missing telemetry.

### EXPL-047 — Operational Timing, Delay, Lateness & SLA Question
Distinguish duration, start delay, wait time, completion lateness, freshness/currentness and business/SLA deadline propositions; timing proximity is not causal attribution.

### EXPL-048 — Historical Health, Change & Execution Question
Bind operational answers to the requested event/effective window and knowledge perspective, preserving as-known-at-cut state separately from current retrospective reconstruction.

### EXPL-049 — Inferential-Question Handoff
Provide Group 04 with exact operational propositions and limitations as possible basis while preventing direct state, timing or proximity from silently becoming cause, Impact, control effectiveness or governance conclusions.

## Invariants / boundaries

- ran ≠ succeeded ≠ produced output ≠ produced current/fresh output ≠ healthy;
- output existence ≠ publication ≠ encounter;
- health is dimension/profile/use/context bound;
- structural compatibility ≠ statistical comparability ≠ normative quality;
- Baseline typicality ≠ Expectation outcome;
- warning/severity/waiver ≠ criterion truth;
- reconciliation mismatch ≠ root cause;
- Change Intent ≠ Deployment ≠ activation ≠ realized Change;
- intent realization ≠ health/cause;
- active Deployment ≠ run-specific implementation state;
- dependency ≠ precedence ≠ waiting ≠ consumption;
- missing telemetry ≠ no run/output/consumption;
- timing/lateness ≠ causality.

## Architecture boundary

This contract does not choose vendor run-status mappings, telemetry sources, scheduler APIs, UI wording/templates, LLM/prompt architecture, freshness SLAs, version-attestation implementation, persistence schema or source integrations.

## Provenance

- `docs/concepts/phase_008/03_health_change_execution_question_semantics/README.md`
- Phase 008 Group 03 accepted EXPL-029–EXPL-049.
