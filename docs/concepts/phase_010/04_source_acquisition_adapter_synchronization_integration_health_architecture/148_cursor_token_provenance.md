# ARCH-148 — Cursor / Token Provenance

**Status:** Accepted

Opaque page tokens, cursors and source sequence markers remain source-owned continuation artifacts tied to the exact request and surface that produced them.

They are not portable across source versions or query shapes unless the vendor contract explicitly guarantees that behavior.
