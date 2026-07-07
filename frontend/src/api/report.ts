import api from "./axios";

export interface Report {
  id: number;
  interview_id: number;
  company: string;
  role: string;
  overall_score: number;
  communication_score: number;
  technical_score: number;
  feedback: string;
  created_at: string;
}

export async function getReports() {
  const { data } = await api.get<Report[]>("/reports");
  return data;
}