# Group 02 Source Capability Matrix

Support is proposition + source set + context bound. `Conditional` means the surface can support the proposition only after an explicit framework authority/mapping rule or environment feature is established.

| Proposition / capability | Primary evaluated surfaces | Group 02 result | Key boundary / residual gap |
|---|---|---|---|
| Current Unity Catalog object identity | UC namespace/API/Information Schema + metastore/workspace context | Supported in platform scope | Ecosystem identity, rename/recreate continuity and cross-system identity still require crosswalk evidence |
| Collibra resource identity | Asset/domain/community UUID | Supported in Collibra scope | UUID does not prove equivalence to UC/GitHub/Immuta object |
| Repository identity | GitHub repository ID/coordinates + revision/path | Supported in repository scope | Not data-asset identity by default |
| User/group/service-principal identity used by UC | Databricks account identities/SCIM; external IAM when configured | Partially supported | Upstream IAM source and historical membership must be identified; workspace-local legacy groups differ |
| Cross-system Entity Identity | Explicit mapped identifiers/relations/configuration | Partially supported | No universal native crosswalk discovered; name/timestamp joins prohibited |
| Monitoring Scope | None natively; candidate governed repo property/config/Collibra attribute | Unsupported out of box / Conditional | Framework must define authoritative vocabulary, subject binding and history |
| Business Semantic Definition | Collibra governed asset attributes/relations when designated | Conditional | Authority depends on operating model; optional product |
| Technical description/schema declaration | Unity Catalog metadata/comments; repository definitions | Partially supported | Current declaration not realized state; comments are not authority by origin |
| Responsibility Assignment | Collibra Responsibilities; narrow UC owner/CODEOWNERS context | Conditional / Partially supported | Must map exact responsibility type; UC owner and CODEOWNERS are not general business ownership |
| Classification | UC governed tags; Collibra Data Classes | Conditional | Explicit scheme authority required; ordinary Collibra tags/Immuta tags are not Classification truth by default |
| Policy Context documentation | Collibra policy/governance assets where configured | Conditional | Policy text/reference authority may differ from subject applicability and enforcement |
| UC data-access policy/context | UC privileges/ownership/workspace restrictions/ABAC | Supported for UC securables | Current-state focus; preview/Beta features and principal-filtered metadata must be explicit |
| Immuta-managed data-access policy/context | Immuta subscription/data policies | Supported for registered Immuta scope | Integration/user registration and remote-platform interaction are material |
| Assertion Authority rules | No native universal source | Unsupported out of box / Conditional | Requires explicit governed authority-rule registry; vendor roles/ownership cannot substitute |
| Capability Authorization — UC data access | UC privilege/ownership/ABAC/workspace state + principal identity | Supported for exact UC action | Not framework-wide capability; historical authorization requires audit/history |
| Capability Authorization — Immuta-governed UC access | Immuta policy/identity metadata + UC state | Partially supported as composed proposition | Registered vs unregistered users and integration mode matter; no universal source precedence |
| Capability Authorization — Collibra actions | Collibra global/resource permissions | Supported for Collibra actions | Does not grant underlying data access or framework action capability |
| Capability Authorization — GitHub actions | Repository/org roles, rulesets, CODEOWNERS where relevant | Supported for repository actions | Does not grant data-platform/framework capability |
| Current UC metadata visibility | Information Schema / APIs | Supported but observer-relative | Result filtering means non-return is not absence; TABLE_PRIVILEGES has documented MANAGE-view limitation |
| Databricks governance history | `system.access.audit` + source event coverage | Partially supported | 365-day free retention, Public Preview table, region/event coverage; long-term replay needs external retention |
| Collibra governance history | Resource history | Partially supported | History logging can be disabled for selected attributes; field-level completeness must be known |
| Immuta authorization history | Application/query audit + IAM/remote-platform history | Partially supported | 90-day default unless exported; full effective replay may require upstream IAM and UC history |
| GitHub governance history | Org/enterprise audit log | Partially supported / Conditional | Plan/scope dependent; 180-day general retention, seven-day Git events |
| Optional Collibra/Immuta absence | Explicit source-presence profile | Supported as degradation finding | Absence cannot create benign governance defaults |

## Consolidated gaps carried forward

1. A concrete authoritative **Monitoring Scope registry** is not supplied out of the box.
2. A concrete **Assertion Authority rule registry** is not supplied out of the box.
3. Cross-system data-asset identity requires an explicit governed **Entity Identity crosswalk**.
4. Historical governance replay is retention/configuration limited across all evaluated platforms unless independently retained.
5. External IAM/IdP authority is environment-specific and remains unverified until the actual identity provider/provisioning mode is known.
6. Effective authorization across Immuta + Unity Catalog is a composed, population-specific proposition rather than a single-source lookup.
7. Observer-relative metadata visibility must not be interpreted as absence.
