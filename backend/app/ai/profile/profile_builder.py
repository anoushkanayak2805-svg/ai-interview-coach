from app.ai.profile.candidate_profile import (
    CandidateProfile,
)


def build_candidate_profile(
    intelligence: dict,
):
    """
    Convert Resume Intelligence into a
    CandidateProfile object.
    """

    return CandidateProfile.from_dict(
        intelligence
    )