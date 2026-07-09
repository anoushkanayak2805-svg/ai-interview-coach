import json
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from app.ai.client import client

from app.ai.constants import (
    RESUME_MODEL,
)

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

    If Gemini is unavailable, build a deterministic
    fallback report from valid saved evaluations.
    """

    logger.info(
        "Generating interview report"
    )

    prompt = build_report_prompt(
        answers
    )

    try:
        start = time.time()

        response = (
            client.models.generate_content(
                model=RESUME_MODEL,
                contents=prompt,
            )
        )

        logger.info(
            "Interview report generated in "
            f"{time.time() - start:.2f}s"
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty "
                "report response."
            )

        text = response.text.strip()

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
                    "Report is missing "
                    f"required field: {field}"
                )

        logger.info(
            "Interview report validated "
            "successfully"
        )

        return report

    except Exception as error:
        logger.warning(
            "Gemini report generation failed. "
            "Using fallback report. "
            f"Error: {error}"
        )

        return build_fallback_report(
            answers
        )


def build_fallback_report(
    answers: list[dict],
):
    """
    Build a deterministic report using only genuine
    answer evaluations.

    Answers affected by AI-service failures are not
    included in numerical score calculations.
    """

    if not answers:
        return {
            "overall_score": 0,

            "summary": (
                "No interview answers were "
                "available for report generation."
            ),

            "strengths": (
                "No strengths could be "
                "determined."
            ),

            "weaknesses": (
                "Complete an interview to "
                "receive performance feedback."
            ),

            "recommendations": (
                "Practice interview questions "
                "and provide complete, "
                "structured answers."
            ),

            "learning_roadmap": (
                "Begin with core technical "
                "concepts, then practice "
                "communication and mock "
                "interviews."
            ),

            "hiring_recommendation": (
                "Insufficient data for "
                "assessment."
            ),
        }

    valid_answers = [
        answer
        for answer in answers
        if answer.get(
            "evaluation_available",
            True,
        )
    ]

    total_count = len(answers)
    valid_count = len(valid_answers)
    unavailable_count = (
        total_count - valid_count
    )

    if valid_count == 0:
        return {
            "overall_score": 0,

            "summary": (
                f"The candidate completed "
                f"{total_count} interview "
                "answers, but numerical scoring "
                "was unavailable because the AI "
                "evaluation service could not "
                "successfully evaluate any "
                "answers."
            ),

            "strengths": (
                "The candidate completed the "
                "interview and submitted answers."
            ),

            "weaknesses": (
                "Performance could not be "
                "reliably scored because AI "
                "evaluation was unavailable."
            ),

            "recommendations": (
                "Retry the interview evaluation "
                "when the AI service is available."
            ),

            "learning_roadmap": (
                "Continue reviewing technical "
                "concepts and practicing clear, "
                "structured interview responses."
            ),

            "hiring_recommendation": (
                "Insufficient scored data for "
                "a reliable hiring assessment."
            ),
        }

    technical_scores = [
        float(
            answer.get(
                "technical_score",
                0,
            )
            or 0
        )
        for answer in valid_answers
    ]

    communication_scores = [
        float(
            answer.get(
                "communication_score",
                0,
            )
            or 0
        )
        for answer in valid_answers
    ]

    confidence_scores = [
        float(
            answer.get(
                "confidence_score",
                0,
            )
            or 0
        )
        for answer in valid_answers
    ]

    avg_technical = (
        sum(technical_scores)
        / valid_count
    )

    avg_communication = (
        sum(communication_scores)
        / valid_count
    )

    avg_confidence = (
        sum(confidence_scores)
        / valid_count
    )

    overall_score = round(
        (
            avg_technical
            + avg_communication
            + avg_confidence
        )
        / 3,
        2,
    )

    strengths = [
        answer.get("strengths")
        for answer in valid_answers
        if answer.get("strengths")
    ]

    weaknesses = [
        answer.get("weaknesses")
        for answer in valid_answers
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
            "Strong candidate. Recommended "
            "to proceed to the next interview "
            "stage."
        )

    elif overall_score >= 65:
        hiring_recommendation = (
            "Promising candidate. Consider "
            "proceeding after further "
            "technical evaluation."
        )

    elif overall_score >= 50:
        hiring_recommendation = (
            "Candidate shows potential but "
            "requires additional preparation "
            "before proceeding."
        )

    else:
        hiring_recommendation = (
            "Further preparation is "
            "recommended before proceeding "
            "to the next interview stage."
        )

    if unavailable_count > 0:
        scoring_note = (
            f" {unavailable_count} answer(s) "
            "were excluded from numerical "
            "scoring because AI evaluation "
            "was unavailable."
        )
    else:
        scoring_note = ""

    return {
        "overall_score": overall_score,

        "summary": (
            f"The candidate completed "
            f"{total_count} interview answers. "
            f"{valid_count} answer(s) were "
            f"successfully scored, with an "
            f"average technical score of "
            f"{avg_technical:.1f}, "
            f"communication score of "
            f"{avg_communication:.1f}, and "
            f"confidence score of "
            f"{avg_confidence:.1f}."
            f"{scoring_note}"
        ),

        "strengths": (
            "\n".join(
                f"• {item}"
                for item in unique_strengths[
                    :5
                ]
            )
            if unique_strengths
            else (
                "The candidate completed the "
                "interview and attempted all "
                "available questions."
            )
        ),

        "weaknesses": (
            "\n".join(
                f"• {item}"
                for item in unique_weaknesses[
                    :5
                ]
            )
            if unique_weaknesses
            else (
                "Continue improving technical "
                "depth, clarity, and confidence."
            )
        ),

        "recommendations": (
            "Review weak technical topics, "
            "practice structured answers using "
            "clear examples, and complete "
            "additional mock interviews under "
            "timed conditions."
        ),

        "learning_roadmap": (
            "1. Review the technical concepts "
            "identified as weak areas.\n"
            "2. Practice explaining solutions "
            "clearly and step by step.\n"
            "3. Solve role-specific interview "
            "questions.\n"
            "4. Complete another timed mock "
            "interview.\n"
            "5. Compare your next report with "
            "this result to measure improvement."
        ),

        "hiring_recommendation": (
            hiring_recommendation
        ),
    }