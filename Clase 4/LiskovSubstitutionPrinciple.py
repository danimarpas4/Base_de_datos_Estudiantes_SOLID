# SOLID: Liskov Substitution Principle (LSP)
# Core Concept: Subtypes must be substitutable for their base types without altering correctness.

# Abstract Interface
# Responsibility: Define a common protocol for notifications.
class Notificacion:
    def enviar(self, estudiante, mensaje):
        raise NotImplementedError

# --- POLYMORPHIC IMPLEMENTATIONS ---
# Both classes adhere strictly to the 'Notificacion' contract.

class NotificacionEmail(Notificacion):
    def enviar(self, estudiante, mensaje):
        # Simulation of SMTP protocol
        print(f"Email enviado a {estudiante.nombre} : {mensaje}")

class NotificacionSMS(Notificacion):
    def enviar(self, estudiante, mensaje):
        # Simulation of SMS Gateway
        print(f"SMS enviado a {estudiante.nombre} : {mensaje}")