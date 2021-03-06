"""empty message

Revision ID: d97d312834ab
Revises: dca3e4804bb3
Create Date: 2018-03-24 10:24:33.527047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd97d312834ab'
down_revision = 'dca3e4804bb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'post_user_id_fkey', 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'post_user_id_fkey', 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
