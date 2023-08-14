"""initdds

Revision ID: 1c802cede958
Revises: 69dc155bc443
Create Date: 2023-08-14 18:49:13.551741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c802cede958'
down_revision: Union[str, None] = '69dc155bc443'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
