from app.ai.analyzers.resume_intelligence import (
    analyze_resume,
)

from app.ai.generators.question_generator import (
    generate_questions,
)

from app.ai.evaluators.answer_evaluator import (
    evaluate_answer,
)

from app.ai.strategies.company_strategy import (
    get_company_strategy,
)


class AIService:

    @staticmethod
    def analyze_resume(
        resume_text: str,
    ):
        return analyze_resume(
            resume_text,
        )

    @staticmethod
    def generate_questions(
        company: str,
        role: str,
        difficulty: str,
        resume_text: str | None = None,
        intelligence: dict | None = None,
    ):
        return generate_questions(
            company=company,
            role=role,
            difficulty=difficulty,
            resume_text=resume_text,
            intelligence=intelligence,
        )

    @staticmethod
    def evaluate_answer(
        question: str,
        answer: str,
    ):
        return evaluate_answer(
            question,
            answer,
        )

    @staticmethod
    def company_strategy(
        company: str,
    ):
        return get_company_strategy(
            company,
        )