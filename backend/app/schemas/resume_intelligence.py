from pydantic import BaseModel, Field


class ResumeIntelligenceResponse(BaseModel):
    """
    AI-generated Resume Intelligence.
    Used for generating personalized interviews.
    """

    candidate_level: str

    career_level: str

    experience_level: str

    coding_level: str

    backend_level: str

    database_level: str

    system_design_level: str

    communication_level: str

    confidence_level: str

    skills: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    technologies: list[str] = Field(default_factory=list)

    strengths: list[str] = Field(default_factory=list)

    weak_topics: list[str] = Field(default_factory=list)

    recommended_topics: list[str] = Field(default_factory=list)

    experience_summary: str