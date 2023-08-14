"""initdds

Revision ID: 426ffe289346
Revises: 1c802cede958
Create Date: 2023-08-14 18:54:51.238041

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '426ffe289346'
down_revision: Union[str, None] = '1c802cede958'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
