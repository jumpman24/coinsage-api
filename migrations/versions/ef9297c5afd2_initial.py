"""initial

Revision ID: ef9297c5afd2
Revises: 
Create Date: 2022-01-19 19:35:21.390384

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'ef9297c5afd2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exchange',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.Column('exchange_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('api_key', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('secret_key', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.Column('transaction_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('transaction_date', sa.DateTime(), nullable=False),
    sa.Column('buy_asset', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('buy_amount', sa.Numeric(), nullable=True),
    sa.Column('sell_asset', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('sell_amount', sa.Numeric(), nullable=True),
    sa.Column('fee_asset', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('fee_amount', sa.Numeric(), nullable=True),
    sa.Column('external_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('note', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('exchange')
    op.drop_table('portfolio')
    op.drop_table('user')
    # ### end Alembic commands ###
