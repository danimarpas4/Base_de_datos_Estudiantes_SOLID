import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

# Configuracion de la base de datos
DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_URL = "sqlite:///estudiantes.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
