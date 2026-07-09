from sqlalchemy.orm import Session

from app.models.report import InterviewReport

from app.repositories.answer_repository import (
    get_answers_by_interview,
)

from app.repositories.report_repository import (
    create_report,
    get_report_by_interview,
)

from app.ai.generators.report_generator import (
    generate_report,
)


def _is_failed_ai_evaluation(
    answer,
) -> bool:
    """
    Determine whether an answer was not genuinely
    scored because the AI service was unavailable.

    A genuine low score of 0 must still count.
    Only explicit AI-service failures are excluded.
    """

    feedback = str(
        getattr(
            answer,
            "feedback",
            "",
        )
        or ""
    ).lower()

    weaknesses = str(
        getattr(
            answer,
            "weaknesses",
            "",
        )
        or ""
    ).lower()

    combined_text = (
        f"{feedback} {weaknesses}"
    )

    failure_markers = [
        "ai evaluation unavailable",
        "evaluation unavailable",
        "ai service or quota failure",
        "gemini quota was exceeded",
        "default evaluation used",
        "ai evaluation service was temporarily unavailable",
    ]

    return any(
        marker in combined_text
        for marker in failure_markers
    )


def generate_interview_report(
    db: Session,
    interview_id: int,
):
    """
    Generate the final AI interview report.

    AI-service failures are excluded from score
    calculations instead of being treated as poor
    candidate performance.
    """

    existing = get_report_by_interview(
        db,
        interview_id,
    )

    if existing:
        return existing

    answers = get_answers_by_interview(
        db,
        interview_id,
    )

    if not answers:
        raise ValueError(
            "No interview answers found."
        )

    answer_data = []

    valid_technical_scores = []
    valid_communication_scores = []
    valid_confidence_scores = []

    for answer in answers:
        evaluation_available = (
            not _is_failed_ai_evaluation(
                answer
            )
        )

        if evaluation_available:
            valid_technical_scores.append(
                float(
                    answer.technical_score
                    or 0
                )
            )

            valid_communication_scores.append(
                float(
                    answer.communication_score
                    or 0
                )
            )

            valid_confidence_scores.append(
                float(
                    answer.confidence_score
                    or 0
                )
            )

        answer_data.append(
            {
                "answer": (
                    answer.answer_text
                ),

                "technical_score": (
                    answer.technical_score
                ),

                "communication_score": (
                    answer.communication_score
                ),

                "confidence_score": (
                    answer.confidence_score
                ),

                "strengths": (
                    answer.strengths
                ),

                "weaknesses": (
                    answer.weaknesses
                ),

                "feedback": getattr(
                    answer,
                    "feedback",
                    None,
                ),

                "evaluation_available": (
                    evaluation_available
                ),
            }
        )

    valid_count = len(
        valid_technical_scores
    )

    if valid_count > 0:
        avg_technical = (
            sum(valid_technical_scores)
            / valid_count
        )

        avg_communication = (
            sum(
                valid_communication_scores
            )
            / valid_count
        )

        avg_confidence = (
            sum(valid_confidence_scores)
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

    else:
        avg_technical = 0
        avg_communication = 0
        avg_confidence = 0
        overall_score = 0

    ai_report = generate_report(
        answer_data
    )

    # The deterministic score calculated from valid
    # saved evaluations is the source of truth.
    # Do not allow Gemini report generation to invent
    # or alter the candidate's final numerical score.
    ai_report["overall_score"] = (
        overall_score
    )

    report = InterviewReport(
        interview_id=interview_id,

        overall_score=overall_score,

        technical_score=round(
            avg_technical,
            2,
        ),

        communication_score=round(
            avg_communication,
            2,
        ),

        confidence_score=round(
            avg_confidence,
            2,
        ),

        summary=ai_report["summary"],

        strengths=ai_report["strengths"],

        weaknesses=ai_report["weaknesses"],

        recommendations=(
            ai_report[
                "recommendations"
            ]
        ),

        learning_roadmap=(
            ai_report[
                "learning_roadmap"
            ]
        ),

        hiring_recommendation=(
            ai_report[
                "hiring_recommendation"
            ]
        ),
    )

    return create_report(
        db,
        report,
    )