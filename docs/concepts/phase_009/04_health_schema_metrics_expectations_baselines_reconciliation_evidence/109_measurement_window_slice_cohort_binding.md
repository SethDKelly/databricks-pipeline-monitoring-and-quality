# INTG-109 — Measurement Window, Slice & Cohort Binding

**Status:** Accepted — Phase 009 Group 04

DQX filters, data-profiling windows/slices, metric-view fields/filters/parameters and query predicates can all change the measured population.

Every Observation/Assessment must preserve exact population/window/slice/cohort semantics. A whole-table metric cannot silently satisfy a subgroup proposition, and a sampled/sliced result cannot become global coverage.
