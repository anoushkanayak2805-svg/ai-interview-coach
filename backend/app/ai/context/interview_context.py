from sqlalchemy.orm import Session

from app.models.interview import InterviewSession
from app.models.answer import InterviewAnswer
from app.models.question import InterviewQuestion
from app.models.resume import Resume


def build_interview_context(
    db: Session,
    interview: InterviewSession,
):
    """
    Build the complete interview context that will
    be sent to Gemini for adaptive interviewing.
    """

    resume = (
        db.query(Resume)
        .filter(Resume.user_id == interview.user_id)
        .order_by(Resume.id.desc())
        .first()
    )

    questions = (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.interview_id == interview.id
        )
        .order_by(
            InterviewQuestion.question_number
        )
        .all()
    )

    answers = (
        db.query(InterviewAnswer)
        .filter(
            InterviewAnswer.interview_id == interview.id
        )
        .order_by(
            InterviewAnswer.id
        )
        .all()
    )

    avg_score = 0

    if answers:

        avg_score = sum(
            a.technical_score
            for a in answers
        ) / len(answers)

    return {

        "company": interview.company,

        "role": interview.role,

        "difficulty": interview.difficulty,

        "current_question": interview.current_question,

        "resume_text": (
            resume.extracted_text
            if resume
            else ""
        ),

        "previous_questions": [
            q.question_text
            for q in questions
        ],

        "previous_answers": [
            a.answer_text
            for a in answers
        ],

        "average_score": round(
            avg_score,
            2,
        ),
    }