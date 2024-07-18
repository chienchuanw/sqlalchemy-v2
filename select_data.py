from database import SessionLocal
import logging
from models import Hospital, Patient, Doctor


def select_all_hospitals():
    try:
        with SessionLocal() as session:
            hospitals = session.query(Hospital).all()

            # Display hospital object individually
            for hospital in hospitals:
                logging.info(hospital)

            # Display total number of the hospitals in database
            logging.info(f"Total hospital number: {len(hospitals)}")

    except Exception as e:
        logging.error(f"Error selecting hospitals: {e}")


def select_all_patients():
    try:
        with SessionLocal() as session:
            patients = session.query(Patient).all()

            for patient in patients:
                logging.info(patient)

            logging.info(f"Total patient number: {len(patients)}")

    except Exception as e:
        logging.error(f"Error selecting patients: {e}")


def select_all_doctors():
    try:
        with SessionLocal() as session:
            doctors = session.query(Doctor).all()

            for doctor in doctors:
                logging.info(doctor)

            logging.info(f"Total doctor number: {len(doctors)}")

    except Exception as e:
        logging.error(f"Error selecting doctors: {e}")


if __name__ == "__main__":
    # select_all_hospitals()
    # select_all_patients()
    select_all_doctors()
