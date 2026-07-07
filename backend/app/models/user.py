from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    full_name = Column(
        String,
        nullable=False,
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    role = Column(
        String,
        default="user",
        nullable=False,
    )

    # -------------------------
    # Relationships
    # -------------------------

    interviews = relationship(
        "InterviewSession",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    resumes = relationship(
        "Resume",
        back_populates="user",
        cascade="all, delete-orphan",
    )