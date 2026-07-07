from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)

from sqlalchemy.orm import relationship

from app.database import Base


class InterviewQuestion(Base):

    __tablename__ = "interview_questions"

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

    question_number = Column(
        Integer,
        nullable=False,
    )

    question_text = Column(
        Text,
        nullable=False,
    )

    category = Column(
        String,
        nullable=False,
    )

    difficulty = Column(
        String,
        nullable=False,
    )

    # -------------------------
    # Relationships
    # -------------------------

    interview = relationship(
        "InterviewSession",
        back_populates="questions",
    )

    answers = relationship(
        "InterviewAnswer",
        back_populates="question",
        cascade="all, delete-orphan",
    )

    # -------------------------
    # Helper Methods
    # -------------------------

    def __repr__(self):
        return (
            f"<InterviewQuestion("
            f"id={self.id}, "
            f"question_number={self.question_number}, "
            f"category='{self.category}')>"
        )