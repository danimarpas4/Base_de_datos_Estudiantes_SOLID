# PRINCIPIO DE INVERSION DE DEPENDENCIA
# Las clases deben depender de abstracciones y no de implementaciones concretas

# ABSTRACCION DE BASE DE DATOS PARA UNA IMPLEMENTACION INDISTINTA


# Abstraccion para guardar datos
class BaseDeDatos:
    def guardar(self, data):
        raise NotImplementedError


# Implementacion concreta de BD CON SQLALCHEMY
class SQLAlchemyDB(BaseDeDatos):
    def __init__(self, session):
        self.session = session

    def guardar(self, data):
        self.session.add(data)
        self.session.commit()
