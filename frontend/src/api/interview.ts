import api from "./axios";

/* ---------- Types ---------- */

export interface CreateInterviewRequest {
  title: string;
  company: string;
  role: string;
  interview_type: string;
  difficulty: string;
}

export interface InterviewResponse {
  id: number;
  title: string;
  company: string;
  role: string;
  interview_type: string;
  difficulty: string;
  status: string;
  created_at?: string;
}

export interface Question {
  id: number;
  question: string;
  category?: string;
  difficulty?: string;
}

export interface SubmitAnswerRequest {
  question_id: number;
  answer_text: string;
}

/* ---------- APIs ---------- */

// Create Interview
export async function createInterview(
  payload: CreateInterviewRequest
): Promise<InterviewResponse> {
  const { data } = await api.post<InterviewResponse>(
    "/interviews",
    payload
  );

  return data;
}

// Get All Interviews
export async function getInterviews(): Promise<InterviewResponse[]> {
  const { data } = await api.get<InterviewResponse[]>(
    "/interviews"
  );

  return data;
}

// Get Single Interview
export async function getInterview(
  id: number | string
): Promise<InterviewResponse> {
  const { data } = await api.get<InterviewResponse>(
    `/interviews/${id}`
  );

  return data;
}

// Generate Questions
export async function generateQuestions(
  id: number | string
): Promise<Question[]> {
  const { data } = await api.post<Question[]>(
    `/interviews/${id}/generate`
  );

  return data;
}

// Submit Answer
export async function submitAnswer(
  id: number | string,
  payload: SubmitAnswerRequest
) {
  const { data } = await api.post(
    `/interviews/${id}/answer`,
    payload
  );

  return data;
}

// Move to Next Question
export async function nextQuestion(
  id: number | string
) {
  const { data } = await api.post(
    `/interviews/${id}/next`
  );

  return data;
}