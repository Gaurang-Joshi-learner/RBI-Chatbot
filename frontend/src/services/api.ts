
import axios, { AxiosError } from "axios";

const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_BASE_URL ||
    "http://localhost:8000/ask",
  timeout: 120000,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  validateStatus: (status) => status >= 200 && status < 500, // let us handle errors
});
api.interceptors.request.use(
  (config) => {

    const token =
      localStorage.getItem("token");

    if (token) {

      config.headers.Authorization =
        `Bearer ${token}`;
    }

    return config;
  }
);
interface ChatResponse {
  answer: string;

  sources?: Array<{
    title: string;
    issue_date?: string;
    source?: string;
  }>;

  mode?: string;

  session_id?: number;
}
export const getSessions = async () => {

  const token =
    localStorage.getItem("token");

  const res = await axios.get(
    "http://localhost:8000/sessions",
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return res.data;
};
export const getSessionMessages = async (
  sessionId: number
) => {

  const token =
    localStorage.getItem("token");

  const res = await axios.get(
    `http://localhost:8000/sessions/${sessionId}/messages`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return res.data;
};
export const sendChatMessage = async (
  message: string,
  sessionId?: number
): Promise<ChatResponse> => {

  try {

    const res = await api.post<ChatResponse>(
      "/",
      {
        question: message,
        session_id: sessionId,
      }
    );

    console.log("API response:", res.data);

    if (
      res.status >= 200 &&
      res.status < 300 &&
      res.data?.answer
    ) {
      return res.data;
    }

    throw new Error(
      "Unexpected response from server"
    );

  } catch (error) {

    const err = error as AxiosError<any>;

    console.error(
      "API request failed:",
      err
    );

    const detail =
      err.response?.data?.detail ||
      err.response?.data?.error ||
      err.message ||
      "Network error";

    throw new Error(detail);
  }
};
export const deleteBackendSession = async (
  sessionId: number
) => {

  const token =
    localStorage.getItem("token");

  const res = await axios.delete(
    `http://localhost:8000/sessions/${sessionId}`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return res.data;
};