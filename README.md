# claude-skills

A curated collection of Claude Code skills, plugins, hooks, and utilities — the tools I reach for regularly, gathered in one marketplace.

Where a well-regarded upstream maintainer publishes a skill or plugin, this marketplace references it directly so it stays current with upstream. Skills I author myself will live in this repo.

## Install

```
/plugin marketplace add lpbayliss/claude-skills
```

Then install individual plugins:

```
/plugin install react-best-practices@lpbayliss-skills
```

Or browse everything interactively with `/plugin`.

## Curated plugins

| Plugin | Covers | Upstream | Maintainer |
| --- | --- | --- | --- |
| `react-best-practices` | React, Next.js | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel (official guidelines) |
| `vite` | Vite | [antfu/skills](https://github.com/antfu/skills) | Anthony Fu (Vite core team) |
| `vitest` | Vitest | [antfu/skills](https://github.com/antfu/skills) | Anthony Fu (Vitest team lead) |
| `pnpm` | pnpm | [antfu/skills](https://github.com/antfu/skills) | Anthony Fu (docs-derived) |
| `tailwind-css` | Tailwind CSS | [PaulRBerg/agent-skills](https://github.com/PaulRBerg/agent-skills) | Paul Razvan Berg (community) |
| `javascript-typescript` | TypeScript, modern JS | [wshobson/agents](https://github.com/wshobson/agents) | Seth Hobson (community) |
| `cicd-automation` | GitHub Actions, CI/CD | [wshobson/agents](https://github.com/wshobson/agents) | Seth Hobson (community) |
| `postgres-best-practices` | PostgreSQL | [neondatabase/postgres-skills](https://github.com/neondatabase/postgres-skills) | Neon (official, vendor-agnostic) |
| `prisma` | Prisma ORM | [prisma/skills](https://github.com/prisma/skills) | Prisma (official) |
| `drizzle-best-practices` | Drizzle ORM | [honra-io/drizzle-best-practices](https://github.com/honra-io/drizzle-best-practices) | Honra (community, early-stage) |
| `frontend-design` | UI/UX design quality | [anthropics/claude-plugins-public](https://github.com/anthropics/claude-plugins-public) | Anthropic (official) |
| `mobbin-mcp` | Design reference (MCP) | Local wrapper for [Mobbin's official MCP](https://mobbin.com/mcp) | Mobbin (official server; OAuth, paid plans) |

## Alternatives worth knowing

- **PostgreSQL via Supabase** — [supabase/agent-skills](https://github.com/supabase/agent-skills) is a popular official marketplace with a `supabase-postgres-best-practices` skill; add it directly if you use Supabase. Neon's was chosen here for being explicitly vendor-agnostic.
- **SQLite via Turso** — [tursodatabase/agent-skills](https://github.com/tursodatabase/agent-skills) is official but Turso-flavored (their SQLite-compatible platform), not vanilla SQLite.
- **Docker MCP Toolkit** — [docker/claude-plugins](https://github.com/docker/claude-plugins) is Docker Inc's official marketplace, but it only covers Docker Desktop's MCP Toolkit integration, not Dockerfile/Compose authoring.
- **Anthropic official marketplaces** — [anthropics/skills](https://github.com/anthropics/skills) (document/creative skills) and the [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) marketplace (e.g. `pr-review-toolkit`) are worth adding separately; `frontend-design` is already referenced here.

## Gaps

Tools I use with no credible upstream skill as of September 2026 — candidates for authoring here:

| Tool | Status |
| --- | --- |
| Docker / Docker Compose | No first-party skill. Best community coverage (`docker-patterns` in [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)) only installs as a 286-skill mega-plugin. |
| SQLite (vanilla) | Nothing credible beyond Turso's platform-flavored skills. |
| tRPC | No official skill; only unmaintained auto-conversions from Cursor rules. |
| Biome | [biomejs/biome](https://github.com/biomejs/biome) ships skills for *developing Biome itself*, not for using it in projects. |
| React Testing Library | Only tiny untraction repos; partially covered by `vitest` and wshobson's `unit-testing` plugin. |
| npm / yarn | No dedicated skills (pnpm is covered). |

## License

MIT — see [LICENSE](LICENSE). Referenced upstream plugins carry their own licenses.
