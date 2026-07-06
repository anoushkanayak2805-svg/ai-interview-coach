def build_evaluation_prompt(
    question: str,
    answer: str,
):
    return f"""
You are a Senior Software Engineer interviewer at a top product company.

Evaluate the candidate's interview answer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer on the following metrics.

1. Technical correctness (0-10)
2. Communication clarity (0-10)
3. Confidence (0-10)

Also provide:

- strengths
- weaknesses
- an improved version of the answer
- overall feedback

Return ONLY valid JSON.

{{
    "technical_score": 0,
    "communication_score": 0,
    "confidence_score": 0,
    "strengths": [
        ""
    ],
    "weaknesses": [
        ""
    ],
    "improved_answer": "",
    "feedback": ""
}}
"""