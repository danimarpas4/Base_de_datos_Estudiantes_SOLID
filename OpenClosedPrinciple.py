# SOLID: Open/Closed Principle (OCP)
# Core Concept: Software entities should be OPEN for extension, but CLOSED for modification.

# Abstract Base Strategy
# Responsibility: Define the contract for scholarship calculations.
class CalculadoraBeca:
    def calcular(self, estudiante):
        raise NotImplementedError

# --- CONCRETE STRATEGIES ---
# We can add new calculation methods without modifying the existing code.

# Strategy 1: Merit-based Scholarship
class BecaPorRendimiento(CalculadoraBeca):
    def calcular(self, estudiante):
        # Logic: Full scholarship for top-tier grades
        return "Beca completa" if estudiante.grado == "A" else "beca no aplicable"

# Strategy 2: Need-based Scholarship
class BecaPorNecesidad(CalculadoraBeca):
    def calcular(self, estudiante):
        # Logic: Partial aid for specific grades
        return (
            "50 porciento de beca"
            if estudiante.grado in ["B", "C"]
            else "beca no aplicable"
        )