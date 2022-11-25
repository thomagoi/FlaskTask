"""added tag field to Todo-Model

Revision ID: c49214075c8b
Revises: 
Create Date: 2022-11-23 14:26:53.654695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c49214075c8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_todo_tag_tag', 'tag', ['tag'], ['id'], ondelete='SET NULL')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_constraint('fk_todo_tag_tag', type_='foreignkey')
        batch_op.drop_column('tag')

    # ### end Alembic commands ###
