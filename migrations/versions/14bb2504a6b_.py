"""empty message

Revision ID: 14bb2504a6b
Revises: 1e4da1aa6
Create Date: 2015-10-23 01:58:35.468111

"""

# revision identifiers, used by Alembic.
revision = '14bb2504a6b'
down_revision = '1e4da1aa6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###