"""empty message

Revision ID: 4f8e98f23dd6
Revises: 
Create Date: 2021-06-26 02:02:45.179147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f8e98f23dd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bundle',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('words', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], name=op.f('fk_bundle_creator_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bundle'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bundle')
    # ### end Alembic commands ###