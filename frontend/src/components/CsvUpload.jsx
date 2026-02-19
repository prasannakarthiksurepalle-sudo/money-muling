import { useState } from "react";
import { uploadCsv } from "../api";

export default function CsvUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleUpload() {
    if (!file) return alert("Select a CSV file first");

    setLoading(true);
    try {
      const result = await uploadCsv(file);
      onResult(result);
    } catch (err) {
      const msg =
      err?.response?.data?.detail ||
      err?.message ||
      "Upload failed. Check backend logs.";
      alert(msg);
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

return (
  <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
    <input
      type="file"
      accept=".csv"
      onChange={(e) => setFile(e.target.files[0])}
      style={{
        background: "#020617",
        color: "#e5e7eb",
        padding: "8px",
        borderRadius: "8px",
        border: "1px solid rgba(255,255,255,0.2)",
        flex: 1,
      }}
    />
    <button onClick={handleUpload} disabled={loading} className="button">
      {loading ? "Processing..." : "Upload CSV"}
    </button>
  </div>
);

}
