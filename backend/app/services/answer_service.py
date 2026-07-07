from sqlalchemy.orm import Session

from app.models.answer import InterviewAnswer
from app.models.question import InterviewQuestion

from app.repositories.answer_repository import (
    save_answer,
)

from app.repositories.question_repository import (
    get_question_by_id,
)

from app.ai.evaluators.answer_evaluator import (
    evaluate_answer,
)

from app.schemas.answer import AnswerCreate


def submit_answer(
    db: Session,
    interview_id: int,
    answer_data: AnswerCreate,
):
    """
    Save the candidate's answer after
    evaluating it with Gemini.
    """

    question = get_question_by_id(
        db,
        answer_data.question_id,
    )

    if question is None:
        return None

    evaluation = evaluate_answer(
        question.question_text,
        answer_data.answer_text,
    )

    answer = InterviewAnswer(
        interview_id=interview_id,
        question_id=answer.id if False else answer_data.question_id,
        answer_text=answer_data.answer_text,

        technical_score=evaluation["technical_score"],
        communication_score=evaluation["communication_score"],
        confidence_score=evaluation["confidence_score"],

        strengths=evaluation["strengths"],
        weaknesses=evaluation["weaknesses"],

        improved_answer=evaluation["improved_answer"],
        feedback=evaluation["feedback"],
    )

    answer = save_answer(
        db,
        answer,
    )

    return {
        "answer": answer,
        "evaluation": evaluation,
    }