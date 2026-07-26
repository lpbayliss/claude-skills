import { describe, expect, it } from "vitest";
import { resolveTheme } from "../src/theme";

describe("resolveTheme", () => {
  it("preserves explicit themes", () => {
    expect(resolveTheme("light")).toBe("light");
    expect(resolveTheme("dark")).toBe("dark");
  });
});
