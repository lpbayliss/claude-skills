# Detailed Specification Workflow

Read this reference for full, high-risk, migration, or multi-agent specifications. Apply only the sections relevant to the decision; it is a depth guide, not a mandate to produce every heading.

## Contents

- Repository grounding
- Behavior, boundaries, and invariants
- Requirement contracts
- Design comparison and decisions
- Verification design
- Change and operating safety
- Uncertainty and readiness
- Readiness-resolution and implementation work
- Traceability and maintenance

## Repository grounding

Inspect before prescribing:

- `CLAUDE.md`, `AGENTS.md`, contribution guidance, and local rules;
- module boundaries and comparable implementations;
- public APIs, events, schemas, storage ownership, migrations, and generated artifacts;
- tests, fixtures, build scripts, CI, lint, type-check, and test commands;
- deployment, feature-control, telemetry, alerting, and rollback conventions;
- ADRs, incidents, issues, support evidence, prior specs, and deprecations;
- branch and working-tree constraints if implementation may follow.

Record exact paths and executable commands. Distinguish direct evidence from inference. A path mentioned in an old document is not current repository evidence until verified.

For source conflicts, record:

| Topic | Source A | Source B | Practical impact | Resolution authority |
|---|---|---|---|---|

Do not resolve a conflict by silently ranking prose over executable behavior or vice versa. Current behavior may itself be the defect; accepted intent may itself be stale. State what each source proves and obtain the decision that matters.

## Behavior, boundaries, and invariants

Cover only materially relevant dimensions:

- primary user and operator journeys;
- alternate, validation, cancellation, timeout, and recovery flows;
- concurrency, retries, idempotency, ordering, and backpressure;
- lifecycle, migration, compatibility, deletion, and restoration;
- abuse, misuse, privacy, and threat scenarios;
- system, trust, data, ownership, and external dependency boundaries.

Write invariants and forbidden outcomes where positive examples leave dangerous ambiguity. Examples:

- An acknowledged write must not disappear after a single worker failure.
- A cached result must not cross authorization boundaries.
- A rollback must not reinterpret already persisted data silently.

Use a state machine, sequence diagram, data-flow diagram, or decision table when prose would hide transitions or ownership. Describe every diagram in prose so the contract survives rendering and accessibility differences.

## Requirement contracts

Use stable IDs when requirements must trace into decisions, tasks, tests, or rollout evidence:

- `FR-*` — functional behavior;
- `QR-*` — quality and service targets;
- `SEC-*` — security and privacy;
- `DATA-*` — integrity, ownership, retention, and lifecycle;
- `INT-*` — interfaces and compatibility;
- `OPS-*` — operations and release readiness.

A useful requirement has:

```text
[condition] + [subject] + must/should/may + [observable behavior] +
[object] + [measurable limit or qualification]
```

Keep one independently failing obligation per requirement. For every mandatory obligation, provide:

- evidence or rationale;
- acceptance authority;
- planned verification method;
- observable pass condition;
- pre-implementation evidence required before coding;
- post-implementation result/status, left pending until executed;
- unresolved target or dependency, if any.

Do not invent numeric targets. If the owner has not accepted a target, write a blocking placeholder or define a delegated measurement with a decision rule. An observed baseline is evidence, not automatically an SLO.

Separate:

- **Requirement:** what must be true.
- **Design decision:** how the selected system will make it true.
- **Task:** the bounded implementation work.
- **Evidence:** what proves the requirement after implementation.

## Design comparison and decisions

Start with the simplest credible design and the status quo where relevant. Compare serious options on:

- accepted requirements covered;
- responsibilities, interfaces, state, and data ownership;
- failure and degraded behavior;
- security and privacy boundaries;
- operational load, capacity, observability, and cost;
- migration, rollback, compatibility, and version skew;
- implementation and maintenance complexity;
- assumptions and evidence gaps.

Avoid straw alternatives and decorative option lists. If only one option is credible, explain why the others were excluded rather than pretending to compare equal candidates.

Capture a consequential decision with:

- context and decision question;
- decision owner and status;
- selected option and rationale;
- alternatives considered;
- positive and negative consequences;
- evidence that could trigger reconsideration;
- supersession relationship to prior decisions.

## Verification design

Create a requirement-to-verification matrix when traceability matters:

