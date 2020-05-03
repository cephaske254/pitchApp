"""empty message

Revision ID: be70aef291c9
Revises: 42ce7e48d485
Create Date: 2020-05-03 14:42:02.325261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be70aef291c9'
down_revision = '42ce7e48d485'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('user_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'tags', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tags', type_='foreignkey')
    op.drop_column('tags', 'user_id')
    # ### end Alembic commands ###
