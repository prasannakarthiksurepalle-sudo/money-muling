export default function SummaryStats({ summary }) {
  const cardStyle = {
    background: "rgba(255,255,255,0.05)",
    borderRadius: 12,
    padding: 16,
    minWidth: 160,
    textAlign: "center",
  };

  return (
    <div style={{ display: "flex", gap: 16, flexWrap: "wrap", marginBottom: 16 }}>
      <div style={cardStyle}>
        <div style={{ fontSize: 12, color: "#9ca3af" }}>Total Accounts</div>
        <div style={{ fontSize: 22, fontWeight: 700 }}>
          {summary.total_accounts_analyzed}
        </div>
      </div>

      <div style={cardStyle}>
        <div style={{ fontSize: 12, color: "#9ca3af" }}>Suspicious Accounts</div>
        <div style={{ fontSize: 22, fontWeight: 700 }}>
          {summary.suspicious_accounts_flagged}
        </div>
      </div>

      <div style={cardStyle}>
        <div style={{ fontSize: 12, color: "#9ca3af" }}>Fraud Rings</div>
        <div style={{ fontSize: 22, fontWeight: 700 }}>
          {summary.fraud_rings_detected}
        </div>
      </div>

      <div style={cardStyle}>
        <div style={{ fontSize: 12, color: "#9ca3af" }}>Processing Time (s)</div>
        <div style={{ fontSize: 22, fontWeight: 700 }}>
          {Number(summary.processing_time_seconds).toFixed(2)}
        </div>
      </div>
    </div>
  );
}
