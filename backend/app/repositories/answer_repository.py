from sqlalchemy.orm import Session

from app.models.answer import InterviewAnswer


def save_answer(
    db: Session,
    answer: InterviewAnswer,
):
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer


def get_answer_by_id(
    db: Session,
    answer_id: int,
):
    return (
        db.query(InterviewAnswer)
        .filter(
            InterviewAnswer.id == answer_id
        )
        .first()
    )


def get_answers_by_interview(
    db: Session,
    interview_id: int,
):
    return (
        db.query(InterviewAnswer)
        .filter(
            InterviewAnswer.interview_id == interview_id
        )
        .order_by(
            InterviewAnswer.created_at
        )
        .all()
    )


def get_latest_answer(
    db: Session,
    interview_id: int,
):
    return (
        db.query(InterviewAnswer)
        .filter(
            InterviewAnswer.interview_id == interview_id
        )
        .order_by(
            InterviewAnswer.created_at.desc()
        )
        .first()
    )


def update_answer(
    db: Session,
    answer: InterviewAnswer,
):
    db.commit()
    db.refresh(answer)
    return answer


def delete_answer(
    db: Session,
    answer: InterviewAnswer,
):
    db.delete(answer)
    db.commit()