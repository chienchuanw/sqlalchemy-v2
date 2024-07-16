"""Initial migration

Revision ID: 5413d2ea6b20
Revises: 
Create Date: 2024-07-17 00:55:32.069970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5413d2ea6b20'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hospitals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('gender', sa.Enum('Male', 'Female', 'Other', name='genderenum'), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('gender', sa.Enum('Male', 'Female', 'Other', name='genderenum'), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hospital_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospitals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hospital_patient_association',
    sa.Column('hospital_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospitals.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('hospital_id', 'patient_id')
    )
    op.create_table('doctor_patient_association',
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('doctor_id', 'patient_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('doctor_patient_association')
    op.drop_table('hospital_patient_association')
    op.drop_table('doctors')
    op.drop_table('patients')
    op.drop_table('hospitals')
    # ### end Alembic commands ###
