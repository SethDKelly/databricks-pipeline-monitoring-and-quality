# ARCH-160 — Schema-Evolution Tolerance

**Status:** Accepted

Adapters are designed for additive source-schema evolution and preserve unrecognized fields safely where policy permits.

New fields do not automatically break ingestion, but their semantics remain unknown until parser/schema support is verified.
