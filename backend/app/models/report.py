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

    overall_score = Column(
        Float,
        nullable=False,
    )

    technical_score = Column(
        Float,
        nullable=False,
    )

    communication_score = Column(
        Float,
        nullable=False,
    )

    confidence_score = Column(
        Float,
        nullable=False,
    )

    hiring_recommendation = Column(
        Text,
        nullable=True,
    )

    summary = Column(
        Text,
        nullable=True,
    )

    strengths = Column(
        Text,
        nullable=True,
    )

    weaknesses = Column(
        Text,
        nullable=True,
    )

    recommendations = Column(
        Text,
        nullable=True,
    )

    learning_roadmap = Column(
        Text,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    # Must match back_populates="interview"
    # in the InterviewSession model
    interview = relationship(
        "InterviewSession",
        back_populates="report",
    )