from database import SessionLocal
import logging
from models import Hospital, Patient, Doctor


def delete_hospital(hospital_id):
    try:
        with SessionLocal() as session:
            # Fetch the hospital to delete
            hospital = session.query(Hospital).filter(Hospital.id == hospital_id).one()

            session.delete(hospital)
            session.commit()

            logging.info(
                f"Hospital '{hospital.name}', id={hospital.id} deleted successfully."
            )
    except Exception as e:
        logging.error(f"Error deleting hospital: {e}")


def delete_patient(patient_id):
    try:
        with SessionLocal() as session:
            patient = session.query(Patient).filter(Patient.id == patient_id).one()

            session.delete(patient)
            session.commit()

            logging.info(
                f"Patient '{patient.name}, id={patient.id} deleted successfully.'"
            )
    except Exception as e:
        logging.error(f"Error deleting patient: {e}")


def delete_doctor(doctor_id):
    try:
        with SessionLocal() as session:
            # Fetch the doctor to delete
            doctor = session.query(Doctor).filter(Doctor.id == doctor_id).one()

            session.delete(doctor)
            session.commit()

            logging.info(
                f"Doctor '{doctor.name}, id={doctor.id} deleted successfully.'"
            )

    except Exception as e:
        logging.error(f"Error deleting doctor:{e}")


if __name__ == "__main__":
    delete_hospital(1)
    # delete_doctor(1)
    # delete_patient(2)
