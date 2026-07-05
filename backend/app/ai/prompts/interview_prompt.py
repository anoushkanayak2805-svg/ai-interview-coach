def build_interview_prompt(
    company: str,
    role: str,
    difficulty: str,
    resume_text: str | None = None,
):

    prompt = f"""
You are an experienced software engineering interviewer.

Generate exactly 10 interview questions.

Company:
{company}

Role:
{role}

Difficulty:
{difficulty}
"""

    if resume_text:
        prompt += f"""

Candidate Resume:

{resume_text}

Generate questions specifically based on the candidate's resume.
"""

    prompt += """

Return ONLY valid JSON.

Example:

[
  {
    "question":"Explain REST APIs.",
    "category":"Technical"
  },
  {
    "question":"What is dependency injection?",
    "category":"Backend"
  }
]
"""

    return prompt