from app.ai.prompts.interview_prompt import build_interview_prompt


def generate_questions(
    company,
    role,
    difficulty,
):

    prompt = build_interview_prompt(
        company,
        role,
        difficulty,
    )

    print(prompt)

    return [
        {
            "question": "Explain REST API",
            "category": "Technical",
        }
    ]