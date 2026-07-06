from sqlalchemy.orm import Session

from app.models.answer import InterviewAnswer
from app.models.question import InterviewQuestion

from app.repositories.answer_repository import save_answer
from app.ai.evaluators.answer_evaluator import evaluate_answer

from app.schemas.answer import AnswerCreate


def submit_answer(
    db: Session,
    interview_id: int,
    answer_data: AnswerCreate,
):
    question = (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.id == answer_data.question_id
        )
        .first()
    )

    if question is None:
        return None

    evaluation = evaluate_answer(
        question.question_text,
        answer_data.answer_text,
    )

    answer = InterviewAnswer(
        interview_id=interview_id,
        question_id=answer_data.question_id,
        answer_text=answer_data.answer_text,

        technical_score=evaluation["technical_score"],
        communication_score=evaluation["communication_score"],
        confidence_score=evaluation["confidence_score"],

        strengths=evaluation["strengths"],
        weaknesses=evaluation["weaknesses"],

        improved_answer=evaluation["improved_answer"],
        feedback=evaluation["feedback"],
    )

    return save_answer(
        db,
        answer,
    )