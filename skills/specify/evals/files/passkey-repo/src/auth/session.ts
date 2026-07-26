export type AuthMethod = "password";

export interface Session {
  userId: string;
  method: AuthMethod;
  createdAt: number;
}

export function createSession(userId: string, method: AuthMethod): Session {
  return { userId, method, createdAt: Date.now() };
}
