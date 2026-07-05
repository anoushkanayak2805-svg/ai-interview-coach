from sqlalchemy.orm import Session

from app.models.interview import InterviewSession
from app.repositories.interview_repository import create_interview
from app.ai.generators.question_generator import generate_questions

from app.models.question import InterviewQuestion
from app.repositories.question_repository import save_questions

from app.repositories.interview_repository import (
    update_interview,
)
from app.repositories.question_repository import (
    get_questions_by_interview,
)
def create_new_interview(
    db: Session,
    user,
    interview_data
):
    interview = InterviewSession(
        title=interview_data.title,
        company=interview_data.company,
        role=interview_data.role,
        interview_type=interview_data.interview_type,
        difficulty=interview_data.difficulty,
        user_id=user.id,
        status="CREATED"
    )

    return create_interview(
        db,
        interview
    )
def move_to_next_question(
    db,
    interview
):

    interview.current_question += 1

    if interview.current_question > interview.total_questions:
        interview.completed = 1
        interview.status = "COMPLETED"

    return update_interview(
        db,
        interview
    )

def generate_interview_questions(
    db: Session,
    interview
):

    ai_questions = generate_questions(
        interview.company,
        interview.role,
        interview.difficulty
    )

    questions = []

    for index, item in enumerate(ai_questions):

        questions.append(

            InterviewQuestion(

                interview_id=interview.id,

                question_number=index + 1,

                question_text=item["question"],

                category=item["category"],

                difficulty=interview.difficulty

            )

        )

    return save_questions(
        db,
        questions
    )

def get_interview_questions(
    db,
    interview_id: int
):
    return get_questions_by_interview(
        db,
        interview_id
    )