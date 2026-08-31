# ARCH-434 — API Schema Versioning

**Status:** Accepted

Externally consumed request/response/event schemas are versioned and compatibility-managed independently from canonical table physical layout.

Breaking serving changes require an explicit version/migration rather than silent reinterpretation of historical clients.