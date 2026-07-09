import api from "./axios";


/* ---------------------------------
   Resume Intelligence Analysis
---------------------------------- */

export interface ResumeAnalysis {
  candidate_level?: string;

  career_level?: string;

  experience_level?: string;

  coding_level?: string;

  backend_level?: string;

  database_level?: string;

  system_design_level?: string;

  communication_level?: string;

  confidence_level?: string;

  skills?: string[];

  projects?: string[];

  technologies?: string[];

  strengths?: string[];

  weak_topics?: string[];

  recommended_topics?: string[];

  experience_summary?: string;
}


/* ---------------------------------
   Raw Backend Resume Response
---------------------------------- */

interface RawResumeResponse {
  id: number;

  file_name: string;

  skills: string | null;

  projects: string | null;

  analysis: string | null;

  created_at: string;
}


/* ---------------------------------
   Frontend Resume Response
---------------------------------- */

export interface ResumeResponse {
  id: number;

  file_name: string;

  skills: string[];

  projects: string[];

  analysis: ResumeAnalysis | null;

  created_at: string;
}


/* ---------------------------------
   Safe JSON Parser
---------------------------------- */

function parseJSON<T>(
  value: string | null,
  fallback: T
): T {
  if (!value) {
    return fallback;
  }

  try {
    return JSON.parse(value) as T;
  } catch (error) {
    console.error(
      "Failed to parse resume JSON:",
      error
    );

    return fallback;
  }
}


/* ---------------------------------
   Transform Backend Response
---------------------------------- */

function transformResume(
  data: RawResumeResponse
): ResumeResponse {
  return {
    id: data.id,

    file_name: data.file_name,

    skills: parseJSON<string[]>(
      data.skills,
      []
    ),

    projects: parseJSON<string[]>(
      data.projects,
      []
    ),

    analysis:
      parseJSON<ResumeAnalysis | null>(
        data.analysis,
        null
      ),

    created_at: data.created_at,
  };
}


/* ---------------------------------
   Upload Resume
---------------------------------- */

export async function uploadResume(
  file: File
): Promise<ResumeResponse> {
  const formData = new FormData();

  formData.append(
    "file",
    file
  );

  const { data } =
    await api.post<RawResumeResponse>(
      "/resume/upload",
      formData,
      {
        headers: {
          "Content-Type":
            "multipart/form-data",
        },
      }
    );

  return transformResume(data);
}


/* ---------------------------------
   Get Current User Resume
---------------------------------- */

export async function getMyResume():
  Promise<ResumeResponse> {

  const { data } =
    await api.get<RawResumeResponse>(
      "/resume/me"
    );

  return transformResume(data);
}