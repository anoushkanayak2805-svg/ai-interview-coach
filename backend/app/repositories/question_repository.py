from sqlalchemy.orm import Session

from app.models.question import InterviewQuestion


def save_questions(
    db: Session,
    questions: list[InterviewQuestion]
):
    db.add_all(questions)
    db.commit()

    for question in questions:
        db.refresh(question)

    return questions


def get_questions_by_interview(
    db: Session,
    interview_id: int
):
    return (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.interview_id == interview_id
        )
        .order_by(
            InterviewQuestion.question_number
        )
        .all()
    )