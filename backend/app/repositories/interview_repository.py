from sqlalchemy.orm import Session

from app.models.interview import InterviewSession


def create_interview(db: Session, interview: InterviewSession):
    db.add(interview)
    db.commit()
    db.refresh(interview)
    return interview


def get_interviews_by_user(db: Session, user_id: int):
    return (
        db.query(InterviewSession)
        .filter(InterviewSession.user_id == user_id)
        .order_by(InterviewSession.created_at.desc())
        .all()
    )
def update_interview(db, interview):
    db.commit()
    db.refresh(interview)
    return interview

def get_interview_by_id(
    db: Session,
    interview_id: int
):
    return (
        db.query(InterviewSession)
        .filter(
            InterviewSession.id == interview_id
        )
        .first()
    )