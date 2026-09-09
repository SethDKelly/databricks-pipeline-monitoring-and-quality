# ARCH-075 — Archive Restore Semantics

**Status:** Accepted

Restoring cold evidence SHALL preserve original durable IDs, provenance, time coordinates, digest/integrity context and retention history rather than creating a new evidence occurrence.

Restore latency may vary by service class; restore failure remains unavailability, not domain absence.
