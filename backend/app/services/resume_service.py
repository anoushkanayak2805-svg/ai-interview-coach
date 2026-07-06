import os
import shutil
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resume import Resume

from app.repositories.resume_repository import (
    save_resume,
    update_resume_text,
)

from app.utils.pdf_parser import extract_text_from_pdf


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

    unique_filename = f"{uuid4()}_{file.filename}"

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

    # Save resume metadata
    resume = Resume(
        user_id=user.id,
        file_name=file.filename,
        file_path=file_path,
    )

    resume = save_resume(
        db,
        resume,
    )

    # Extract text from PDF
    text = extract_text_from_pdf(
        file_path,
    )

    # Update extracted text
    resume = update_resume_text(
        db,
        resume,
        text,
    )

    return resume