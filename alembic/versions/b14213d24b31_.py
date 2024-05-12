"""empty message

Revision ID: b14213d24b31
Revises: a3a9a548532d
Create Date: 2024-05-09 22:42:34.007393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b14213d24b31'
down_revision: Union[str, None] = 'a3a9a548532d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=2048),
               type_=sa.BINARY(length=2048),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.BINARY(length=2048),
               type_=sa.VARCHAR(length=2048),
               existing_nullable=False)
    # ### end Alembic commands ###