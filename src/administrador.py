from usuario import usuario
class administrador(usuario):
    """Clase que representa a un Supervisor"""

    def __init__(self, dni, nombre, apellido, carrito):
        """Constructor de clase Supervisor"""
        # Invoca al constructor de clase Persona
        usuario.__init__(self, dni, nombre, apellido)
