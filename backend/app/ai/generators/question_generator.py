import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from app.ai.client import client
from app.ai.constants import QUESTION_MODEL
from app.ai.prompts.interview_prompt import build_interview_prompt
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
    resume_text: str | None = None,
    intelligence: dict | None = None,
):
    logger.info(
        f"Generating interview questions for {company} - {role}"
    )

    prompt = build_interview_prompt(
        company=company,
        role=role,
        difficulty=difficulty,
        resume_text=resume_text,
        intelligence=intelligence,
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
        logger.exception("Gemini returned invalid JSON")
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