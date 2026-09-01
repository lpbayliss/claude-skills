// Desktop notification for Stop and Notification hook events.
// Convenience hook: fails open — always exits 0, never blocks the loop.
import { spawn } from "node:child_process";
import { readFileSync } from "node:fs";
import { basename } from "node:path";

let input = {};
try {
  const chunks = [];
  for await (const c of process.stdin) chunks.push(c);
  input = JSON.parse(Buffer.concat(chunks).toString());
} catch {
  process.exit(0);
}

// No friendly session title exists in hook input; project dir + short id is
// the most recognizable session identifier available.
const project = basename(input.cwd ?? process.env.CLAUDE_PROJECT_DIR ?? "claude");
const shortId = (input.session_id ?? "").slice(0, 8);
const title = shortId ? `Claude · ${project} (${shortId})` : `Claude · ${project}`;

let detail;
if (input.hook_event_name === "Notification") {
  detail = input.message ?? input.title ?? "Claude needs your input";
} else {
  detail = lastAssistantText(input.transcript_path) ?? "Finished — ready for review";
}
detail = detail.replace(/\s+/g, " ").trim().slice(0, 140) || "Done";

notify(title, detail);
process.exit(0);

function lastAssistantText(path) {
  if (!path) return null;
  try {
    const lines = readFileSync(path, "utf8").split("\n").filter(Boolean);
    for (let i = lines.length - 1; i >= 0 && i >= lines.length - 50; i--) {
      try {
        const entry = JSON.parse(lines[i]);
        if (entry.type !== "assistant") continue;
        const blocks = entry.message?.content ?? [];
        const text = blocks.filter((b) => b.type === "text").map((b) => b.text).join(" ");
        if (text.trim()) return text;
      } catch {
        // partial or non-JSON line; keep scanning
      }
    }
  } catch {
    // unreadable transcript; fall through to generic detail
  }
  return null;
}

function notify(t, m) {
  try {
    if (process.platform === "darwin") {
      const dq = (s) => s.replace(/[\\"]/g, "\\$&");
      run("osascript", ["-e", `display notification "${dq(m)}" with title "${dq(t)}"`]);
    } else if (process.platform === "win32") {
      const sq = (s) => s.replace(/'/g, "''");
      run("powershell.exe", [
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        `Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; ` +
          `$n = New-Object System.Windows.Forms.NotifyIcon; $n.Icon = [System.Drawing.SystemIcons]::Information; ` +
          `$n.Visible = $true; $n.ShowBalloonTip(5000, '${sq(t)}', '${sq(m)}', 'Info'); ` +
          `Start-Sleep -Seconds 6; $n.Dispose()`,
      ]);
    } else {
      run("notify-send", [t, m]); // absent notify-send = silent no-op via error handler
    }
  } catch {
    // notification is best-effort
  }
}

function run(cmd, args) {
  const child = spawn(cmd, args, { detached: true, stdio: "ignore" });
  child.on("error", () => {});
  child.unref();
}
