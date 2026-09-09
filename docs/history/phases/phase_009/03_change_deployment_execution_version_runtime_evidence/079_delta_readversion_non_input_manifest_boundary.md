# INTG-079 — Delta `readVersion` Non-Input-Manifest Boundary

**Status:** Accepted — Phase 009 Group 03

Delta history `readVersion` is retained with the semantics of the table transaction/operation being described. It is not accepted as a universal manifest of every upstream table/version read by arbitrary Spark/SQL work.

The framework must not transform one Delta-history field into multi-input consumption truth by naming convenience.
