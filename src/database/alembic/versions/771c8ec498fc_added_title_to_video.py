"""Added title to video

Revision ID: 771c8ec498fc
Revises: d3b61d4dc259
Create Date: 2022-09-06 22:52:54.374903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '771c8ec498fc'
down_revision = 'd3b61d4dc259'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'title')
    # ### end Alembic commands ###
