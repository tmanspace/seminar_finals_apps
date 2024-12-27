import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

data_directory = "./data"

if not os.path.exists(data_directory):
    os.makedirs(data_directory)
    print(f"Директория '{data_directory}' создана.")

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/shorturl.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
