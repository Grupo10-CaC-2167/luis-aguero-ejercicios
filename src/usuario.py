class usuario ():
    "Clase que representa una persona."
    def __init__(self, dni, nombre, apellido):
        "Constructor de Persona"
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def carritoCompras(self,carrito):
        self.carrito=carrito
        return
    def __str__(self):
        return f"{self.dni}{self.nombre}{self.apellido}"