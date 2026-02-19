import { useEffect, useRef } from "react";
import { Network } from "vis-network/standalone";

export default function GraphView({ data }) {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!data) return;

    const nodesMap = new Map();
    const edges = [];

    data.fraud_rings.forEach((ring) => {
      const members = ring.member_accounts;
      members.forEach((acc) => {
        if (!nodesMap.has(acc)) {
          nodesMap.set(acc, {
            id: acc,
            label: acc,
            color: "red",
          });
        }
      });

      for (let i = 0; i < members.length - 1; i++) {
        edges.push({ from: members[i], to: members[i + 1] });
      }
    });

    const nodes = Array.from(nodesMap.values());

    const network = new Network(containerRef.current, { nodes, edges }, {
      nodes: { shape: "dot", size: 15 },
      edges: { arrows: "to" },
      physics: { stabilization: true },
    });

    return () => network.destroy();
  }, [data]);

  return (
    <div>
      <h3>🔗 Fraud Network Graph</h3>
      <div ref={containerRef} style={{ height: "400px", border: "1px solid #ccc" }} />
    </div>
  );
}
