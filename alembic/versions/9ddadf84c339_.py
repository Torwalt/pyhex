"""Create part table

Revision ID: 9ddadf84c339
Revises:
Create Date: 2021-12-08 10:50:08.430409

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "9ddadf84c339"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "part",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("modified_timestamp", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("part")
