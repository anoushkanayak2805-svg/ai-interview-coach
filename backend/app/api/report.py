from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user

from app.repositories.interview_repository import (
    get_interview_by_id,
)

from app.services.report_service import (
    generate_interview_report,
)

router = APIRouter(
    prefix="/interviews",
    tags=["Reports"],
)


@router.get(
    "/{interview_id}/report",
)
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