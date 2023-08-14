"""create tables

Revision ID: 567d6921bad7
Revises: ea2a0aec719b
Create Date: 2023-08-14 17:00:26.570637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '567d6921bad7'
down_revision: Union[str, None] = 'ea2a0aec719b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
