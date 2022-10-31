"""empty message

Revision ID: 60117a696ae3
Revises: a9eb8522c7b1
Create Date: 2022-10-30 18:50:56.129528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60117a696ae3'
down_revision = 'a9eb8522c7b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('proudct')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proudct',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='proudct_pkey')
    )
    op.drop_table('product')
    # ### end Alembic commands ###
