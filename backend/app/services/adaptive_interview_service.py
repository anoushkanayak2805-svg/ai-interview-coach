from sqlalchemy.orm import Session

from app.ai.context.interview_context import (
    build_interview_context,
)

from app.ai.decision.interview_decision import (
    decide_next_step,
)


class AdaptiveInterviewService:

    @staticmethod
    def next_question(
        db: Session,
        interview,
    ):
        """
        Generate the next adaptive interview question.

        Workflow

        1. Build interview context

        2. Decide interview strategy

        3. Generate next question

        4. Save question

        5. Return question
        """

        context = build_interview_context(
            db,
            interview,
        )

        decision = decide_next_step(
            context,
        )

        return {
            "context": context,
            "decision": decision,
        }