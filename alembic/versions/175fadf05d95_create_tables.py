"""create tables

Revision ID: 175fadf05d95
Revises: 567d6921bad7
Create Date: 2023-08-14 17:01:38.313836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '175fadf05d95'
down_revision: Union[str, None] = '567d6921bad7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
