# ARCH-056 — Canonical vs Derived Store Roles

**Status:** Accepted

Every persistence/index component SHALL be classified as canonical retained record, source-payload storage, or rebuildable derived projection/cache.

Two stores may not silently become competing truth owners for the same architecture-owned state.
