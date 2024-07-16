from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from models import Base


def create_database(name):
    try:
        # Create a SQLite database
        engine = create_engine(f"sqlite:///{name}.db", echo=True)

        # Create all tables in database
        Base.metadata.create_all(bind=engine)

        print(f"Database {name}.db and tables are created successfully")

    except SQLAlchemyError as error:
        print(f"An error occurred while creating the database: {error}")


if __name__ == "__main__":
    database_name = "medical_database"
    create_database(database_name)
