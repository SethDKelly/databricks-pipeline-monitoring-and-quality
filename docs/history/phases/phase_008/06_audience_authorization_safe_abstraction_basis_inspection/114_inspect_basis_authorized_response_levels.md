# EXPL-114 — `inspectBasis` Authorized Response Levels

**Status:** Accepted — Phase 008 Group 06

## Requirement

`inspectBasis` resolves the requester-specific authorized projection of statement basis. Depending on policy it may return:

- exact basis/evidence references and values;
- source/provenance class without exact identity;
- basis role/status without underlying values;
- redacted references;
- authorized opaque-existence/limitation indication;
- or safe non-disclosure.

No level is automatically safe. Counts, source classes, timestamps, redaction markers and existence signals may themselves be sensitive.