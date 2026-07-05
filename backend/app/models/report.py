from sqlalchemy import Column, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database import Base


class InterviewReport(Base):

    __tablename__ = "interview_reports"

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

    overall_score = Column(
        Float,
        default=0
    )

    strengths = Column(
        Text,
        default=""
    )

    weaknesses = Column(
        Text,
        default=""
    )

    recommendations = Column(
        Text,
        default=""
    )

    interview = relationship(
        "InterviewSession"
    )