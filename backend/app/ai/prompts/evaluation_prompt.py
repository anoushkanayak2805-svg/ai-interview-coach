def build_evaluation_prompt(
    question: str,
    answer: str
):
    return f"""
You are a Senior Google Software Engineer.

Evaluate the following interview answer.

Question:
{question}

Candidate Answer:
{answer}

Return ONLY valid JSON.

{{
    "technical_score":8,
    "communication_score":7,
    "confidence_score":9,
    "strengths":"...",
    "weaknesses":"...",
    "improved_answer":"...",
    "feedback":"..."
}}
"""