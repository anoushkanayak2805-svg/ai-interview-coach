import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from app.ai.client import client
from app.ai.constants import RESUME_MODEL
from app.ai.prompts.resume_intelligence_prompt import (
    build_resume_intelligence_prompt,
)
from app.core.logging import logger
from app.schemas.resume_intelligence import (
    ResumeIntelligenceResponse,
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10,
    ),
)
def analyze_resume(
    resume_text: str,
):

    logger.info("Starting Resume Intelligence analysis")

    prompt = build_resume_intelligence_prompt(
        resume_text
    )

    start = time.time()

    response = client.models.generate_content(
        model=RESUME_MODEL,
        contents=prompt,
    )

    logger.info(
        f"Gemini completed in {time.time()-start:.2f} sec"
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = (
            text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

    try:
        data = json.loads(text)

    except json.JSONDecodeError:

        logger.exception(
            "Invalid JSON returned by Gemini"
        )

        raise ValueError(
            "Gemini returned invalid JSON."
        )

    validated = (
        ResumeIntelligenceResponse
        .model_validate(data)
    )

    logger.info(
        "Resume Intelligence completed"
    )

    return validated.model_dump()