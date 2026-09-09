# EXPL-078 — Capability Authorization & Permission Question

**Status:** Accepted — Phase 008 Group 04

## Requirement

Questions such as `can Alice see this?`, `can this responder retry?`, `can they activate/release the safeguard?`, or `can they override the gate?` bind principal + named capability + subject/context/time.

Responsibility, Policy Context, Classification, Assertion Authority, monitoring scope, administrator status or repository ownership do not grant permission.

Permission to attempt an action does not prove the action occurred or succeeded. Missing authorization evidence is not permission.