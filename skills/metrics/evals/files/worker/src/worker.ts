import type { Metrics } from "./metrics.ts";

export type Job = { id: string; kind: "email" | "export" };

export interface JobHandler {
  run(job: Job): Promise<void>;
}

export class Worker {
  private readonly handler: JobHandler;
  private readonly metrics: Metrics;
  private readonly maxAttempts: number;

  constructor(handler: JobHandler, metrics: Metrics, maxAttempts = 3) {
    this.handler = handler;
    this.metrics = metrics;
    this.maxAttempts = maxAttempts;
  }

  async process(job: Job): Promise<void> {
    let lastError: unknown;
    for (let attempt = 1; attempt <= this.maxAttempts; attempt += 1) {
      try {
        await this.handler.run(job);
        return;
      } catch (error) {
        lastError = error;
      }
    }
    throw lastError;
  }
}
