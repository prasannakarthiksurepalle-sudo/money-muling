import axios from "axios";

const API_BASE = "https://money-muling-4.onrender.com";

export async function uploadCsv(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${API_BASE}/upload-csv`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return res.data;
}
