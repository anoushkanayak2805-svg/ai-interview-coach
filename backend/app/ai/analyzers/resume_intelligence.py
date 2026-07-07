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
    """
    Analyze a resume using Gemini AI.

    Returns a validated Resume Intelligence dictionary.

    Output example:

    {
        "candidate_level": "...",
        "skills": [...],
        "projects": [...],
        "technologies": [...],
        "recommended_topics": [...],
        "weak_topics": [...]
    }
    """

    logger.info(
        "Starting Resume Intelligence analysis"
    )

    prompt = build_resume_intelligence_prompt(
        resume_text
    )

    start_time = time.time()

    response = client.models.generate_content(
        model=RESUME_MODEL,
        contents=prompt,
    )

    elapsed = time.time() - start_time

    logger.info(
        f"Resume Intelligence completed in {elapsed:.2f} seconds"
    )

    text = response.text.strip()

    # Gemini sometimes wraps JSON inside markdown
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
            "Gemini returned invalid Resume Intelligence JSON"
        )

        raise ValueError(
            "Gemini returned invalid JSON."
        )

    validated = ResumeIntelligenceResponse.model_validate(
        data
    )

    intelligence = validated.model_dump()

    required_fields = [
        "candidate_level",
        "skills",
        "projects",
        "technologies",
        "recommended_topics",
        "weak_topics",
    ]

    for field in required_fields:

        if field not in intelligence:

            raise ValueError(
                f"Resume Intelligence missing '{field}'."
            )

    logger.info(
        "Resume Intelligence validated successfully"
    )

    return intelligence