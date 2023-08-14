"""initddscc

Revision ID: 80e466156c24
Revises: 426ffe289346
Create Date: 2023-08-14 19:07:43.769569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80e466156c24'
down_revision: Union[str, None] = '426ffe289346'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
