from app.ai.company.strategy import (
    get_company_profile,
)

from app.ai.profile.candidate_profile import (
    CandidateProfile,
)


def build_interview_strategy(
    company: str,
    difficulty: str,
    candidate: CandidateProfile,
):
    """
    Combine Candidate Profile with Company Profile
    to create the interview strategy used by Gemini.
    """

    profile = get_company_profile(company)

    return {

        # -------------------------
        # Company Information
        # -------------------------

        "company": company,

        "style": profile["style"],

        "difficulty": difficulty,

        "focus": profile["focus"],

        "preferred_topics": profile["preferred_topics"],

        "behavioral_weight": profile["behavioral_weight"],

        "technical_weight": profile["technical_weight"],

        "coding_difficulty": profile["coding_difficulty"],

        "system_design": profile["system_design"],

        "resume_weight": profile["resume_weight"],

        # -------------------------
        # Candidate Profile
        # -------------------------

        "candidate_level": candidate.candidate_level,

        "career_level": candidate.career_level,

        "experience_level": candidate.experience_level,

        "coding_level": candidate.coding_level,

        "backend_level": candidate.backend_level,

        "database_level": candidate.database_level,

        "system_design_level": candidate.system_design_level,

        "communication_level": candidate.communication_level,

        "confidence_level": candidate.confidence_level,

        "skills": candidate.skills,

        "projects": candidate.projects,

        "technologies": candidate.technologies,

        "strengths": candidate.strengths,

        "weak_topics": candidate.weak_topics,

        "recommended_topics": candidate.recommended_topics,

        "experience_summary": candidate.experience_summary,
    }