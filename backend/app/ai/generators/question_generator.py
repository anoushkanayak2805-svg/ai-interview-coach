import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from app.ai.client import client
from app.ai.constants import QUESTION_MODEL

from app.ai.profile.candidate_profile import (
    CandidateProfile,
)

from app.ai.company.interview_strategy import (
    build_interview_strategy,
)

from app.ai.prompts.interview_prompt import (
    build_interview_prompt,
)

from app.core.logging import logger


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10,
    ),
)
def generate_questions(
    company: str,
    role: str,
    difficulty: str,
    candidate: CandidateProfile | None = None,
    resume_text: str | None = None,
):
    """
    Generate personalized interview questions using:

    Resume
        ↓
    Candidate Profile
        ↓
    Company Strategy
        ↓
    Gemini
    """

    logger.info(
        f"Generating interview questions for {company} - {role}"
    )

    if candidate is None:

        candidate = CandidateProfile(
            candidate_level="Unknown",
            career_level="Unknown",
            experience_level="Unknown",
            coding_level="Unknown",
            backend_level="Unknown",
            database_level="Unknown",
            system_design_level="Unknown",
            communication_level="Unknown",
            confidence_level="Unknown",
            skills=[],
            projects=[],
            technologies=[],
            strengths=[],
            weak_topics=[],
            recommended_topics=[],
            experience_summary="",
        )

    strategy = build_interview_strategy(
        company=company,
        difficulty=difficulty,
        candidate=candidate,
    )

    prompt = build_interview_prompt(
        role=role,
        strategy=strategy,
        resume_text=resume_text,
    )

    start_time = time.time()

    response = client.models.generate_content(
        model=QUESTION_MODEL,
        contents=prompt,
    )

    elapsed = time.time() - start_time

    logger.info(
        f"Question generation completed in {elapsed:.2f} seconds"
    )

    text = response.text.strip()

    # Remove markdown code blocks if Gemini wraps JSON
    if text.startswith("```"):
        text = (
            text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    try:
        questions = json.loads(text)

    except json.JSONDecodeError:

        logger.exception(
            "Gemini returned invalid JSON"
        )

        raise ValueError(
            "Gemini returned invalid JSON."
        )

    if not isinstance(questions, list):
        raise ValueError(
            "Gemini response is not a JSON list."
        )

    if len(questions) != 10:
        raise ValueError(
            f"Expected 10 questions, received {len(questions)}."
        )

    required_fields = [
        "question",
        "category",
    ]

    for index, question in enumerate(
        questions,
        start=1,
    ):

        for field in required_fields:

            if field not in question:

                raise ValueError(
                    f"Question {index} is missing '{field}'."
                )

    logger.info(
        "Interview questions generated successfully"
    )

    return questions