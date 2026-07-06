import json

from app.ai.client import client
from app.ai.prompts.interview_prompt import build_interview_prompt


def generate_questions(
    company: str,
    role: str,
    difficulty: str,
    resume_text: str | None = None,
):
    prompt = build_interview_prompt(
        company,
        role,
        difficulty,
        resume_text,
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

   # Remove markdown code fences if present
    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    questions = json.loads(text)

    if len(questions) != 10:
        raise ValueError("Gemini did not return exactly 10 questions.")

    return questions