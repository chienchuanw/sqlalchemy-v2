from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, ForeignKey, Enum
from typing import List, Optional
import enum


class Base(DeclarativeBase):
    pass


class GenderEnum(enum.Enum):
    Male = "M"
    Female = "F"
    Other = "O"


class Hospital(Base):
    __tablename__ = "hospitals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    doctors: Mapped[List["Doctor"]] = relationship("Doctor", back_populates="hospital")
    patients: Mapped[List["Patient"]] = relationship(
        "Patient", secondary="hospital_patient_association", back_populates="hospitals"
    )

    def __repr__(self) -> str:
        return f"Hospital(id={self.id}, name='{self.name}')"


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped["GenderEnum"] = mapped_column(Enum(GenderEnum), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String)
    hospital_id: Mapped[int] = mapped_column(ForeignKey("hospitals.id"), nullable=False)
    hospital: Mapped["Hospital"] = relationship("Hospital", back_populates="doctors")
    patients: Mapped[List["Patient"]] = relationship(
        "Patient", secondary="doctor_patient_association", back_populates="doctors"
    )

    def __repr__(self) -> str:
        return f"Doctor(id={self.id}, name='{self.name}', email='{self.email}')"


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped["GenderEnum"] = mapped_column(Enum(GenderEnum), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    birthday: Mapped[Date] = mapped_column(Date, nullable=False)
    hospitals: Mapped[List["Hospital"]] = relationship(
        "Hospital", secondary="hospital_patient_association", back_populates="patients"
    )
    doctors: Mapped[List["Doctor"]] = relationship(
        "Doctor", secondary="doctor_patient_association", back_populates="patients"
    )

    def __repr__(self) -> str:
        return f"Patient(id={self.id}, name='{self.name}', age={self.age})"


class HospitalPatientAssociation(Base):
    __tablename__ = "hospital_patient_association"

    hospital_id: Mapped[int] = mapped_column(
        ForeignKey("hospitals.id"), primary_key=True
    )
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), primary_key=True)


class DoctorPatientAssociation(Base):
    __tablename__ = "doctor_patient_association"

    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"), primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), primary_key=True)
