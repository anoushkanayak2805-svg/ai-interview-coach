from dataclasses import dataclass, field


@dataclass
class CandidateProfile:
    """
    Represents the complete AI understanding
    of the candidate.
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

    skills: list[str] = field(default_factory=list)

    projects: list[str] = field(default_factory=list)

    technologies: list[str] = field(default_factory=list)

    strengths: list[str] = field(default_factory=list)

    weak_topics: list[str] = field(default_factory=list)

    recommended_topics: list[str] = field(default_factory=list)

    experience_summary: str = ""

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):
        return cls(**data)