// Theme controller: "system" | "light" | "dark". Persisted in localStorage.
export type ThemeMode = "system" | "light" | "dark";
const KEY = "veritas.theme";

export function getStoredTheme(): ThemeMode {
  const v = localStorage.getItem(KEY);
  return v === "light" || v === "dark" ? v : "system";
}

export function applyTheme(mode: ThemeMode): void {
  const root = document.documentElement;
  if (mode === "system") root.removeAttribute("data-theme");
  else root.setAttribute("data-theme", mode);
  localStorage.setItem(KEY, mode);
}
