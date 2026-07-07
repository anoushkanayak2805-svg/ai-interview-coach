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


def generate_interview_report(
    db: Session,
    interview_id: int,
):
    """
    Generate the final AI interview report.
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

    technical = 0
    communication = 0
    confidence = 0

    for answer in answers:

        technical += answer.technical_score
        communication += answer.communication_score
        confidence += answer.confidence_score

        answer_data.append(
            {
                "answer": answer.answer_text,
                "technical_score": answer.technical_score,
                "communication_score": answer.communication_score,
                "confidence_score": answer.confidence_score,
                "strengths": answer.strengths,
                "weaknesses": answer.weaknesses,
            }
        )

    count = len(answer_data)

    avg_technical = technical / count
    avg_communication = communication / count
    avg_confidence = confidence / count

    ai_report = generate_report(
        answer_data
    )

    report = InterviewReport(

        interview_id=interview_id,

        overall_score=ai_report["overall_score"],

        technical_score=avg_technical,

        communication_score=avg_communication,

        confidence_score=avg_confidence,

        summary=ai_report["summary"],

        strengths=ai_report["strengths"],

        weaknesses=ai_report["weaknesses"],

        recommendations=ai_report["recommendations"],

        learning_roadmap=ai_report["learning_roadmap"],

        hiring_recommendation=ai_report[
            "hiring_recommendation"
        ],
    )

    return create_report(
        db,
        report,
    )