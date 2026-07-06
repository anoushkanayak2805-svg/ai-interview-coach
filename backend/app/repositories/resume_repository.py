from sqlalchemy.orm import Session

from app.models.resume import Resume


def save_resume(
    db: Session,
    resume: Resume,
):
    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume


def get_latest_resume(
    db: Session,
    user_id: int,
):
    return (
        db.query(Resume)
        .filter(
            Resume.user_id == user_id
        )
        .order_by(
            Resume.created_at.desc()
        )
        .first()
    )

def update_resume_text(
    db,
    resume: Resume,
    extracted_text: str,
):

    resume.extracted_text = extracted_text

    db.commit()

    db.refresh(resume)

    return resume

def update_resume_analysis(
    db,
    resume,
    analysis,
):

    resume.analysis = analysis["experience_summary"]

    resume.skills = ",".join(
        analysis["skills"]
    )

    resume.projects = ",".join(
        analysis["projects"]
    )

    db.commit()

    db.refresh(resume)

    return resume