import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
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


class AIEvaluationError(Exception):
    """
    Raised when Gemini cannot successfully evaluate
    an interview answer.
    """

    pass


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10,
    ),
    retry=retry_if_exception_type(
        AIEvaluationError
    ),
    reraise=True,
)
def _evaluate_with_gemini(
    question: str,
    answer: str,
):
    """
    Perform Gemini answer evaluation.

    Exceptions are re-raised so Tenacity can retry
    the operation up to 3 times.
    """

    logger.info(
        "Starting Gemini answer evaluation"
    )

    prompt = build_evaluation_prompt(
        question,
        answer,
    )

    try:
        start_time = time.time()

        response = client.models.generate_content(
            model=EVALUATION_MODEL,
            contents=prompt,
        )

        elapsed = (
            time.time() - start_time
        )

        logger.info(
            f"Gemini response received in "
            f"{elapsed:.2f} seconds"
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        text = response.text.strip()

        # Remove Markdown code blocks if Gemini
        # wraps the JSON response.
        if text.startswith("```"):
            text = (
                text.replace(
                    "```json",
                    "",
                )
                .replace(
                    "```",
                    "",
                )
                .strip()
            )

        evaluation = json.loads(text)

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
                raise ValueError(
                    f"Missing field: {field}"
                )

        score_fields = [
            "technical_score",
            "communication_score",
            "confidence_score",
        ]

        for field in score_fields:
            try:
                score = float(
                    evaluation[field]
                )
            except (
                TypeError,
                ValueError,
            ) as error:
                raise ValueError(
                    f"Invalid numeric score "
                    f"for {field}."
                ) from error

            if not (
                MIN_SCORE
                <= score
                <= MAX_SCORE
            ):
                raise ValueError(
                    f"{field} must be between "
                    f"{MIN_SCORE} and {MAX_SCORE}."
                )

        validated = (
            EvaluationResponse.model_validate(
                evaluation
            )
        )

        result = validated.model_dump()

        logger.info(
            "Answer evaluation completed "
            "successfully"
        )

        return result

    except Exception as error:
        logger.warning(
            "Gemini evaluation attempt failed. "
            f"Error: {error}"
        )

        # Important:
        # Re-raise as AIEvaluationError so
        # Tenacity actually retries.
        raise AIEvaluationError(
            str(error)
        ) from error


def evaluate_answer(
    question: str,
    answer: str,
):
    """
    Evaluate an interview answer.

    If Gemini remains unavailable after all retry
    attempts, return a storage-compatible fallback.

    The fallback scores are zero only because the
    current database/schema expects numerical values.

    These scores must be excluded from report
    averaging by report_service.py using the explicit
    failure marker saved in feedback/weaknesses.
    """

    try:
        return _evaluate_with_gemini(
            question,
            answer,
        )

    except Exception as error:
        logger.exception(
            "Gemini evaluation failed after "
            "all retries. Returning unscored "
            "fallback evaluation."
        )

        return {
            "technical_score": 0,
            "communication_score": 0,
            "confidence_score": 0,

            "strengths": (
                "Candidate submitted an answer, "
                "but AI evaluation was unavailable."
            ),

            "weaknesses": (
                "This answer was not scored because "
                "the AI evaluation service was "
                "temporarily unavailable."
            ),

            "improved_answer": answer,

            # Keep this exact wording because
            # report_service.py uses it to detect
            # failed AI evaluations.
            "feedback": (
                "Evaluation unavailable due to an "
                "AI service or quota failure."
            ),
        }