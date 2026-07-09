import json
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

from app.utils.pdf_parser import (
    extract_text_from_pdf,
)

from app.ai.analyzers.resume_intelligence import (
    analyze_resume,
)

from app.core.logging import logger


UPLOAD_FOLDER = "uploads/resumes"


def upload_resume(
    db: Session,
    user,
    file: UploadFile,
):
    """
    Upload a resume, extract its text,
    analyze it with Resume Intelligence,
    and save the results in the database.

    If AI analysis fails because of quota limits,
    network errors, or another API issue,
    the resume upload will still succeed.
    """

    # ---------------------------------
    # Validate PDF
    # ---------------------------------

    if not file.filename:
        raise ValueError(
            "File name is missing."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise ValueError(
            "Only PDF files are allowed."
        )

    # ---------------------------------
    # Create Upload Directory
    # ---------------------------------

    os.makedirs(
        UPLOAD_FOLDER,
        exist_ok=True,
    )

    # ---------------------------------
    # Save PDF File
    # ---------------------------------

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

    logger.info(
        f"Resume file saved: {file.filename}"
    )

    # ---------------------------------
    # Save Resume Metadata
    # ---------------------------------

    resume = Resume(
        user_id=user.id,
        file_name=file.filename,
        file_path=file_path,
    )

    resume = save_resume(
        db,
        resume,
    )

    logger.info(
        f"Resume metadata saved with ID: "
        f"{resume.id}"
    )

    # ---------------------------------
    # Extract Text From PDF
    # ---------------------------------

    try:
        logger.info(
            f"Extracting text from resume: "
            f"{file.filename}"
        )

        text = extract_text_from_pdf(
            file_path
        )

    except Exception as error:
        logger.warning(
            f"Resume text extraction failed. "
            f"Error: {error}"
        )

        return resume

    # ---------------------------------
    # Validate Extracted Text
    # ---------------------------------

    if not text or not text.strip():
        logger.warning(
            "No readable text found in resume."
        )

        return resume

    # ---------------------------------
    # Save Extracted Text
    # ---------------------------------

    try:
        resume = update_resume_text(
            db,
            resume,
            text,
        )

        logger.info(
            "Extracted resume text saved successfully"
        )

    except Exception as error:
        logger.warning(
            f"Failed to save extracted resume text. "
            f"Error: {error}"
        )

        db.rollback()

        return resume

    # ---------------------------------
    # Run Resume Intelligence
    # ---------------------------------

    try:
        logger.info(
            "Running Resume Intelligence "
            "during resume upload"
        )

        intelligence = analyze_resume(
            text
        )

        # ---------------------------------
        # Extract AI Results
        # ---------------------------------

        skills = intelligence.get(
            "skills",
            [],
        )

        projects = intelligence.get(
            "projects",
            [],
        )

        # ---------------------------------
        # Save AI Analysis
        #
        # Database columns are Text fields,
        # so lists and dictionaries are
        # stored as JSON strings.
        # ---------------------------------

        resume.skills = json.dumps(
            skills,
            ensure_ascii=False,
        )

        resume.projects = json.dumps(
            projects,
            ensure_ascii=False,
        )

        resume.analysis = json.dumps(
            intelligence,
            ensure_ascii=False,
        )

        db.commit()

        db.refresh(
            resume
        )

        logger.info(
            "Resume Intelligence saved successfully"
        )

    except Exception as error:
        logger.warning(
            f"Resume Intelligence failed. "
            f"Resume upload will continue "
            f"without AI analysis. "
            f"Error: {error}"
        )

        try:
            db.rollback()
        except Exception:
            pass

        try:
            db.refresh(resume)
        except Exception:
            pass

    # ---------------------------------
    # Return Resume
    # ---------------------------------

    return resume