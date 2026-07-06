from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
    skills: list[str]
    projects: list[str]

    experience_summary: str

    strengths: list[str]

    improvement_areas: list[str]