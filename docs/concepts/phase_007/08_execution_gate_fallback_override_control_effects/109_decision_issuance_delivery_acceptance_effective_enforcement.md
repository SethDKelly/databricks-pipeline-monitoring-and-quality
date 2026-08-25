# OPS-109 — Decision Issuance, Delivery, Acceptance & Effective Enforcement

**Status:** Accepted — Phase 007 Group 08

## Purpose

Refine REF-025/026 so control intent and external runtime behavior remain separately evidenced.

## Control chain

A decision may have independently evidenced stages:

**decision recorded/issued → delivered to control boundary → accepted/acknowledged → effective Gate constraint/removal → downstream execution outcome**.

Not every implementation exposes every stage; missing stages remain unknown rather than inferred.

## Rules

- framework decision emission is not external enforcement proof;
- generic control-service health is not opportunity-specific enforcement;
- acknowledgement can be evidence without universally proving the requested behavior took effect;
- enforcement binds exact target/opportunity/action/interval;
- a decision arriving after the controlled start already occurred cannot retroactively govern that execution opportunity;
- restricted control details may be projected safely without strengthening enforcement state.

Execution History owns actual start/run facts.