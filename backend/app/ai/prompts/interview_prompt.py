def build_interview_prompt(
    company: str,
    role: str,
    difficulty: str,
    resume_text: str | None = None,
    intelligence: dict | None = None,
):
    prompt = f"""
You are a Senior {company} Software Engineering Interviewer.

Generate exactly 10 interview questions.

Company:
{company}

Role:
{role}

Difficulty:
{difficulty}
"""

    # Use Resume Intelligence if available
    if intelligence:

        prompt += f"""

Candidate Level:
{intelligence.get("candidate_level", "")}

Skills:
{", ".join(intelligence.get("skills", []))}

Projects:
{", ".join(intelligence.get("projects", []))}

Technologies:
{", ".join(intelligence.get("technologies", []))}

Recommended Interview Topics:
{", ".join(intelligence.get("recommended_topics", []))}

Weak Topics:
{", ".join(intelligence.get("weak_topics", []))}

Experience Summary:
{intelligence.get("experience_summary", "")}

Instructions:

1. Tailor the interview to the candidate.
2. Ask questions about their projects.
3. Ask questions about the technologies they used.
4. Focus more on weak topics.
5. Include at least one behavioural question.
6. If difficulty is Hard, include one System Design question.
"""

    # Fallback for resume text (older flow)
    elif resume_text:

        prompt += f"""

Candidate Resume:

{resume_text}

Generate interview questions using the resume.
"""

    else:

        prompt += """

Generate a balanced interview based only on the company, role and difficulty.
"""

    prompt += """

Return ONLY valid JSON.

Example:

[
    {
        "question": "Explain dependency injection in FastAPI.",
        "category": "Backend"
    },
    {
        "question": "How does JWT authentication work?",
        "category": "Security"
    }
]
"""

    return prompt