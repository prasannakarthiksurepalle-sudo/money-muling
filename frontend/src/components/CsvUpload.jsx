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
      alert("Upload failed. Check backend.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ marginBottom: 20 }}>
      <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} disabled={loading} style={{ marginLeft: 10 }}>
        {loading ? "Processing..." : "Upload CSV"}
      </button>
    </div>
  );
}
