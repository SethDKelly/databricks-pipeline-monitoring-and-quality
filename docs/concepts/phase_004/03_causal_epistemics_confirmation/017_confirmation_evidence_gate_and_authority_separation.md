# REF-017 — Confirmation Evidence Gate and Authority Separation

**Status:** Accepted — Phase 004 Group 03

## Purpose

Define the minimum evidence-side semantics for `confirmed` Causal Claim status while keeping confirmation authority, organizational approval, and source precedence separate for Phase 005.

## Confirmation profile

Confirmation is evaluated against an explicit **confirmation profile/standard** appropriate to the causal claim class. A deterministic control-mechanism claim may require different evidence from a complex data-population claim. The framework does not impose one universal evidence checklist or score.

A confirmation profile identifies the causal dimensions and evidence conditions that are necessary for that class of claim.

## Minimum confirmation gate

Regardless of claim class, `confirmed` requires all of the following:

1. **Bound proposition** — the cause, outcome, causal role, context, and relevant time are explicit enough to evaluate.
2. **Cause and effect evidence** — the proposed cause condition and effect are sufficiently evidenced under the applicable profile.
3. **Required causal ordering/mechanism conditions** — necessary temporal, relationship, encounter, transmission, or control-mechanism conditions identified by the profile are sufficiently evidenced.
4. **Material contradiction review** — known material contradicting evidence is addressed; no unresolved decisive contradiction remains under the profile.
5. **Material alternative review** — alternatives relevant to the profile and bounded Investigation scope are evaluated enough that confirmation does not merely mean `best available hypothesis`. Compatible co-contributors do not have to be excluded.
6. **Coverage adequacy** — negative/exclusion conclusions relied upon by confirmation satisfy REF-001–REF-005.
7. **Named standard/profile provenance** — the evidence/decision standard being satisfied is explicit and version/time aware.
8. **Confirmation authority resolved** — Capability Authorization or another later accepted authority mechanism permits the confirming principal/process for the claim/context.
9. **Confirmation action/provenance** — who/what confirmed, when, under which standard, and on which evidence cut is retained.

## Authority boundary

Phase 004 does **not** decide which job title, team, service, automated process, or vendor source is allowed to confirm a cause. Phase 005 owns source/actor authority and capability refinement.

No human title automatically confers confirmation authority. No automated reasoning process automatically has confirmation authority either.

Automated confirmation remains possible in principle only when a later accepted confirmation policy/profile explicitly permits it, the required Capability Authorization resolves appropriately, and the evidence gate is satisfied. Until such semantics exist for a claim class, automation must stop at an evidence-supported non-confirmed status.

## Rules

- `supported` can be operationally useful without being `confirmed`.
- Confirmation does not require absence of every uncertainty; it requires satisfaction of the explicit profile and no unresolved decisive limitation under that profile.
- Time pressure, incident closure, ranking dominance, management preference, or lack of competing telemetry cannot substitute for the confirmation gate.
- Confirmation never grants access to restricted supporting evidence.

## Non-goals

- deciding confirmation approvers/roles;
- selecting approval workflow or IAM implementation;
- defining legal/audit-grade causality guarantees;
- universal causal threshold numbers.
