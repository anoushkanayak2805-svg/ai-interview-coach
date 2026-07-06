from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Float

from sqlalchemy.sql import func
from app.database import Base


class InterviewAnswer(Base):

    __tablename__ = "interview_answers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    interview_id = Column(
        Integer,
        ForeignKey("interview_sessions.id"),
        nullable=False
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

    technical_score = Column(
        Float,
        default=0
    )

    communication_score = Column(
        Float,
        default=0
    )

    confidence_score = Column(
        Float,
        default=0
    )

    strengths = Column(
        Text
    )

    weaknesses = Column(
        Text
    )

    improved_answer = Column(
        Text
    )

    feedback = Column(
        Text
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )