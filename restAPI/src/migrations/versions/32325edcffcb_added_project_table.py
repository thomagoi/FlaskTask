"""added project table

Revision ID: 32325edcffcb
Revises: c49214075c8b
Create Date: 2022-12-04 16:22:09.008557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32325edcffcb'
down_revision = 'c49214075c8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('project', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_todo_project_project', 'project', ['project'], ['id'], ondelete='SET NULL')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_constraint('fk_todo_project_project', type_='foreignkey')
        batch_op.drop_column('project')

    # ### end Alembic commands ###
