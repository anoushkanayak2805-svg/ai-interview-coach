from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user

from app.repositories.interview_repository import (
    get_interview_by_id,
)

from app.repositories.report_repository import (
    get_reports_by_user,
)

from app.services.report_service import (
    generate_interview_report,
)


# --------------------------------------------------
# Reports History Router
# Endpoint: GET /reports
# --------------------------------------------------

reports_router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@reports_router.get("")
def get_all_reports(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Return all interview reports belonging
    to the currently authenticated user.
    """

    reports = get_reports_by_user(
        db,
        current_user.id,
    )

    result = []

    for report in reports:

        interview = report.interview

        result.append(
            {
                "id": report.id,
                "interview_id": report.interview_id,

                "company": interview.company,
                "role": interview.role,

                "overall_score": report.overall_score,
                "technical_score": report.technical_score,
                "communication_score": report.communication_score,
                "confidence_score": report.confidence_score,

                "summary": report.summary,
                "strengths": report.strengths,
                "weaknesses": report.weaknesses,
                "recommendations": report.recommendations,
                "learning_roadmap": report.learning_roadmap,
                "hiring_recommendation": report.hiring_recommendation,

                "created_at": report.created_at,
            }
        )

    return result


# --------------------------------------------------
# Single Interview Report Router
# Endpoint: GET /interviews/{interview_id}/report
# --------------------------------------------------

router = APIRouter(
    prefix="/interviews",
    tags=["Reports"],
)


@router.get("/{interview_id}/report")
def get_report(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    interview = get_interview_by_id(
        db,
        interview_id,
    )

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview not found",
        )

    if interview.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    return generate_interview_report(
        db,
        interview_id,
    )