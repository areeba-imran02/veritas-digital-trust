// API client. Base path is relative so it works in dev (Vite proxy) and production (same origin).
export interface Health {
  status: string; service: string; version: string; environment: string; llm_configured: boolean;
}

export async function getHealth(): Promise<Health> {
  const r = await fetch("/api/health");
  if (!r.ok) throw new Error(`Health check failed: ${r.status}`);
  return r.json();
}
// analyze() is added in Prompt 2 together with the /api/analyze endpoint.
