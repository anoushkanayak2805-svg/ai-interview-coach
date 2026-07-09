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

    If Gemini is unavailable because of quota limits,
    network errors, invalid JSON, or another API failure,
    return a fallback report so the interview flow can continue.
    """

    logger.info("Generating interview report")

    prompt = build_report_prompt(
        answers
    )

    try:
        start = time.time()

        response = client.models.generate_content(
            model=RESUME_MODEL,
            contents=prompt,
        )

        logger.info(
            f"Interview report generated in "
            f"{time.time() - start:.2f}s"
        )

        text = response.text.strip()

        # Remove markdown code blocks if Gemini wraps JSON
        if text.startswith("```"):
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        report = json.loads(text)

        required_fields = [
            "overall_score",
            "summary",
            "strengths",
            "weaknesses",
            "recommendations",
            "learning_roadmap",
            "hiring_recommendation",
        ]

        for field in required_fields:
            if field not in report:
                raise ValueError(
                    f"Report is missing required field: {field}"
                )

        logger.info(
            "Interview report validated successfully"
        )

        return report

    except Exception as error:
        logger.warning(
            f"Gemini report generation failed. "
            f"Using fallback report. Error: {error}"
        )

        return build_fallback_report(
            answers
        )


def build_fallback_report(
    answers: list[dict],
):
    """
    Build a deterministic fallback report from saved
    answer evaluation scores when Gemini is unavailable.
    """

    if not answers:
        return {
            "overall_score": 0,
            "summary": (
                "No interview answers were available "
                "for report generation."
            ),
            "strengths": (
                "No strengths could be determined."
            ),
            "weaknesses": (
                "Complete an interview to receive "
                "performance feedback."
            ),
            "recommendations": (
                "Practice interview questions and provide "
                "complete, structured answers."
            ),
            "learning_roadmap": (
                "Begin with core technical concepts, then "
                "practice communication and mock interviews."
            ),
            "hiring_recommendation": (
                "Insufficient data for assessment."
            ),
        }

    technical_scores = [
        float(answer.get("technical_score", 0) or 0)
        for answer in answers
    ]

    communication_scores = [
        float(answer.get("communication_score", 0) or 0)
        for answer in answers
    ]

    confidence_scores = [
        float(answer.get("confidence_score", 0) or 0)
        for answer in answers
    ]

    count = len(answers)

    avg_technical = (
        sum(technical_scores) / count
    )

    avg_communication = (
        sum(communication_scores) / count
    )

    avg_confidence = (
        sum(confidence_scores) / count
    )

    overall_score = round(
        (
            avg_technical
            + avg_communication
            + avg_confidence
        ) / 3,
        2,
    )

    strengths = [
        answer.get("strengths")
        for answer in answers
        if answer.get("strengths")
    ]

    weaknesses = [
        answer.get("weaknesses")
        for answer in answers
        if answer.get("weaknesses")
    ]

    unique_strengths = list(
        dict.fromkeys(strengths)
    )

    unique_weaknesses = list(
        dict.fromkeys(weaknesses)
    )

    if overall_score >= 80:
        hiring_recommendation = (
            "Strong candidate. Recommended to proceed "
            "to the next interview stage."
        )

    elif overall_score >= 65:
        hiring_recommendation = (
            "Promising candidate. Consider proceeding "
            "after further technical evaluation."
        )

    elif overall_score >= 50:
        hiring_recommendation = (
            "Candidate shows potential but requires "
            "additional preparation before proceeding."
        )

    else:
        hiring_recommendation = (
            "Further preparation is recommended before "
            "proceeding to the next interview stage."
        )

    return {
        "overall_score": overall_score,

        "summary": (
            f"The candidate completed {count} interview "
            f"answers with an average technical score of "
            f"{avg_technical:.1f}, communication score of "
            f"{avg_communication:.1f}, and confidence score "
            f"of {avg_confidence:.1f}. This report was "
            f"generated from the saved answer evaluations."
        ),

        "strengths": (
            "\n".join(
                f"• {item}"
                for item in unique_strengths[:5]
            )
            if unique_strengths
            else (
                "The candidate completed the interview "
                "and attempted all available questions."
            )
        ),

        "weaknesses": (
            "\n".join(
                f"• {item}"
                for item in unique_weaknesses[:5]
            )
            if unique_weaknesses
            else (
                "Continue improving technical depth, "
                "clarity, and confidence."
            )
        ),

        "recommendations": (
            "Review weak technical topics, practice "
            "structured answers using clear examples, "
            "and complete additional mock interviews "
            "under timed conditions."
        ),

        "learning_roadmap": (
            "1. Review the technical concepts identified "
            "as weak areas.\n"
            "2. Practice explaining solutions clearly and "
            "step by step.\n"
            "3. Solve role-specific interview questions.\n"
            "4. Complete another timed mock interview.\n"
            "5. Compare your next report with this result "
            "to measure improvement."
        ),

        "hiring_recommendation": hiring_recommendation,
    }