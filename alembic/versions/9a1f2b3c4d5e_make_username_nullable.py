"""Make username nullable

Revision ID: 9a1f2b3c4d5e
Revises: 86e9edbf0f0e
Create Date: 2026-04-29 11:30:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "9a1f2b3c4d5e"
down_revision: Union[str, Sequence[str], None] = "86e9edbf0f0e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "users",
        "username",
        existing_type=sa.VARCHAR(length=256),
        nullable=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "users",
        "username",
        existing_type=sa.VARCHAR(length=256),
        nullable=False,
    )
