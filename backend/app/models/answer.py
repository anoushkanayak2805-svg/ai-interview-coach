from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class InterviewAnswer(Base):

    __tablename__ = "interview_answers"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    interview_id = Column(
        Integer,
        ForeignKey("interview_sessions.id"),
        nullable=False,
    )

    question_id = Column(
        Integer,
        ForeignKey("interview_questions.id"),
        nullable=False,
    )

    answer_text = Column(
        Text,
        nullable=False,
    )

    # -------------------------
    # AI Evaluation Scores
    # -------------------------

    technical_score = Column(
        Float,
        default=0,
    )

    communication_score = Column(
        Float,
        default=0,
    )

    confidence_score = Column(
        Float,
        default=0,
    )

    # -------------------------
    # AI Feedback
    # -------------------------

    strengths = Column(
        Text,
    )

    weaknesses = Column(
        Text,
    )

    improved_answer = Column(
        Text,
    )

    feedback = Column(
        Text,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    # -------------------------
    # Relationships
    # -------------------------

    interview = relationship(
        "InterviewSession",
        back_populates="answers",
    )

    question = relationship(
        "InterviewQuestion",
        back_populates="answers",
    )