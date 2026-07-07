from app.ai.company.profiles import COMPANY_PROFILES


def get_company_profile(
    company: str,
):
    """
    Return interview strategy for a company.
    """

    return COMPANY_PROFILES.get(
        company,
        {
            "style": "General",

            "focus": [
                "Coding",
                "Problem Solving",
                "Behavioral",
            ],

            "behavioral_weight": 30,

            "technical_weight": 70,

            "coding_difficulty": "Medium",

            "system_design": False,

            "resume_weight": 70,

            "preferred_topics": [
                "DSA",
                "DBMS",
                "OOP",
            ],
        },
    )