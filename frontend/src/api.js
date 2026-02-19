import axios from "axios";

const API_BASE = "http://localhost:8000";

export async function uploadCsv(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${API_BASE}/upload-csv`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return res.data;
}
