"""update interview_report schema

Revision ID: 3fe27d6bc4e2
Revises: ae82ba48d382
Create Date: 2026-07-07 10:49:14.923438

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3fe27d6bc4e2"
down_revision: Union[str, Sequence[str], None] = "ae82ba48d382"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Remove old score column
    op.drop_column(
        "interview_answers",
        "score",
    )

    # Add new interview report fields
    op.add_column(
        "interview_reports",
        sa.Column(
            "technical_score",
            sa.Float(),
            nullable=True,
        ),
    )

    op.add_column(
        "interview_reports",
        sa.Column(
            "communication_score",
            sa.Float(),
            nullable=True,
        ),
    )

    op.add_column(
        "interview_reports",
        sa.Column(
            "confidence_score",
            sa.Float(),
            nullable=True,
        ),
    )

    op.add_column(
        "interview_reports",
        sa.Column(
            "hiring_recommendation",
            sa.String(length=50),
            nullable=True,
        ),
    )

    op.add_column(
        "interview_reports",
        sa.Column(
            "summary",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "interview_reports",
        sa.Column(
            "learning_roadmap",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "interview_reports",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )

    op.create_unique_constraint(
        "uq_interview_reports_interview_id",
        "interview_reports",
        ["interview_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "uq_interview_reports_interview_id",
        "interview_reports",
        type_="unique",
    )

    op.drop_column(
        "interview_reports",
        "created_at",
    )

    op.drop_column(
        "interview_reports",
        "learning_roadmap",
    )

    op.drop_column(
        "interview_reports",
        "summary",
    )

    op.drop_column(
        "interview_reports",
        "hiring_recommendation",
    )

    op.drop_column(
        "interview_reports",
        "confidence_score",
    )

    op.drop_column(
        "interview_reports",
        "communication_score",
    )

    op.drop_column(
        "interview_reports",
        "technical_score",
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "score",
            sa.Float(),
            nullable=True,
        ),
    )