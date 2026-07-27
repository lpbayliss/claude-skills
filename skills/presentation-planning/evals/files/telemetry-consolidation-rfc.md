# Telemetry consolidation proposal

Status: Draft for architecture review
Owner: Platform Observability

## Current state

Four product groups currently use separate telemetry SDK wrappers and two vendors. Service teams configure exporters themselves. The platform team sampled 62 production services in May:

- 41 use the shared legacy wrapper;
- 13 call a vendor SDK directly;
- 8 have no structured traces;
- 19 use metric label keys that conflict with another team’s definition.

During the previous two quarters, the incident review catalogue linked 11 of 47 severity-1 or severity-2 incidents to missing, inconsistent, or unusable diagnostic context. This is an association from post-incident reviews, not proof that telemetry consolidation would have prevented all 11.

Annual vendor and storage spend is estimated at AUD 1.4 million. Finance has not validated the allocation model below service level.

## Proposal

Adopt OpenTelemetry APIs and semantic conventions at application boundaries. Route signals through a managed collector tier owned by Platform. Keep vendor exporters behind the collector so service code does not depend directly on a backend.

Phase 1 would cover HTTP service telemetry for six volunteer services. It would not migrate product analytics, security audit logs, mobile telemetry, or existing dashboards.

## Claimed benefits

- one application-level instrumentation contract;
- backend changes without service-code changes;
- central cardinality and sensitive-attribute controls;
- more consistent cross-service context propagation;
- lower duplicated SDK maintenance.

No production evidence yet establishes reduced incident duration or cost. Phase 1 is intended to measure migration effort, signal completeness, cardinality, and collector reliability.

## Key risks

- the collector tier becomes shared operational infrastructure;
- unstable semantic conventions may require versioned mappings;
- dual publishing could temporarily increase cost;
- teams may lose vendor-specific features;
- incorrect collector policy could drop required diagnostic context;
- the platform team has no accepted support SLO for the collector tier.

## Alternatives

1. Keep the current model and publish better wrapper guidance.
2. Standardise directly on the current primary vendor SDK.
3. Adopt OpenTelemetry APIs but let teams operate exporters.
4. Adopt OpenTelemetry with a centrally managed collector tier (proposal).

## Requested architecture decision

Approve Phase 1 design work and implementation for six volunteer services, contingent on:

- a collector failure/isolation design;
- an attribute privacy and cardinality policy;
- a rollback path to existing exporters;
- named service owners;
- baseline and phase-exit measures;
- security review of collector data handling.

This is not approval for organisation-wide migration or vendor consolidation.
