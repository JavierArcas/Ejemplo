class Vehiculo:
    combustible = ""
    caballos = 0
    direccionAsistida = None
    ABS = None

    def __init__(self, combustible, caballos, direccionasistida, ABS):
        self.combustible = combustible
        self.caballos = caballos
        self.direccionAsistida = direccionasistida
        self.ABS = ABS

    def imprimir(self):
        print("Combustible: " + self.combustible + "Caballos: " + self.caballos)
        print("Pienso: " + self.combustible + "Gramos: " + self.caballos)

