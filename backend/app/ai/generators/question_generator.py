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

    # Temporary mock
    return [
        {
            "question": "Explain REST APIs.",
            "category": "Technical",
        },
        {
            "question": "What is dependency injection in FastAPI?",
            "category": "Backend",
        },
    ]