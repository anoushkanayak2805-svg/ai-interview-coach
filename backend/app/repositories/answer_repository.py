from sqlalchemy.orm import Session

from app.models.answer import InterviewAnswer


def create_answer(
    db: Session,
    answer: InterviewAnswer
):

    db.add(answer)

    db.commit()

    db.refresh(answer)

    return answer


def get_answer_by_question(
    db: Session,
    question_id: int
):

    return (
        db.query(InterviewAnswer)
        .filter(
            InterviewAnswer.question_id == question_id
        )
        .first()
    )