import { useEffect, useRef } from "react";
import { Network } from "vis-network/standalone";

export default function GraphView({ data }) {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!data || !containerRef.current) return;

    const nodesMap = new Map();
    const edges = [];

    // Build nodes & edges from fraud rings
    data.fraud_rings.forEach((ring) => {
      const members = ring.member_accounts;

      members.forEach((acc) => {
        if (!nodesMap.has(acc)) {
          nodesMap.set(acc, {
            id: acc,
            label: acc,
            color: "#ef4444", // red for suspicious nodes
          });
        }
      });

      for (let i = 0; i < members.length - 1; i++) {
        edges.push({ from: members[i], to: members[i + 1] });
      }
    });

    const nodes = Array.from(nodesMap.values());

    const network = new Network(
      containerRef.current,
      { nodes, edges },
      {
        nodes: {
          shape: "dot",
          size: 16,
          font: { color: "#e5e7eb" },
        },
        edges: {
          arrows: "to",
          color: { color: "rgba(255,255,255,0.5)" },
        },
        physics: {
          stabilization: true,
        },
        interaction: {
          hover: true,
        },
      }
    );

    return () => {
      network.destroy();
    };
  }, [data]);

  return (
    <div>
      <h3 style={{ marginBottom: 12 }}>🔗 Fraud Network Visualization</h3>
      <div
        ref={containerRef}
        style={{
          height: "500px",
          width: "100%",
          border: "1px solid rgba(255,255,255,0.12)",
          borderRadius: 12,
          background: "linear-gradient(135deg, #020617, #0f172a)",
        }}
      />
    </div>
  );
}
