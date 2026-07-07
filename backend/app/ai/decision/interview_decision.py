def decide_next_step(context: dict):
    """
    Decide how the interview should progress.

    The backend decides the interview strategy.
    Gemini only generates the actual question.
    """

    score = context["average_score"]

    current_question = context["current_question"]

    if current_question >= 10:

        return {
            "action": "END_INTERVIEW"
        }

    if score >= 8.5:

        return {
            "action": "INCREASE_DIFFICULTY",
            "difficulty": "Hard"
        }

    if score >= 6:

        return {
            "action": "KEEP_DIFFICULTY",
            "difficulty": context["difficulty"]
        }

    return {
        "action": "DECREASE_DIFFICULTY",
        "difficulty": "Easy"
    }