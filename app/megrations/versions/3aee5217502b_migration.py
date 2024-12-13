"""migration

Revision ID: 3aee5217502b
Revises: 778dcf533386
Create Date: 2024-12-14 00:56:57.356427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3aee5217502b'
down_revision: Union[str, None] = '778dcf533386'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
#