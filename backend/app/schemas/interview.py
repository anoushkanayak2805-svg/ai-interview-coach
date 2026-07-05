from pydantic import BaseModel
from datetime import datetime


class InterviewCreate(BaseModel):
    title: str
    company: str
    role: str
    interview_type: str
    difficulty: str


class InterviewResponse(BaseModel):
    id: int
    title: str
    company: str
    role: str
    interview_type: str
    difficulty: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True