"""change table

Revision ID: 266686f26f2e
Revises: c91a14e401ba
Create Date: 2022-06-25 10:04:57.691087

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '266686f26f2e'
down_revision = 'c91a14e401ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('stock', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_type_assosiation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('product_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_type_id'], ['product.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('posts')
    op.add_column('user_detail', sa.Column('name', sa.String(), nullable=True))
    op.drop_constraint('user_detail_username_key', 'user_detail', type_='unique')
    op.create_foreign_key(None, 'user_detail', 'users', ['username'], ['username'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('user_detail', 'first_name')
    op.drop_column('user_detail', 'middle_name')
    op.drop_column('user_detail', 'last_name')
    op.add_column('users', sa.Column('password', sa.Text(), nullable=True))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_nomor_telepon_key', 'users', type_='unique')
    op.drop_column('users', 'email')
    op.drop_column('users', 'jenis_kelamin')
    op.drop_column('users', 'middle_name')
    op.drop_column('users', 'nomor_telepon')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('last_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('nomor_telepon', sa.REAL(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('middle_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('jenis_kelamin', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True))
    op.create_unique_constraint('users_nomor_telepon_key', 'users', ['nomor_telepon'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_column('users', 'password')
    op.drop_column('users', 'name')
    op.add_column('user_detail', sa.Column('last_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('user_detail', sa.Column('middle_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('user_detail', sa.Column('first_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_detail', type_='foreignkey')
    op.drop_constraint(None, 'user_detail', type_='foreignkey')
    op.drop_constraint(None, 'user_detail', type_='foreignkey')
    op.create_unique_constraint('user_detail_username_key', 'user_detail', ['username'])
    op.drop_column('user_detail', 'name')
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('crated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_modified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='posts_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='posts_pkey')
    )
    op.drop_table('product_type_assosiation')
    op.drop_table('product')
    op.drop_table('product_type')
    # ### end Alembic commands ###
