import logging
from faker import Faker
from database import SessionLocal
from models import Hospital, Doctor, Patient, GenderEnum
import random
from insert_data import insert_hospital, insert_doctor, insert_patient

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


def create_fake_patient(num):
    for _ in range(num):
        insert_patient(
            name=fake.name(),
            gender=random.choice(list(GenderEnum)),
            birthday=fake.date(),
        )


if __name__ == "__main__":
    # create_fake_hospital(10)
    # create_fake_doctor(20)
    create_fake_patient(50)
