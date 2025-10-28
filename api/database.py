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





SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
