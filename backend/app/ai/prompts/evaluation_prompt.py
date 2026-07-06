def build_evaluation_prompt(
    question: str,
    answer: str,
):
    return f"""
You are a Senior Software Engineer interviewer.

Evaluate the candidate's answer.

Interview Question:
{question}

Candidate Answer:
{answer}

Return ONLY valid JSON.

{{
    "score": 0,
    "strengths": [],
    "weaknesses": [],
    "improvements": []
}}
"""