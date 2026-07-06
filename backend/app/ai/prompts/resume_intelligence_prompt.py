def build_resume_intelligence_prompt(
    resume_text: str,
):
    return f"""
You are a Senior Software Engineering Interviewer.

Analyze the candidate's resume.

Resume:

{resume_text}

Extract ONLY the information required for conducting an interview.

Return ONLY valid JSON.

{{
    "candidate_level": "",

    "skills": [],

    "projects": [],

    "technologies": [],

    "strengths": [],

    "weak_topics": [],

    "recommended_topics": [],

    "experience_summary": ""
}}

Rules:

1. Return valid JSON only.

2. Do not include markdown.

3. Skills should be technical.

4. Projects should contain project names only.

5. Weak topics should be inferred from the resume.

6. Recommended topics should be interview topics.
"""