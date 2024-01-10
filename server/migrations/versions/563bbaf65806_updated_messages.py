"""updated messages

Revision ID: 563bbaf65806
Revises: 
Create Date: 2024-01-10 03:01:40.290657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '563bbaf65806'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
