"""empty message

Revision ID: 3b29eabc89ae
Revises: 
Create Date: 2023-07-08 08:16:09.974788

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3b29eabc89ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Customer')
    op.drop_table('accounts')
    op.drop_table('customers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('contact_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('adress', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='customers_pkey')
    )
    op.create_table('accounts',
    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='accounts_pkey'),
    sa.UniqueConstraint('email', name='accounts_email_key'),
    sa.UniqueConstraint('username', name='accounts_username_key')
    )
    op.create_table('Customer',
    sa.Column('Contact name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('Adress', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('City', sa.VARCHAR(length=100), autoincrement=False, nullable=False)
    )
    # ### end Alembic commands ###