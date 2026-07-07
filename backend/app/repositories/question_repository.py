from sqlalchemy.orm import Session

from app.models.question import InterviewQuestion


def save_question(
    db: Session,
    question: InterviewQuestion,
):
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def save_questions(
    db: Session,
    questions: list[InterviewQuestion],
):
    db.add_all(questions)
    db.commit()

    for question in questions:
        db.refresh(question)

    return questions


def get_question_by_id(
    db: Session,
    question_id: int,
):
    return (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.id == question_id
        )
        .first()
    )


def get_questions_by_interview(
    db: Session,
    interview_id: int,
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


def get_current_question(
    db: Session,
    interview_id: int,
    question_number: int,
):
    return (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.interview_id == interview_id,
            InterviewQuestion.question_number == question_number,
        )
        .first()
    )


def get_latest_question(
    db: Session,
    interview_id: int,
):
    return (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.interview_id == interview_id
        )
        .order_by(
            InterviewQuestion.question_number.desc()
        )
        .first()
    )