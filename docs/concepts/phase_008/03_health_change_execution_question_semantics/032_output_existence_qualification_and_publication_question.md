# EXPL-032 — Output Existence, Qualification & Publication Question

**Status:** Accepted — Phase 008 Group 03

## Requirement

Questions such as `did it produce data?`, `is the output there?`, or `was the expected output produced?` resolve separately from execution success.

Preserve:

**execution outcome ≠ output existence ≠ qualifying/committed output ≠ publication/availability ≠ current/fresh/healthy output**.

## Rules

- successful execution with unknown output evidence remains output-unknown;
- failed/partial execution may still have material output;
- output identity/version/scope must match the requested proposition;
- `exists` cannot be paraphrased as `ready`, `current`, `fresh`, `healthy`, or `consumed`;
- no-output conclusions require the accepted negative-evidence coverage.