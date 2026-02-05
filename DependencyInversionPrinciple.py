# SOLID: Dependency Inversion Principle (DIP)
# Core Concept: High-level modules should not depend on low-level modules. Both should depend on abstractions.

# --- ABSTRACTION LAYER ---
# Defines the standard for ANY database implementation (SQL, NoSQL, File, etc.)
class BaseDeDatos:
    def guardar(self, data):
        raise NotImplementedError

# --- LOW-LEVEL IMPLEMENTATION (ADAPTER) ---
# Concrete implementation using SQLAlchemy.
# This details can change without breaking the high-level logic.
class SQLAlchemyDB(BaseDeDatos):
    def __init__(self, session):
        self.session = session

    def guardar(self, data):
        self.session.add(data)
        self.session.commit()