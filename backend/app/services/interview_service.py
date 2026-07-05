from sqlalchemy.orm import Session

from app.models.interview import InterviewSession
from app.repositories.interview_repository import create_interview
from app.ai.generators.question_generator import generate_questions

from app.models.question import InterviewQuestion
from app.repositories.question_repository import save_questions

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