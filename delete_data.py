from database import SessionLocal
import logging
from models import Hospital


def delete_hospital(hospital_id):
    try:
        with SessionLocal() as session:
            hospital = session.query(Hospital).filter(Hospital.id == hospital_id).one()
            session.delete(hospital)
            session.commit()
    except Exception as e:
        logging.error(f"Error deleting hospital: {e}")


if __name__ == "__main__":
    delete_hospital(2)
