from pydantic import BaseModel
from datetime import datetime


class AnswerCreate(BaseModel):
    question_id: int
    answer_text: str


class AnswerResponse(BaseModel):
    id: int
    interview_id: int
    question_id: int

    answer_text: str

    technical_score: float
    communication_score: float
    confidence_score: float

    strengths: str | None = None
    weaknesses: str | None = None
    improved_answer: str | None = None
    feedback: str | None = None

    created_at: datetime

    model_config = {
        "from_attributes": True
    }