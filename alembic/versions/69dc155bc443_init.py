"""init

Revision ID: 69dc155bc443
Revises: 5c48ff2fd5fa
Create Date: 2023-08-14 18:47:02.116828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69dc155bc443'
down_revision: Union[str, None] = '5c48ff2fd5fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
