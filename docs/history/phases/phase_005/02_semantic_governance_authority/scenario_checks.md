# Phase 005 Group 02 — Scenario Checks

**Status:** Accepted

These scenarios apply Assertion Authority and AUTH-009–AUTH-015 to descriptive/governance state without defining Phase 006 metric/statistical behavior or selecting concrete vendors as universal authorities.

| Scenario | Governance question | Accepted result |
|---|---|---|
| Business definition vs technical schema description | different semantic facets have different authorities | both resolve independently; no conflict unless same facet/context disagrees |
| Git contract declares `customer_id`; runtime catalog shows it missing | declared schema meaning vs realized schema state | governance assertion remains; Observation/Change shows realized mismatch; health requires Expectation/Assessment |
| Source proposes rename `customer_id` → `customer_identifier` | is this rename or drop/add? | no semantic identity inferred from names alone; Change Intent/Semantic Definition/identity evidence required |
| Business key declared but duplicates observed | key meaning vs data integrity | authoritative key role remains semantic; uniqueness can independently violate an Expectation |
| Column added upstream | does every downstream consumer break? | no; compatibility is consumer/context-specific and belongs to later schema-health/Lineage analysis |
| Grain changes without column-name change | are existing metrics/Baselines still comparable? | semantic grain Change can trigger applicability/comparability review; no automatic global reset |
| Technical owner asserts business definition | responsibility exists; no semantic authority rule | assertion may be advisory; responsibility does not confer semantic authority |
| Two sources name different technical owners | same responsibility type/context | apply Responsibility Assignment authority; unresolved co-authoritative disagreement remains conflict |
| Operational `Tier 1` and confidentiality `Restricted` | different Classification schemes | both coexist; labels are not conflicting because schemes differ |
| Business-critical for one consumer only | criticality is context-specific | represent under explicit criticality scheme/context; no universal criticality projection |
| Crosswalk maps PHI to internal Restricted | is crosswalk authoritative? | crosswalk is separately governed with provenance; original source label retained |
| PHI classification exists but policy applicability unknown | can policy be inferred? | no; Classification may support applicability but Policy Context remains unknown until authoritative assertion resolves |
| Policy text authority differs from applicability authority | same policy, different governance targets | legitimate; authority can be separate for policy reference and subject/context applicability |
| Local definition is more specific than enterprise definition | no explicit specific-over-broad rule | specificity alone does not win; resolve by distinct context or preserve authority conflict |
| Upstream table is Restricted | does downstream inherit Classification automatically? | no; Lineage does not propagate Classification without explicit governed derivation rule |
| Domain has technical owner | does child table inherit owner? | no implicit responsibility inheritance; explicit rule required |
| Schema/tag inference labels a table sensitive | automated derivation exists | assertion retains derivation provenance; authoritative standing only if explicit authority rule grants it |
| Critical table is reachable downstream | does criticality establish Impact? | no; criticality can prioritize analysis but does not prove exposure/effect/consequence |
| Authoritative policy says control required | does that prove enforcement? | no; policy context and enforcement evidence remain separate |
| Business meaning changes historically | current definition differs from incident-time definition | historical effective/knowledge-time authority resolves the definition known/applicable then |

## Group result

All scenarios compose with the 24 accepted concepts and AUTH-001–AUTH-015. No additional truth-owning concept is required for semantic/governance authority or schema/DDL validation at this stage.

Schema/DDL checks remain expressible through Semantic Definition + Expectation + Observation/Change + Assessment, with Change Intent/Lineage/Impact supplying planned and downstream context. The technical location of checks remains deferred.
