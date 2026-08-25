# OPS-120 — Execution Gate + Propagation Safeguard Coordination

**Status:** Accepted — Phase 007 Group 08

## Purpose

Compose the two active controls without merging start/admission protection with output/publication/consumption protection.

## Rules

- Gate HOLD does not protect an already published/served prior state; a Safeguard may separately protect that path;
- Gate ADMIT does not release an active Safeguard;
- Safeguard release does not ADMIT a Gate-held execution;
- Gate override does not override/release Safeguard protection;
- an execution may start after ADMIT while its output remains safeguarded;
- a Gate-held opportunity can coexist with safe-but-stale or suspect published state depending on independent Safeguard/Impact evidence;
- each control keeps separate authority, lifecycle, enforcement and historical replay;
- one control's success/failure does not manufacture the other's state.

Control-induced effects involving both controls require evidence for each material mechanism rather than control-name proximity.