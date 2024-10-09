import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./index.css";
import Navbar from "./components/navbar";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <div className="bg-gray-900 h-100">
    <Navbar />
    <App />
    </div>
  </StrictMode>
);
