from sqlalchemy.orm import Session

from app.models.interview import InterviewSession
from app.models.question import InterviewQuestion

from app.repositories.interview_repository import (
    create_interview,
    update_interview,
)

from app.repositories.question_repository import (
    save_questions,
    get_questions_by_interview,
)

from app.repositories.resume_repository import (
    get_latest_resume,
)

from app.ai.generators.question_generator import (
    generate_questions,
)

from app.ai.analyzers.resume_intelligence import (
    analyze_resume,
)


def create_new_interview(
    db: Session,
    user,
    interview_data,
):
    interview = InterviewSession(
        title=interview_data.title,
        company=interview_data.company,
        role=interview_data.role,
        interview_type=interview_data.interview_type,
        difficulty=interview_data.difficulty,
        user_id=user.id,
        status="CREATED",
    )

    return create_interview(
        db,
        interview,
    )


def move_to_next_question(
    db: Session,
    interview,
):
    interview.current_question += 1

    if interview.current_question > interview.total_questions:
        interview.completed = 1
        interview.status = "COMPLETED"

    return update_interview(
        db,
        interview,
    )


def generate_interview_questions(
    db: Session,
    interview,
):
    """
    Generate interview questions.

    If the user has uploaded a resume,
    use Resume Intelligence to personalize
    the interview.

    Otherwise generate generic questions.
    """

    intelligence = None
    resume_text = None

    resume = get_latest_resume(
        db,
        interview.user_id,
    )

    if resume:

        resume_text = resume.extracted_text

        if resume_text:
            intelligence = analyze_resume(
                resume_text,
            )

    ai_questions = generate_questions(
        company=interview.company,
        role=interview.role,
        difficulty=interview.difficulty,
        resume_text=resume_text,
        intelligence=intelligence,
    )

    questions = []

    for index, item in enumerate(
        ai_questions,
        start=1,
    ):

        questions.append(
            InterviewQuestion(
                interview_id=interview.id,
                question_number=index,
                question_text=item["question"],
                category=item["category"],
                difficulty=interview.difficulty,
            )
        )

    return save_questions(
        db,
        questions,
    )


def get_interview_questions(
    db: Session,
    interview_id: int,
):
    return get_questions_by_interview(
        db,
        interview_id,
    )