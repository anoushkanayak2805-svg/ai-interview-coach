"""add resume analysis fields

Revision ID: ae82ba48d382
Revises: 27a292ebb15f
Create Date: 2026-07-06 20:47:58.492704
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ae82ba48d382"
down_revision: Union[str, Sequence[str], None] = "27a292ebb15f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "resumes",
        sa.Column(
            "analysis",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "resumes",
        sa.Column(
            "skills",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "resumes",
        sa.Column(
            "projects",
            sa.Text(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "resumes",
        "projects",
    )

    op.drop_column(
        "resumes",
        "skills",
    )

    op.drop_column(
        "resumes",
        "analysis",
    )