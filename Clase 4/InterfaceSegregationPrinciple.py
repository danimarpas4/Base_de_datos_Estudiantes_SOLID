# PRINCIPIO DE SEGREGACION DE INTERFACES
# Las clases no dependen de metodos que no usan

# Interfaces especificas


class GeneradorReportes:
    def generar_reporte(self, estudiante):
        raise NotImplementedError


class ExportadorPDF:
    def exportar_pdf(self, reporte):
        raise NotImplementedError


# Clases que cumplen ISP
class ReporteEsudiante(GeneradorReportes):
    def generar_reporte(self, estudiante):
        return f"Reporte para : {estudiante.nombre} en grado {estudiante.grado}"


class ExportadorReporte(ExportadorPDF):
    def exportar_pdf(self, reporte):
        print(f"Exportando PDF de reporte para: {reporte}")
