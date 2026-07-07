from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Text,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class InterviewReport(Base):

    __tablename__ = "interview_reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    interview_id = Column(
        Integer,
        ForeignKey("interview_sessions.id"),
        nullable=False,
        unique=True,
    )

    # -------------------------
    # Overall Scores
    # -------------------------

    overall_score = Column(
        Float,
        default=0.0,
    )

    technical_score = Column(
        Float,
        default=0.0,
    )

    communication_score = Column(
        Float,
        default=0.0,
    )

    confidence_score = Column(
        Float,
        default=0.0,
    )

    # -------------------------
    # AI Hiring Decision
    # -------------------------

    hiring_recommendation = Column(
        String(50),
        default="Pending",
    )

    # -------------------------
    # AI Feedback
    # -------------------------

    summary = Column(
        Text,
        default="",
    )

    strengths = Column(
        Text,
        default="",
    )

    weaknesses = Column(
        Text,
        default="",
    )

    recommendations = Column(
        Text,
        default="",
    )

    learning_roadmap = Column(
        Text,
        default="",
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
        back_populates="report",
    )