import logging
from database import SessionLocal
from models import Hospital, Doctor, GenderEnum


def update_hospital(id: int, name: str = None, address: str = None) -> None:
    try:
        with SessionLocal() as session:
            # Fetch the hospital record by id
            hospital = session.query(Hospital).filter_by(id=id).one_or_none()

            # Return None if there's no hospital with the provided id
            if not hospital:
                logging.warning(f"Hospital with id={id} not found.")
                return None

            # Update hospital with provided arguments, else use default 'None'
            if name:
                hospital.name = name
            if address:
                hospital.address = address

            session.commit()
            logging.info(f"Hospital updated successfully: '{hospital}'.")

    except Exception as e:
        # The `exc_info=True`` parameter in `logging.error`` provides a full traceback in the log for debugging.
        logging.error(f"Error updating hospital: {e}", exc_info=True)
        session.rollback()


def update_doctor(
    id: int,
    name: str = None,
    gender: GenderEnum = None,
    email: str = None,
    hospital_id: int = None,
) -> None:
    try:
        with SessionLocal() as session:
            doctor = session.query(Doctor).filter_by(id=id).one_or_none()
            hospital = session.query(Hospital).filter_by(id=hospital_id).one_or_none()

            if not doctor:
                logging.warning(f"Doctor with id={id} not found.")
                return None

            if name:
                doctor.name = name
            if gender:
                doctor.gender = gender
            if email:
                doctor.email = email
            # Update doctor's hospital_id if provided and hospital exists
            if hospital_id and hospital:
                doctor.hospital_id = hospital_id

            session.commit()
            logging.info(f"Doctor updated successfully: '{doctor}'.")

    except Exception as e:
        logging.error(f"Error updating doctor: {e}", exc_info=True)
        session.rollback()


if __name__ == "__main__":
    # update_hospital(
    #     1,
    #     name="Greenfield General Hospital",
    #     address="1234 Elm Street, Springfield, IL 62704",
    # )

    # update_doctor(
    #     1,
    #     name="Susan Jones",
    #     gender=GenderEnum.Female,
    #     email="susanjones@gamil.com",
    #     hospital_id=3,
    # )
