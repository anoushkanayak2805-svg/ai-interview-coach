from pydantic import BaseModel


class ResumeIntelligenceResponse(BaseModel):

    candidate_level: str

    skills: list[str]

    projects: list[str]

    technologies: list[str]

    strengths: list[str]

    weak_topics: list[str]

    recommended_topics: list[str]

    experience_summary: str