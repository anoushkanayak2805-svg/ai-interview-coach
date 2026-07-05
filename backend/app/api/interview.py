from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.interview import (
    InterviewCreate,
    InterviewResponse,
)
from app.services.interview_service import (
    create_new_interview,
)
from app.repositories.interview_repository import (
    get_interviews_by_user,
)

from fastapi import HTTPException

from app.repositories.interview_repository import (
    get_interview_by_id,
)

from app.services.interview_service import (
    generate_interview_questions,
)

from app.schemas.question import QuestionResponse

from app.repositories.question_repository import (
    get_questions_by_interview,
)
router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"],
)


@router.post(
    "",
    response_model=InterviewResponse,
)
def create_interview(
    interview: InterviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_new_interview(
        db,
        current_user,
        interview,
    )


@router.get(
    "",
    response_model=list[InterviewResponse],
)
def get_my_interviews(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_interviews_by_user(
        db,
        current_user.id,
    )

@router.post(
    "/{interview_id}/generate",
    response_model=list[QuestionResponse]
)
def generate_questions(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    interview = get_interview_by_id(
        db,
        interview_id
    )

    if interview is None:

        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    if interview.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return generate_interview_questions(
        db,
        interview
    )

@router.get(
    "/{interview_id}/questions",
    response_model=list[QuestionResponse]
)
def get_questions(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    interview = get_interview_by_id(
        db,
        interview_id
    )

    if interview is None:

        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    return get_questions_by_interview(
        db,
        interview_id
    )



