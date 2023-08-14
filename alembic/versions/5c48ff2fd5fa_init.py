"""init

Revision ID: 5c48ff2fd5fa
Revises: 3ad3acf90a9f
Create Date: 2023-08-14 18:46:15.188492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c48ff2fd5fa'
down_revision: Union[str, None] = '3ad3acf90a9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
