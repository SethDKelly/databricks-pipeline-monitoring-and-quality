# Phase 010 Group 03 — Identity / Authority / Disclosure Scenario Review

**Suite:** IAD03-01–IAD03-84

All scenarios pass against ARCH-081–ARCH-132.

| ID | Scenario | Expected architecture result |
|---|---|---|
| IAD03-01 | Databricks table renamed with stable source ID | preserve source binding/canonical entity; record name history |
| IAD03-02 | Table deleted and recreated with same name but new stable ID | new source incarnation; no automatic same entity |
| IAD03-03 | GitHub repository renamed but numeric repository ID stable | preserve repository source identity; update descriptive path |
| IAD03-04 | GitHub path reused by a different repository | do not merge by path |
| IAD03-05 | Collibra asset name matches UC table name | candidate only; explicit mapping evidence required |
| IAD03-06 | Source IDs differ but governed crosswalk says same business entity | bind both source identities to canonical entity with crosswalk provenance |
| IAD03-07 | Two crosswalk sources disagree | identity mapping conflicting; exact cross-system proposition blocked |
| IAD03-08 | Analyst manually maps entities without mapping authority | annotation/provisional mapping only |
| IAD03-09 | Same email appears in GitHub and Databricks | principal mapping candidate, not identity proof |
| IAD03-10 | Upstream IdP immutable ID maps both accounts | strong principal binding where verified |
| IAD03-11 | Human owns service principal | identities remain distinct; management relation explicit |
| IAD03-12 | Job runs as service principal after human trigger | trigger actor and run-as principal remain separate |
| IAD03-13 | User impersonation evidenced | acting/impersonation relation explicit; identities not merged |
| IAD03-14 | Current group membership exists, incident-time history missing | current authorization answer possible; historical membership unresolved |
| IAD03-15 | Historical membership retained and effective then | usable historical authorization input |
| IAD03-16 | User removed from group today | prior membership history remains; current permission reevaluates |
| IAD03-17 | Entity IDs collide across tenants | tenant boundary prevents cross-tenant identity |
| IAD03-18 | Shared enterprise object intentionally federated across tenants | requires explicit governed federation mapping |
| IAD03-19 | Discovered table is technically visible but not in Monitoring Scope | accessible ≠ monitored; remain out-of-scope if explicit rule says so |
| IAD03-20 | In-scope table is inaccessible to integration principal | scope remains in-scope; collection capability degraded |
| IAD03-21 | Selector includes `critical` Collibra classification | selector revision + classification authority/provenance retained |
| IAD03-22 | Collibra temporarily unavailable during selector evaluation | membership unresolved/unknown; not automatically excluded |
| IAD03-23 | Scope selector revision expands to new domain | new effective scope; earlier coverage not rewritten |
| IAD03-24 | Scope selector revision removes asset | historical earlier in-scope state retained |
| IAD03-25 | Account-wide negative claim uses only one workspace materialization | insufficient population coverage |
| IAD03-26 | Materialization includes explicit exclusions | exclusions visible with governing rule |
| IAD03-27 | Materialization has unresolved candidates | strong `none/all` claim narrowed or blocked |
| IAD03-28 | Source collection succeeds for 90 of 100 expected entities | scope population known; observation coverage incomplete |
| IAD03-29 | Admin can query every table | permission does not expand Monitoring Scope |
| IAD03-30 | Scope rule owner changes | new governance state; no authority inference from ownership alone |
| IAD03-31 | Unity Catalog table owner asserts business definition | vendor ownership alone not DMTZ semantic Assertion Authority |
| IAD03-32 | Organization authority rule maps Collibra steward for business definition | steward assertion can be authoritative for exact mapped facet |
| IAD03-33 | Same steward asserts data-quality pass | business-definition authority does not transfer to health truth |
| IAD03-34 | GitHub code owner asserts deployment occurred | review responsibility not deployment truth authority by default |
| IAD03-35 | Two co-authoritative semantic sources disagree | retain conflict until explicit resolver |
| IAD03-36 | Newer assertion conflicts with older co-authoritative source | recency alone does not resolve |
| IAD03-37 | Authority rule explicitly prefers source A for this facet | apply bounded precedence and retain competing assertion history |
| IAD03-38 | Fallback source configured but primary is merely inconvenient | fallback not active without governed activation condition |
| IAD03-39 | Primary source unavailable and fallback condition evidenced | fallback may resolve within exact rule scope |
| IAD03-40 | Authority rule changes after incident | current resolution can change; incident-time rule remains historical |
| IAD03-41 | Senior executive says model result is root cause | title/seniority not automatic causal-confirmation authority |
| IAD03-42 | Authorized confirmer + insufficient causal evidence | claim cannot become confirmed |
| IAD03-43 | Sufficient evidence + confirmer lacks authority | claim cannot become confirmed |
| IAD03-44 | Sufficient evidence + authorized confirmer | confirmation eligible subject to exact REF/AUTH conditions |
| IAD03-45 | Databricks service principal has SELECT | source access fact only; not requester authorization or Assertion Authority |
| IAD03-46 | DMTZ policy allows inspect but UC denies source query | organization authorization allowed; source enforcement unavailable/denied separately |
| IAD03-47 | UC permits raw query but DMTZ policy denies user raw-data view | requester denied despite service/source access |
| IAD03-48 | GitHub App has repo metadata read but not Actions permission | authorization proposition differs by exact action |
| IAD03-49 | App installed enterprise-wide but not repo permission | enterprise permission does not imply repository permission |
| IAD03-50 | Collibra responsibility inherited from parent community | usable only according to mapped inheritance/authority rule |
| IAD03-51 | Immuta persona grants audit access | source-local capability; not DMTZ export/publish permission |
| IAD03-52 | Group allow and direct deny conflict with no composition rule | authorization `conflicting`, no invented deny-wins |
| IAD03-53 | Explicit policy defines deny precedence for one capability | apply that capability-specific resolver |
| IAD03-54 | Missing authorization rule | unknown/unavailable, not allow |
| IAD03-55 | Authorization backend unavailable while cached prior allow exists | prior allow not silently current unless governed cache/fallback rule permits |
| IAD03-56 | Material decision journal records allow | proves decision evaluation occurred, not action/enforcement |
| IAD03-57 | Later replay yields allow but no historical decision exists | label replay-derived; do not claim actor was actually authorized then |
| IAD03-58 | Actual historical deny followed by later policy change | retain actual deny; current policy does not rewrite it |
| IAD03-59 | Past actor was authorized then but revoked now | historical state yes; current permission no |
| IAD03-60 | Current requester can inspect old authorization audit | only if current disclosure permits it |
| IAD03-61 | Service principal may read sensitive audit table | application processing permission does not grant user raw audit view |
| IAD03-62 | Break-glass grant expires | current grant inactive; historical emergency action remains auditable |
| IAD03-63 | Break-glass user confirms causal claim without confirmation authority | emergency access does not manufacture Assertion Authority |
| IAD03-64 | User may view conclusion but not basis | show authorized conclusion with required limitations; basis withheld |
| IAD03-65 | User may view basis references but not payloads | show authorized references/opaque forms only |
| IAD03-66 | Basis item path itself sensitive | omit/redact path independent of conclusion visibility |
| IAD03-67 | Hidden basis item count sensitive | do not reveal hidden count |
| IAD03-68 | Three basis items visible, two withheld | internal basis remains five; visible projection need not expose total |
| IAD03-69 | Redaction removes name but would merge two distinct subjects | transformation rejected/narrowed |
| IAD03-70 | Coarse summary would hide material `coverage incomplete` limitation | summary must retain limiting language or be withheld |
| IAD03-71 | Redacted status changes `unknown` to `healthy` | invalid strengthening; reject projection |
| IAD03-72 | Opaque lineage path shown as direct dependency | invalid; opacity cannot imply directness/path completeness |
| IAD03-73 | User can inspect current result but export is denied | in-app view allowed; export denied separately |
| IAD03-74 | User can export to internal channel but not external customer | delivery/audience context changes authorization |
| IAD03-75 | Requester saw basis last month before revocation | prior visibility does not create current permission |
| IAD03-76 | Retained evidence is COLD_PINNED | retention state does not grant disclosure |
| IAD03-77 | Provenance stub survives payload expiry | stub visibility independently authorized; payload cannot be reconstructed |
| IAD03-78 | Authorized user requests restore from cold archive | authorization may permit restore request; restore action remains separately audited |
| IAD03-79 | Cross-residency request can use result but payload movement prohibited | resolve/provide permitted projection without centralizing payload |
| IAD03-80 | Cross-shard reference existence is classified | even reference may be withheld |
| IAD03-81 | Repeated coarse queries would reveal restricted group membership | mosaic-aware policy narrows/withholds later projection |
| IAD03-82 | One restricted basis item among independent sibling statements | restrict affected basis/statement only; authorized siblings can remain |
| IAD03-83 | Vendor capability documented but tenant lacks required entitlement | capability unavailable for that deployment; no architecture assumption |
| IAD03-84 | Group 04 connector starts with canonical identity/scope/auth primitives | correct handoff; connector must not invent source-specific truth/permission semantics |

## Result

**IAD03-01–IAD03-84 pass.** The suite validates identity continuity/conflict, Monitoring Scope denominators, explicit authority, composed authorization, actual-versus-replay decision history, itemwise disclosure, residency and vendor-deployment variability without introducing a universal IAM/authority score.