"""empty message

Revision ID: b4f18f29686e
Revises: 692e5844f1de
Create Date: 2017-09-22 13:37:09.053240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4f18f29686e'
down_revision = '692e5844f1de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact_submission', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=True)

    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=True)

    with op.batch_alter_table('contact_submission', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###