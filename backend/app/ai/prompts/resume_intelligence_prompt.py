def build_resume_intelligence_prompt(
    resume_text: str,
):
    return f"""
You are a Senior Software Engineer, Hiring Manager, and Technical Interviewer.

Your task is to analyze the candidate's resume and generate Interview Intelligence.

======================================================
CANDIDATE RESUME
======================================================

{resume_text}

======================================================
OBJECTIVE
======================================================

Extract information that will help an AI interviewer conduct
a personalized technical interview.

Infer the candidate's strengths and weak areas based on
projects, skills, technologies, education and experience.

======================================================
RETURN ONLY VALID JSON
======================================================

{{
    "candidate_level": "",

    "career_level": "",

    "experience_level": "",

    "coding_level": "",

    "backend_level": "",

    "database_level": "",

    "system_design_level": "",

    "communication_level": "",

    "confidence_level": "",

    "skills": [],

    "projects": [],

    "technologies": [],

    "strengths": [],

    "weak_topics": [],

    "recommended_topics": [],

    "experience_summary": ""
}}

======================================================
GUIDELINES
======================================================

1. Return ONLY valid JSON.

2. Do NOT include markdown.

3. Do NOT include explanations.

4. Skills must contain ONLY technical skills.

5. Projects must contain ONLY project names.

6. Technologies should include frameworks, databases, cloud platforms and developer tools.

7. Infer weak technical areas from the resume.

8. Recommend interview topics based on the resume.

9. Estimate the candidate's career level.

Examples:

Intern

SDE-1

SDE-2

New Graduate

10. Estimate coding ability.

Examples:

Beginner

Intermediate

Advanced

11. Estimate backend knowledge.

12. Estimate database knowledge.

13. Estimate system design knowledge.

14. Estimate communication ability from the resume quality.

15. Estimate confidence level based on project quality and technical depth.

16. Experience summary should be a concise 2-3 sentence overview of the candidate.

17. If information is unavailable, make a reasonable inference instead of leaving fields empty.

18. Return ONLY valid JSON.
"""