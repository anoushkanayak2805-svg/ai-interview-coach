from app.repositories.answer_repository import (
    get_answers_by_interview,
)


def build_interview_memory(
    db,
    interview_id: int,
):
    """
    Build interview memory from previous answers.
    """

    answers = get_answers_by_interview(
        db,
        interview_id,
    )

    memory = {

        "questions_answered": len(answers),

        "technical_average": 0,

        "communication_average": 0,

        "confidence_average": 0,

        "weak_categories": [],

        "strong_categories": [],

        "recent_feedback": [],
    }

    if not answers:
        return memory

    technical = 0
    communication = 0
    confidence = 0

    category_scores = {}

    for answer in answers:

        technical += answer.technical_score
        communication += answer.communication_score
        confidence += answer.confidence_score

        category = (
            answer.question.category
            if hasattr(answer, "question")
            else "General"
        )

        category_scores.setdefault(category, []).append(
            answer.technical_score
        )

        if answer.feedback:
            memory["recent_feedback"].append(
                answer.feedback
            )

    count = len(answers)

    memory["technical_average"] = technical / count

    memory["communication_average"] = communication / count

    memory["confidence_average"] = confidence / count

    for category, scores in category_scores.items():

        average = sum(scores) / len(scores)

        if average >= 8:

            memory["strong_categories"].append(
                category
            )

        elif average <= 5:

            memory["weak_categories"].append(
                category
            )

    return memory