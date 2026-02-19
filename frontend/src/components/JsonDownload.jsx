export default function JsonDownload({ data }) {
  function download() {
    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "fraud_report.json";
    a.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div style={{ marginTop: 20 }}>
      <button onClick={download}>⬇️ Download JSON Report</button>
    </div>
  );
}
