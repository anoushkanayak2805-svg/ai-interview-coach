from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class InterviewSession(Base):

    __tablename__ = "interview_sessions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    title = Column(
        String,
        nullable=False,
    )

    company = Column(
        String,
        nullable=False,
    )

    role = Column(
        String,
        nullable=False,
    )

    interview_type = Column(
        String,
        nullable=False,
    )

    difficulty = Column(
        String,
        nullable=False,
    )

    status = Column(
        String,
        default="CREATED",
    )

    current_question = Column(
        Integer,
        default=1,
    )

    completed = Column(
        Integer,
        default=0,
    )

    total_questions = Column(
        Integer,
        default=10,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    # -------------------------
    # Relationships
    # -------------------------

    user = relationship(
        "User",
        back_populates="interviews",
        lazy="selectin",
    )

    questions = relationship(
        "InterviewQuestion",
        back_populates="interview",
        cascade="all, delete-orphan",
        lazy="selectin",
        order_by="InterviewQuestion.question_number",
    )

    answers = relationship(
        "InterviewAnswer",
        back_populates="interview",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    report = relationship(
        "InterviewReport",
        back_populates="interview",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    # -------------------------
    # Helper Methods
    # -------------------------

    def __repr__(self):
        return (
            f"<InterviewSession("
            f"id={self.id}, "
            f"company='{self.company}', "
            f"role='{self.role}', "
            f"status='{self.status}')>"
        )