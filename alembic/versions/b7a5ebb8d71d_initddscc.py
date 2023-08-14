"""initddscc

Revision ID: b7a5ebb8d71d
Revises: 80e466156c24
Create Date: 2023-08-14 19:08:09.733682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7a5ebb8d71d'
down_revision: Union[str, None] = '80e466156c24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
