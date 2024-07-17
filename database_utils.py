from database import SessionLocal
from models import Doctor, Hospital, Patient
import logging


def get_hospital_by_id(session, hospital_id):
    try:
        return session.get(Hospital, hospital_id)
    except Exception as e:
        logging.error(f"Error getting hospital by id: {e}")
        return None


def get_doctor_by_id(session, doctor_id):
    try:
        return session.get(Doctor, doctor_id)
    except Exception as e:
        logging.error(f"Error getting patient by id: {e}")
        return None


def get_patient_by_id(session, patient_id):
    try:
        return session.get(Patient, patient_id)
    except Exception as e:
        logging.error({e})
        return None


# Associate patient with doctors and hospitals
def associate_patient(patient_id, doctor_id, hospital_id):
    try:
        with SessionLocal() as session:
            # Get query objects
            patient = get_patient_by_id(session, patient_id)
            hospital = get_hospital_by_id(session, hospital_id)
            doctor = get_doctor_by_id(session, doctor_id)

            if patient and hospital and doctor:
                # Add hospital and doctor to patient's list
                patient.hospitals.append(hospital)
                patient.doctors.append(doctor)

                session.add(patient)
                session.commit()
                logging.info(
                    f"Patient '{patient.name}' associated with Doctor '{doctor.name}' and Hospital '{hospital.name}'."
                )
            else:
                logging.error(
                    "Invalid patient_id, doctor_id, or hospital_id provided for association."
                )
    except Exception as e:
        logging.error(f"Error associating patient: {e}")


if __name__ == "__main__":
    associate_patient(1, 1, 1)
