# 1. Importamos engine y Base
from setup import Session, engine, Base 

# 2. Al importar esto, Python "aprende" que existe una tabla llamada 'estudiantes'
from SingleResponsibilityPrinciple import Estudiante, EstudiantesBD
from OpenClosedPrinciple import BecaPorNecesidad, BecaPorRendimiento
from LiskovSubstitutionPrinciple import NotificacionEmail, NotificacionSMS
from InterfaceSegregationPrinciple import ReporteEsudiante, ExportadorReporte
from DependencyInversionPrinciple import SQLAlchemyDB

# --- AGREGA ESTO AQUÍ OBLIGATORIAMENTE ---
# Ahora que Python ya leyó las líneas de arriba y sabe qué es "Estudiante",
# le ordenamos crear la tabla en la base de datos.
print("Creando tablas en SQLite...")  # Un print para que veas que pasa por aquí
Base.metadata.create_all(engine)
# -----------------------------------------

# Crear la sesion de base de datos...
session = Session()
# ... resto del código ...

# Crear la sesion de base de datos -> DIV
session = Session()
db = SQLAlchemyDB(session)
repositorio = EstudiantesBD(session)


# Agregar estudiantes -> SRP
estudiante_1 = Estudiante(nombre="Ana Martinez", grado="A")
estudiante_2 = Estudiante(nombre="Sergio Machado", grado="B")
estudiante_3 = Estudiante(nombre="Juan Garcia", grado="C")

db.guardar(estudiante_1)
db.guardar(estudiante_2)
db.guardar(estudiante_3)

# Listar los estudiantes
estudiantes = repositorio.listar_estudiantes()
for estudiante in estudiantes:
    print(f"ID: {estudiante.id} , Nombre:{estudiante.nombre}, Grado:{estudiante.grado}")


# Calcular becas -> ocp
calculadora_rendimiento = BecaPorRendimiento()
claculadora_necesidad = BecaPorNecesidad()

for estudiante in estudiantes:
    print(
        f"{estudiante.nombre} - Beca por rendimiento: {calculadora_rendimiento.calcular(estudiante)}"
    )
    print(
        f"{estudiante.nombre} - Beca por necesidad: {claculadora_necesidad.calcular(estudiante)}"
    )

# Enviar notificaciones -> LSP
notificacion_email = NotificacionEmail()
notificacion_sms = NotificacionSMS()
for estudiante in estudiantes:
    mensaje = "Felicidades, estas registrado"
    notificacion_email.enviar(estudiante, mensaje)
    notificacion_sms.enviar(estudiante, mensaje)

# Generar y exportar los reportes -> ISP
reporte_generador = ReporteEsudiante()
exportador_reportes = ExportadorReporte()

for estudiante in estudiantes:
    reporte = reporte_generador.generar_reporte(estudiante)
    exportador_reportes.exportar_pdf(reporte)
