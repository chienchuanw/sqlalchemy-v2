from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def create_database(name):
    try:
        # Create a SQLite database
        engine = create_engine(f"sqlite:///{name}.db")

        # Establish a connection and thus create a database
        with engine.connect():
            pass

        print(f"Database {name}.db is created successfully")

    except SQLAlchemyError as error:
        print(f"An error occurred while creating the database: {error}")


if __name__ == "__main__":
    database_name = "my_database"
    create_database(database_name)
