# README

## Workflow

### Step 1: Set up a project

1. Create a project directory
2. Create a virtual environment
3. Install SQLAlchemy and Alembic  

    - Install SQLAlchemy
    `$ pip install SQLAlchemy`
    - Install Alembic  
    `$ pip install alembic`

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
