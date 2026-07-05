from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.answer import (
    AnswerCreate,
    AnswerResponse
)

from app.services.answer_service import save_answer

router = APIRouter(
    prefix="/questions",
    tags=["Answers"]
)


@router.post(
    "/{question_id}/answer",
    response_model=AnswerResponse
)
def submit_answer(
    question_id: int,
    answer: AnswerCreate,
    db: Session = Depends(get_db)
):

    return save_answer(
        db,
        question_id,
        answer.answer_text
    )