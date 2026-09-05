# CKR-J Routing Conservation Matrix

**Status:** CANDIDATE — CKR-J IN EXECUTION

## Purpose

CKR-J changes discovery, stable-reference resolution and drift enforcement only. It must make canonical ownership cheaper and more deterministic to reach without creating another semantic authority, rewriting accepted contract meaning, undoing CKR-I progressive disclosure, or making design history undiscoverable.

## Conservation rules

| Surface | Before CKR-J | CKR-J accepted target | Must not become |
|---|---|---|---|
| OKF | portable routing projection; some domain text still reflects pre-CKR-I ownership | canonical-first current-truth routing with history explicitly labeled as provenance | semantic authority, contract copy, or source of current truth |
| Stable ID | frozen family/range + exact occurrence search + manual authority resolution | exact accepted ID → exactly one inventoried canonical stable definition → renderer-neutral `owner_path::ID` locator | first-match search, line-number identity, duplicated contract registry, or forced document expansion |
| ARCH stable definitions | CKR-I compact segment owners using explicit stable-ID indexes or named stable-contract lists | retain both accepted compact forms as canonical addressability | 500 duplicated headings or restoration of the Phase 010 one-file-per-ID tree |
| Historical stable-ID search | mixed into default occurrence result set | explicit secondary/on-demand history discovery | current-owner selection or proof that a historical occurrence is current |
| Agent routing | root authority + optional OKF + manual exact-hit resolution | root authority + canonical-first routing + deterministic exact owner resolver | full-corpus preload, tool-specific semantic forks, or memory/search-order authority |
| Knowledge maintenance | broken links and direct resource impact checks | current-route drift checks plus body-link impact review where routing depends on secondary canonical links | automatic semantic edits generated from OKF |
| CI | structural OKF/reference/status checks | structural checks + exact canonical stable-reference coverage + route-state enforcement + adversarial drift guards | domain-health/production-readiness claim |
| Phase 001–010 | design-history/provenance after migration | remains fully discoverable for rationale/history/change reconstruction | alternate current semantic owner |

## Stable-reference invariants

1. Accepted ranges remain exactly SYN-001–035, REF-001–030, AUTH-001–053, HLTH-001–066, OPS-001–123, EXPL-001–160, INTG-001–270 and ARCH-001–500.
2. The accepted total remains **1,237 stable IDs**.
3. Every accepted ID must have exactly one canonical stable definition inside the inventoried `target_documents` for its family.
4. Accepted canonical definition forms are intentionally bounded: **737 definition headings** for SYN/REF/AUTH/HLTH/OPS/EXPL/INTG, **416 `Stable ID index` members** in seven CKR-I ARCH segments, and **84 named `Stable contracts` list members** in the runtime/health/Lineage/Impact ARCH segment.
5. A definition-like occurrence outside the inventoried target set cannot become canonical merely because it resembles a definition.
6. Default exact-ID resolution returns the canonical owner only.
7. Historical occurrence discovery is separate and opt-in; it never competes with current ownership.
8. The stable locator is `owner_path::ID`. The owner path is selected by the ownership inventory; the ID token is the stable section selector independent of whether the accepted owner form is a heading, index member or stable-contract list member.
9. Line numbers, repository search rank, Markdown-renderer slug generation, file recency, Git history and first textual occurrence are not stable identity.
10. The stable-reference registry/routing machinery contains no contract prose and cannot strengthen, weaken, supersede or reinterpret contract meaning.
11. Missing/duplicate canonical stable definitions are routing/conformance failures, not permission to infer meaning from history or memory.
12. CKR-J may not manufacture per-ID canonical prose for ARCH where CKR-I intentionally conserved the accepted architecture at segment level.

## OKF invariants

1. OKF remains Open Knowledge Format v0.2 under the accepted DMTZ producer profile.
2. `knowledge/` is a routing/catalog projection, never DMTZ Assertion Authority or semantic ownership.
3. Stable current semantic domain routes must point primarily to a current canonical resource after CKR-I.
4. A body may link design history only for explicitly historical/provenance use; it may not describe Phase 010 as current ARCH authority after CKR-I.
5. The seven domain routes stay compact; CKR-J does **not** create one OKF entry per stable ID.
6. `stable`, `verified`, `stale_after`, provenance and tags retain OKF lifecycle/routing meaning only.
7. Broken/moved canonical links fail routing validation; they do not imply the underlying DMTZ constraint disappeared.
8. Canonical changes may create routing review candidates but do not automatically make every linked OKF concept stale.

## Agent-routing invariants

1. Human-selected task/scope remains the starting authority boundary.
2. Current semantic owner outranks OKF, search order, phase chronology, vendor guidance, model/tool memory and generated indexes.
3. A known stable ID may bypass OKF and resolve directly to its canonical owner locator.
4. A semantic question without a known ID may use one bounded OKF route, then the canonical owner, then exact IDs only as needed.
5. History is loaded only for a concrete provenance/rationale/change question or explicit historical occurrence search.
6. Agents must not preload the full stable-ID corpus or all OKF concepts merely because deterministic routing exists.
7. Agent/tool adapters may project the shared routing rule but may not maintain independent semantic routing tables.
8. Implementation traceability must cite accepted stable IDs plus the resolved canonical owner/evidence; it may not treat a routing helper result as implementation proof.

## Drift-enforcement invariants

1. All eight stable-ID families must remain `canonicalized` before CKR-J can be accepted.
2. Canonical stable-definition coverage must remain **1,237/1,237: 737 headings + 416 ARCH index members + 84 ARCH stable-contract list members**, with no duplicate owner resolution inside family target documents.
3. Stable OKF domain routes may not regress to Phase 003–010 current-owner language after CKR-J cutover.
4. The routing manifest is a machine-checkable projection; it cannot change semantic authority or invent a new family/range.
5. Agent routing surfaces must continue to name the ownership inventory and canonical exact-ID resolver.
6. Historical discovery must remain explicitly separated from default resolution.
7. Any future canonical path move must either update the inventory/route atomically or fail validation.
8. Conformance failure preserves the prior accepted semantic meaning; it does not authorize automatic semantic repair.

## Non-goals

CKR-J does not add a knowledge server, remote catalog service, vector index, graph database, MCP server, Attested Computation runtime, new stable IDs, 500 new ARCH definition sections, implementation traceability records, product code, or provider-specific agent memory. CKR-K remains responsible for whole-retrofit consolidation and exit acceptance.
