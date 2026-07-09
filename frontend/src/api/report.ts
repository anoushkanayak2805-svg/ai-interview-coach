import api from "./axios";

/* ---------- Types ---------- */

export interface Report {
  id?: number;
  interview_id: number;

  overall_score: number;
  technical_score: number;
  communication_score: number;
  confidence_score: number;

  summary: string;

  strengths: string | string[];
  weaknesses: string | string[];
  recommendations: string | string[];
  learning_roadmap: string | string[];

  hiring_recommendation: string;

  created_at?: string;
}

/* ---------- Get Single Interview Report ---------- */

export async function getReport(
  interviewId: number | string
): Promise<Report> {
  const { data } = await api.get<Report>(
    `/interviews/${interviewId}/report`
  );

  return data;
}

/* ---------- Get All Reports ---------- */

/*
  Your backend currently does NOT have GET /reports.

  This function is kept for future use when we add
  the reports history endpoint.
*/

export async function getReports(): Promise<Report[]> {
  try {
    const { data } = await api.get<Report[]>("/reports");

    return data;
  } catch (error: any) {
    if (error.response?.status === 404) {
      console.warn(
        "Reports history endpoint is not available yet."
      );

      return [];
    }

    throw error;
  }
}