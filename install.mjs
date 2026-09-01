#!/usr/bin/env node
// Interactive installer for the lpbayliss-skills marketplace.
// Node stdlib only; works on macOS, Linux, and Windows.
//
//   node install.mjs
import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createInterface } from "node:readline/promises";

const MARKETPLACE = "lpbayliss-skills";
const GITHUB_REPO = "lpbayliss/claude-skills";
const repoRoot = dirname(fileURLToPath(import.meta.url));
// Interactive on a TTY; with piped stdin, consume all answers upfront so
// type-ahead lines aren't dropped between prompts (scriptable/CI use).
let rl = null;
let queued = null;
if (process.stdin.isTTY) {
  rl = createInterface({ input: process.stdin, output: process.stdout });
} else {
  const chunks = [];
  for await (const c of process.stdin) chunks.push(c);
  queued = Buffer.concat(chunks).toString().split(/\r?\n/);
}
const ask = async (q, fallback = "") => {
  if (queued) {
    const answer = (queued.shift() ?? "").trim();
    console.log(q + answer);
    return answer || fallback;
  }
  return (await rl.question(q)).trim() || fallback;
};

function claude(...args) {
  // The Windows `claude` shim is a .cmd, which needs a shell; build one quoted
  // string so args aren't naively concatenated (avoids DEP0190).
  const quote = (a) => (/[\s"]/.test(a) ? `"${a.replace(/"/g, '\\"')}"` : a);
  const res =
    process.platform === "win32"
      ? spawnSync(["claude", ...args.map(quote)].join(" "), { encoding: "utf8", shell: true })
      : spawnSync("claude", args, { encoding: "utf8" });
  return { ok: res.status === 0, out: `${res.stdout ?? ""}${res.stderr ?? ""}` };
}

// --- preflight ---------------------------------------------------------------
const version = claude("--version");
if (!version.ok) {
  console.error("The `claude` CLI is not on PATH. Install Claude Code first: https://claude.com/claude-code");
  process.exit(1);
}
console.log(`\nClaude Code detected (${version.out.trim().split("\n")[0]})\n`);

let manifest;
try {
  manifest = JSON.parse(readFileSync(join(repoRoot, ".claude-plugin", "marketplace.json"), "utf8"));
} catch {
  console.error("Could not read .claude-plugin/marketplace.json — run this script from a claude-skills checkout.");
  process.exit(1);
}

// --- marketplace -------------------------------------------------------------
const marketplaces = claude("plugin", "marketplace", "list").out;
if (marketplaces.includes(MARKETPLACE)) {
  const update = await ask(`Marketplace "${MARKETPLACE}" already added. Update it from source? [y/N] `);
  if (/^y/i.test(update)) {
    const res = claude("plugin", "marketplace", "update", MARKETPLACE);
    console.log(res.ok ? "Marketplace updated." : `Update failed:\n${res.out}`);
  }
} else {
  console.log(`Marketplace "${MARKETPLACE}" is not configured yet.`);
  const src = await ask(`Add from (1) GitHub ${GITHUB_REPO} or (2) this local checkout? [1/2, default 1] `, "1");
  const source = src === "2" ? repoRoot : GITHUB_REPO;
  const res = claude("plugin", "marketplace", "add", source);
  if (!res.ok) {
    console.error(`Failed to add marketplace:\n${res.out}`);
    process.exit(1);
  }
  console.log(`Marketplace added from ${source}.`);
}

// --- selection ---------------------------------------------------------------
const installedOut = claude("plugin", "list").out;
const plugins = manifest.plugins.map((p) => ({
  name: p.name,
  description: p.description ?? "",
  installedHere: installedOut.includes(`${p.name}@${MARKETPLACE}`),
  installedElsewhere:
    !installedOut.includes(`${p.name}@${MARKETPLACE}`) && new RegExp(`❯ ${p.name}@`, "u").test(installedOut),
}));

console.log("\nCurated plugins:\n");
plugins.forEach((p, i) => {
  const mark = p.installedHere ? " [installed]" : p.installedElsewhere ? " [installed from another marketplace]" : "";
  console.log(`  ${String(i + 1).padStart(2)}. ${p.name}${mark}`);
  console.log(`      ${p.description}`);
});

const choice = await ask('\nInstall which? ("all", "missing", numbers like "1,3,5", or Enter to quit) ');
let selected = [];
if (/^all$/i.test(choice)) selected = plugins;
else if (/^missing$/i.test(choice)) selected = plugins.filter((p) => !p.installedHere);
else if (choice) {
  const idx = new Set(
    choice
      .split(",")
      .map((s) => Number.parseInt(s.trim(), 10))
      .filter((n) => n >= 1 && n <= plugins.length),
  );
  selected = plugins.filter((_, i) => idx.has(i + 1));
}
if (selected.length === 0) {
  console.log("Nothing selected — done.");
  rl?.close();
  process.exit(0);
}

const scope = await ask("Scope — user (all projects), project (this repo, shared), local (this repo, just you)? [user] ", "user");
if (!["user", "project", "local"].includes(scope)) {
  console.error(`Unknown scope "${scope}".`);
  process.exit(1);
}

// --- install -----------------------------------------------------------------
const results = [];
for (const p of selected) {
  process.stdout.write(`Installing ${p.name}@${MARKETPLACE} (${scope})... `);
  const res = claude("plugin", "install", `${p.name}@${MARKETPLACE}`, "--scope", scope, "--yes");
  results.push({ name: p.name, ok: res.ok, out: res.out });
  console.log(res.ok ? "ok" : "FAILED");
}

console.log("\nSummary:");
for (const r of results) {
  console.log(`  ${r.ok ? "✔" : "✘"} ${r.name}`);
  if (!r.ok) console.log(`      ${r.out.trim().split("\n").slice(-3).join("\n      ")}`);
}

const names = new Set(results.filter((r) => r.ok).map((r) => r.name));
console.log("\nNext steps:");
console.log("  - Start a new Claude Code session to pick up the changes.");
if (names.has("mobbin-mcp")) console.log("  - mobbin-mcp: first use opens Mobbin's browser OAuth (paid plan required).");
if (names.has("notify")) console.log("  - notify: needs `node` on PATH; check /hooks to see its Stop and Notification hooks.");
if (names.has("lpbayliss")) console.log("  - lpbayliss: /create-skill and /create-hook are now invocable.");

rl?.close();
