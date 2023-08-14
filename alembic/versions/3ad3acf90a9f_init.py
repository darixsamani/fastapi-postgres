"""init

Revision ID: 3ad3acf90a9f
Revises: 175fadf05d95
Create Date: 2023-08-14 18:25:23.195856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ad3acf90a9f'
down_revision: Union[str, None] = '175fadf05d95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
