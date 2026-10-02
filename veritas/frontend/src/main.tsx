import React from "react";
import { createRoot } from "react-dom/client";
import "./styles/tokens.css";
import { applyTheme, getStoredTheme } from "./theme/theme";
import App from "./App";

applyTheme(getStoredTheme());
createRoot(document.getElementById("root")!).render(<React.StrictMode><App /></React.StrictMode>);
