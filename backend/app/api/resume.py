from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User
from app.models.resume import Resume

from app.schemas.resume import ResumeResponse

from app.services.resume_service import (
    upload_resume,
)


router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


# ---------------------------------
# Upload Resume
# ---------------------------------

@router.post(
    "/upload",
    response_model=ResumeResponse,
)
def upload_resume_endpoint(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    return upload_resume(
        db,
        current_user,
        file,
    )


# ---------------------------------
# Get Current User's Latest Resume
# ---------------------------------

@router.get(
    "/me",
    response_model=ResumeResponse,
)
def get_my_resume(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):
    resume = (
        db.query(Resume)
        .filter(
            Resume.user_id == current_user.id
        )
        .order_by(
            Resume.id.desc()
        )
        .first()
    )

    if resume is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No resume found for this user.",
        )

    return resume