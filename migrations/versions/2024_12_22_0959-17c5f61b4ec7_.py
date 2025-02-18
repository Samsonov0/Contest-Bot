"""empty message

Revision ID: 17c5f61b4ec7
Revises: 
Create Date: 2024-12-22 09:59:50.414360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17c5f61b4ec7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prizes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('created_by_channel', sa.String(), nullable=False),
    sa.Column('ask_to_prize', sa.String(), nullable=False),
    sa.Column('is_used', sa.Boolean(), nullable=True),
    sa.Column('prize', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prizes')
    # ### end Alembic commands ###
