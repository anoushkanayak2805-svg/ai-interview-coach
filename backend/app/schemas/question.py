from pydantic import BaseModel


class QuestionResponse(BaseModel):
    id: int
    question_number: int
    question_text: str
    category: str
    difficulty: str

    class Config:
        from_attributes = True