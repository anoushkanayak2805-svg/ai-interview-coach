def build_interview_prompt(
    role: str,
    strategy: dict,
    resume_text: str | None = None,
):
    """
    Build the interview prompt using
    Company Strategy + Resume Intelligence.
    """

    resume_section = ""

    if resume_text:
        resume_section = f"""
Candidate Resume

{resume_text}
"""

    return f"""
You are a Senior {strategy["company"]} interviewer.

Conduct an interview exactly like {strategy["company"]}.

======================================================
COMPANY INTERVIEW PROFILE
======================================================

Interview Style:
{strategy["style"]}

Technical Weight:
{strategy["technical_weight"]}%

Behavioral Weight:
{strategy["behavioral_weight"]}%

Coding Difficulty:
{strategy["difficulty"]}

Include System Design:
{strategy["system_design"]}

Preferred Topics:
{", ".join(strategy["preferred_topics"])}

Main Focus Areas:
{", ".join(strategy["focus"])}

======================================================
CANDIDATE PROFILE
======================================================

Candidate Level:
{strategy["candidate_level"]}

Skills:
{", ".join(strategy["skills"])}

Projects:
{", ".join(strategy["projects"])}

Technologies:
{", ".join(strategy["technologies"])}

Weak Topics:
{", ".join(strategy["weak_topics"])}

Recommended Topics:
{", ".join(strategy["recommended_topics"])}

======================================================
TARGET ROLE
======================================================

Role:
{role}

{resume_section}

======================================================
RULES
======================================================

1. Generate EXACTLY 10 interview questions.

2. Questions should match the interview style of the selected company.

3. Use the candidate's resume while asking questions.

4. Ask questions about the candidate's projects.

5. Ask questions about technologies used by the candidate.

6. Ask follow-up questions on weak topics.

7. Prioritize the company's preferred topics.

8. Mix technical and behavioral questions according to the specified weights.

9. If System Design is enabled, include ONE system design question.

10. Questions should become progressively more challenging.

11. Return ONLY valid JSON.

======================================================
JSON FORMAT
======================================================

[
    {{
        "question": "Explain dependency injection in FastAPI.",
        "category": "Backend"
    }},
    {{
        "question": "Design a URL shortening service.",
        "category": "System Design"
    }}
]
"""