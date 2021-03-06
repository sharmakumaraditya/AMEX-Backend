"""empty message

Revision ID: 006a79854e65
Revises: 42693b5af75b
Create Date: 2020-08-16 22:22:29.297695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006a79854e65'
down_revision = '42693b5af75b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('user_email', sa.String(), nullable=True),
    sa.Column('upi_id', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payment_data_description'), 'payment_data', ['description'], unique=False)
    op.create_index(op.f('ix_payment_data_email'), 'payment_data', ['email'], unique=False)
    op.create_index(op.f('ix_payment_data_user_id'), 'payment_data', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_payment_data_user_id'), table_name='payment_data')
    op.drop_index(op.f('ix_payment_data_email'), table_name='payment_data')
    op.drop_index(op.f('ix_payment_data_description'), table_name='payment_data')
    op.drop_table('payment_data')
    # ### end Alembic commands ###
