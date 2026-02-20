💸 Money Muling Detection System (Graph-Based Fraud Detection)

A full-stack web application to detect money muling and fraud rings using graph theory and simple pattern detection (cycles, fan-in, fan-out, shell networks).
The system allows users to upload transaction CSV files and visualizes suspicious account networks, fraud rings, and risk scores.

🚀 Features

📂 Upload CSV transaction data
🔗 Build transaction graph (sender → receiver)
🧠 Detect fraud patterns:

Cycles (circular money flow)
Smurfing (fan-in / fan-out)
Shell networks (multi-hop low-degree intermediaries)

📊 Visualize fraud network (graph)
📋 Show fraud rings & risk scores in a table
⬇️ Download JSON fraud report

🧱 Tech Stack

Frontend

React (Vite)
Axios
vis-network (graph visualization)

Backend

FastAPI
NetworkX (graph processing)
Pandas (CSV parsing)
Uvicorn (ASGI server)

Deployment

Frontend Hosted: Vercel
Backend Hosted: Render

📁 Repository Structure
money-muling/
├── backend/        # FastAPI backend (Render)
├── frontend/       # React frontend (Vercel)
├── sample.csv      # Sample CSV for testing
└── README.md

🛠️ Run Locally
1️⃣ Backend (FastAPI)
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload

Backend runs at:

http://localhost:8000

Swagger UI:

http://localhost:8000/docs

2️⃣ Frontend (React + Vite)
cd frontend
npm install
npm run dev

Frontend runs at:

http://localhost:5173

📄 CSV Format

Your CSV must contain these columns:
transaction_id,sender_id,receiver_id,amount,timestamp

Example:

transaction_id,sender_id,receiver_id,amount,timestamp
t1,A,B,100,2025-01-01 10:00:00
t2,B,C,50,2025-01-01 11:00:00
t3,C,A,30,2025-01-01 12:00:00

🌐 Deployment
Backend (Render)

Root Directory: backend

Build Command:

pip install -r requirements.txt

Start Command:

uvicorn main:app --host 0.0.0.0 --port $PORT
Frontend (Vercel)
Root Directory: frontend
Framework: Vite

Build Command:

npm run build
Output Directory:
dist
Update API base URL in frontend/src/api.js:
const API_BASE = "https://your-backend.onrender.com";

🧪 Demo Flow
Upload CSV from frontend
Backend analyzes transactions
Fraud rings and suspicious accounts are detected
Graph + table visualization shown
Download JSON fraud report

📌 Future Improvements
Time-window based smurfing detection
ML-based risk scoring
Node coloring by risk level
User authentication
Real-time transaction streams

Built by Team : Think Tank
Hackathon Project :  Money Muling Detection System (Graph-Based Fraud Detection)
