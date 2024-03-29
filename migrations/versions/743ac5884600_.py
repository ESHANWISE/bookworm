"""empty message

Revision ID: 743ac5884600
Revises: 
Create Date: 2023-09-14 13:13:08.217556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '743ac5884600'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_username', sa.String(length=20), nullable=True),
    sa.Column('admin_pwd', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('category',
    sa.Column('cat_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cat_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('cat_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_fullname', sa.String(length=100), nullable=False),
    sa.Column('user_email', sa.String(length=120), nullable=True),
    sa.Column('user_pwd', sa.String(length=120), nullable=True),
    sa.Column('user_pix', sa.String(length=120), nullable=True),
    sa.Column('user_datereg', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('book_title', sa.Text(), nullable=False),
    sa.Column('book_desc', sa.Text(), nullable=True),
    sa.Column('book_cover', sa.String(length=100), nullable=True),
    sa.Column('book_publication', sa.Date(), nullable=True),
    sa.Column('book_catid', sa.Integer(), nullable=False),
    sa.Column('book_status', sa.Enum('1', '0'), server_default='0', nullable=False),
    sa.ForeignKeyConstraint(['book_catid'], ['category.cat_id'], ),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('donation',
    sa.Column('don_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('don_amt', sa.Float(), nullable=False),
    sa.Column('don_userid', sa.Integer(), nullable=True),
    sa.Column('don_fullname', sa.String(length=100), nullable=True),
    sa.Column('don_email', sa.String(length=100), nullable=True),
    sa.Column('don_refno', sa.String(length=20), nullable=False),
    sa.Column('don_paygate_response', sa.Text(), nullable=True),
    sa.Column('don_date', sa.DateTime(), nullable=True),
    sa.Column('don_status', sa.Enum('pending', 'failed', 'paid'), server_default='pending', nullable=False),
    sa.ForeignKeyConstraint(['don_userid'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('don_id')
    )
    op.create_table('reviews',
    sa.Column('rev_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rev_title', sa.String(length=255), nullable=False),
    sa.Column('rev_text', sa.String(length=255), nullable=False),
    sa.Column('rev_date', sa.DateTime(), nullable=True),
    sa.Column('rev_userid', sa.Integer(), nullable=False),
    sa.Column('rev_bookid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rev_bookid'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['rev_userid'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('rev_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('donation')
    op.drop_table('book')
    op.drop_table('user')
    op.drop_table('category')
    op.drop_table('admin')
    # ### end Alembic commands ###
