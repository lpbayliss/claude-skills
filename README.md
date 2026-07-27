# LPBayliss Claude Skills

A versioned Claude Code plugin and portable [Agent Skills](https://agentskills.io/) collection for software engineering work.

## Skills

### `specify`

Creates, reviews, repairs, and transforms software specifications into decision-ready, implementation-ready contracts.

Use it for specs, RFCs, PRDs, technical designs, scoped issue contracts, migrations, readiness reviews, and transforming rough artifacts into testable requirements.

```text
/lpbayliss:specify docs/proposal.md
```

### `metrics`

Identifies, defines, implements, and verifies trustworthy software, product, delivery, reliability, experiment, and AI-system metrics.

Use it to decide what to measure, audit misleading metrics, add repository instrumentation, design metric contracts, or verify dashboards and alerts without inventing targets or creating unsafe cardinality.

```text
/lpbayliss:metrics Add retry-safe worker outcome and latency metrics to this repository.
```

### `presentation-planning`

Plans and writes the underlying content for presentations before physical slide production.

Use it for audience strategy, governing idea, narrative architecture, technical claim/evidence flow, timed beat plans, speaker intent, visual direction, Q&A, rehearsal, and production briefs for executive, technical, research, pitch, training, keynote, and demo presentations.

```text
/lpbayliss:presentation-planning Turn this architecture RFC into a 12-minute decision presentation for the review board. Plan content only.
```

The plugin namespace is `lpbayliss`, giving every skill a stable owner-scoped command such as `/lpbayliss:metrics`. This intentionally replaces the earlier `software-specification` namespace.

## Install in Claude Code

### Plugin marketplace

Run inside Claude Code:

```text
/plugin marketplace add lpbayliss/claude-skills
/plugin install lpbayliss@lpbayliss-skills
/reload-plugins
```

Or from a shell:

```bash
claude plugin marketplace add lpbayliss/claude-skills
claude plugin install lpbayliss@lpbayliss-skills
```

Claude can select a skill automatically from its description or you can invoke a namespaced skill directly.

### Install individual personal skills

```bash
git clone https://github.com/lpbayliss/claude-skills.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/claude-skills/skills/specify" ~/.claude/skills/specify
ln -s "$(pwd)/claude-skills/skills/metrics" ~/.claude/skills/metrics
ln -s "$(pwd)/claude-skills/skills/presentation-planning" ~/.claude/skills/presentation-planning
```

Copy instead of symlinking if preferred. Standalone personal skills are invoked as `/specify`, `/metrics`, and `/presentation-planning`.

### Upload an individual skill to Claude Desktop or Claude.ai

Build the archives:

```bash
python3 scripts/package_skill.py
python3 scripts/check_packages.py
```

Then upload one of:

- `dist/specify.zip`
- `dist/metrics.zip`
- `dist/presentation-planning.zip`

In Claude, open **Customize → Skills**, click **+ → Create skill → Upload a skill**, select the ZIP, then enable it. Code execution and file creation must be enabled. Each ZIP contains the required top-level `<skill-name>/` folder.

### Install a project skill

From a project root:

```bash
mkdir -p .claude/skills
cp -R /path/to/this-repo/skills/metrics .claude/skills/metrics
```

Commit the skill directory if the workflow should travel with the project.

## Example requests

```text
Create an implementation-ready specification for passkey login. Inspect this repository first. Do not implement it.
```

```text
Review docs/payments-redesign.md. Preserve accepted intent, identify blockers, and produce a corrected spec suitable for parallel implementation.
```

```text
We are adding recurring reminders. Identify the smallest outcome, driver, and guardrail metric set, then add the instrumentation and tests using this repository's existing analytics stack.
```

```text
Audit weekly_active_user from source event through warehouse query and dashboard. Fix semantic drift, cardinality, and tests; do not invent a target.
```

```text
Turn this research paper into a 12-minute conference presentation for a mixed technical audience. Develop the governing idea, story, evidence, speaker content, visual intent, timing, and likely Q&A; do not build the deck yet.
```

```text
Review this executive presentation outline, identify why the argument does not land, then produce a repaired production brief with an explicit decision and honest treatment of risk.
```

## Repository structure

```text
.claude-plugin/                 Marketplace and plugin metadata
skills/specify/                 Software specification skill, references, and evals
skills/metrics/                 Metrics skill, references, fixtures, and evals
skills/presentation-planning/   Presentation content/story skill, references, fixtures, and evals
docs/                           Design evidence and evaluation notes
scripts/check.py                Dependency-free multi-skill repository checks
scripts/check_packages.py       Verifies generated archive set, layout, and parity
scripts/package_skill.py        Builds each .skill/.zip archive and the complete plugin zip
dist/                           Generated archives
```

Each skill is independently portable. The repository root is the multi-skill Claude Code plugin.

## Validate and package

```bash
python3 scripts/check.py
python3 scripts/package_skill.py
python3 scripts/check_packages.py
for archive in dist/*.skill dist/*.zip; do python3 -m zipfile -t "$archive"; done
```

When Claude Code is installed:

```bash
claude plugin validate .
claude --plugin-dir .
```

Expected archives:

- `dist/specify.skill`
- `dist/specify.zip`
- `dist/metrics.skill`
- `dist/metrics.zip`
- `dist/presentation-planning.skill`
- `dist/presentation-planning.zip`
- `dist/lpbayliss-skills.zip`

Each individual `.skill` and `.zip` pair contains the same top-level `<skill-name>/` directory. Use the `.zip` files for manual upload through Claude Desktop or Claude.ai. The plugin zip contains the complete collection for local plugin loading. Successful GitHub Actions runs publish all seven files in the `lpbayliss-skill-bundles` artifact.

## Skill quality rules

- Use precise trigger descriptions with realistic positive and difficult negative trigger evals.
- Keep the core workflow under 500 lines and load deeper references conditionally.
- Inspect source evidence before making repository-specific claims.
- Do not fabricate product decisions, targets, paths, commands, approvals, or observed results.
- Scale output and implementation to the decision and risk.
- Pair semantic review with deterministic checks for package shape, links, eval schemas, and fixtures.
- Keep each skill independently installable and testable.
- Implement requested work and verify it with real execution rather than stopping at advice.

Evidence for the authoring approach is in [docs/skill-design-research.md](docs/skill-design-research.md). Specification sources are in [docs/specification-workflow-basis.md](docs/specification-workflow-basis.md). Metrics sources are in [docs/metrics-design-basis.md](docs/metrics-design-basis.md). Presentation sources are in [docs/presentation-planning-basis.md](docs/presentation-planning-basis.md). Specify evaluation results are in [docs/evaluation.md](docs/evaluation.md).

## Adding another skill

1. Create `skills/<name>/SKILL.md` with matching `name` frontmatter and a trigger-focused description.
2. Put optional depth in `references/`, deterministic helpers in `scripts/`, and realistic inputs in `evals/files/`.
3. Add at least three output evals to `evals/evals.json` and 20 balanced trigger cases to `evals/trigger-evals.json`.
4. Update this README and plugin metadata keywords when the new domain changes discovery.
5. Run repository checks, package all artifacts, validate the plugin, and exercise representative skill prompts before release.

## License

MIT. See [LICENSE](LICENSE).