| Requirement | Planned method/evidence | Pre-implementation evidence complete? | Command or location | Pass condition | Result/status |
|---|---|---|---|---|---|

Choose test levels based on failure mode, not completeness theater. Consider, when material:

- unit and property checks for local rules and invariants;
- integration and contract checks for boundaries;
- end-to-end checks for critical journeys;
- migration and compatibility checks for state/schema evolution;
- performance and capacity evidence against accepted workloads and targets;
- security, privacy, and accessibility checks;
- resilience, backup/restore, and production evidence.

Include existing regression commands. Verify that tests encode the accepted interpretation rather than only mirroring the implementation.

## Change and operating safety

For production-facing work, prefer reversibility. If reversal is unsafe or impossible, require an explicitly accepted roll-forward/recovery strategy. Address as relevant:

- enable/disable and blast-radius controls;
- staged rollout cohorts or boundaries;
- objective expansion, stop, and rollback or recovery signals;
- old/new path compatibility and mixed versions;
- data written before, during, and after rollback or the point of no return;
- schema upgrade, downgrade, and roll-forward strategy;
- dependency failure, overload, resource exhaustion, and cost;
- telemetry, alerts, dashboards, runbooks, and ownership;
- backup, restore, disaster recovery, retention, and deletion.

A flag is one mechanism. It is only a valid rollback control when disablement is fast enough, the previous path still works, and data remains interpretable. For roll-forward-only work, record irreversibility, containment, backups or recovery, rehearsal evidence, and the authority accepting residual risk.

## Uncertainty and readiness

Classify each unresolved item:

- **Blocking** — implementation would invent intent or accept material unmanaged risk.
- **Delegated** — a named investigation can resolve it using explicit evidence and a decision rule.
- **Deferred** — intentionally outside the current contract, with no hidden dependency on current work.

Classify design latitude:

- **Fixed** — invariant, accepted decision, mandatory behavior, or compatibility contract.
- **Preferred** — established pattern; deviation requires rationale.
- **Open** — bounded implementation choice.

Do not use `Open` to disguise a product decision. Do not use `Deferred` for work required to make the current change safe.

Keep artifact lifecycle separate from implementation readiness. Record artifact status (`Draft`, `Proposed`, `Accepted`, and later lifecycle states) independently from the readiness verdict for a named scope.

Readiness requires more than filled headings. A **Ready** verdict requires:

- accepted problem and scope;
- no blocking product or safety question;
- mandatory requirements with planned verification and required pre-implementation evidence;
- credible design and boundary ownership;
- repository-grounded paths and commands when implementation is next;
- viable rollout plus rollback or accepted roll-forward/recovery for production change;
- required specialist review completed.

**Conditionally ready** means coding for the named scope may start; only named follow-up that does not gate starting that scope remains. State any later completion or rollout gate separately. Required acceptance, safety, or specialist approval needed before starting the named scope makes it **Not ready**.

## Readiness-resolution and implementation work

While implementation is **Not ready**, define only bounded readiness-resolution work:

```text
question or decision to resolve
inspection, measurement, spike, review, or owner action
evidence target
decision rule
owner and stop condition
```

These tasks may gather evidence but do not authorize product implementation.

Only decompose accepted implementation scope. Prefer small, independently verifiable vertical slices. Each slice records:

```text
ID and objective
requirements covered
expected files or components
preconditions and dependencies
implementation steps
new or changed tests
exact verification command
expected observable result
rollback or cleanup
parallel-safety and shared-write warnings
```

Parallelize only independent decisions and write sets. Shared schemas, migrations, public interfaces, generated files, and central registries need one authoritative owner or explicit sequencing.

Do not fabricate exact files for a greenfield project. Identify expected component responsibilities and leave repository paths open until the scaffold or stack is accepted.

## Traceability and maintenance

Maintain a lightweight chain:

```text
need → requirement → design decision → implementation slice → evidence
```

Use stable identifiers or links where the chain crosses artifacts. Avoid repeating entire requirement text in every location.

When implementation reveals a false assumption or forces a design change:

1. Stop work affected by the invalid contract.
2. Record the new evidence.
3. Update the requirement or decision through the acceptance authority.
4. Mark superseded content explicitly.
5. Recheck dependent tasks, tests, rollout, and rollback.

A specification is either maintained, accepted as historical, or explicitly superseded. Silent divergence makes it unsafe as an agent contract.
