class empleado:
    def __init__(self, nombre, cargo, sueldo, anios_experiencia):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
        self.anios_experiencia = años_experiencia

    def mostrar_informacion(self):                                                   
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Sueldo: {self.sueldo}"
    def experiencia(self):
        return f"Experiencia: {self.años_experiencia} años"
def aplicar_aumento(self, porcentaje):
    aumento = self.sueldo * (porcentaje / 100)
    self.sueldo += aumento  
    empleado1=empleado("jose", "ingeniero", 5000)   
    empleado2=empleado("maria", "desarrolladora", 5000)  
                       