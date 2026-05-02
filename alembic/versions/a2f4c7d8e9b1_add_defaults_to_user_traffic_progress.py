"""Add defaults to user traffic progress flags

Revision ID: a2f4c7d8e9b1
Revises: 43cf20693414
Create Date: 2026-05-03 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "a2f4c7d8e9b1"
down_revision: Union[str, Sequence[str], None] = "43cf20693414"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "user_traffic_progress",
        "passed_0",
        existing_type=sa.Boolean(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    op.alter_column(
        "user_traffic_progress",
        "passed_5mb",
        existing_type=sa.Boolean(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )
    op.alter_column(
        "user_traffic_progress",
        "passed_100mb",
        existing_type=sa.Boolean(),
        server_default=sa.text("false"),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "user_traffic_progress",
        "passed_100mb",
        existing_type=sa.Boolean(),
        server_default=None,
        existing_nullable=False,
    )
    op.alter_column(
        "user_traffic_progress",
        "passed_5mb",
        existing_type=sa.Boolean(),
        server_default=None,
        existing_nullable=False,
    )
    op.alter_column(
        "user_traffic_progress",
        "passed_0",
        existing_type=sa.Boolean(),
        server_default=None,
        existing_nullable=False,
    )
