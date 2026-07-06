def build_resume_analysis_prompt(
    resume_text: str,
):
    return f"""
You are an expert software engineering interviewer.

Analyze the following resume.

Resume:

{resume_text}

Return ONLY valid JSON.

{{
    "skills": [],
    "projects": [],
    "experience_summary": "",
    "strengths": [],
    "improvement_areas": []
}}
"""