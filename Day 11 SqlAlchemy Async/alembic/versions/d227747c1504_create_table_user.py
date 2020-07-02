"""create table user

Revision ID: d227747c1504
Revises: 
Create Date: 2020-06-22 09:44:03.580116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd227747c1504'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('user')
