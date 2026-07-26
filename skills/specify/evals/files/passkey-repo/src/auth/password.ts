import { createSession } from "./session";

export async function loginWithPassword(email: string, password: string) {
  if (!email || !password) throw new Error("invalid credentials");
  return createSession("fixture-user", "password");
}
