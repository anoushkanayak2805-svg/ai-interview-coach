import os
import shutil
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.repositories.resume_repository import save_resume


UPLOAD_FOLDER = "uploads/resumes"


def upload_resume(
    db: Session,
    user,
    file: UploadFile,
):

    if not file.filename.endswith(".pdf"):
        raise ValueError("Only PDF files are allowed.")

    os.makedirs(
        UPLOAD_FOLDER,
        exist_ok=True,
    )

    unique_filename = (
        f"{uuid4()}_{file.filename}"
    )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename,
    )

    with open(
        file_path,
        "wb",
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer,
        )

    resume = Resume(
        user_id=user.id,
        file_name=file.filename,
        file_path=file_path,
    )

    return save_resume(
        db,
        resume,
    )