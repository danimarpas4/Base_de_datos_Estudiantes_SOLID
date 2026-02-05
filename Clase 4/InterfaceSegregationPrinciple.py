# SOLID: Interface Segregation Principle (ISP)
# Core Concept: Clients should not be forced to depend upon interfaces that they do not use.

# --- GRANULAR INTERFACES ---
# Instead of one "fat" interface, we split responsibilities.

class GeneradorReportes:
    def generar_reporte(self, estudiante):
        raise NotImplementedError

class ExportadorPDF:
    def exportar_pdf(self, reporte):
        raise NotImplementedError

# --- SPECIALIZED IMPLEMENTATIONS ---

# Service dedicated solely to report generation logic
class ReporteEsudiante(GeneradorReportes):
    def generar_reporte(self, estudiante):
        return f"Reporte para : {estudiante.nombre} en grado {estudiante.grado}"

# Service dedicated solely to format conversion (PDF)
class ExportadorReporte(ExportadorPDF):
    def exportar_pdf(self, reporte):
        print(f"Exportando PDF de reporte para: {reporte}")