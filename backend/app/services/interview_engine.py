from sqlalchemy.orm import Session

from app.models.interview import InterviewSession

from app.services.answer_service import (
    submit_answer,
)

from app.ai.context.interview_context import (
    build_interview_context,
)

from app.ai.decision.interview_decision import (
    decide_next_step,
)

from app.ai.generators.followup_generator import (
    generate_followup_question,
)

from app.repositories.question_repository import (
    get_latest_question,
    save_question,
)

from app.models.question import InterviewQuestion


class InterviewEngine:

    @staticmethod
    def process_answer(
        db: Session,
        interview: InterviewSession,
        answer_data,
    ):
        """
        Adaptive interview workflow.

        1. Save candidate answer
        2. Evaluate using Gemini
        3. Build interview context
        4. Decide next interview step
        5. Generate follow-up question
        6. Save new question
        7. Return response
        """

        result = submit_answer(
            db,
            interview.id,
            answer_data,
        )

        if result is None:
            return None

        evaluation = result["evaluation"]

        context = build_interview_context(
            db,
            interview,
        )

        decision = decide_next_step(
            context,
        )

        if decision["action"] == "END_INTERVIEW":

            return {
                "completed": True,
                "evaluation": evaluation,
                "message": "Interview completed."
            }

        latest_question = get_latest_question(
            db,
            interview.id,
        )

        followup = generate_followup_question(
            company=interview.company,
            role=interview.role,
            previous_question=latest_question.question_text,
            candidate_answer=answer_data.answer_text,
            evaluation=evaluation,
        )

        new_question = InterviewQuestion(
            interview_id=interview.id,
            question_number=latest_question.question_number + 1,
            question_text=followup["question"],
            category=followup["category"],
            difficulty=decision["difficulty"],
        )

        save_question(
            db,
            new_question,
        )

        return {
            "completed": False,
            "evaluation": evaluation,
            "next_question": {
                "id": new_question.id,
                "question": new_question.question_text,
                "category": new_question.category,
                "difficulty": new_question.difficulty,
            },
            "progress": {
                "current": new_question.question_number,
                "total": interview.total_questions,
            },
        }