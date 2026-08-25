# Group 02 Scenario Review

**Status:** PASS — GOV02-01–GOV02-48

1. **GOV02-01** UC `catalog.schema.table` resolves current platform object → platform identity supported; ecosystem identity separate.
2. **GOV02-02** UC object renamed without governed crosswalk → rename continuity unresolved.
3. **GOV02-03** table deleted/recreated with same name → same logical Entity Identity not inferred.
4. **GOV02-04** Collibra asset UUID persists while display name changes → Collibra resource identity preserved.
5. **GOV02-05** Collibra asset and UC table share name only → cross-system identity unresolved.
6. **GOV02-06** explicit governed UC↔Collibra mapped identifier → bounded crosswalk supported.
7. **GOV02-07** GitHub repository ID known → repository identity supported, data identity not inferred.
8. **GOV02-08** Databricks external group synchronized from IdP → Databricks membership is a projection; upstream source retained.
9. **GOV02-09** workspace-local legacy group → not treated as account-level UC group.
10. **GOV02-10** no Monitoring Scope field exists in any source → scope unknown/unsupported, not out of scope.
11. **GOV02-11** GitHub custom property `monitoring_scope=required` under explicit authority rule → valid Monitoring Scope assertion.
12. **GOV02-12** Collibra operating-model `scope` exists → not converted into Monitoring Scope.
13. **GOV02-13** UC table comment provides technical description → semantic assertion only at authorized facet.
14. **GOV02-14** AI-generated UC comment saved → origin does not grant semantic authority.
15. **GOV02-15** Collibra governed Business Definition facet designated authoritative → business semantic assertion supported.
16. **GOV02-16** UC object owner = platform owner → not automatically business owner/accountable party.
17. **GOV02-17** GitHub CODEOWNERS team → code-review responsibility only.
18. **GOV02-18** Collibra Owner responsibility directly assigned → governed responsibility if that role/type is authoritative.
19. **GOV02-19** Collibra responsibility inherited from domain → inheritance preserved rather than rewritten as direct assignment.
20. **GOV02-20** UC governed tag under accepted sensitivity scheme → Classification assertion may be authoritative.
21. **GOV02-21** ordinary UC/Collibra free-form tag → no Classification authority without explicit scheme rule.
22. **GOV02-22** Collibra Data Class accepted by governed workflow → Classification supported for that scheme.
23. **GOV02-23** Immuta tag targets policy → policy metadata only, not automatically Classification truth.
24. **GOV02-24** Collibra and UC classifications conflict under co-authority → conflict retained.
25. **GOV02-25** Collibra policy asset provides policy text → does not prove subject applicability/enforcement.
26. **GOV02-26** UC privilege/ABAC applies to table → UC access-policy context supported.
27. **GOV02-27** Immuta subscription policy applies to registered data source/user → Immuta authorization input supported.
28. **GOV02-28** no explicit Assertion Authority registry → source precedence remains unresolved, not newest-wins.
29. **GOV02-29** governed repository authority rule names Collibra for business definition → conditional authority valid if rule provenance/standing is satisfied.
30. **GOV02-30** UC direct grant visible → current UC capability authorization supported for exact privilege.
31. **GOV02-31** TABLE_PRIVILEGES omits grants visible only through broader grant inspection → absence in relation is not deny/no-grant.
32. **GOV02-32** Immuta registered user has direct UC grant but Immuta policy revokes access → effective authorization uses integration-specific composition.
33. **GOV02-33** non-Immuta user has UC grant → Immuta state is not assumed to govern that user.
34. **GOV02-34** Collibra user can edit asset → no underlying table SELECT permission inferred.
35. **GOV02-35** GitHub ruleset blocks branch update → repository authorization only; no Databricks capability inferred.
36. **GOV02-36** Databricks audit event inside documented retention → candidate historical governance evidence.
37. **GOV02-37** historical UC grant older than available audit history with no retained export → as-known grant replay unsupported/partial.
38. **GOV02-38** Collibra attribute history logging disabled → empty history cannot prove attribute never changed.
39. **GOV02-39** Immuta event older than default audit retention and no export → historical authorization input unavailable.
40. **GOV02-40** GitHub governance event older than 180 days without streaming/export → audit reconstruction unavailable.
41. **GOV02-41** current UC tag assignment exists, historical assignment record missing → current Classification possible; historical Classification unresolved.
42. **GOV02-42** requester cannot see UC object through privilege-filtered Information Schema → not-returned does not prove object absent.
43. **GOV02-43** Collibra view permission hides related asset → hidden relation not interpreted as nonexistent.
44. **GOV02-44** authority-preferred source unavailable and no fallback rule → authority unresolved; secondary source not promoted.
45. **GOV02-45** explicit fallback rule activates on evidenced outage → fallback standing may apply only to bounded proposition/time.
46. **GOV02-46** Collibra absent → business-governance capability classified by remaining sources/gap; no benign default.
47. **GOV02-47** Immuta absent → UC authorization remains evaluable for UC scope; Immuta-specific policy propositions become not applicable/unsupported as appropriate.
48. **GOV02-48** Group 03 receives resolved repo/UC/Collibra/Immuta/principal identity mappings → still must independently prove revision→deployment→run→version association.

All scenarios preserve INTG-001–INTG-022, AUTH-001–AUTH-053 and the accepted evidence/time boundaries.
