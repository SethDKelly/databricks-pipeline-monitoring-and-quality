# ARCH-164 — Malformed Payload Quarantine

**Status:** Accepted

Malformed or unsupported payloads are retained/quarantined according to data-minimization policy with explicit parse status and source provenance.

Dropping malformed records silently is prohibited when their absence could affect coverage or later reasoning.
