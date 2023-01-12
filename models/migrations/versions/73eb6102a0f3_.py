"""empty message

Revision ID: 73eb6102a0f3
Revises: 
Create Date: 2023-01-12 22:05:07.283388

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '73eb6102a0f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    PAYMENT_STATE = [
        ("Возврат", "Возврат"),
        ("Оплачено", "Оплачено"),
        ("В ожидании", "В ожидании"),
        ("Не aктуально", "Не aктуально"),
    ]

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payments',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('paid_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(PAYMENT_STATE), nullable=True),
    sa.Column('order_id', sa.VARCHAR(length=50), nullable=True),
    sa.Column('order_link', sa.String(), nullable=True),
    sa.Column('creator_username', sa.VARCHAR(length=100), nullable=True),
    sa.Column('creator_telegram_id', sa.BigInteger(), nullable=True),
    sa.Column('lesson_type', sa.VARCHAR(length=20), nullable=False),
    sa.Column('parents_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('description', sa.VARCHAR(length=512), nullable=True),
    sa.Column('amount', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pushes',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('file', sa.VARCHAR(), nullable=False),
    sa.Column('offset', sa.BigInteger(), nullable=True),
    sa.Column('sheet', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pushes')
    op.drop_table('payments')
    # ### end Alembic commands ###
