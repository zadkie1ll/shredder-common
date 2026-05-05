"""Add telegram_username to users

Revision ID: f7a4c2b1d9e0
Revises: a2f4c7d8e9b1
Create Date: 2026-05-05 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "f7a4c2b1d9e0"
down_revision: Union[str, Sequence[str], None] = "a2f4c7d8e9b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users",
        sa.Column("telegram_username", sa.String(length=256), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", "telegram_username")
