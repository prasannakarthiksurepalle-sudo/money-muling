import { useState } from "react";
import CsvUpload from "./components/CsvUpload";
import GraphView from "./components/GraphView";
import FraudTable from "./components/FraudTable";
import JsonDownload from "./components/JsonDownload";
import SummaryStats from "./components/SummaryStats";
import "./App.css";

const PAGE_SIZE = 50;

export default function App() {
  const [data, setData] = useState(null);
  const [page, setPage] = useState(0);

  return (
    <div className="app-container">
      {/* Home / Upload */}
      <div className="card">
        <h1 className="title">💸 Money Muling Detection</h1>
        <p className="subtitle">
          Upload transaction data to detect suspicious fraud networks.
        </p>

        <CsvUpload onResult={(res) => {
          setPage(0);      // reset pagination on new upload
          setData(res);
        }} />
      </div>

      {/* Results */}
      {data && (
        <>
          {/* Summary */}
          <div className="card">
            <SummaryStats summary={data.summary} />
          </div>

          {/* Graph */}
          <div className="card">
            <GraphView
              data={{
                ...data,
                fraud_rings: data.fraud_rings.slice(
                  page * PAGE_SIZE,
                  (page + 1) * PAGE_SIZE
                ),
              }}
            />
          </div>

          {/* Table + Pagination */}
          <div className="card">
            <FraudTable
              rings={data.fraud_rings.slice(
                page * PAGE_SIZE,
                (page + 1) * PAGE_SIZE
              )}
            />

            <div style={{ display: "flex", justifyContent: "space-between", marginTop: 12 }}>
              <button
                className="button"
                disabled={page === 0}
                onClick={() => setPage((p) => Math.max(0, p - 1))}
              >
                ◀ Previous 50
              </button>

              <div style={{ color: "#9ca3af" }}>
                Showing {page * PAGE_SIZE + 1}–
                {Math.min((page + 1) * PAGE_SIZE, data.fraud_rings.length)} of{" "}
                {data.fraud_rings.length}
              </div>

              <button
                className="button"
                disabled={(page + 1) * PAGE_SIZE >= data.fraud_rings.length}
                onClick={() => setPage((p) => p + 1)}
              >
                Next 50 ▶
              </button>
            </div>
          </div>

          {/* Download */}
          <div className="card" style={{ textAlign: "right" }}>
            <JsonDownload data={data} />
          </div>
        </>
      )}
    </div>
  );
}
