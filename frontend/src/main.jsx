import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

function App() {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    fetch("/api/incidents/")
      .then((response) => response.json())
      .then((data) => setIncidents(data.incidents || []))
      .catch(() => setIncidents([]));
  }, []);

  return (
    <main>
      <h1>Siklab AI</h1>
      <p>Fire incident transactions</p>
      <ul>
        {incidents.map((incident) => (
          <li key={incident.id}>
            {incident.description} — {incident.severity}
          </li>
        ))}
      </ul>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
