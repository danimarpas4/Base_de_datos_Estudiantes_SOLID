# 1. Initialize Infrastructure (Engine & Session)
from setup import Session, engine, Base 

# 2. Import Logic Modules
# The ORM needs to register the 'Estudiante' class metadata before initialization
from SingleResponsibilityPrinciple import Estudiante, EstudiantesBD
from OpenClosedPrinciple import BecaPorNecesidad, BecaPorRendimiento
from LiskovSubstitutionPrinciple import NotificacionEmail, NotificacionSMS
from InterfaceSegregationPrinciple import ReporteEsudiante, ExportadorReporte
from DependencyInversionPrinciple import SQLAlchemyDB

# --- MIGRATION SCRIPT ---
# Executing DDL to provision the schema in the local node (SQLite)
print("Initializing database schema...") 
Base.metadata.create_all(engine)
# ------------------------

# Start a new transaction session
session = Session()

# Dependency Injection for Database Operations
db_adapter = SQLAlchemyDB(session)
repository = EstudiantesBD(session)

# SRP Implementation: Adding records
estudiante_1 = Estudiante(nombre="Ana Martinez", grado="A")
estudiante_2 = Estudiante(nombre="Sergio Machado", grado="B")
estudiante_3 = Estudiante(nombre="Juan Garcia", grado="C")

# Committing transactions
db_adapter.guardar(estudiante_1)
db_adapter.guardar(estudiante_2)
db_adapter.guardar(estudiante_3)

# List los studients
estudiantes = repository.listar_estudiantes()
for estudiante in estudiantes:
    print(f"ID: {estudiante.id} , Nombre:{estudiante.nombre}, Grado:{estudiante.grado}")


# Calculate scholarships -> ocp
calculadora_rendimiento = BecaPorRendimiento()
claculadora_necesidad = BecaPorNecesidad()

for estudiante in estudiantes:
    print(
        f"{estudiante.nombre} - Beca por rendimiento: {calculadora_rendimiento.calcular(estudiante)}"
    )
    print(
        f"{estudiante.nombre} - Beca por necesidad: {claculadora_necesidad.calcular(estudiante)}"
    )

# Send notifications -> LSP
notificacion_email = NotificacionEmail()
notificacion_sms = NotificacionSMS()
for estudiante in estudiantes:
    mensaje = "Felicidades, estas registrado"
    notificacion_email.enviar(estudiante, mensaje)
    notificacion_sms.enviar(estudiante, mensaje)

# Generate and export the reports -> ISP
reporte_generador = ReporteEsudiante()
exportador_reportes = ExportadorReporte()

for estudiante in estudiantes:
    reporte = reporte_generador.generar_reporte(estudiante)
    exportador_reportes.exportar_pdf(reporte)