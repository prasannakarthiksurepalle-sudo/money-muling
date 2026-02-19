import { useState } from "react";
import CsvUpload from "./components/CsvUpload";
import GraphView from "./components/GraphView";
import FraudTable from "./components/FraudTable";
import JsonDownload from "./components/JsonDownload";

export default function App() {
  const [data, setData] = useState(null);

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>💸 Money Muling Detection Dashboard</h1>

      <CsvUpload onResult={setData} />

      {data && (
        <>
          <GraphView data={{ ...data, fraud_rings: data.fraud_rings.slice(0, 50) }} />
          <FraudTable rings={data.fraud_rings} />
          <JsonDownload data={data} />
        </>
      )}
    </div>
  );
}
