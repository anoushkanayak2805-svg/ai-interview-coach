from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user

from app.schemas.answer import (
    AnswerCreate,
    AnswerResponse
)

from app.services.answer_service import submit_answer

router = APIRouter(
    prefix="/interviews",
    tags=["Answers"]
)


@router.post(
    "/{interview_id}/answer",
    response_model=AnswerResponse
)
def submit_interview_answer(
    interview_id: int,
    answer: AnswerCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    result = submit_answer(
        db,
        interview_id,
        answer
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return result