import assert from "node:assert/strict";
import test from "node:test";
import { InMemoryMetrics } from "../src/metrics.ts";
import { Worker, type JobHandler } from "../src/worker.ts";

test("processes a successful job", async () => {
  const metrics = new InMemoryMetrics();
  const handler: JobHandler = { run: async () => undefined };
  await new Worker(handler, metrics).process({ id: "job-1", kind: "email" });
  assert.equal(metrics.calls.length, 0);
});

test("retries and eventually succeeds", async () => {
  const metrics = new InMemoryMetrics();
  let calls = 0;
  const handler: JobHandler = {
    run: async () => {
      calls += 1;
      if (calls < 3) throw new Error("temporary");
    },
  };
  await new Worker(handler, metrics).process({ id: "job-2", kind: "export" });
  assert.equal(calls, 3);
});

test("throws after terminal failure", async () => {
  const metrics = new InMemoryMetrics();
  const handler: JobHandler = { run: async () => { throw new Error("terminal"); } };
  await assert.rejects(
    new Worker(handler, metrics, 2).process({ id: "job-3", kind: "email" }),
    /terminal/,
  );
});
