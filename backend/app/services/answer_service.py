from sqlalchemy.orm import Session

from app.models.answer import InterviewAnswer

from app.repositories.answer_repository import create_answer


def save_answer(
    db: Session,
    question_id: int,
    answer_text: str
):

    answer = InterviewAnswer(

        question_id=question_id,

        answer_text=answer_text,

        score=0,

        feedback="Pending AI Evaluation"

    )

    return create_answer(
        db,
        answer
    )