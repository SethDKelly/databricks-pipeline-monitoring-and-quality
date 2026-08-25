# EXPL-043 — Run-Specific Implementation, Input & Output Version Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

`Which version ran?`, `what input did this run use?`, or `which output version did it produce?` requires run-specific **Execution History** binding evidence.

## Rules

- active Deployment constrains possibilities but does not automatically prove run-specific implementation state;
- repository revision ≠ full runtime implementation identity;
- latest upstream output ≠ consumed input;
- most recent successful upstream run ≠ consumed version;
- output produced by a run must be separately bound to that execution;
- unknown facets/multi-input members remain unknown rather than filled from current state;
- current/fresh/expected/healthy status of the version is a separate HLTH proposition.