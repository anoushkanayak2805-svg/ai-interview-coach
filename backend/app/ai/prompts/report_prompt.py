def build_report_prompt(
    answers: list[dict],
):
    interview_data = ""

    for index, answer in enumerate(answers, start=1):

        interview_data += f"""
Question {index}

Answer:
{answer["answer"]}

Technical Score:
{answer["technical_score"]}

Communication Score:
{answer["communication_score"]}

Confidence Score:
{answer["confidence_score"]}

Strengths:
{answer["strengths"]}

Weaknesses:
{answer["weaknesses"]}

----------------------------------------
"""

    return f"""
You are an experienced Senior Software Engineering Interviewer.

Analyze the complete interview below.

{interview_data}

Generate a final interview report.

Return ONLY valid JSON.

{{
    "summary":"",

    "overall_score":8.5,

    "technical_score":8.4,

    "communication_score":8.6,

    "confidence_score":8.2,

    "strengths":"",

    "weaknesses":"",

    "recommendations":"",

    "learning_roadmap":"",

    "hiring_recommendation":"Hire"
}}
"""