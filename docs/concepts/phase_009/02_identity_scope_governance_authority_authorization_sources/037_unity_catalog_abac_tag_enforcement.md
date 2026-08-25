# INTG-037 — Unity Catalog ABAC & Governed-Tag Enforcement

**Status:** Accepted — Phase 009 Group 02

Unity Catalog ABAC policies use governed tags as enforcement attributes for supported row-filter, column-mask and privilege-grant behavior. Tag-edit permissions are themselves security-sensitive because changing tags can change policy applicability.

Feature state matters: some ABAC capabilities, including GRANT policies and governed-tag system tables, are documented as Beta. Preview/Beta capability is recorded explicitly rather than normalized to GA behavior.
