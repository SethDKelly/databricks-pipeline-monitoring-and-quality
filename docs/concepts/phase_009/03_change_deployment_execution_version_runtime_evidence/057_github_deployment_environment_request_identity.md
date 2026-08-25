# INTG-057 — GitHub Deployment & Environment Request Identity

**Status:** Accepted — Phase 009 Group 03

A GitHub Deployment object can bind a deployment request to repository, resolved SHA/ref and environment. Environment-referencing Actions jobs can create deployment/deployment-status records.

This is strong GitHub-side deployment-request identity. It is not automatically the Databricks Deployment truth owner or proof that the target accepted/activated the requested state.
