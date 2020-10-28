"""Initial migration

Revision ID: cebb316157f1
Revises: 
Create Date: 2020-10-27 23:36:44.211118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cebb316157f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(length=40), nullable=0))
    op.add_column('users', sa.Column('profile_photo', sa.String(length=20), nullable=0))
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=0)
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_column('users', 'profile_photo')
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    op.drop_table('post')
    # ### end Alembic commands ###