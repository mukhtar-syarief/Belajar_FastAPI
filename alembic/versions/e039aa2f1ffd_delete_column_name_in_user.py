"""delete column name in user

Revision ID: e039aa2f1ffd
Revises: e1ee88ac63a2
Create Date: 2022-06-21 12:25:25.936711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e039aa2f1ffd'
down_revision = 'e1ee88ac63a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
