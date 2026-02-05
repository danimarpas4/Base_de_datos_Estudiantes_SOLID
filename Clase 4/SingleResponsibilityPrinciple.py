# PRINCIPIO DE RESPONSABILIDAD UNICA
# nota: Una clase debe tener una sola responsabilidad

from sqlalchemy import Column, Integer, String # Mantén tus imports de tipos
from setup import Base  

# setup


# Clase para representar la entidad Estudiante - cuya responsabilidad es instanciar o crear un estudiante
class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    grado = Column(String, nullable=False)


# Clase para manejar operaciones de bd del repositorio del estudiante
# Operaciones: agregar estudiantes , listar estudiantes ->  CREATE /  READ


class EstudiantesBD:
    def __init__(self, session):
        self.session = session

    def agregar_estudiante(self, estudiante):
        try:
            self.session.add(estudiante)
            self.session.commit()
            print(f"Estudiante {estudiante} agregado correctamente")
        except:
            print("No se pudo agregar al estudiante")

    def listar_estudiantes(self):
        return self.session.query(Estudiante).all()
