from sqlalchemy import Column, Integer, Text, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.database import Base


class InterviewAnswer(Base):

    __tablename__ = "interview_answers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question_id = Column(
        Integer,
        ForeignKey("interview_questions.id"),
        nullable=False
    )

    answer_text = Column(
        Text,
        nullable=False
    )

    score = Column(
        Float,
        default=0
    )

    feedback = Column(
        Text,
        default=""
    )

    question = relationship(
        "InterviewQuestion"
    )