# ARCH-478 — Optional Model / Search Health

**Status:** Accepted

Model, semantic/vector search and tracing/prompt facilities have independent availability/latency/quota/cost health so their failure is visible while deterministic exact paths continue where possible.

Their outage cannot become source or control degradation unless an explicitly optional user experience depends on them.