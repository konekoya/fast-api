"""create posts table

Revision ID: 2f20ea4d5d5b
Revises: 
Create Date: 2023-03-01 14:45:06.677086

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '2f20ea4d5d5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False,
                    primary_key=True), sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
