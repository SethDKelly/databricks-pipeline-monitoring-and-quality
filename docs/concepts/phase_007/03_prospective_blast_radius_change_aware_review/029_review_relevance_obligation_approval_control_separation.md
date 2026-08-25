# OPS-029 — Review Relevance, Obligation, Approval & Control Separation

**Status:** Accepted — Phase 007 Group 03

## Purpose

Prevent a useful analytical review signal from silently becoming policy, authorization or a deployment gate.

## Contract

Preserve four separate layers:

1. **analytical review relevance** — evidence/semantics indicate a surface or candidate should be examined;
2. **governed review obligation** — an applicable authoritative policy/rule requires a review or named evidence before proceeding;
3. **review/approval action** — an authorized principal/process performs or approves the required action under Capability Authorization/Assertion Authority rules;
4. **deployment/control decision or enforcement** — a separate control mechanism actually constrains execution/deployment where explicitly designed.

Group 03 defines the first layer and can consume the others as context. It does not invent the latter three.

## Result discipline

`review relevant` can coexist with no mandatory review policy. Conversely, a policy may require review even where analytical evidence finds no material downstream path.

A completed review can remain unresolved/conflicting and does not imply approval. Approval does not prove the proposal is safe, deployed or correctly enforced.

## Invariants

- review trigger ≠ predicted defect;
- review relevant ≠ review required;
- review required ≠ approval required unless policy says so;
- approval ≠ deployment;
- approval ≠ control enforcement;
- authority to review/approve ≠ evidence sufficiency;
- no automatic CI gate is created by Phase 007 Group 03.

## Handoff

OPS-030 defines how criticality/priority may enrich review without becoming risk probability or Impact truth.