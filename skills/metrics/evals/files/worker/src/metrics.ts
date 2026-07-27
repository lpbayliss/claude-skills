export interface Metrics {
  increment(name: string, labels?: Record<string, string>, value?: number): void;
  observe(name: string, value: number, labels?: Record<string, string>): void;
}

export type MetricCall = {
  kind: "increment" | "observe";
  name: string;
  value: number;
  labels: Record<string, string>;
};

export class InMemoryMetrics implements Metrics {
  readonly calls: MetricCall[] = [];

  increment(name: string, labels: Record<string, string> = {}, value = 1): void {
    this.calls.push({ kind: "increment", name, value, labels });
  }

  observe(name: string, value: number, labels: Record<string, string> = {}): void {
    this.calls.push({ kind: "observe", name, value, labels });
  }
}
