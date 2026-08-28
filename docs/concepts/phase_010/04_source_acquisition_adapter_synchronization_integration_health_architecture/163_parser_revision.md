# ARCH-163 — Parser / Normalizer Revision

**Status:** Accepted

Every normalized record binds the parser/normalizer revision that produced it; reparsing old raw material produces a new derived interpretation linked to the predecessor.

Parser updates do not rewrite earlier as-known derived state silently.
