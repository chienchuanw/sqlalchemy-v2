# SQLAlchemy 2.0 Tutorial

## Workflow

### Step 1: Set up a project

1. Create a project directory
2. Create a virtual environment
3. Install SQLAlchemy and Alembic  

    - Install SQLAlchemy
    `pip install SQLAlchemy`
    - Install Alembic  
    `pip install alembic`

        > Alembic is a lightweight database migration tool for use with SQLAlchemy. It allows you to manage database schema changes in a version-controlled manner.

4. Create a `models.py` for your ORM Models
5. create a `database.py` for database connection

### Step 2: Initialize Alembic

1. Initialize Alembic
    `$ alembic init alembic`

2. Configure Alembic  
    Edit `alembic.ini` to set the SQLAlchemy URL:
    (*If you are using SQLite*)
    `sqlalchemy.url = sqlite:///<database_filename>.db`  

    - Configure Timezone  

        ```ini
        [alembic]
        # ... other configurations
        timezone = Asia/Taipei
        ```

3. Configure the Alembic Environment  
    Edit `alembic/env.py` to include your models. Modify the file to reflect your models' metadata.

    ```py
    from models import Base
    target_metadata = Base.metadata
    ```

### Step 3: Create and Apply Migrations

1. Create an initial migration  
    `alembic revision --autogenerate -m "Initial migration"`

2. Apply the initial migration  
    `alembic upgrade head`

### Step 4: Making Changes to Models and Managing Migrations

1. Modify Your Models  
    Make some changes in your SQLAlchemy models which is usually located in `models.pys`

2. Generate a New Migration  
    `alembic revision --autogenerate -m "Describe the changes"`

3. Apply the New Migration  
    `alembic upgrade head`

### Additional: Highlight Logs with Rich

`Rich` is a Python library for rich text and beautiful formatting in the terminal. Use packages like `Rich` to highlight and format the logs of your database interactions in a more readable and visually appealing way.

1. Install Rich  
    `pip install rich`

2. Configure SQLAlchemy Logging and Create a Custom Logging Handler with Rich  

    ```py
    # database.py
    import logging
    from rich.logging import RichHandler
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from models import Base

    # Configure Rich logging
    logging.basicConfig(level=logging.INFO, format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])

    # Get the logger for SQLAlchemy
    logger = logging.getLogger('sqlalchemy.engine')
    logger.setLevel(logging.INFO)

    # Database URL for SQLite
    DATABASE_URL = "sqlite:///medical_database.db"

    # Create an engine that will interact with the SQLite database
    engine = create_engine(DATABASE_URL, echo=False)  # Set echo=False and use logging instead

    # Create a configured "Session" class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Function to initialize the database
    def init_db():
        Base.metadata.create_all(bind=engine)

    if __name__ == "__main__":
        init_db()
        logging.info("Database and tables created successfully.")
    ```
