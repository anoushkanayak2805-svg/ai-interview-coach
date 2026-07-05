def build_interview_prompt(
    company,
    role,
    difficulty,
):

    return f"""
You are an expert technical interviewer.

Generate exactly 10 interview questions.

Company:
{company}

Role:
{role}

Difficulty:
{difficulty}

Return ONLY valid JSON.

Example:

[
 {{
   "question":"Explain REST API",
   "category":"Technical"
 }}
]
"""