export default function FraudTable({ rings }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h3>📋 Fraud Rings</h3>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Ring ID</th>
            <th>Pattern</th>
            <th>Members</th>
            <th>Risk Score</th>
          </tr>
        </thead>
        <tbody>
          {rings.map((ring) => (
            <tr key={ring.ring_id}>
              <td>{ring.ring_id}</td>
              <td>{ring.pattern_type}</td>
              <td>{ring.member_accounts.join(", ")}</td>
              <td>{ring.risk_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
