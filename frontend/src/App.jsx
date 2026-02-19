import { useState } from "react";
import CsvUpload from "./components/CsvUpload";
import GraphView from "./components/GraphView";
import FraudTable from "./components/FraudTable";
import JsonDownload from "./components/JsonDownload";
import "./App.css";

export default function App() {
  const [data, setData] = useState(null);

  return (
    <div className="app-container">
      {/* Header / Home Section */}
      <div className="card">
        <h1 className="title">💸 Money Muling Detection</h1>
        <p className="subtitle">
          Upload transaction data to detect suspicious fraud networks using graph analysis.
        </p>

        <CsvUpload onResult={setData} />
      </div>

      {/* Results Section */}
      {data && (
        <>
          <div className="card">
            <GraphView data={{ ...data, fraud_rings: data.fraud_rings.slice(0, 50) }} />
          </div>

          <div className="card">
            <FraudTable rings={data.fraud_rings} />
          </div>

          <div className="card" style={{ textAlign: "right" }}>
            <JsonDownload data={data} />
          </div>
        </>
      )}
    </div>
  );
}
