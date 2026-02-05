# SOLID: Single Responsibility Principle (SRP)
# Core Concept: A class should have one, and only one, reason to change.

from sqlalchemy import Column, Integer, String
from setup import Base  

# --- ENTITY LAYER ---
# Responsibility: Define the data structure/schema of the 'Student' asset.
class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    grado = Column(String, nullable=False)

# --- REPOSITORY LAYER ---
# Responsibility: Handle data persistence and transactions (CRUD).
# This decouples business logic from database operations.
class EstudiantesBD:
    def __init__(self, session):
        self.session = session

    def agregar_estudiante(self, estudiante):
        try:
            self.session.add(estudiante)
            self.session.commit()
            print(f"Success: Student {estudiante} committed to database.")
        except Exception as e:
            print(f"Error: Transaction failed. {e}")

    def listar_estudiantes(self):
        # Fetching state from the ledger (database)
        return self.session.query(Estudiante).all()
