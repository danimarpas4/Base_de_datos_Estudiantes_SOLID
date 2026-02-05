# PRINCIPIO DE ABIERTO Y CERRADO
# Una clase de orden superior debe estar cerrada a modificacion pero abierta a extension
# Clase que calcule becas
class CalculadoraBeca:
    def calcular(self, estudiante):
        raise NotImplementedError


# 1 Extension para calculo por rendimiento
class BecaPorRendimiento(CalculadoraBeca):
    def calcular(self, estudiante):
        return "Beca completa" if estudiante.grado == "A" else "beca no aplicable"


# 2 Extension para calculo por necesidad
class BecaPorNecesidad(CalculadoraBeca):
    def calcular(self, estudiante):
        return (
            "50 porciento de beca"
            if estudiante.grado in ["B", "C"]
            else "beca no aplicable"
        )
