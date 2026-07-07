import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from app.ai.client import client
from app.ai.constants import RESUME_MODEL
from app.ai.prompts.report_prompt import (
    build_report_prompt,
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
def generate_report(
    answers: list[dict],
):
    """
    Generate the final interview report using Gemini.
    """

    logger.info("Generating interview report")

    prompt = build_report_prompt(
        answers
    )

    start = time.time()

    response = client.models.generate_content(
        model=RESUME_MODEL,
        contents=prompt,
    )

    logger.info(
        f"Interview report generated in {time.time()-start:.2f}s"
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = (
            text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    try:
        return json.loads(text)

    except json.JSONDecodeError:

        logger.exception(
            "Invalid report JSON returned by Gemini"
        )

        raise ValueError(
            "Gemini returned invalid report JSON."
        )