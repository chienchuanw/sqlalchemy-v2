from faker import Faker
from database import SessionLocal
from models import Hospital, Doctor, Patient, GenderEnum
import random
from insert_data import insert_hospital, insert_doctor, insert_patient
from database_utils import get_doctor_by_id, get_hospital_by_id, get_patient_by_id
import logging

# Initialize Faker
fake = Faker()


def create_fake_hospital(num):
    for _ in range(num):
        insert_hospital(
            name=fake.company(),
            address=fake.address(),
        )


def create_fake_doctor(num):
    hospitals = SessionLocal().query(Hospital).all()

    for _ in range(num):
        insert_doctor(
            name=fake.name(),
            gender=random.choice(list(GenderEnum)),
            email=fake.email(),
            hospital_id=random.choice(hospitals).id,
        )

    SessionLocal().close()


def create_fake_patient(num):
    for _ in range(num):
        insert_patient(
            name=fake.name(),
            gender=random.choice(list(GenderEnum)),
            birthday=fake.date(),
        )
    SessionLocal().close()


def associate_patients_randomly():
    try:
        with SessionLocal() as session:
            patients = session.query(Patient).all()
            doctors = session.query(Doctor).all()

            for patient in patients:
                patient = get_patient_by_id(session, patient.id)

                doctor = get_doctor_by_id(session, random.choice(doctors).id)
                hospital = get_hospital_by_id(session, doctor.hospital_id)

                patient.doctors.append(doctor)
                patient.hospitals.append(hospital)

                session.add(patient)
                session.commit()

                logging.info(
                    f"Patient '{patient.name}' associated with Doctor '{doctor.name}' and Hospital '{hospital.name}'."
                )

    except Exception as e:
        logging.error(f"Error associating patient: {e}")


if __name__ == "__main__":
    # create_fake_hospital(10)
    # create_fake_doctor(20)
    # create_fake_patient(30)
    associate_patients_randomly()
