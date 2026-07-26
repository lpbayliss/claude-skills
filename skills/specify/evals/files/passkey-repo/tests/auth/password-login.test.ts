import { describe, expect, it } from "vitest";
import { loginWithPassword } from "../../src/auth/password";

describe("password login", () => {
  it("creates a password session", async () => {
    const session = await loginWithPassword("a@example.test", "secret");
    expect(session.method).toBe("password");
  });
});
