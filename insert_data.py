from database import SessionLocal
from models import Hospital, Doctor, Patient, GenderEnum
import logging
from datetime import datetime


# Use `with` statement to close session properly
def insert_hospital(name, address):
    try:
        with SessionLocal() as session:
            new_hospital = Hospital(name=name, address=address)

            session.add(new_hospital)
            session.commit()

            logging.info(f"Hospital '{name}' inserted successfully.")

    except Exception as e:
        logging.error(f"Error inserting hospital: {e}")


# Use 'session.close()' to close session manually
def insert_doctor(name, gender, email, hospital_id):
    session = SessionLocal()
    try:
        new_doctor = Doctor(
            name=name, gender=gender, email=email, hospital_id=hospital_id
        )

        session.add(new_doctor)
        session.commit()

        logging.info(f"Doctor '{name}' inserted successfully.")
    except Exception as e:
        # `session.rollback()` undoes any changes made to the database during transaction when an error occurs.
        # This ensures that the database remains in a consistent state, and no partial or invalid data modifications are left in the database.
        # Using `with` statement automatically handles the rollback in case of an exception
        session.rollback()

        logging.error(f"Error inserting doctor: {e}")

    # Use `finally` to ensure that the session will be closed no matter what happens during the transaction.
    finally:
        session.close()


def insert_patient(name, gender, birthday):
    try:
        with SessionLocal() as session:
            # Convert the birthday string to a date object
            date_format = "%Y-%m-%d"
            birthday_date_object = datetime.strptime(birthday, date_format)

            # Create a patient object
            new_patient = Patient(
                name=name, gender=gender, birthday=birthday_date_object
            )

            session.add(new_patient)
            session.commit()

            logging.info(f"Patient '{name}' inserted successfully.")

    except Exception as e:
        logging.error(f"Error inserting patient: {e}")


if __name__ == "__main__":
    # insert_hospital("General Hospital", "123 Main St")
    # insert_doctor("Dr. Smith", GenderEnum.Male, "dr.smith@example.com", 1)
    # insert_patient("John Doe", GenderEnum.Male, "2000-01-01")
    insert_patient("Peter Su", GenderEnum.Male, "1995-03-05")
