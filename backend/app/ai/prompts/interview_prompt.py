def build_interview_prompt(
    company: str,
    role: str,
    difficulty: str,
    resume_text: str | None = None,
):

    prompt = f"""
You are an experienced Software Engineering interviewer.

Generate EXACTLY 10 interview questions.

Company: {company}
Role: {role}
Difficulty: {difficulty}
"""

    if resume_text:
        prompt += f"""

Candidate Resume:

{resume_text}

Generate questions that are personalized based on the candidate's resume.
"""

    prompt += """

Rules:
1. Return EXACTLY 10 questions.
2. Include a mix of technical, coding, system design (if applicable), behavioral, and role-specific questions.
3. Do NOT include explanations.
4. Do NOT wrap the response inside markdown.
5. Return ONLY valid JSON.

Return this exact format:

[
    {
        "question": "Explain REST APIs.",
        "category": "Technical"
    }
]
"""

    return prompt