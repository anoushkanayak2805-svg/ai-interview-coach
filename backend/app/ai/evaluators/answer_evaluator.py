import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from app.ai.client import client
from app.ai.constants import (
    EVALUATION_MODEL,
    MIN_SCORE,
    MAX_SCORE,
)
from app.ai.prompts.evaluation_prompt import (
    build_evaluation_prompt,
)
from app.core.logging import logger
from app.schemas.ai import EvaluationResponse


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10,
    ),
)
def evaluate_answer(
    question: str,
    answer: str,
):
    logger.info("Starting Gemini answer evaluation")

    prompt = build_evaluation_prompt(
        question,
        answer,
    )

    start_time = time.time()

    response = client.models.generate_content(
        model=EVALUATION_MODEL,
        contents=prompt,
    )

    elapsed = time.time() - start_time

    logger.info(
        f"Gemini response received in {elapsed:.2f} seconds"
    )

    text = response.text.strip()

    # Remove markdown code blocks if present
    if text.startswith("```"):
        text = (
            text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    try:
        evaluation = json.loads(text)

    except json.JSONDecodeError:
        logger.exception("Gemini returned invalid JSON")
        raise ValueError(
            "Gemini returned invalid JSON."
        )

    required_fields = [
        "technical_score",
        "communication_score",
        "confidence_score",
        "strengths",
        "weaknesses",
        "improved_answer",
        "feedback",
    ]

    for field in required_fields:
        if field not in evaluation:
            logger.error(f"Missing field: {field}")
            raise ValueError(
                f"Missing field: {field}"
            )

    for score in (
        evaluation["technical_score"],
        evaluation["communication_score"],
        evaluation["confidence_score"],
    ):

        if not MIN_SCORE <= score <= MAX_SCORE:
            logger.error(
                "Gemini returned invalid score"
            )

            raise ValueError(
                "Invalid score returned by Gemini."
            )

    validated = EvaluationResponse.model_validate(
        evaluation
    )

    logger.info("Answer evaluation completed successfully")

    return validated.model_dump()