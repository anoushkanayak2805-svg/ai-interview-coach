"""create interview answers

Revision ID: b3a5ae34b2a0
Revises: 11a524f32c36
Create Date: 2026-07-06 12:06:59.298508

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b3a5ae34b2a0"
down_revision: Union[str, Sequence[str], None] = "11a524f32c36"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "interview_answers",
        sa.Column(
            "interview_id",
            sa.Integer(),
            nullable=False
        )
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "technical_score",
            sa.Float(),
            nullable=True
        )
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "communication_score",
            sa.Float(),
            nullable=True
        )
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "confidence_score",
            sa.Float(),
            nullable=True
        )
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "strengths",
            sa.Text(),
            nullable=True
        )
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "weaknesses",
            sa.Text(),
            nullable=True
        )
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "improved_answer",
            sa.Text(),
            nullable=True
        )
    )

    op.add_column(
        "interview_answers",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True
        )
    )

    op.create_foreign_key(
        "fk_interview_answers_interview_id",
        "interview_answers",
        "interview_sessions",
        ["interview_id"],
        ["id"]
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_interview_answers_interview_id",
        "interview_answers",
        type_="foreignkey"
    )

    op.drop_column(
        "interview_answers",
        "created_at"
    )

    op.drop_column(
        "interview_answers",
        "improved_answer"
    )

    op.drop_column(
        "interview_answers",
        "weaknesses"
    )

    op.drop_column(
        "interview_answers",
        "strengths"
    )

    op.drop_column(
        "interview_answers",
        "confidence_score"
    )

    op.drop_column(
        "interview_answers",
        "communication_score"
    )

    op.drop_column(
        "interview_answers",
        "technical_score"
    )

    op.drop_column(
        "interview_answers",
        "interview_id"
    )