# Metrics Implementation Guide

Use this reference when adding, migrating, querying, visualizing, or alerting on metrics.

## Contents

- Repository discovery
- Instrumentation placement
- Naming, units, and dimensions
- Common metric shapes
- Product event concerns
- Dashboards and alerts
- Migration and rollout
- Verification

## Repository discovery

Find the established measurement path before editing:

- telemetry/bootstrap initialization;
- wrappers around metrics or analytics SDKs;
- instrument registries and naming constants;
- existing semantic conventions;
- event schemas and schema-version policy;
- collector/exporter configuration;
- dashboard, recording-rule, and alert definitions;
- tests or in-memory exporters;
- privacy, consent, retention, and data-classification rules;
- build, lint, typecheck, and test commands.

Search for comparable instrumentation and follow its lifecycle and dependency-injection pattern. Avoid creating instruments repeatedly on hot paths.

## Instrumentation placement

Instrument the authoritative state transition:

- Count a completed operation where completion is committed, not where a request first arrives.
- Count attempts separately from successful outcomes.
- Record latency around the scope named by the contract; state whether queueing, retries, and downstream time are included.
- For asynchronous work, use stable correlation and explicit lifecycle events rather than pretending enqueue-to-return is completion.
- For retries, expose attempt count and final outcome without double-counting the business result.
- For caches, distinguish lookup, hit, miss, stale serve, load success, and load failure only when each distinction is actionable.

Prefer one trusted emission point over duplicated call-site instrumentation.

## Naming, units, and dimensions

Follow the repository or telemetry system’s current convention. When no convention exists:

- use a stable domain-oriented name;
- encode units according to the selected telemetry standard rather than inventing suffixes blindly;
- keep descriptions explicit about population and semantics;
- use enums or allowlists for status, operation, component, reason class, and coarse route/template;
- never attach raw user IDs, request IDs, email addresses, prompts, exception messages, full URLs, file paths, SQL, or arbitrary tenant-provided strings as metric dimensions.

Estimate cardinality as the product of possible values across dimensions, then consider instances, environments, and retention. A dimension can be bounded individually but explosive in combination.

Use logs or traces for high-cardinality exemplars and investigation context. Metrics should retain bounded aggregate dimensions.

## Common metric shapes

### Request/service metrics

Start with user-visible latency, traffic, errors, and saturation when they answer the operating question. Define success from user outcome, not merely HTTP status, where the application has richer semantics.

### Queue and worker metrics

Useful shapes include arrival rate, completion rate, failure rate, queue age, queue depth, execution latency, retry count, and saturation. Queue depth alone can hide stalled old work; pair it with age when backlog delay matters.

### Ratios

Emit additive source counts and derive the ratio in the query layer when practical. This preserves aggregation and enables reconciliation. Protect zero denominators and label missing data correctly.

### Latency

Record a distribution with one documented unit. Choose buckets around meaningful user or SLO boundaries when explicit buckets are required. Verify clock and async boundary semantics.

### Resource/cost metrics

Tie consumption to a bounded service, operation, model, or tier when actionable. Avoid user-level or request-level dimensions. Pair cost with a useful outcome (for example, cost per accepted task) rather than optimizing raw spend alone.

## Product event concerns

Product events need stronger identity and time semantics than service counters:

- define actor and subject;
- define assignment/exposure separately from outcome for experiments;
- define event time versus ingestion time;
- use stable deduplication where delivery is at-least-once;
- define sessionization, funnel ordering, conversion window, re-entry, and cross-device behaviour;
- exclude staff, tests, bots, and synthetic traffic only through accepted rules;
- preserve consent and deletion obligations;
- version schemas compatibly and monitor unknown/malformed versions.

If a metric requires joining sources, document join keys, one-to-many behaviour, late-arriving data, and the authoritative side.

## Dashboards and alerts

A dashboard panel should state:

- question answered;
- exact metric contract/version;
- query and unit;
- population/window;
- useful comparison or baseline;
- owner and drill-down path.

Do not hide important denominator or missing-data behaviour in dashboard code.

Alert only when a human action is required now or soon. Define:

- symptom or imminent risk;
- threshold provenance or burn-rate policy;
- evaluation window and missing-data handling;
- severity, owner, runbook, and expected action;
- inhibition/deduplication and recovery semantics.

Do not copy a familiar threshold without workload evidence.

## Migration and rollout

When changing a definition or name:

1. Version or rename when meaning changes materially.
2. Dual-publish old and new only for a bounded comparison window.
3. Compare volume, dimensions, distribution, and known invariants.
4. Update queries, dashboards, alerts, docs, and consumers.
5. Mark the cutover time so historical discontinuities are visible.
6. Remove old emission and downstream artifacts after the agreed window.

Avoid permanent aliases that let two meanings share one name.

## Verification

Use the strongest available evidence:

1. Unit test instrument calls or event construction.
2. Test success, failure, retry, cancellation, and exclusion paths.
3. Inspect an in-memory/test exporter or local collector output.
4. Validate dimensions against allowlists and cardinality expectations.
5. Run query fixtures or recording-rule tests when repository tooling supports them.
6. Reconcile against an authoritative fixture/store.
7. Run repository format, lint, typecheck, and affected tests.
8. State production-only checks such as freshness, volume, and cost as rollout checks—not completed verification.
