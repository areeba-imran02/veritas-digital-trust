import { useEffect, useState } from "react";
import { getHealth, type Health } from "./lib/api";

// Foundation shell only. It verifies frontend <-> backend wiring and uses design tokens.
// The real interface is built in Prompts 8-9.
export default function App() {
  const [health, setHealth] = useState<Health | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getHealth().then(setHealth).catch((e) => setError(String(e.message ?? e)));
  }, []);

  return (
    <main style={{ minHeight: "100%", display: "grid", placeItems: "center", padding: "var(--space-5)" }}>
      <section style={{ background: "var(--surface)", border: "1px solid var(--border)",
        borderRadius: "var(--radius-lg)", boxShadow: "var(--shadow)", padding: "var(--space-6)", maxWidth: 480 }}>
        <h1 style={{ margin: 0, fontSize: "var(--text-2xl)", letterSpacing: "0.12em" }}>VERITAS</h1>
        <p style={{ color: "var(--text-muted)", marginTop: "var(--space-2)" }}>Understand. Verify. Trust.</p>
        <p style={{ fontFamily: "var(--font-mono)", fontSize: "var(--text-sm)" }}>
          {error ? `API unreachable: ${error}`
            : health ? `API ${health.status} · v${health.version} · LLM ${health.llm_configured ? "configured" : "not configured"}`
            : "Checking API…"}
        </p>
      </section>
    </main>
  );
}
