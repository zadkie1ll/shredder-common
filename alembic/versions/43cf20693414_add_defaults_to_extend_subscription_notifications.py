"""Add defaults to extend subscription notifications

Revision ID: 43cf20693414
Revises: 9a1f2b3c4d5e
Create Date: 2026-05-02 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "43cf20693414"
down_revision: Union[str, Sequence[str], None] = "9a1f2b3c4d5e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "extend_subscription_notifications",
        "three_days_before",
        existing_type=sa.Boolean(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    op.alter_column(
        "extend_subscription_notifications",
        "one_day_before",
        existing_type=sa.Boolean(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "extend_subscription_notifications",
        "one_day_before",
        existing_type=sa.Boolean(),
        server_default=None,
        existing_nullable=False,
    )
    op.alter_column(
        "extend_subscription_notifications",
        "three_days_before",
        existing_type=sa.Boolean(),
        server_default=None,
        existing_nullable=False,
    )
