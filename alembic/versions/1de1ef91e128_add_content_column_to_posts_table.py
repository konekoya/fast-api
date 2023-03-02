"""add content column to posts table

Revision ID: 1de1ef91e128
Revises: 2f20ea4d5d5b
Create Date: 2023-03-01 15:56:10.739781

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '1de1ef91e128'
down_revision = '2f20ea4d5d5b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
