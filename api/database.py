""" Database configuration and connection setup. """

from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

# Define your database URL here
SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db" 

# create the database engine which will manage connections
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
    )

# Define a session local class which will be used to create sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for declarative models
Base = declarative_base()

# tester le code avec la connexion
if __name__ == "__main__":
    try:
        # Try to connect to the database
        with engine.connect() as connection:
            print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")
