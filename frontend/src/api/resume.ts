import api from "./axios";

export interface ResumeResponse {
  id: number;
  filename: string;
  extracted_skills?: string[];
  extracted_projects?: string[];
}

export async function uploadResume(file: File) {
  const formData = new FormData();

  formData.append("file", file);

  const { data } = await api.post(
    "/resume/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return data as ResumeResponse;
}