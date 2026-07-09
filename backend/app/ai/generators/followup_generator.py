import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from app.ai.client import client
from app.ai.constants import QUESTION_MODEL
from app.core.logging import logger


# Default fallback follow-up questions
FALLBACK_QUESTIONS = [
    {
        "question": "Can you explain the time complexity of Binary Search?",
        "category": "DSA",
    },
    {
        "question": "What is the difference between a process and a thread?",
        "category": "Operating Systems",
    },
    {
        "question": "Explain normalization in DBMS.",
        "category": "DBMS",
    },
    {
        "question": "What are the four pillars of Object-Oriented Programming?",
        "category": "OOP",
    },
    {
        "question": "Describe a challenging project you have worked on.",
        "category": "Behavioral",
    },
]


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(
        multiplier=1,
        min=2,
        max=10,
    ),
)
def generate_followup_question(
    company: str,
    role: str,
    previous_question: str,
    candidate_answer: str,
    evaluation: dict,
):
    logger.info("Generating adaptive follow-up question")

    prompt = f"""
You are a Senior {company} interviewer.

Role:
{role}

Previous Question:
{previous_question}

Candidate Answer:
{candidate_answer}

Evaluation

Technical Score:
{evaluation["technical_score"]}

Communication Score:
{evaluation["communication_score"]}

Confidence Score:
{evaluation["confidence_score"]}

Strengths:
{evaluation["strengths"]}

Weaknesses:
{evaluation["weaknesses"]}

Generate ONE intelligent follow-up question.

Rules:

• If answer was excellent, increase difficulty.
• If answer was weak, ask a simpler conceptual question.
• Ask only ONE question.

Return ONLY JSON.

{{
    "question":"...",
    "category":"..."
}}
"""

    try:
        start = time.time()

        response = client.models.generate_content(
            model=QUESTION_MODEL,
            contents=prompt,
        )

        logger.info(
            f"Generated follow-up in {time.time() - start:.2f}s"
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(text)

    except Exception as e:
        logger.exception(
            "Gemini unavailable. Using fallback follow-up question."
        )

        logger.warning(str(e))

        # Rotate fallback questions based on previous question
        index = abs(hash(previous_question)) % len(FALLBACK_QUESTIONS)

        return FALLBACK_QUESTIONS[index]